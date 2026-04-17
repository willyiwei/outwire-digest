import structlog
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

log = structlog.get_logger()

_BASE = "https://outwire.substack.com"
_TIMEOUT = 30


class SubstackClient:
    def __init__(self, sid: str) -> None:
        self._client = httpx.Client(
            headers={
                "Cookie": f"substack.sid={sid}",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Content-Type": "application/json",
                "Referer": _BASE,
            },
            timeout=_TIMEOUT,
        )

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def create_draft(self, title: str, html_body: str, subtitle: str = "") -> str:
        payload = {
            "type": "newsletter",
            "draft_title": title,
            "draft_subtitle": subtitle,
            "draft_body": html_body,
            "draft_bylines": [],
        }
        resp = self._client.post(f"{_BASE}/api/v1/drafts", json=payload)
        resp.raise_for_status()
        draft_id = str(resp.json()["id"])
        log.info("draft_created", draft_id=draft_id, title=title)
        return draft_id

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def publish_draft(self, draft_id: str, send_email: bool = True) -> bool:
        payload = {"send_email": send_email, "free": True}
        resp = self._client.post(f"{_BASE}/api/v1/drafts/{draft_id}/publish", json=payload)
        resp.raise_for_status()
        log.info("published", draft_id=draft_id, send_email=send_email)
        return True

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "SubstackClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


def publish_digest(sid: str, title: str, html_body: str, subtitle: str, send_email: bool = True) -> bool:
    with SubstackClient(sid) as client:
        draft_id = client.create_draft(title, html_body, subtitle)
        return client.publish_draft(draft_id, send_email=send_email)
