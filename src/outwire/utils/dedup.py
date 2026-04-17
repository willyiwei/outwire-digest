import hashlib
import re


def url_to_id(url: str) -> str:
    return hashlib.sha256(url.strip().lower().encode()).hexdigest()[:16]


def _normalize_title(title: str) -> str:
    return re.sub(r"\W+", " ", title.lower()).strip()


def is_duplicate_title(title: str, seen_titles: list[str], threshold: float = 0.8) -> bool:
    norm = _normalize_title(title)
    norm_words = set(norm.split())
    if not norm_words:
        return False
    for seen in seen_titles:
        seen_words = set(_normalize_title(seen).split())
        if not seen_words:
            continue
        overlap = len(norm_words & seen_words) / max(len(norm_words), len(seen_words))
        if overlap >= threshold:
            return True
    return False
