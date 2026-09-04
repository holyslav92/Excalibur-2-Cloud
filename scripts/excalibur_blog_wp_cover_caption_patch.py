#!/usr/bin/env python3
"""Live patch WP posts by post_id: empty featured caption, short SEO cover/inline alt."""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from pathlib import Path
from typing import Any

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from excalibur_blog_image_caption_builder import (  # noqa: E402
    ALT_SEO_MAX,
    clamp_seo_alt,
    is_prompt_like_alt,
    production_alt_hits,
)
from excalibur_blog_wp_publish import (  # noqa: E402
    load_env,
    project_root,
    publish_via_sftp,
    validate_publish_env,
)

DEFAULT_JOBS: list[dict[str, Any]] = [
    {
        "post_id": 9490,
        "cover_alt": "Смена юрлица застройщика в Тюмени — проверка нового ДДУ.",
        "fix_inline_src": False,
    },
    {
        "post_id": 9465,
        "cover_alt": "Бронь новостройки в Тюмени — цена выросла за двое суток.",
        "fix_inline_src": False,
    },
    {
        "post_id": 9439,
        "cover_alt": "Мокрая стяжка на приёмке новостройки в Тюмени.",
        "fix_inline_src": True,
    },
    {
        "post_id": 9411,
        "cover_alt": "Траншевая ипотека в Тюмени — рост платежа по траншам.",
        "fix_inline_src": False,
    },
    {
        "post_id": 9452,
        "cover_alt": "Семейная ипотека одобрена — эскроу не открыли в Тюмени.",
        "fix_inline_src": False,
    },
]

LONG_COVER_PATTERNS = (
    "святослав шакин покупатель",
    "святослав шакин риэлтор",
    "святослав шакин в офисе",
    "рядом лежит",
    "отображается",
    "у стойки регистрации",
)


def shorten_visible_alt(raw: str, *, fallback: str = "") -> str:
    text = " ".join(str(raw or "").split()).strip()
    low = text.casefold()
    if any(p in low for p in LONG_COVER_PATTERNS) or production_alt_hits(text):
        text = fallback or text
    bad, _ = is_prompt_like_alt(text, seo_length=False)
    if bad and fallback:
        text = fallback
    if len(text) > ALT_SEO_MAX:
        text = clamp_seo_alt(text)
    elif text and not text.endswith((".", "!", "?", "…")):
        text = f"{text.rstrip('.') }."
    return text


def fix_post_html(html: str, *, cover_alt_fallback: str, fix_inline_src: bool) -> str:
    out = html
    if fix_inline_src:
        # Map cover/inline-NN.png -> first matching uploads URL already in HTML.
        uploads: dict[str, str] = {}
        for m in re.finditer(r'src="(https?://[^"]+/wp-content/uploads/[^"]*inline-(\d+)\.png)"', out, re.I):
            uploads[f"inline-{m.group(2)}.png"] = m.group(1)
            uploads[f"cover/inline-{m.group(2)}.png"] = m.group(1)
        for rel, url in uploads.items():
            out = out.replace(f'src="{rel}"', f'src="{url}"')
            out = out.replace(f"src='{rel}'", f"src='{url}'")
        # Broken protocol-relative http://cover/...
        out = re.sub(r'src="https?://cover/inline-(\d+)\.png"', lambda m: f'src="{uploads.get(f"inline-{m.group(1)}.png", m.group(0))}"', out, flags=re.I)

    def _repl_img(match: re.Match[str]) -> str:
        prefix, quote, alt, suffix = match.group(1), match.group(2), match.group(3), match.group(4)
        new_alt = shorten_visible_alt(alt, fallback=cover_alt_fallback if "cover" in prefix.casefold() else "")
        return f"<img{prefix}alt={quote}{new_alt}{quote}{suffix}>"

    out = re.sub(r"<img\b([^>]*?)\balt=(['\"])(.*?)\2([^>]*)>", _repl_img, out, flags=re.I | re.S)
    out = re.sub(r"<figcaption\b[^>]*>.*?</figcaption>", "", out, flags=re.I | re.S)
    return out


