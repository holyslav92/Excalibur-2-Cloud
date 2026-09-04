#!/usr/bin/env python3
"""Sol trim chunking — 3 Derouter parts when post-Sol article.html needs shortening (B20 pattern).

Splits article.html by H2 sections, trims each chunk via Derouter powerful tier,
merges back to article.html + drafts/variant-a.html. Use when quality-bar word_count > 2200.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


TRIM_HEADER = """ROLE: Sol TRIM pass — сжать финальный article.html на ~80–150 слов. НЕ переписывать с нуля.

Задача: убрать spine-once повторы (одни тезисы в соседних H2), склеить лишние однострочные абзацы, сократить пересказы.
ЦЕЛЬ: итог ~2000–2150 слов при сохранении casus arc, agency ending, comment magnet.

СОХРАНИТЬ БЕЗ ИЗМЕНЕНИЙ URL/структуры:
- все H2 дословно (заголовки в этом чанке)
- все <figure class="inline-quad" data-slot="inline_N"> с alt и src
- excalibur-cta-early, excalibur-cta-mid, excalibur-cta-end целиком
- comment magnet и interlink href
- таблицы и casus spine (лид, финал, agency ending)

excalibur-cta-end ОБЯЗАТЕЛЬНО: dual CTA — consult («консультац»/«напишите») + deal («подключаюсь к сделке»/«от брони до ключей»/«веду переписку»).
Ссылки в end CTA: literal href="/gajdy/", href="/", href="/rieltor-tyumen/" — НЕ {{SITE_BASE}}.

