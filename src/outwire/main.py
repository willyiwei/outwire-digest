import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import structlog

from outwire.utils.config import Config
from outwire.utils.state import get_last_issue_number, get_seen_ids, save_state

log = structlog.get_logger()

_OUTPUT_DIR = Path(__file__).parents[2] / "output"


def _week_date() -> str:
    from datetime import timezone
    return datetime.now(timezone.utc).strftime("%B %d, %Y")


_LAST_MD = _OUTPUT_DIR / "last_digest.md"
_LAST_HTML = _OUTPUT_DIR / "last_digest.html"


def _save_output(digest_md: str, digest_html: str, issue: int) -> None:
    _OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d")
    (_OUTPUT_DIR / f"issue_{issue:03d}_{stamp}.md").write_text(digest_md)
    (_OUTPUT_DIR / f"issue_{issue:03d}_{stamp}.html").write_text(digest_html)
    # Always keep a stable "last" copy for --reuse-last
    _LAST_MD.write_text(digest_md)
    _LAST_HTML.write_text(digest_html)
    log.info("output_saved", issue=issue, dir=str(_OUTPUT_DIR))


def _load_last_output() -> tuple[str, str] | None:
    if _LAST_MD.exists() and _LAST_HTML.exists():
        return _LAST_MD.read_text(), _LAST_HTML.read_text()
    return None


def run(cfg: Config, publish: bool = False, no_llm: bool = False, reuse_last: bool = False) -> None:
    from outwire.collector.rss import collect_all

    seen_ids = get_seen_ids()
    issue_number = get_last_issue_number() + 1
    week = _week_date()

    log.info("pipeline_start", issue=issue_number, week=week, dry_run=cfg.dry_run, reuse_last=reuse_last)

    # --reuse-last: skip collection+scoring+editorial, republish from cached output
    if reuse_last:
        cached = _load_last_output()
        if not cached:
            log.error("no_cached_output", hint="Run without --reuse-last first to generate output")
            return
        digest_md, digest_html = cached
        log.info("reusing_cached_output")
        if cfg.dry_run or not publish:
            print(digest_md)
            return
        # Re-render HTML in case renderer changed
        from outwire.editorial.renderer import markdown_to_substack_html
        digest_html = markdown_to_substack_html(digest_md)
        _last_html_path = _OUTPUT_DIR / "last_digest.html"
        _last_html_path.write_text(digest_html)
        _publish(cfg, digest_html, issue_number, week)
        return

    # 1. Collect
    articles = collect_all(seen_ids)
    if not articles:
        log.warning("no_articles_collected")
        return

    if no_llm or cfg.no_llm:
        log.info("no_llm_mode", article_count=len(articles))
        for a in articles[:5]:
            print(f"  [{a.source_name}] {a.title}")
        return

    # 2. Score
    from outwire.scorer.haiku import score_articles
    scored = score_articles(articles, cfg.anthropic_api_key, cfg.min_score, top_k=20)
    if not scored:
        log.warning("no_articles_passed_scoring")
        return

    # 3. Generate digest
    from outwire.editorial.sonnet import generate_digest
    digest_md = generate_digest(scored, cfg.anthropic_api_key, issue_number, week)

    # 4. Render HTML
    from outwire.editorial.renderer import markdown_to_simple_html
    digest_html = markdown_to_simple_html(digest_md)

    _save_output(digest_md, digest_html, issue_number)

    # Save state after every successful generation (not just after publish)
    new_ids = [a.article.id for a in scored]
    save_state(new_ids, issue_number)

    if cfg.dry_run or not publish:
        log.info("dry_run_complete", issue=issue_number)
        print(digest_md)
        return

    _publish(cfg, digest_html, issue_number, week)


def _publish(cfg: Config, digest_html: str, issue_number: int, week: str) -> None:
    title = f"Outwire #{issue_number} — AI Security Digest, {week}"
    subtitle = "Top 10 AI Security stories this week"
    published = False

    if cfg.substack_sid:
        try:
            if cfg.no_email:
                from outwire.publisher.substack import SubstackClient
                with SubstackClient(cfg.substack_sid) as client:
                    draft_id = client.create_draft(title, digest_html, subtitle)
                log.info("draft_only", draft_id=draft_id)
                published = True
            else:
                from outwire.publisher.substack import publish_digest
                published = publish_digest(
                    cfg.substack_sid, title, digest_html, subtitle,
                    send_email=cfg.publish_send_email,
                )
        except Exception as exc:
            log.error("substack_failed", error=str(exc))

    if not published and cfg.gmail_username:
        from outwire.publisher.email_backup import send_digest_email
        send_digest_email(cfg.gmail_username, cfg.gmail_app_password, title, digest_html)

    log.info("pipeline_complete", issue=issue_number, published=published)


def cli() -> None:
    parser = argparse.ArgumentParser(description="Outwire AI Security digest pipeline")
    parser.add_argument("--publish", action="store_true", help="Publish to Substack")
    parser.add_argument("--dry-run", action="store_true", help="Collect + score + generate, no publish")
    parser.add_argument("--no-llm", action="store_true", help="Collect only, skip LLM")
    parser.add_argument("--no-email", action="store_true", help="Create draft but do not send email")
    parser.add_argument("--reuse-last", action="store_true", help="Skip LLM, republish from last cached output")
    args = parser.parse_args()

    cfg = Config()
    if args.dry_run:
        cfg.dry_run = True
    if args.no_llm:
        cfg.no_llm = True
    if args.no_email:
        cfg.no_email = True
        cfg.publish_send_email = False

    try:
        run(cfg, publish=args.publish, no_llm=args.no_llm, reuse_last=args.reuse_last)
    except Exception as exc:
        log.error("pipeline_error", error=str(exc))
        sys.exit(1)


if __name__ == "__main__":
    cli()
