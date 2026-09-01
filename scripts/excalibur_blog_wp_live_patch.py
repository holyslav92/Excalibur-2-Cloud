#!/usr/bin/env python3
"""Live patch published WP posts: body-only or media-meta-only (no cover regen)."""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from datetime import date
from html import unescape
from pathlib import Path
from typing import Any

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from excalibur_blog_wp_publish import (  # noqa: E402
    expand_site_base,
    load_env,
    project_root,
    publish_via_sftp,
    validate_publish_env,
)


def parse_wp_publish_attachments(raw_output: str) -> dict[str, Any]:
    featured_id = 0
    inline: list[dict[str, Any]] = []
    post_id = 0
    for line in (raw_output or "").splitlines():
        line = line.strip()
        if line.startswith("OK post="):
            try:
                post_id = int(line.split("=", 1)[1].strip().split()[0])
            except ValueError:
                post_id = 0
        elif line.startswith("OK featured_image="):
            try:
                featured_id = int(line.split("=", 1)[1].strip())
            except ValueError:
                featured_id = 0
        elif line.startswith("OK inline_image_upload="):
            m = re.match(r"OK inline_image_upload=(\d+)\s+src=(\S+)", line)
            if m:
                inline.append({"id": int(m.group(1)), "src": m.group(2)})
    return {"post_id": post_id, "featured_id": featured_id, "inline": inline}


def ledger_articles_since(root: Path, since: str) -> list[dict[str, str]]:
    ledger = root / "shared" / "published-articles.md"
    if not ledger.is_file():
        return []
    since_d = date.fromisoformat(since)
    rows: list[dict[str, str]] = []
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        try:
            row_date = date.fromisoformat(parts[0])
        except ValueError:
            continue
        if row_date < since_d:
            continue
        rows.append(
            {
                "date": parts[0],
                "topic_id": parts[1],
                "slug": parts[2],
                "path": parts[3],
                "status": parts[4],
            }
        )
    return rows


def find_article_dir(root: Path, topic_id: str, slug: str) -> Path | None:
    base = root / "memory" / "blog" / "articles"
    for path in base.iterdir():
        if not path.is_dir():
            continue
        if path.name.startswith(f"{topic_id}-") or slug in path.name:
            meta = path / "article.meta.json"
            if meta.is_file():
                try:
                    data = json.loads(meta.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    continue
                if str(data.get("topic_id") or "") == topic_id or str(data.get("slug") or "") == slug:
                    return path
    return None


def build_media_meta_payload(article_dir: Path, root: Path, public_base: str) -> dict[str, Any]:
    from excalibur_blog_image_caption_builder import apply_article_captions, resolve_slot_alt, load_hero_name, load_visual_type_labels
    from excalibur_blog_wp_publish import load_json as _lj, registry_asset_index, resolve_cover_media_fields

    apply_article_captions(article_dir, root)
    meta_path = article_dir / "article.meta.json"
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    registry_path = article_dir / "cover" / "cover-registry.json"
    html_path = article_dir / "article.html"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    registry = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.is_file() else {}
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)

    wp_result_path = article_dir / "wp-publish-result.json"
    if not wp_result_path.is_file():
        raise FileNotFoundError(f"missing {wp_result_path}")
    wp_result = json.loads(wp_result_path.read_text(encoding="utf-8"))
    att = parse_wp_publish_attachments(str(wp_result.get("raw_output") or ""))
    post_id = int(meta.get("wp_post_id") or att["post_id"] or wp_result.get("post_id") or 0)
    if post_id <= 0:
        raise ValueError("wp_post_id missing in article.meta.json / wp-publish-result.json")

    cover_media = resolve_cover_media_fields(meta, registry, quad_manifest=manifest, article_dir=article_dir, root=root)
    attachments: list[dict[str, Any]] = []
    if att["featured_id"]:
        attachments.append(
            {
                "id": att["featured_id"],
                "role": "cover",
                "alt": cover_media["alt"],
                "caption": "",
                "description": cover_media["description"],
                "title": cover_media["title"],
            }
        )

    assets = registry_asset_index(registry)
    src_to_slot: dict[str, str] = {}
    for slot_key, slot in (manifest.get("slots") or {}).items():
        if not isinstance(slot, dict) or slot_key == "cover":
            continue
        idx = slot_key.split("_")[-1]
        src_to_slot[f"inline-{idx}.png"] = slot_key

    for item in att["inline"]:
        src = str(item.get("src") or "")
        basename = Path(src.replace("\\", "/")).name
        slot_key = src_to_slot.get(basename, "")
        slot = (manifest.get("slots") or {}).get(slot_key) or {}
        alt = resolve_slot_alt(slot_key, slot, manifest, meta, host_name=host_name, labels_map=labels_map) if slot_key else ""
        asset = assets.get(src) or assets.get(basename) or {}
        if not alt:
            alt = str(asset.get("alt") or "")
        attachments.append(
            {
                "id": int(item["id"]),
                "role": "inline",
                "src": src,
                "alt": alt,
                "caption": "",
                "description": alt,
                "title": alt[:120],
            }
        )

    # Sync inline alts in local HTML for consistency.
    if html_path.is_file():
        html = html_path.read_text(encoding="utf-8")
        new_html = html
        for slot_key, slot in (manifest.get("slots") or {}).items():
            if slot_key == "cover" or not isinstance(slot, dict):
                continue
            alt = resolve_slot_alt(slot_key, slot, manifest, meta, host_name=host_name, labels_map=labels_map)
            pattern = re.compile(
                rf'(<figure[^>]*\bdata-slot="{re.escape(slot_key)}"[^>]*>\s*<img\b[^>]*\balt=")([^"]*)(")',
                re.I | re.S,
            )
            new_html, _ = pattern.subn(rf"\1{alt}\3", new_html, count=1)
        if new_html != html:
            html_path.write_text(new_html, encoding="utf-8", newline="\n")

    return {"post_id": post_id, "slug": meta.get("slug", ""), "attachments": attachments}


