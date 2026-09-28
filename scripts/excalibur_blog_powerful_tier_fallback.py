#!/usr/bin/env python3
"""После FAIL quality-score + один repair: Writer+Sol на gpt-6-astra (слот не пустой)."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_lock(root: Path) -> dict:
    path = root / "shared" / "owner-runtime-lock.json"
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description="Powerful tier fallback → gpt-6-astra Writer+Sol")
    ap.add_argument("--article-dir", required=True, type=Path)
    ap.add_argument("--reason", default="quality_score_fail_after_repair")
    args = ap.parse_args()
    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article-dir not found: {article_dir}", file=sys.stderr)
        return 2

    lock = load_lock(root)
    fallback = str(
        (lock.get("writing_model") or {}).get("powerful", {}).get("fallback_model") or "gpt-6-astra"
    )
    stamp_path = article_dir / "powerful-tier-fallback.json"
    stamp = {
        "reason": args.reason,
        "fallback_model": fallback,
        "from_model": (lock.get("writing_model") or {}).get("powerful", {}).get("model"),
    }
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    env = os.environ.copy()
    env["DEROUTER_POWERFUL_MODEL"] = fallback
    derouter = root / "scripts" / "excalibur_blog_derouter_opus_chat.py"
    writer_chunk = root / "scripts" / "excalibur_blog_writer_chunk.py"
    sol_chunk = root / "scripts" / "excalibur_blog_sol_chunk.py"

    steps: list[list[str]] = []
    if writer_chunk.is_file():
        steps.append(
            [
                sys.executable,
                str(writer_chunk),
                "--article-dir",
                str(article_dir),
            ]
        )
    else:
        steps.append(
            [
                sys.executable,
                str(derouter),
                "--role",
                "writer",
                "--article-dir",
                str(article_dir),
                "--system-file",
                str(root / ".cursor/agents/excalibur-blog-writer.md"),
                "--user-file",
                str(article_dir / "assembled-writer-inputs.md"),
                "--output",
                str(article_dir / "drafts/writer.html"),
            ]
        )

    if sol_chunk.is_file():
        steps.append(
            [
                sys.executable,
                str(sol_chunk),
                "--article-dir",
                str(article_dir),
            ]
        )
    else:
        steps.append(
            [
                sys.executable,
                str(derouter),
                "--role",
                "sol",
                "--article-dir",
                str(article_dir),
                "--system-file",
                str(root / ".cursor/agents/excalibur-blog-sol.md"),
                "--user-file",
                str(article_dir / "assembled-sol-inputs.md"),
                "--output",
                str(article_dir / "article.html"),
            ]
        )

    for cmd in steps:
        proc = subprocess.run(cmd, cwd=root, env=env, check=False)
        if proc.returncode != 0:
            print(f"BLOCKER: fallback step failed: {' '.join(cmd)}", file=sys.stderr)
            return proc.returncode

    print(f"OK powerful-tier fallback complete model={fallback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
