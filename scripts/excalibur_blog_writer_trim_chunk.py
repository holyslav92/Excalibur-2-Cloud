#!/usr/bin/env python3
"""Writer trim chunking — 3 Derouter parts when post-merge draft needs shortening (avoid HTTP 524).

Splits drafts/writer.html by H2 sections, trims each chunk via Derouter powerful tier,
merges back to drafts/writer.html. Use instead of single-shot trim on longform.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


TRIM_HEADER = """ROLE: Writer trim pass — сжать HTML черновик без потери смысла.

Задача: убрать spine-once повторы (одни и те же тезисы в разных H2, дубли interlink на те же URL), сократить пересказы.
Сохранить все H2 в этом чанке один раз, прозаический лид (если в чанке), early/mid/end CTA, comment magnet, phone, interlink URL.
Не добавлять факты. Не менять финал casus. Выход: только HTML фрагмент без fences.
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
    """Split writer HTML into preamble + H2-led sections."""
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
        f"=== WRITER TRIM CHUNK {part_index}/{total_parts} ===\n"
        f"Сожми ТОЛЬКО этот HTML-фрагмент. Не дублируй секции из других чанков.\n"
        f"HTML whitelist: <b> не <strong>, <i> не <em>.\n\n"
        f"Текущий фрагмент:\n{section_html}\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--input", default="drafts/writer.html", help="Draft to trim in-place")
    ap.add_argument("--user-file", help="Optional extra trim instructions (header only; body ignored)")
    ap.add_argument("--parts", type=int, default=3)
    ap.add_argument(
        "--if-over",
        type=int,
        default=0,
        help="Skip unless draft word count exceeds this threshold (0 = always run)",
    )
    ap.add_argument(
        "--single-shot",
        action="store_true",
        help="Force one Derouter call with full draft (not recommended on longform)",
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
        print(f"WRITER TRIM BLOCKER: missing {in_path}", file=sys.stderr)
        return 1

    draft = in_path.read_text(encoding="utf-8")
    wc = word_count(draft)
    if args.if_over and wc <= args.if_over:
        print(f"SKIP writer trim: word_count={wc} <= --if-over={args.if_over}")
        return 0

    extra_instructions = ""
    if args.user_file:
        user_path = Path(args.user_file)
        if not user_path.is_absolute():
            user_path = root / user_path
        if user_path.is_file():
            raw = user_path.read_text(encoding="utf-8")
            # assembled-writer-trim-inputs.md embeds full draft after marker
            marker = "Текущий черновик:"
            if marker in raw:
                extra_instructions = raw.split(marker, 1)[0].strip()
            else:
                extra_instructions = raw.strip()

    derouter = root / "scripts" / "excalibur_blog_derouter_opus_chat.py"
    system_path = root / "skills/writer-excalibur-blog/SKILL.md"

    if args.single_shot:
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
            tf.write(build_trim_part_prompt(extra_instructions, 1, 1, draft))
            tmp_user = Path(tf.name)
        cmd = [
            sys.executable,
            str(derouter),
            "--role",
            "writer",
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
        return rc

    sections = split_html_by_h2(draft)
    if len(sections) < 2:
        print("WRITER TRIM BLOCKER: need H2 sections to chunk trim", file=sys.stderr)
        return 1

    groups = split_h2_groups(sections, max(1, args.parts))
    fragments: list[str] = []

    with tempfile.TemporaryDirectory(prefix="writer-trim-chunk-") as tmpdir:
        tmp = Path(tmpdir)
        for i, group in enumerate(groups, start=1):
            chunk_html = "\n\n".join(group)
            part_user = tmp / f"writer-trim-part-{i}-user.md"
            part_out = tmp / f"writer-trim-part-{i}.html"
            part_user.write_text(
                build_trim_part_prompt(extra_instructions, i, len(groups), chunk_html),
                encoding="utf-8",
            )
            cmd = [
                sys.executable,
                str(derouter),
                "--role",
                "writer",
                "--system-file",
                str(system_path),
                "--user-file",
                str(part_user),
                "--output",
                str(part_out),
                "--article-dir",
                str(article_dir),
                "--stamp-path",
                str(article_dir / f"derouter-opus-stamp-writer-trim-part{i}.json"),
            ]
            print(f"WRITER TRIM chunk {i}/{len(groups)} sections={len(group)} words≈{word_count(chunk_html)}")
            rc = subprocess.call(cmd, cwd=str(root))
            if rc != 0:
                print(
                    f"DEROUTER WRITER TRIM BLOCKER chunk {i}/{len(groups)} exit={rc}",
                    file=sys.stderr,
                )
                return rc
            fragments.append(part_out.read_text(encoding="utf-8"))

    merged = merge_trim_fragments(fragments)
    in_path.write_text(merged, encoding="utf-8")
    stamp = {
        "role": "writer_trim",
        "method": "writer_trim_chunk",
        "parts": len(groups),
        "word_count_before": wc,
        "word_count_after": word_count(merged),
    }
    import json

    (article_dir / "derouter-opus-stamp-writer-trim.json").write_text(
        json.dumps(stamp, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"WROTE {in_path} (trim merged {len(groups)} chunks, "
        f"{wc}→{stamp['word_count_after']} words)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
