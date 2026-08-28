#!/usr/bin/env python3
"""Assemble Derouter user prompt for cover-text with exact meme id roster."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from excalibur_blog_meme_canon import catalog_meme_id_roster, load_meme_catalog
from excalibur_blog_quad_slots import active_inline_keys, inline_count_from_tenant


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_h2_sections(article_html: Path) -> list[tuple[str, list[str]]]:
    if not article_html.is_file():
        return []
    text = article_html.read_text(encoding="utf-8")
    sections: list[tuple[str, list[str]]] = []
    current_title = ""
    bullets: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>|<li[^>]*>(.*?)</li>", text, flags=re.I | re.S):
        if match.group(1) is not None:
            if current_title:
                sections.append((current_title, bullets[:8]))
            current_title = re.sub(r"<[^>]+>", "", match.group(1))
            current_title = re.sub(r"\s+", " ", current_title).strip()
            bullets = []
            continue
        if not current_title:
            continue
        item = re.sub(r"<[^>]+>", "", match.group(2) or "")
        item = re.sub(r"\s+", " ", item).strip()
        if item and len(item) < 120:
            bullets.append(item)
    if current_title:
        sections.append((current_title, bullets[:8]))
    return sections


def recent_meme_ids(root: Path, days: int = 14) -> list[str]:
    path = root / "memory/cover/used-motifs.json"
    if not path.is_file():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    recent: list[str] = []
    for row in data.get("recent") or []:
        if not isinstance(row, dict):
            continue
        meme = row.get("meme") or row.get("meme_ids") or []
        if isinstance(meme, str):
            recent.append(meme)
        elif isinstance(meme, list):
            recent.extend(str(x) for x in meme if str(x).strip())
    return sorted(set(recent))


def build_markdown(article_dir: Path, root: Path) -> str:
    meta = load_json(article_dir / "article.meta.json")
    tenant_path = root / "shared/tenant-config.json"
    tenant = load_json(tenant_path) if tenant_path.is_file() else {}
    inline_count = inline_count_from_tenant(tenant)
    catalog = load_meme_catalog(root)
    roster = catalog_meme_id_roster(catalog)
    anti_repeat = recent_meme_ids(root)

    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]
    title = str(meta.get("title") or meta.get("h1") or "").strip()
    sections = extract_h2_sections(article_dir / "article.html")
    inline_keys = active_inline_keys(inline_count)

    lines = [
        f"# Cover-text inputs — {topic_id}",
        "",
        "ROLE: cover-text. Выход: только валидный JSON без markdown fences.",
        "",
        "## Контекст",
        "",
        f"- topic_id: {topic_id}",
        f"- tenant: {tenant.get('brand_name') or 'The Риэлтор'}, {tenant.get('city') or 'Тюмень'}",
        f"- H1: {title}",
        "",
        "## Meme picks (HARD — exact catalog ids only)",
        "",
        "Каталог: `memory/cover/meme-top100.json`. **Не выдумывай** id вроде `business_cat`.",
        "",
        f"ALLOWED IDS ({len(roster)}): " + ", ".join(roster),
        "",
        "- Variety: people + cats (не cats-only)",
        f"- Slots: cover (1–2), {', '.join(k for k in inline_keys if k in {'inline_1', 'inline_5', 'inline_7'})}",
    ]
    if anti_repeat:
        lines.append(f"- Anti-repeat 14д — не использовать: {', '.join(anti_repeat)}")
    lines.extend(
        [
            "",
            "## Правила gate",
            "",
            "- hook: **4–7** слов, highlight = одно слово из hook",
            "- sticky: до 5 слов",
            "- phone_cta: +7 922 001 65 05",
            f"- inline_labels: 2–6 подписей на {', '.join(inline_keys)}",
            "- Только кириллица (латиница только бренды)",
            "",
            "## Факты из article.html для inline_labels",
            "",
        ]
    )
    for idx, key in enumerate(inline_keys):
        title_h2 = sections[idx][0] if idx < len(sections) else f"Секция {idx + 1}"
        bullets = sections[idx][1] if idx < len(sections) else []
        lines.append(f"### {key} — {title_h2}")
        for bullet in bullets[:6]:
            lines.append(f"- {bullet}")
        if not bullets:
            lines.append("- (извлеки 2–6 коротких фактов из параграфа под H2)")
        lines.append("")

    lines.extend(
        [
            "## JSON shape",
            "",
            "```json",
            "{",
            '  "hook": "...",',
            '  "highlight": "...",',
            '  "sticky": "...",',
            '  "phone_cta": "+7 922 001 65 05",',
            '  "inline_labels": { ... },',
            '  "meme_picks": { "cover": ["id1", "id2"], "inline_1": ["id"] }',
            "}",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument(
        "-o",
        "--output",
        default="assembled-cover-text-inputs.md",
        help="Output path relative to article dir unless absolute",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    if not article_dir.is_dir():
        print(f"FAIL: article dir missing: {article_dir}", file=sys.stderr)
        return 2

    md = build_markdown(article_dir, root)
    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = article_dir / out_path
    out_path.write_text(md, encoding="utf-8")
    print(f"OK cover-text inputs → {out_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
