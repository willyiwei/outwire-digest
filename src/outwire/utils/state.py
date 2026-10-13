import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

STATE_FILE = Path(__file__).parents[3] / "state" / "seen_articles.json"


def current_week_key(when: datetime | None = None) -> str:
    """Return the ISO date (YYYY-MM-DD) of this week's Monday in UTC."""
    when = when or datetime.now(timezone.utc)
    monday = (when - timedelta(days=when.weekday())).date()
    return monday.isoformat()


def load_state() -> dict[str, Any]:
    if not STATE_FILE.exists():
        return {"last_run": None, "seen_ids": [], "last_issue_number": 0}
    loaded: dict[str, Any] = json.loads(STATE_FILE.read_text())
    return loaded


def save_state(seen_ids: list[str], issue_number: int, issue_week: str | None = None) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = load_state()
    all_ids = list(set(state.get("seen_ids", []) + seen_ids))
    # Keep last 500 to avoid unbounded growth
    all_ids = all_ids[-500:]
    STATE_FILE.write_text(json.dumps({
        "last_run": datetime.now(timezone.utc).isoformat(),
        "seen_ids": all_ids,
        "last_issue_number": issue_number,
        "last_issue_week": issue_week or current_week_key(),
    }, indent=2))


def get_seen_ids() -> set[str]:
    return set(load_state().get("seen_ids", []))


def get_last_issue_number() -> int:
    return int(load_state().get("last_issue_number", 0))


def _stored_week(state: dict[str, Any]) -> str | None:
    """Week key for the last issued digest.

    Falls back to inferring the week from ``last_run`` so state files written
    before week-keying was introduced don't trigger a spurious increment.
    """
    week = state.get("last_issue_week")
    if week:
        return str(week)
    last_run = state.get("last_run")
    if last_run:
        try:
            when = datetime.fromisoformat(last_run)
            if when.tzinfo is None:
                when = when.replace(tzinfo=timezone.utc)
            return current_week_key(when)
        except ValueError:
            return None
    return None


def resolve_issue_number(issue_week: str | None = None) -> int:
    """Return this week's issue number. Idempotent within a calendar week.

    The number only advances when a new week starts, so re-runs
    (retry cron, workflow_dispatch, local --reuse-last publish) never
    double-increment the sequence. A brand-new state file starts at 1.
    """
    state = load_state()
    week = issue_week or current_week_key()
    last_issue = int(state.get("last_issue_number", 0))
    if _stored_week(state) == week:
        return last_issue
    return max(last_issue, 0) + 1
