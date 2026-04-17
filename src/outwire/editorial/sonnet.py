import json
from datetime import datetime

import anthropic
import structlog

from outwire.collector.models import ScoredArticle
from outwire.scorer.prompts import load_editorial_prompt

log = structlog.get_logger()

MODEL = "claude-sonnet-4-6"
_MAX_TOKENS = 4096


def _articles_to_json(articles: list[ScoredArticle]) -> str:
    return json.dumps(
        [
            {
                "title": a.title,
                "url": a.url,
                "source_name": a.source_name,
                "description": a.description,
                "score": a.score,
                "score_reason": a.score_reason,
            }
            for a in articles
        ],
        indent=2,
    )


def generate_digest(
    articles: list[ScoredArticle],
    api_key: str,
    issue_number: int,
    week_date: str | None = None,
) -> str:
    if week_date is None:
        week_date = datetime.now().strftime("%B %d, %Y")

    client = anthropic.Anthropic(api_key=api_key)
    system = [{"type": "text", "text": load_editorial_prompt(), "cache_control": {"type": "ephemeral"}}]

    user_content = (
        f"Week date: {week_date}\n"
        f"Issue number: {issue_number}\n\n"
        f"Articles (JSON):\n{_articles_to_json(articles)}"
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=_MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user_content}],
    )
    usage = response.usage
    log.info(
        "editorial_complete",
        input_tokens=usage.input_tokens,
        output_tokens=usage.output_tokens,
        cache_create=getattr(usage, "cache_creation_input_tokens", 0),
        cache_read=getattr(usage, "cache_read_input_tokens", 0),
    )
    return response.content[0].text
