#!/usr/bin/env python3
"""Stamp assembled-sol-inputs.md with canonical Sol brief + {{SITE_BASE}} CTA URLs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CTA_MARKER = "CTA end:"
SITE_BASE_GUIDES = "{{SITE_BASE}}/gajdy/"
FULL_CTA_RE = re.compile(
    r"CTA end:.*\{\{SITE_BASE\}\}/gajdy/",
    re.IGNORECASE | re.DOTALL,
)


def project_root() -> Path:
    env_root = __import__("os").environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_tenant(root: Path) -> dict[str, Any]:
    return load_json(root / "shared/tenant-config.json")


def build_cta_block(channels: dict[str, Any]) -> str:
    tg = channels.get("telegram_lead") or "https://t.me/Tyumen_Rieltor"
    max_url = channels.get("max") or "https://max.ru/id561413315447_biz"
    dzen = channels.get("dzen") or "https://dzen.ru/holyslav"
    vk = channels.get("vk") or "https://vk.ru/tymenrieltor"
    guides = channels.get("guides") or SITE_BASE_GUIDES
    about = channels.get("about") or "{{SITE_BASE}}/rieltor-tyumen/"
    site = channels.get("site") or "{{SITE_BASE}}"
    phone = channels.get("phone") or "+79220016505"
    phone_display = channels.get("phone_display") or "+7 922 001 65 05"
    return (
        "CTA early (после лида, до H2): excalibur-cta-early — только TG "
        f"{tg} + MAX {max_url}\n"
        "CTA mid (после таблицы/практики): excalibur-cta-mid — TG + MAX\n"
        "CTA end: excalibur-cta-end excalibur-social-cta — dual CTA + полный набор: "
        f"TG, MAX, tel, Дзен {dzen}, VK {vk}, {guides}, {about}\n\n"
        "End CTA HTML (канон — {{SITE_BASE}} для site/guides/about; НЕ голый href=\"/\"):\n"
        f'<p><a href="{tg}">Telegram</a> · <a href="{max_url}">MAX</a> · '
        f'<a href="tel:{phone}">{phone_display}</a> · '
        f'<a href="{site}">Сайт</a> · <a href="{dzen}">Дзен</a> · '
        f'<a href="{vk}">VK</a> · <a href="{guides}">Гайды</a> · '
        f'<a href="{about}">Обо мне</a></p>'
    )


def extract_interlink_paths(writer_html: str) -> list[str]:
    paths: list[str] = []
    for m in re.finditer(r'href="(/blog/[^"]+)"', writer_html or ""):
        p = m.group(1).strip()
        if p not in paths:
            paths.append(p)
    return paths


def read_h1(article_dir: Path) -> str:
    brief = article_dir / "title-brief.json"
    if brief.is_file():
        data = load_json(brief)
        return str(data.get("h1") or data.get("title") or "").strip()
    return ""


def read_comment_magnet(article_dir: Path) -> str:
    writer_inputs = article_dir / "assembled-writer-inputs.md"
    if writer_inputs.is_file():
        text = writer_inputs.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "comment magnet" in line.lower() and "«" in line:
                m = re.search(r"«([^»]+)»", line)
                if m:
                    return m.group(1).strip()
    brief = article_dir / "title-brief.json"
    if brief.is_file():
        data = load_json(brief)
        angle = str(data.get("comment_magnet_angle") or "").strip()
        if angle:
            return angle
    return ""


def has_full_cta_block(text: str) -> bool:
    return bool(FULL_CTA_RE.search(text))


def merge_cta_into_existing(text: str, cta_block: str) -> str:
    if has_full_cta_block(text):
        return text
    # Replace truncated CTA end line
    lines = text.splitlines()
    out: list[str] = []
    replaced = False
    for line in lines:
        if not replaced and line.strip().startswith("CTA early"):
            out.append(cta_block)
            replaced = True
            continue
        if not replaced and line.strip().startswith("CTA end:"):
            out.append(cta_block)
            replaced = True
            continue
        if replaced and line.strip().startswith("CTA "):
            continue
        if replaced and line.strip().startswith("End CTA HTML"):
            continue
        if replaced and line.strip().startswith("<p><a href="):
            continue
        out.append(line)
    if not replaced:
        out.append("")
        out.append(cta_block)
    return "\n".join(out).rstrip() + "\n"


def build_sol_inputs(article_dir: Path, root: Path) -> str:
    topic_id = ""
    meta = article_dir / "article.meta.json"
    if meta.is_file():
        topic_id = str(load_json(meta).get("topic_id") or "")
    if not topic_id:
        m = re.match(r"(B\d+)-", article_dir.name, flags=re.I)
        topic_id = m.group(1).upper() if m else "Bxx"

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    h1 = read_h1(article_dir)
    comment = read_comment_magnet(article_dir)
    channels = load_tenant(root).get("cta_channels") or {}
    cta_block = build_cta_block(channels)

    writer_path = article_dir / "drafts/writer.html"
    interlinks = extract_interlink_paths(writer_path.read_text(encoding="utf-8") if writer_path.is_file() else "")
    interlink_lines = "\n".join(f"  {p}" for p in interlinks[:6]) if interlinks else "  (из drafts/writer.html — 2–4 sibling)"

    comment_line = (
        f"- **Comment magnet:** «{comment}» — сразу после финала casus."
        if comment
        else "- **Comment magnet:** один острый bipolar-вопрос — сразу после финала casus."
    )

    return (
        f"Assembled Sol inputs — {topic_id} — {today}\n\n"
        "ROLE: Sol — перепиши целиком смысл из drafts/writer.html в слог тенанта (SOUL + good-outputs).\n"
        "Выход: только сырой HTML-фрагмент без markdown fences, без h1.\n\n"
        f"H1 context (НЕ в HTML): {h1}\n\n"
        "HARD:\n"
        "- **~1400–1800 слов** (orientir dzen-engagement; hard max 2400; writer длинный — "
        "**ужать** без потери фактов, убрать повторы и recap). Spine once: casus один проход.\n"
        "- Не выдумывать факты/URL. HTML: `<b>` не `<strong>`, `<i>` не `<em>`.\n"
        "- Прозаический лид **4–6 предложений** до первого H2. Без TL;DR, без bullets до первого H2.\n"
        "- **6 H2** из writer — каждый один раз. **7 figure.inline-quad** после H2:\n"
        '<figure class="inline-quad" data-slot="inline_N"><img src="cover/inline-0N.png" alt="" loading="lazy"></figure>\n'
        "(N=1…7, zero-padded inline-01…inline-07)\n"
        "- Interlink сохранить (URL не менять), **2–4 уникальных sibling**:\n"
        f"{interlink_lines}\n"
        "- Телефон один раз в excalibur-cta-end: <a href=\"tel:+79220016505\">+7 922 001 65 05</a>\n"
        f"{comment_line}\n"
        "- **Ending landing:** agency, not panic — не подписывать под давлением; письменный расчёт до акта.\n"
        "- **no composite disclaimer**\n"
        "- Короткие абзацы, диалоги в кавычках, контраст обычный/профи.\n\n"
        f"{cta_block}\n\n"
        "Soul: Klyshin rhythm, Shakin facts. «Расскажу изнутри», не агентство.\n\n"
        "Полный смысл — в drafts/writer.html (переписать в слог, не копировать дословно).\n"
    )


def cmd_stamp(article_dir: Path, root: Path) -> int:
    out_path = article_dir / "assembled-sol-inputs.md"
    if out_path.is_file() and out_path.stat().st_size > 500 and has_full_cta_block(out_path.read_text(encoding="utf-8")):
        print(f"OK assembled-sol-inputs already has full CTA block: {out_path}")
        return 0
    if out_path.is_file() and out_path.stat().st_size > 2000:
        merged = merge_cta_into_existing(out_path.read_text(encoding="utf-8"), build_cta_block(load_tenant(root).get("cta_channels") or {}))
        out_path.write_text(merged, encoding="utf-8")
        print(f"OK merged CTA block into {out_path}")
        return 0
    content = build_sol_inputs(article_dir, root)
    out_path.write_text(content, encoding="utf-8")
    print(f"OK wrote {out_path}")
    return 0


def cmd_check(article_dir: Path) -> int:
    path = article_dir / "assembled-sol-inputs.md"
    if not path.is_file():
        print(f"FAIL assembled-sol-inputs.md missing: {path}", file=sys.stderr)
        return 1
    text = path.read_text(encoding="utf-8")
    if not has_full_cta_block(text):
        print(
            "FAIL assembled-sol-inputs must include CTA end with "
            "{{SITE_BASE}}/gajdy/ and {{SITE_BASE}}/rieltor-tyumen/ — "
            "run excalibur_blog_assemble_sol_inputs.py --stamp",
            file=sys.stderr,
        )
        return 1
    print(f"OK assembled-sol-inputs CTA contract: {path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Stamp/check assembled-sol-inputs.md CTA contract")
    parser.add_argument("--article-dir", required=True, help="memory/blog/articles/<topic>-<slug>")
    parser.add_argument("--stamp", action="store_true", help="Write or merge assembled-sol-inputs.md")
    parser.add_argument("--check", action="store_true", help="FAIL if CTA block incomplete")
    args = parser.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    if not article_dir.is_dir():
        print(f"FAIL article dir not found: {article_dir}", file=sys.stderr)
        return 1
    if args.check:
        return cmd_check(article_dir)
    if args.stamp:
        return cmd_stamp(article_dir, root)
    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
