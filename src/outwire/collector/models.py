from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RawArticle:
    id: str  # sha256 of URL
    title: str
    url: str
    source_name: str
    published_at: datetime
    description: str  # truncated to 500 chars for scoring

    def scoring_text(self) -> str:
        return f"Title: {self.title}\nSource: {self.source_name}\nSummary: {self.description}\nURL: {self.url}"


@dataclass
class ScoredArticle:
    article: RawArticle
    score: int
    score_reason: str

    @property
    def title(self) -> str:
        return self.article.title

    @property
    def url(self) -> str:
        return self.article.url

    @property
    def source_name(self) -> str:
        return self.article.source_name

    @property
    def published_at(self) -> datetime:
        return self.article.published_at

    @property
    def description(self) -> str:
        return self.article.description
