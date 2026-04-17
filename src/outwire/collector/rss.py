import hashlib
from datetime import datetime, timezone

import feedparser
import structlog
from dateutil import parser as dateparser

from outwire.collector.models import RawArticle
from outwire.collector.sources import SOURCES, FeedSource
from outwire.utils.dedup import is_duplicate_title, url_to_id

log = structlog.get_logger()

_MAX_DESCRIPTION = 600
_MAX_PER_FEED = 15


def _parse_date(entry: feedparser.FeedParserDict) -> datetime:
    for attr in ("published", "updated", "created"):
        val = getattr(entry, attr, None)
        if val:
            try:
                return dateparser.parse(val).astimezone(timezone.utc)
            except Exception:
                pass
    return datetime.now(timezone.utc)


def _truncate(text: str, max_len: int = _MAX_DESCRIPTION) -> str:
    text = text.strip()
    return text[:max_len] + "…" if len(text) > max_len else text


def collect_from_source(source: FeedSource) -> list[RawArticle]:
    try:
        feed = feedparser.parse(source.url)
        articles: list[RawArticle] = []
        seen_titles: list[str] = []
        for entry in feed.entries[:_MAX_PER_FEED]:
            url = getattr(entry, "link", None)
            title = getattr(entry, "title", "").strip()
            if not url or not title:
                continue
            description = getattr(entry, "summary", "") or getattr(entry, "description", "")
            description = _truncate(description)
            article = RawArticle(
                id=url_to_id(url),
                title=title,
                url=url,
                source_name=source.name,
                published_at=_parse_date(entry),
                description=description,
            )
            if not is_duplicate_title(title, seen_titles):
                articles.append(article)
                seen_titles.append(title)
        log.info("collected", source=source.name, count=len(articles))
        return articles
    except Exception as exc:
        log.warning("feed_error", source=source.name, error=str(exc))
        return []


def collect_all(seen_ids: set[str]) -> list[RawArticle]:
    all_articles: list[RawArticle] = []
    global_titles: list[str] = []

    for source in SOURCES:
        for article in collect_from_source(source):
            if article.id in seen_ids:
                continue
            if is_duplicate_title(article.title, global_titles):
                continue
            all_articles.append(article)
            global_titles.append(article.title)

    log.info("collection_complete", total=len(all_articles))
    return all_articles
