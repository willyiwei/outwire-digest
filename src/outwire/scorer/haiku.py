import json

import anthropic
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential

from outwire.collector.models import RawArticle, ScoredArticle
from outwire.scorer.prompts import load_scoring_prompt

log = structlog.get_logger()

MODEL = "claude-haiku-4-5-20251001"
_MAX_TOKENS = 200


def _parse_score(text: str) -> tuple[int, str]:
    text = text.strip()
    # strip markdown code fences if present
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    try:
        data = json.loads(text)
        return int(data["score"]), str(data["reason"])
    except Exception:
        # fallback: try to extract score from text
        import re
        m = re.search(r'"score"\s*:\s*(\d+)', text)
        score = int(m.group(1)) if m else 1
        return score, "parse error"


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def _score_one(
    client: anthropic.Anthropic,
    system: list[dict],
    article: RawArticle,
) -> ScoredArticle:
    response = client.messages.create(
        model=MODEL,
        max_tokens=_MAX_TOKENS,
        system=system,
        messages=[{"role": "user", "content": article.scoring_text()}],
    )
    usage = response.usage
    log.debug(
        "scored",
        title=article.title[:60],
        cache_create=getattr(usage, "cache_creation_input_tokens", 0),
        cache_read=getattr(usage, "cache_read_input_tokens", 0),
    )
    score, reason = _parse_score(response.content[0].text)
    return ScoredArticle(article=article, score=score, score_reason=reason)


def score_articles(
    articles: list[RawArticle],
    api_key: str,
    min_score: int = 6,
    top_k: int = 20,
) -> list[ScoredArticle]:
    client = anthropic.Anthropic(api_key=api_key)
    system = [{"type": "text", "text": load_scoring_prompt(), "cache_control": {"type": "ephemeral"}}]

    scored: list[ScoredArticle] = []
    for i, article in enumerate(articles):
        try:
            result = _score_one(client, system, article)
            scored.append(result)
            log.info("score", n=i + 1, total=len(articles), score=result.score, title=article.title[:50])
        except Exception as exc:
            log.warning("score_failed", title=article.title[:50], error=str(exc))

    filtered = [s for s in scored if s.score >= min_score]
    filtered.sort(key=lambda s: s.score, reverse=True)
    result_set = filtered[:top_k]
    log.info("scoring_complete", total=len(scored), filtered=len(filtered), selected=len(result_set))
    return result_set