def build_body_payload(article_dir: Path, public_base: str) -> dict[str, Any]:
    meta = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    html = (article_dir / "article.html").read_text(encoding="utf-8").strip()
    post_id = int(meta.get("wp_post_id") or 0)
    if post_id <= 0:
        raise ValueError("wp_post_id required for body-only patch")
    return {
        "post_id": post_id,
        "slug": meta.get("slug", ""),
        "content": expand_site_base(html, public_base),
    }


def build_media_meta_php(payload: dict[str, Any]) -> str:
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

$p = json_decode(base64_decode('{b64}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
if ($post_id <= 0) {{
    echo 'ERR missing post_id' . PHP_EOL;
    exit(1);
}}
$n = 0;
foreach (($p['attachments'] ?? []) as $item) {{
    $att_id = (int) ($item['id'] ?? 0);
    if ($att_id <= 0) {{
        continue;
    }}
    $update = ['ID' => $att_id];
    if (array_key_exists('title', $item) && $item['title'] !== '') {{
        $update['post_title'] = sanitize_text_field((string) $item['title']);
    }}
    if (array_key_exists('caption', $item)) {{
        $update['post_excerpt'] = sanitize_text_field((string) $item['caption']);
    }}
    if (array_key_exists('description', $item) && $item['description'] !== '') {{
        $update['post_content'] = wp_kses_post((string) $item['description']);
    }}
    if (count($update) > 1) {{
        wp_update_post($update);
    }}
    if (!empty($item['alt'])) {{
        update_post_meta($att_id, '_wp_attachment_image_alt', sanitize_text_field((string) $item['alt']));
    }}
    $n++;
    echo 'OK attachment_meta=' . $att_id . ' role=' . (string) ($item['role'] ?? '') . PHP_EOL;
}}
echo 'OK media_meta_patched=' . $n . ' post=' . $post_id . PHP_EOL;
"""


def build_body_php(payload: dict[str, Any]) -> str:
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/post.php';

$p = json_decode(base64_decode('{b64}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
if ($post_id <= 0) {{
    echo 'ERR missing post_id' . PHP_EOL;
    exit(1);
}}
wp_update_post([
    'ID' => $post_id,
    'post_content' => wp_slash((string) ($p['content'] ?? '')),
]);
echo 'OK body_updated=' . $post_id . ' slug=' . (string) ($p['slug'] ?? '') . PHP_EOL;
"""


def html_to_owner_md(html: str) -> str:
    text = html
    text = re.sub(r"<h2[^>]*>(.*?)</h2>", r"\n\n## \1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"\n\n### \1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", text, flags=re.I | re.S)
    text = re.sub(r"<li[^>]*>(.*?)</li>", r"- \1\n", text, flags=re.I | re.S)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", action="append", default=[])
    ap.add_argument("--batch-since", default="", help="Patch ledger published rows since YYYY-MM-DD")
    ap.add_argument("--media-meta-only", action="store_true")
    ap.add_argument("--body-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--public-base", default="")
    args = ap.parse_args()

    if bool(args.media_meta_only) == bool(args.body_only):
        print("BLOCKER: specify exactly one of --media-meta-only or --body-only", file=sys.stderr)
        return 2

    root = project_root()
    env = load_env(root)
    public = args.public_base or env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or ""

    targets: list[Path] = []
    for raw in args.article_dir:
        p = Path(raw)
        if not p.is_absolute():
            p = root / p
        targets.append(p)

    if args.batch_since:
        for row in ledger_articles_since(root, args.batch_since):
            if row.get("status") != "published":
                continue
            ad = find_article_dir(root, row["topic_id"], row["slug"])
            if ad and ad not in targets:
                targets.append(ad)

    if not targets:
        print("BLOCKER: no article dirs resolved", file=sys.stderr)
        return 2

    if not args.dry_run:
        if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
            print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
            return 1
        missing = validate_publish_env(env)
        if missing:
            print(f"BLOCKER: missing publish env: {', '.join(missing)}", file=sys.stderr)
            return 2
        if not public:
            print("BLOCKER: PUBLIC_SITE_URL required", file=sys.stderr)
            return 2

    report: list[dict[str, Any]] = []
    for article_dir in targets:
        slug = article_dir.name
        try:
            if args.media_meta_only:
                payload = build_media_meta_payload(article_dir, root, public)
                php = build_media_meta_php(payload)
                mode = "media-meta-only"
            else:
                payload = build_body_payload(article_dir, public)
                php = build_body_php(payload)
                mode = "body-only"
                if not args.dry_run:
                    md_path = article_dir / "article.md"
                    md_path.write_text(html_to_owner_md(payload["content"]), encoding="utf-8")
            if args.dry_run:
                out = f"DRY_RUN {mode} post_id={payload.get('post_id')}"
            else:
                bootstrap = f"excalibur-live-patch-{payload.get('post_id')}.php"
                out = publish_via_sftp(env, php, public, bootstrap_name=bootstrap)
                print(out)
            report.append({"article_dir": str(article_dir), "mode": mode, "status": "OK", "output": out})
        except Exception as exc:  # noqa: BLE001
            report.append({"article_dir": str(article_dir), "status": "BLOCKER", "error": str(exc)})

    print(json.dumps({"patched": report}, ensure_ascii=False, indent=2))
    return 0 if all(r.get("status") == "OK" for r in report) else 1


if __name__ == "__main__":
    raise SystemExit(main())
