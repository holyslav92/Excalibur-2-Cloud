#!/usr/bin/env python3
"""Sol longform chunking — 3 Derouter Opus parts on first try (avoid HTTP 524).

Thin conductor: splits assembled user inputs by H2 outline into ~3 parts,
calls excalibur_blog_derouter_opus_chat.py per part, merges article.html.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from excalibur_blog_writer_chunk import (
    build_part_prompt,
    extract_h2_outline,
    inline_count_from_tenant,
    merge_writer_fragments,
    project_root,
    split_h2_groups,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--system-file", required=True)
    ap.add_argument("--user-file", required=True)
    ap.add_argument("--output", default="article.html")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--parts", type=int, default=3)
    ap.add_argument(
        "--single-shot",
        action="store_true",
        help="Force one Derouter call (skip chunking even on longform)",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    user_path = Path(args.user_file)
    if not user_path.is_absolute():
        user_path = root / user_path
    system_path = Path(args.system_file)
    if not system_path.is_absolute():
        system_path = root / system_path

    user_text = user_path.read_text(encoding="utf-8")
    inline_count = inline_count_from_tenant(root)
    use_chunk = not args.single_shot and inline_count >= 7

    derouter = root / "scripts/excalibur_blog_derouter_opus_chat.py"
    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = article_dir / out_path

    if not use_chunk:
        cmd = [
            sys.executable,
            str(derouter),
            "--role",
            "sol",
            "--system-file",
            str(system_path),
            "--user-file",
            str(user_path),
            "--output",
            str(out_path.name if out_path.is_relative_to(article_dir) else out_path),
            "--article-dir",
            str(article_dir),
        ]
        rc = subprocess.call(cmd, cwd=str(root))
        if rc == 0:
            variant = article_dir / "drafts/variant-a.html"
            variant.parent.mkdir(parents=True, exist_ok=True)
            variant.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")
        return rc

    h2s = extract_h2_outline(user_text)
    groups = split_h2_groups(h2s, max(1, args.parts))
    fragments: list[str] = []

    with tempfile.TemporaryDirectory(prefix="sol-chunk-") as tmpdir:
        tmp = Path(tmpdir)
        for i, group in enumerate(groups, start=1):
            part_user = tmp / f"sol-part-{i}-user.md"
            part_out = tmp / f"sol-part-{i}.html"
            part_prompt = build_part_prompt(user_text, i, len(groups), group).replace(
                "=== WRITER CHUNK",
                "=== SOL CHUNK",
            ).replace(
                "Напиши ТОЛЬКО фрагмент HTML",
                "Перепиши слогом SOUL ТОЛЬКО фрагмент HTML",
            ).replace(
                "без FAQ — Sol добавит",
                "включая FAQ если есть в Writer chunk",
            )
            part_user.write_text(part_prompt, encoding="utf-8")
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
                str(article_dir / f"derouter-opus-stamp-sol-part{i}.json"),
            ]
            print(f"SOL chunk {i}/{len(groups)} H2s={group or ['(auto)']}")
            rc = subprocess.call(cmd, cwd=str(root))
            if rc != 0:
                print(f"DEROUTER SOL BLOCKER chunk {i}/{len(groups)} exit={rc}", file=sys.stderr)
                return rc
            fragments.append(part_out.read_text(encoding="utf-8"))

    merged = merge_writer_fragments(fragments)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(merged, encoding="utf-8")
    variant = article_dir / "drafts/variant-a.html"
    variant.parent.mkdir(parents=True, exist_ok=True)
    variant.write_text(merged, encoding="utf-8")
    print(f"WROTE {out_path} (merged {len(groups)} chunks, {len(merged)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
