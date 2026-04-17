import json
from datetime import datetime, timezone
from pathlib import Path

STATE_FILE = Path(__file__).parents[3] / "state" / "seen_articles.json"


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"last_run": None, "seen_ids": [], "last_issue_number": 0}
    return json.loads(STATE_FILE.read_text())


def save_state(seen_ids: list[str], issue_number: int) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = load_state()
    all_ids = list(set(state.get("seen_ids", []) + seen_ids))
    # Keep last 500 to avoid unbounded growth
    all_ids = all_ids[-500:]
    STATE_FILE.write_text(json.dumps({
        "last_run": datetime.now(timezone.utc).isoformat(),
        "seen_ids": all_ids,
        "last_issue_number": issue_number,
    }, indent=2))


def get_seen_ids() -> set[str]:
    return set(load_state().get("seen_ids", []))


def get_last_issue_number() -> int:
    return load_state().get("last_issue_number", 0)
