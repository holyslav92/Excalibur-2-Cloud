#!/usr/bin/env python3
"""Приводит schema.jsonld к канону gate: {{SITE_BASE}}/<slug>/ без /blog/."""
import json
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: excalibur_blog_schema_slug_fixup.py <article-dir>", file=sys.stderr)
        return 2
    adir = Path(sys.argv[1])
    meta = json.loads((adir / "article.meta.json").read_text(encoding="utf-8"))
    slug = meta["slug"]
    schema_path = adir / "schema.jsonld"
    text = schema_path.read_text(encoding="utf-8")
    # Убрать /blog/<category>/ перед slug в URL-путях
    text = re.sub(
        r"\{\{SITE_BASE\}\}/blog/[^/\"]+/" + re.escape(slug),
        "{{SITE_BASE}}/" + slug,
        text,
    )
    # Любой оставшийся /blog/.../slug
    text = re.sub(
        r"\{\{SITE_BASE\}\}/blog/[^\"']+",
        lambda m: m.group(0) if slug not in m.group(0) else "{{SITE_BASE}}/" + slug,
        text,
    )
    if f"{{{{SITE_BASE}}}}/{slug}/" not in text:
        # Жёсткая подстановка для BlogPosting url/@id если Derouter сломал
        canon = f"{{{{SITE_BASE}}}}/{slug}/"
        text = re.sub(
            r'"url":\s*"[^"]*"',
            f'"url": "{canon}"',
            text,
            count=1,
        )
    schema_path.write_text(text, encoding="utf-8")
    print(json.dumps({"status": "ok", "slug": slug, "path": str(schema_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
