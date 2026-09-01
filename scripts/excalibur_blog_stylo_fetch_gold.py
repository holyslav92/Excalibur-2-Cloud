#!/usr/bin/env python3
"""Скачать GOLD corpus для стилометрии (ритм/голос, не сюжет для Scout).

Не копировать сюжеты в Scout — только memory/stylo/gold/*.txt.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_site_base import (  # noqa: E402
    SITE_BASE_PLACEHOLDER,
    expand_site_base,
    resolve_public_base_from_env,
)
from excalibur_blog_stylo import extract_article_body_html, split_paragraphs_from_html, strip_html  # noqa: E402

# Только path — в git/meta хранится {{SITE_BASE}}/path
GOLD_PATHS: list[tuple[str, str]] = [
    (
        "kupili-kvartiru-bankrotstvo",
        "/blog/vtorichka-i-riski/kupili-kvartiru-v-tyumeni-prodavec-ushel-v-bankrotstvo-finupravlyayuschij-ospori/",
    ),
    (
        "egrn-stroka-avans",
        "/blog/vtorichka-i-riski/v-vypiske-egrn-est-stroka-posle-kotoroj-avans-nelzya/",
    ),
    (
        "vypiska-chisto-tri-mesyaca",
        "/blog/vtorichka-i-riski/v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca/",
    ),
    (
        "rodstvenniki-osporili-prodazhu",
        "/blog/vtorichka-i-riski/rodstvenniki-osporili-prodazhu-v-proshloj-sdelke-deneg-ne-bylo/",
    ),
    (
        "babushka-sobstvennik-osmotr",
        "/blog/vtorichka-i-riski/kvartira-v-tyumeni-babushka-sobstvennik-v-obyavlenii-na-osmotre-pered-avansom-ee/",
    ),
    (
        "akkreditiv-dengi-ne-doshli",
        "/blog/vtorichka-i-riski/akkreditiv-otkryli-prodavcu-dengi-ne-doshli-sdelku-v-tyumeni-sorvali/",
    ),
    (
        "propisannye-pered-avansom",
        "/blog/vtorichka-i-riski/v-tyumeni-pered-avansom-nashli-propisannyh-prodavec-obeschal-vypisat-za-nedelyu/",
    ),
    (
        "dolya-kommunalnaya-sosed",
        "/blog/vtorichka-i-riski/v-tyumeni-kupili-dolyu-v-kommunalnoj-kvartire-sosed-sorval-sdelku-za-den-do-avan/",
    ),
    (
        "chetyre-mesyaca-vtorichka",
        "/blog/vtorichka-i-riski/v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri/",
    ),
    (
        "transhevaya-ipoteka-novostrojka",
        "/blog/ipoteka/transhevaya-ipoteka-novostrojka-tyumen/",
    ),
]


def live_url(path: str, public_base: str) -> str:
    git_path = f"{SITE_BASE_PLACEHOLDER}{path}"
    return expand_site_base(git_path, public_base)


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "ExcaliburStyloGold/1.0"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def extract_title(html: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, flags=re.I | re.S)
    if m:
        return strip_html(m.group(1))
    m = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
    return strip_html(m.group(1)) if m else ""


def html_to_plain_article(html: str) -> str:
    body = extract_article_body_html(html)
    paras = split_paragraphs_from_html(f"<article>{body}</article>")
    return "\n\n".join(paras)


def wp_search_resolve(title_hint: str, public_base: str) -> str | None:
    q = title_hint[:48]
    api = f"{live_url('/wp-json/wp/v2/posts', public_base)}?search={urllib.parse.quote(q)}&per_page=3"
    req = urllib.request.Request(api, headers={"User-Agent": "ExcaliburStyloGold/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, json.JSONDecodeError):
        return None
    if not data:
        return None
    return data[0].get("link")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch stylo gold corpus")
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parents[1] / "memory/stylo/gold")
    args = parser.parse_args()
    out_dir: Path = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    public_base = resolve_public_base_from_env()
    if not public_base:
        print("FAIL PUBLIC_SITE_URL unset — нужен для live fetch", file=sys.stderr)
        return 2

    posts_meta: list[dict[str, str | bool]] = []
    for slug, path in GOLD_PATHS:
        url = live_url(path, public_base)
        html = ""
        try:
            html = fetch_url(url)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                resolved = wp_search_resolve(slug.replace("-", " "), public_base)
                if resolved:
                    print(f"WARN 404 {path} -> {resolved}")
                    html = fetch_url(resolved)
                    url = resolved
            if not html:
                print(f"FAIL fetch {path}: {exc}", file=sys.stderr)
                return 2

        title = extract_title(html)
        plain = html_to_plain_article(html)
        if len(plain) < 200:
            print(f"FAIL слишком короткий текст {slug}", file=sys.stderr)
            return 2

        (out_dir / f"{slug}.txt").write_text(plain + "\n", encoding="utf-8")
        git_url = f"{SITE_BASE_PLACEHOLDER}{path}"
        posts_meta.append(
            {
                "slug": slug,
                "title": title,
                "url": git_url,
                "style_gold": True,
                "plot_for_scout": False,
            }
        )
        print(f"OK {slug} ({len(plain)} chars) — {title[:60]}")

    meta = {
        "description": "GOLD style corpus — rhythm/voice only. Plots FROZEN; Scout must NOT reuse.",
        "market_note": "Secondary hits + one tightened newbuild; newbuild_only pipeline unchanged.",
        "posts": posts_meta,
    }
    (out_dir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(posts_meta)} files -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
