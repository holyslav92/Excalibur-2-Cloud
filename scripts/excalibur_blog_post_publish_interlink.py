#!/usr/bin/env python3
"""Post-publish interlink when tenant.interlink_old_articles=true."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from excalibur_blog_interlink_lib import (
    all_interlink_candidates,
    build_inbound_updates,
    build_interlink_bootstrap_php,
    build_new_article_urls,
    expand_inbound_updates_for_runtime,
    git_safe_inbound_plan,
    load_tenant,
    outbound_links_in_html,
    pick_inbound_targets,
    project_root,
    validate_inbound_updates_href,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-inbound", type=int, default=3)
    args = parser.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    tenant = load_tenant(root)
    if not tenant.get("interlink_old_articles"):
        print("OK interlink skip: interlink_old_articles=false")
        return 0

    meta_path = article_dir / "article.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    topic_id = str(meta.get("topic_id") or "").upper()
    slug = str(meta.get("slug") or "").strip()
    title = str(meta.get("title") or meta.get("h1") or "").strip()
    if not slug:
        print("FAIL interlink: slug missing in article.meta.json", file=sys.stderr)
        return 2

    candidates = all_interlink_candidates(root, exclude_topic_id=topic_id)
    html_path = article_dir / "article.html"
    html = html_path.read_text(encoding="utf-8") if html_path.is_file() else ""
    outbound_found = outbound_links_in_html(html, candidates)
    outbound_missing = [row for row in candidates if row not in outbound_found]
    inbound_targets = pick_inbound_targets(candidates, new_slug=slug, max_inbound=args.max_inbound)

    public = os.environ.get("PUBLIC_SITE_URL", "").strip()
    runtime_url, git_safe_url = build_new_article_urls(slug, article_dir, root, public)

    inbound_runtime = build_inbound_updates(
        new_slug=slug,
        new_title=title,
        new_url=runtime_url,
        targets=inbound_targets,
    )
    inbound_plan = git_safe_inbound_plan(
        build_inbound_updates(
            new_slug=slug,
            new_title=title,
            new_url=git_safe_url,
            targets=inbound_targets,
        ),
        public,
    )

    href_errors = validate_inbound_updates_href(inbound_runtime, slug)
    if href_errors:
        for err in href_errors:
            print(f"FAIL interlink: {err}", file=sys.stderr)
        return 2

    plan = {
        "topic_id": topic_id,
        "slug": slug,
        "title": title,
        "outbound_required_min": 1 if candidates else 0,
        "outbound_found": outbound_found,
        "outbound_missing_suggestions": outbound_missing[:3],
        "inbound_targets": inbound_targets,
        "inbound_updates": inbound_plan,
        "new_url": git_safe_url,
        "dry_run": bool(args.dry_run),
    }
    plan_path = article_dir / "interlink-plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if candidates and len(outbound_found) < 1:
        print(
            "WARN interlink: article.html has no links to published siblings; "
            "add 1–3 contextual links before publish",
            file=sys.stderr,
        )

    print(json.dumps(plan, ensure_ascii=False, indent=2))
    if args.dry_run:
        print("OK interlink dry-run plan written")
        return 0

    if os.environ.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("OK interlink plan only (ALLOW_PUBLISH not yes; inbound skip)")
        return 0

    if not public:
        print("WARN interlink inbound skip: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 0

    if not inbound_runtime:
        print("OK interlink: no inbound targets with post_id")
        return 0

    from excalibur_blog_wp_publish import load_env, publish_via_sftp, validate_publish_env

    env = load_env(root)
    missing = validate_publish_env(env)
    if missing:
        print(f"WARN interlink inbound skip: missing env {', '.join(missing)}", file=sys.stderr)
        return 0

    inbound_apply = expand_inbound_updates_for_runtime(inbound_runtime, public)
    php = build_interlink_bootstrap_php({"updates": inbound_apply})
    out = publish_via_sftp(env, php, public, bootstrap_name="excalibur-blog-interlink-once.php")
    print(out)
    if "OK interlink_done" not in out and "OK interlink_inbound=" not in out and "OK interlink_skip=" not in out:
        print("FAIL interlink inbound bootstrap", file=sys.stderr)
        return 2
    print(f"OK interlink inbound applied: {len(inbound_apply)} targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
