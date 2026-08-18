#!/usr/bin/env python3
"""Post-publish interlink when tenant.interlink_old_articles=true."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from excalibur_blog_site_base import SITE_BASE_PLACEHOLDER, expand_site_base


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_tenant(root: Path) -> dict:
    path = root / "shared/tenant-config.json"
    return json.loads(path.read_text(encoding="utf-8"))


def parse_ledger(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| topic") or line.startswith("|-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        topic_id, slug, status, permalink = cells[:4]
        if status.lower() != "published":
            continue
        rows.append(
            {
                "topic_id": topic_id,
                "slug": slug,
                "permalink": permalink,
            }
        )
    return rows


def slug_in_html(html: str, slug: str) -> bool:
    return slug in html


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

    ledger = parse_ledger(root / "shared/published-articles.md")
    others = [row for row in ledger if row["topic_id"].upper() != topic_id]
    inbound_targets = others[: max(0, args.max_inbound)]

    html_path = article_dir / "article.html"
    html = html_path.read_text(encoding="utf-8") if html_path.is_file() else ""
    outbound_found = [row for row in others if slug_in_html(html, row["slug"])]
    outbound_missing = [row for row in others if row not in outbound_found]

    plan = {
        "topic_id": topic_id,
        "slug": slug,
        "title": title,
        "outbound_required_min": 1 if others else 0,
        "outbound_found": outbound_found,
        "outbound_missing_suggestions": outbound_missing[:3],
        "inbound_targets": inbound_targets,
        "dry_run": bool(args.dry_run),
    }
    plan_path = article_dir / "interlink-plan.json"
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if others and len(outbound_found) < 1:
        print(
            "WARN interlink: article.html has no links to published siblings; "
            "add 1–3 contextual links before publish",
            file=sys.stderr,
        )

    print(json.dumps(plan, ensure_ascii=False, indent=2))
    if args.dry_run:
        print("OK interlink dry-run plan written")
        return 0

    # Inbound WP updates — only when publish credentials + allow flag present.
    import os

    if os.environ.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("OK interlink plan only (ALLOW_PUBLISH not yes; inbound skip)")
        return 0

    public = os.environ.get("PUBLIC_SITE_URL", "").strip()
    if not public:
        print("WARN interlink inbound skip: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 0

    new_url = expand_site_base(f"{SITE_BASE_PLACEHOLDER}/{slug}/", public)
    if not inbound_targets:
        print("OK interlink: no inbound targets")
        return 0

    # WP append delegated to future bootstrap; plan is the contract artifact for now.
    print(
        f"OK interlink plan: inbound {len(inbound_targets)} targets; "
        "apply via shared/interlink-contract.md + manual/media-refresh until bootstrap ships"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