ЗАПРЕЩЕНО: новые факты, composite disclaimer, TL;DR, удаление H2/inline/CTA.
HTML: <b> не <strong>, <i> не <em>. Выход: только HTML фрагмент без fences.
"""


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def word_count(html: str) -> int:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text.split()) if text else 0


def split_html_by_h2(html: str) -> list[str]:
    pattern = re.compile(r"<h2[^>]*>", re.I)
    matches = list(pattern.finditer(html))
    if not matches:
        return [html.strip()] if html.strip() else []
    sections: list[str] = []
    if matches[0].start() > 0:
        preamble = html[: matches[0].start()].strip()
        if preamble:
            sections.append(preamble)
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(html)
        chunk = html[start:end].strip()
        if chunk:
            sections.append(chunk)
    return sections


def split_h2_groups(items: list[str], parts: int) -> list[list[str]]:
    if not items:
        return [[] for _ in range(parts)]
    n = len(items)
    base, rem = divmod(n, parts)
    groups: list[list[str]] = []
    idx = 0
    for p in range(parts):
        size = base + (1 if p < rem else 0)
        groups.append(items[idx : idx + size])
        idx += size
    return groups


def merge_trim_fragments(fragments: list[str]) -> str:
    from excalibur_blog_html_merge_utils import merge_html_fragments

    return merge_html_fragments(fragments, dedupe_h2=True)


def build_trim_part_prompt(
    extra_instructions: str,
    part_index: int,
    total_parts: int,
    section_html: str,
) -> str:
    extra = f"\n{extra_instructions.strip()}\n" if extra_instructions.strip() else ""
    return (
        f"{TRIM_HEADER}{extra}\n"
        f"=== SOL TRIM CHUNK {part_index}/{total_parts} ===\n"
        f"Сожми ТОЛЬКО этот HTML-фрагмент. Не дублируй секции из других чанков.\n"
        f"HTML whitelist: <b> не <strong>, <i> не <em>.\n\n"
        f"Текущий фрагмент:\n{section_html}\n"
    )


def normalize_site_base_hrefs(html: str) -> str:
    """Sol trim sometimes emits {{SITE_BASE}}/path — normalize to site-relative /path."""
    return (html or "").replace("{{SITE_BASE}}", "")


def run_chunk_trim(
    *,
    root: Path,
    article_dir: Path,
    in_path: Path,
    draft: str,
    extra_instructions: str,
    parts: int,
    single_shot: bool,
) -> tuple[int, str]:
    """Run one trim pass; returns (exit_code, merged_html)."""
    derouter = root / "scripts/excalibur_blog_derouter_opus_chat.py"
    system_path = root / "skills/sol-excalibur-blog/SKILL.md"

    if single_shot:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
            tf.write(build_trim_part_prompt(extra_instructions, 1, 1, draft))
            tmp_user = Path(tf.name)
        cmd = [
            sys.executable,
            str(derouter),
            "--role",
            "sol",
            "--system-file",
            str(system_path),
            "--user-file",
            str(tmp_user),
            "--output",
            str(in_path),
            "--article-dir",
            str(article_dir),
        ]
        rc = subprocess.call(cmd, cwd=str(root))
        tmp_user.unlink(missing_ok=True)
        if rc != 0:
            return rc, draft
        merged = normalize_site_base_hrefs(in_path.read_text(encoding="utf-8"))
        return 0, merged

    sections = split_html_by_h2(draft)
    if len(sections) < 2:
        print("SOL TRIM BLOCKER: need H2 sections to chunk trim", file=sys.stderr)
        return 1, draft

    groups = split_h2_groups(sections, max(1, parts))
    fragments: list[str] = []

    with tempfile.TemporaryDirectory(prefix="sol-trim-chunk-") as tmpdir:
        tmp = Path(tmpdir)
        for i, group in enumerate(groups, start=1):
            chunk_html = "\n\n".join(group)
            part_user = tmp / f"sol-trim-part-{i}-user.md"
            part_out = tmp / f"sol-trim-part-{i}.html"
            part_user.write_text(
                build_trim_part_prompt(extra_instructions, i, len(groups), chunk_html),
                encoding="utf-8",
            )
            cmd = [
                sys.executable,
                str(derouter),
                "--role",
                "sol",
                "--system-file",
                str(system_path),
                "--user-file",
                str(part_user),
                "--output",
                str(part_out),
                "--article-dir",
                str(article_dir),
                "--stamp-path",
                str(article_dir / f"derouter-opus-stamp-sol-trim-part{i}.json"),
            ]
            print(f"SOL TRIM chunk {i}/{len(groups)} sections={len(group)} words≈{word_count(chunk_html)}")
            rc = subprocess.call(cmd, cwd=str(root))
            if rc != 0:
                print(
                    f"DEROUTER SOL TRIM BLOCKER chunk {i}/{len(groups)} exit={rc}",
                    file=sys.stderr,
                )
                return rc, draft
            fragments.append(part_out.read_text(encoding="utf-8"))

    merged = normalize_site_base_hrefs(merge_trim_fragments(fragments))
    return 0, merged


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--input", default="article.html", help="Sol final to trim in-place")
    ap.add_argument("--user-file", help="Optional extra trim instructions (header only; body ignored)")
    ap.add_argument("--parts", type=int, default=3)
    ap.add_argument(
        "--if-over",
        type=int,
        default=2200,
        help="Skip unless article word count exceeds this threshold (0 = always run)",
    )
    ap.add_argument(
        "--single-shot",
        action="store_true",
        help="Force one Derouter call with full article (not recommended on longform)",
    )
    ap.add_argument(
        "--until-under",
        type=int,
        default=2200,
        help="After trim, FAIL if word count still above this (0 = no post-check)",
    )
    ap.add_argument(
        "--max-passes",
        type=int,
        default=2,
        help="Re-run chunk trim up to N passes while word count > --until-under",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    in_path = Path(args.input)
    if not in_path.is_absolute():
        in_path = article_dir / in_path
    if not in_path.is_file():
        print(f"SOL TRIM BLOCKER: missing {in_path}", file=sys.stderr)
        return 1

    draft = in_path.read_text(encoding="utf-8")
    wc_before = word_count(draft)
    if args.if_over and wc_before <= args.if_over:
        print(f"SKIP sol trim: word_count={wc_before} <= --if-over={args.if_over}")
        return 0

    extra_instructions = ""
    if args.user_file:
        user_path = Path(args.user_file)
        if not user_path.is_absolute():
            user_path = root / user_path
        if user_path.is_file():
            raw = user_path.read_text(encoding="utf-8")
            marker = "Текущий article.html"
            if marker in raw:
                extra_instructions = raw.split(marker, 1)[0].strip()
            else:
                extra_instructions = raw.strip()

    merged = draft
    wc = wc_before
    passes_run = 0
    max_passes = max(1, args.max_passes)

    while passes_run < max_passes:
        passes_run += 1
        print(f"SOL TRIM pass {passes_run}/{max_passes} words≈{wc}")
        rc, merged = run_chunk_trim(
            root=root,
            article_dir=article_dir,
            in_path=in_path,
            draft=merged,
            extra_instructions=extra_instructions,
            parts=args.parts,
            single_shot=args.single_shot,
        )
        if rc != 0:
            return rc
        wc = word_count(merged)
        if args.until_under and wc <= args.until_under:
            break

    in_path.write_text(merged, encoding="utf-8")
    variant = article_dir / "drafts/variant-a.html"
    variant.parent.mkdir(parents=True, exist_ok=True)
    variant.write_text(merged, encoding="utf-8")
    stamp = {
        "role": "sol_trim",
        "method": "sol_trim_chunk",
        "parts": args.parts,
        "passes": passes_run,
        "word_count_before": wc_before,
        "word_count_after": wc,
    }
    (article_dir / "derouter-opus-stamp-sol-trim.json").write_text(
        json.dumps(stamp, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"WROTE {in_path} (trim {passes_run} pass(es), "
        f"{wc_before}→{wc} words)"
    )
    if args.until_under and wc > args.until_under:
        print(
            f"SOL TRIM BLOCKER: word_count={wc} still > --until-under={args.until_under}",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
