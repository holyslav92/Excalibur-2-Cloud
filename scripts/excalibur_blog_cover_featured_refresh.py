#!/usr/bin/env python3
"""Замена только featured cover на live WP-постах (SFTP bootstrap).

Читает memory/blog/cover-regen/regen-plan.json, заливает cover.png по post_id.
Не трогает post_content и inline-изображения.
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_wp_publish import load_env, project_root, publish_via_sftp


def build_cover_only_php(payload: dict[str, Any]) -> str:
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

$p = json_decode(base64_decode('{b64}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
if ($post_id <= 0) {{
    echo 'ERR missing post_id' . PHP_EOL;
    exit(1);
}}
$post = get_post($post_id);
if (!$post instanceof WP_Post) {{
    echo 'ERR post not found id=' . $post_id . PHP_EOL;
    exit(1);
}}
echo 'OK post=' . $post_id . ' slug=' . $post->post_name . PHP_EOL;

$bin = base64_decode((string) ($p['cover_b64'] ?? ''));
if ($bin === '' || $bin === false) {{
    echo 'ERR empty cover_b64' . PHP_EOL;
    exit(1);
}}
$slug = sanitize_title((string) ($p['slug'] ?? $post->post_name));
$tmp = wp_tempnam('excalibur-cover-refresh-' . $slug . '.png');
file_put_contents($tmp, $bin);
$file_array = [
    'name' => $slug . '-cover.png',
    'tmp_name' => $tmp,
    'type' => 'image/png',
    'error' => 0,
    'size' => strlen($bin),
];
$cover_meta = [
    'alt' => (string) ($p['cover_alt'] ?? ''),
    'caption' => (string) ($p['cover_caption'] ?? ''),
    'description' => (string) ($p['cover_description'] ?? ''),
    'title' => (string) ($p['cover_title'] ?? ($slug . ' cover')),
];
$att_id = media_handle_sideload($file_array, $post_id, null, [
    'post_title' => $cover_meta['title'],
    'post_excerpt' => $cover_meta['caption'],
    'post_content' => $cover_meta['description'],
]);
if (is_wp_error($att_id)) {{
    echo 'ERR cover: ' . $att_id->get_error_message() . PHP_EOL;
    @unlink($tmp);
    exit(1);
}}
set_post_thumbnail($post_id, (int) $att_id);
if ($cover_meta['alt'] !== '') {{
    update_post_meta((int) $att_id, '_wp_attachment_image_alt', sanitize_text_field($cover_meta['alt']));
}}
@unlink($tmp);
echo 'OK featured_image=' . (int) $att_id . PHP_EOL;
echo 'OK featured_url=' . wp_get_attachment_url((int) $att_id) . PHP_EOL;
"""


def upload_one(root: Path, env: dict[str, str], entry: dict[str, Any], *, dry_run: bool) -> dict[str, Any]:
    post_id = int(entry["post_id"])
    slug = str(entry.get("slug") or "")
    cover_rel = str(entry.get("cover_path") or "")
    cover_path = root / cover_rel
    result: dict[str, Any] = {"post_id": post_id, "slug": slug}

    if not cover_path.is_file():
        result["status"] = "fail"
        result["error"] = f"missing cover: {cover_rel}"
        return result

    alt = str(entry.get("alt_text") or f"Святослав Шакин — {entry.get('hook', '')}")
    payload = {
        "post_id": post_id,
        "slug": slug,
        "cover_b64": base64.b64encode(cover_path.read_bytes()).decode("ascii"),
        "cover_alt": alt,
        "cover_caption": "",
        "cover_description": alt,
        "cover_title": f"{slug} cover",
    }

    if dry_run:
        result["status"] = "dry_run"
        result["bytes"] = cover_path.stat().st_size
        return result

    public = env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or env.get("WP_SITE_URL") or ""
    if not public:
        result["status"] = "fail"
        result["error"] = "PUBLIC_SITE_URL missing"
        return result

    php = build_cover_only_php(payload)
    out = publish_via_sftp(env, php, public)
    result["stdout"] = out
    if "OK featured_image=" in out:
        result["status"] = "uploaded"
        for line in out.splitlines():
            if line.startswith("OK featured_url="):
                result["featured_url"] = line.split("=", 1)[1].strip()
    else:
        result["status"] = "fail"
        result["error"] = "featured upload failed"
    return result


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan", default="memory/blog/cover-regen/regen-plan.json")
    ap.add_argument("--post-id", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = project_root()
    plan_path = root / args.plan
    if not plan_path.is_file():
        print(f"FAIL missing plan {plan_path}", file=sys.stderr)
        return 2

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    if not isinstance(plan, list):
        print("FAIL plan must be a list", file=sys.stderr)
        return 2

    entries = [e for e in plan if e.get("status") == "generated"]
    if args.post_id:
        entries = [e for e in entries if int(e.get("post_id", 0)) == args.post_id]
        if not entries:
            print(f"FAIL no generated entry for post_id={args.post_id}", file=sys.stderr)
            return 2

    env = load_env(root)
    results: list[dict[str, Any]] = []
    failures = 0

    for entry in entries:
        res = upload_one(root, env, entry, dry_run=args.dry_run)
        results.append(res)
        if res.get("status") not in {"uploaded", "dry_run"}:
            failures += 1
        print(json.dumps(res, ensure_ascii=False))

    upload_plan_path = plan_path.parent / "upload-results.json"
    upload_plan_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK upload-results={upload_plan_path} failures={failures}/{len(results)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