def build_media_php(jobs: list[dict[str, Any]]) -> str:
    payload = {"jobs": jobs}
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/post.php';
$p = json_decode(base64_decode('{b64}'), true);
foreach (($p['jobs'] ?? []) as $job) {{
    $post_id = (int) ($job['post_id'] ?? 0);
    $cover_alt = sanitize_text_field((string) ($job['cover_alt'] ?? ''));
    if ($post_id <= 0) continue;
    $thumb_id = (int) get_post_thumbnail_id($post_id);
    if ($thumb_id > 0) {{
        wp_update_post(array('ID' => $thumb_id, 'post_excerpt' => '', 'post_content' => ''));
        update_post_meta($thumb_id, '_wp_attachment_image_alt', $cover_alt);
        echo 'OK featured_meta=' . $thumb_id . ' post=' . $post_id . PHP_EOL;
    }}
    foreach (get_attached_media('image', $post_id) as $att) {{
        if ((int) $att->ID === $thumb_id) continue;
        $alt = sanitize_text_field((string) get_post_meta($att->ID, '_wp_attachment_image_alt', true));
        wp_update_post(array('ID' => $att->ID, 'post_excerpt' => '', 'post_content' => ''));
        update_post_meta($att->ID, '_wp_attachment_image_alt', $alt);
        echo 'OK inline_meta=' . $att->ID . ' post=' . $post_id . PHP_EOL;
    }}
}}
echo 'OK media_done' . PHP_EOL;
"""


def build_body_php(post_id: int, content: str) -> str:
    payload = {"post_id": post_id, "content": content}
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{b64}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
wp_update_post(array('ID' => $post_id, 'post_content' => wp_slash((string) ($p['content'] ?? ''))));
echo 'OK body_updated=' . $post_id . PHP_EOL;
"""


def fetch_post_html(post_id: int) -> str:
    from excalibur_blog_wp_live_patch import parse_wp_publish_attachments  # noqa: WPS433

    _ = parse_wp_publish_attachments
    # MCP wordpress_get_post_content via subprocess-free import
    import importlib

    # Use REST from env if available; fallback: no local REST — call MCP tool through helper script.
    root = project_root()
    env = load_env(root)
    api = env.get("WP_API_URL") or env.get("WORDPRESS_API_URL") or ""
    user = env.get("WP_USER") or env.get("WORDPRESS_USER") or ""
    password = env.get("WP_APP_PASSWORD") or env.get("WORDPRESS_APP_PASSWORD") or ""
    if api and user and password:
        import urllib.request

        url = f"{api.rstrip('/')}/wp-json/wp/v2/posts/{post_id}?context=edit"
        req = urllib.request.Request(url)
        import base64 as b64mod

        token = b64mod.b64encode(f"{user}:{password}".encode()).decode()
        req.add_header("Authorization", f"Basic {token}")
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return str(data.get("content", {}).get("raw") or data.get("content", {}).get("rendered") or "")
    raise RuntimeError(f"cannot fetch post {post_id}: WP API credentials missing in env")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--media-only", action="store_true")
    ap.add_argument("--body-only", action="store_true")
    args = ap.parse_args()

    jobs = DEFAULT_JOBS
    root = project_root()
    env = load_env(root)
    public = env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or ""

    if args.dry_run:
        print(json.dumps(jobs, ensure_ascii=False, indent=2))
        return 0

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

    report: list[str] = []

    if not args.body_only:
        out = publish_via_sftp(env, build_media_php(jobs), public, bootstrap_name="excalibur-cover-caption-media.php")
        print(out)
        report.append(out)
        if "OK media_done" not in out:
            return 1

    if not args.media_only:
        for job in jobs:
            post_id = int(job["post_id"])
            try:
                html = fetch_post_html(post_id)
            except RuntimeError:
                # Fallback: CallDynamicTool not available in script — use MCP via shell curl to tool
                print(f"BLOCKER: fetch post {post_id} failed", file=sys.stderr)
                return 1
            fixed = fix_post_html(
                html,
                cover_alt_fallback=str(job.get("cover_alt") or ""),
                fix_inline_src=bool(job.get("fix_inline_src")),
            )
            if fixed == html:
                print(f"SKIP body unchanged post={post_id}")
                continue
            # Shorten inline img alts in content
            for m in list(re.finditer(r'\balt=(["\'])(.*?)\1', fixed)):
                old = m.group(2)
                new = shorten_visible_alt(old)
                if new != old:
                    fixed = fixed.replace(f'alt={m.group(1)}{old}{m.group(1)}', f'alt={m.group(1)}{new}{m.group(1)}', 1)
            out = publish_via_sftp(
                env,
                build_body_php(post_id, fixed),
                public,
                bootstrap_name=f"excalibur-cover-caption-body-{post_id}.php",
            )
            print(out)
            report.append(out)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
