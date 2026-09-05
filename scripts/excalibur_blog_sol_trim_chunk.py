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


def build_trim_header(*, target: int, over_by: int, round_index: int) -> str:
    cut_hint = max(40, min(over_by + 30, 180))
    round_note = ""
    if round_index > 1:
        round_note = (
            f"\nROUND {round_index}: после первого trim всё ещё {over_by} слов выше цели {target}. "
            f"Сожми ещё на ~{cut_hint} слов без потери фактов.\n"
        )
    return f"""ROLE: Sol TRIM pass — сжать финальный article.html. НЕ переписывать с нуля.
{round_note}
Задача: убрать spine-once повторы (одни тезисы в соседних H2), склеить лишние однострочные абзацы, сократить пересказы.
ЦЕЛЬ: итог ≤ {target} слов (quality-bar 1800–2200); сейчас нужно убрать ~{cut_hint} слов при сохранении casus arc, agency ending, comment magnet.

СОХРАНИТЬ БЕЗ ИЗМЕНЕНИЙ URL/структуры:
- все H2 дословно (заголовки в этом чанке)
- все <figure class="inline-quad" data-slot="inline_N"> с alt и src
- excalibur-cta-early, excalibur-cta-mid, excalibur-cta-end целиком
- comment magnet и interlink href
- таблицы и casus spine (лид, финал, agency ending)

ЗАПРЕЩЕНО: новые факты, composite disclaimer, TL;DR, удаление H2/inline/CTA.
HTML: <b> не <strong>, <i> не <em>. Выход: только HTML фрагмент без fences.
"""


TRIM_HEADER = build_trim_header(target=2200, over_by=100, round_index=1)


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
    *,
    target: int,
    over_by: int,
    round_index: int,
) -> str:
    extra = f"\n{extra_instructions.strip()}\n" if extra_instructions.strip() else ""
    header = build_trim_header(target=target, over_by=over_by, round_index=round_index)
    return (
        f"{header}{extra}\n"
        f"=== SOL TRIM CHUNK {part_index}/{total_parts} ===\n"
        f"Сожми ТОЛЬКО этот HTML-фрагмент. Не дублируй секции из других чанков.\n"
        f"HTML whitelist: <b> не <strong>, <i> не <em>.\n\n"
        f"Текущий фрагмент:\n{section_html}\n"
    )


def trim_rounds_needed(word_count_value: int, *, target: int, max_rounds: int) -> int:
    """How many trim rounds to schedule when word_count_value > target (B23 pattern)."""
    if word_count_value <= target:
        return 0
    return min(max_rounds, 2 if word_count_value > target else 0)


def run_chunk_trim_round(
    *,
    root: Path,
    article_dir: Path,
    in_path: Path,
    derouter: Path,
    system_path: Path,
    extra_instructions: str,
    parts: int,
    target: int,
    round_index: int,
    stamp_suffix: str,
) -> tuple[int, str]:
    draft = in_path.read_text(encoding="utf-8")
    wc = word_count(draft)
    over_by = max(0, wc - target)
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
            part_user = tmp / f"sol-trim-{stamp_suffix}-part-{i}-user.md"
            part_out = tmp / f"sol-trim-{stamp_suffix}-part-{i}.html"
            part_user.write_text(
                build_trim_part_prompt(
                    extra_instructions,
                    i,
                    len(groups),
                    chunk_html,
                    target=target,
                    over_by=over_by,
                    round_index=round_index,
                ),
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
                str(
                    article_dir
                    / f"derouter-opus-stamp-sol-trim{stamp_suffix}-part{i}.json"
                ),
            ]
            print(
                f"SOL TRIM round {round_index} chunk {i}/{len(groups)} "
                f"sections={len(group)} words≈{word_count(chunk_html)}"
            )
            rc = subprocess.call(cmd, cwd=str(root))
            if rc != 0:
                print(
                    f"DEROUTER SOL TRIM BLOCKER round {round_index} "
                    f"chunk {i}/{len(groups)} exit={rc}",
                    file=sys.stderr,
                )
                return rc, draft
            fragments.append(part_out.read_text(encoding="utf-8"))

    merged = merge_trim_fragments(fragments)
    in_path.write_text(merged, encoding="utf-8")
    variant = article_dir / "drafts/variant-a.html"
    variant.parent.mkdir(parents=True, exist_ok=True)
    variant.write_text(merged, encoding="utf-8")
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
        "--target",
        type=int,
        default=2200,
        help="Stop trimming when word count is at or below this value (quality-bar max)",
    )
    ap.add_argument(
        "--max-rounds",
        type=int,
        default=2,
        help="Max chunk-trim rounds when still above --target after first pass (B23)",
    )
    ap.add_argument(
        "--single-shot",
        action="store_true",
        help="Force one Derouter call with full article (not recommended on longform)",
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
    wc = word_count(draft)
    if args.if_over and wc <= args.if_over:
        print(f"SKIP sol trim: word_count={wc} <= --if-over={args.if_over}")
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

    derouter = root / "scripts/excalibur_blog_derouter_opus_chat.py"
    system_path = root / "skills/sol-excalibur-blog/SKILL.md"

    if args.single_shot:
        over_by = max(0, wc - args.target)
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
            tf.write(
                build_trim_part_prompt(
                    extra_instructions,
                    1,
                    1,
                    draft,
                    target=args.target,
                    over_by=over_by,
                    round_index=1,
                )
            )
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
        if rc == 0:
            variant = article_dir / "drafts/variant-a.html"
            variant.parent.mkdir(parents=True, exist_ok=True)
            variant.write_text(in_path.read_text(encoding="utf-8"), encoding="utf-8")
        return rc

    word_count_before = wc
    rounds_done = 0
    for round_index in range(1, max(1, args.max_rounds) + 1):
        current_wc = word_count(in_path.read_text(encoding="utf-8"))
        if current_wc <= args.target:
            break
        stamp_suffix = "" if round_index == 1 else f"-r{round_index}"
        rc, _ = run_chunk_trim_round(
            root=root,
            article_dir=article_dir,
            in_path=in_path,
            derouter=derouter,
            system_path=system_path,
            extra_instructions=extra_instructions,
            parts=args.parts,
            target=args.target,
            round_index=round_index,
            stamp_suffix=stamp_suffix,
        )
        rounds_done += 1
        if rc != 0:
            return rc
        after_wc = word_count(in_path.read_text(encoding="utf-8"))
        print(f"SOL TRIM round {round_index}: {current_wc}→{after_wc} words (target≤{args.target})")
        if after_wc <= args.target:
            break
        if after_wc >= current_wc:
            print(
                f"WARN sol trim round {round_index}: no word-count progress ({current_wc}→{after_wc}); stop",
                file=sys.stderr,
            )
            break

    final_wc = word_count(in_path.read_text(encoding="utf-8"))
    stamp = {
        "role": "sol_trim",
        "method": "sol_trim_chunk",
        "parts": args.parts,
        "rounds": rounds_done,
        "target": args.target,
        "word_count_before": word_count_before,
        "word_count_after": final_wc,
    }
    (article_dir / "derouter-opus-stamp-sol-trim.json").write_text(
        json.dumps(stamp, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"WROTE {in_path} (trim {rounds_done} round(s), "
        f"{word_count_before}→{final_wc} words, target≤{args.target})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
