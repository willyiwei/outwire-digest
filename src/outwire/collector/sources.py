from dataclasses import dataclass


@dataclass
class FeedSource:
    name: str
    url: str
    category: str  # "news", "research", "practitioner"


SOURCES: list[FeedSource] = [
    FeedSource("The Hacker News", "https://feeds.feedburner.com/TheHackersNews", "news"),
    FeedSource("Krebs on Security", "https://krebsonsecurity.com/feed/", "practitioner"),
    FeedSource("WIRED Security", "https://www.wired.com/feed/category/security/latest/rss", "news"),
    FeedSource("Dark Reading", "https://www.darkreading.com/rss.xml", "news"),
    FeedSource("Schneier on Security", "https://www.schneier.com/feed/atom", "practitioner"),
    FeedSource("SANS ISC", "https://isc.sans.edu/rssfeed_full.xml", "practitioner"),
    FeedSource("arXiv cs.CR", "https://export.arxiv.org/rss/cs.CR", "research"),
    FeedSource("Google Project Zero", "https://googleprojectzero.blogspot.com/feeds/posts/default", "research"),
    FeedSource("Microsoft Security", "https://www.microsoft.com/en-us/security/blog/feed/", "news"),
    FeedSource("LLM Security", "https://llmsecurity.net/index.xml", "practitioner"),
    FeedSource("Trail of Bits", "https://blog.trailofbits.com/feed", "research"),
    FeedSource("Simon Willison", "https://simonwillison.net/atom/everything/", "practitioner"),
]
