#!/usr/bin/env python3
"""Derouter schema with JSON-LD validation and one retry on invalid/refusal output.

Wraps excalibur_blog_derouter_opus_chat.py → parse JSON-LD → write article_dir/schema.jsonld.
On invalid JSON or prose refusal, appends retry instructions to the user prompt (max 2 calls).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from excalibur_blog_derouter_opus_chat import normalize_schema_jsonld_text

MAX_ATTEMPTS = 2

DEROUTER_SCHEMA_SYSTEM_PREFIX = """You are invoked by scripts/excalibur_blog_schema_derouter.py (utility tier).
Output ONLY valid JSON-LD (one JSON object). No markdown fences, no explanations, no refusals.
The phrase «не пиши schema Cursor» in the skill applies to Cursor Composer only — not to this call.

"""


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_derouter(
    *,
    root: Path,
    article_dir: Path,
    system_file: Path,
    user_file: Path,
    output_path: Path,
) -> int:
    cmd = [
        sys.executable,
        str(root / "scripts/excalibur_blog_derouter_opus_chat.py"),
        "--role",
        "schema",
        "--system-file",
        str(system_file),
        "--user-file",
        str(user_file),
        "--output",
        str(output_path),
        "--article-dir",
        str(article_dir.relative_to(root) if article_dir.is_relative_to(root) else article_dir),
    ]
    proc = subprocess.run(cmd, cwd=root, text=True, capture_output=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--system-file", required=True)
    ap.add_argument("--user-file", required=True)
    ap.add_argument(
        "--max-attempts",
        type=int,
        default=MAX_ATTEMPTS,
        help=f"Derouter calls before BLOCKER (default {MAX_ATTEMPTS})",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    system_file = Path(args.system_file)
    if not system_file.is_absolute():
        system_file = root / system_file
    user_file = Path(args.user_file)
    if not user_file.is_absolute():
        user_file = root / user_file

    schema_path = article_dir / "schema.jsonld"
    base_user = user_file.read_text(encoding="utf-8")
    retry_user_path = article_dir / ".schema-retry-user.md"

    combined_system = article_dir / ".schema-derouter-system.md"
    combined_system.write_text(
        DEROUTER_SCHEMA_SYSTEM_PREFIX + system_file.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

    user_prompt = base_user
    last_errors: list[str] = []

    for attempt in range(1, max(1, args.max_attempts) + 1):
        if attempt > 1:
            retry_user_path.write_text(user_prompt, encoding="utf-8")
            active_user = retry_user_path
        else:
            active_user = user_file

        rc = run_derouter(
            root=root,
            article_dir=article_dir,
            system_file=combined_system,
            user_file=active_user,
            output_path=schema_path,
        )
        if rc != 0:
            print(f"❌ SCHEMA BLOCKER: Derouter failed on attempt {attempt}", file=sys.stderr)
            return rc

        try:
            raw_text = schema_path.read_text(encoding="utf-8")
            normalized = normalize_schema_jsonld_text(raw_text)
        except (OSError, ValueError) as exc:
            last_errors = [str(exc)]
            user_prompt = (
                f"{base_user}\n\n"
                f"## Retry {attempt} — output must be JSON-LD only\n"
                f"- {'; '.join(last_errors)}\n"
                "You are invoked BY derouter; respond with a single JSON object (BlogPosting / @graph). "
                "No markdown fences, no prose refusal."
            )
            continue

        schema_path.write_text(normalized, encoding="utf-8")
        print(f"OK schema={schema_path.relative_to(root)} attempt={attempt}")
        return 0

    print("❌ SCHEMA BLOCKER: invalid JSON-LD after retries", file=sys.stderr)
    for err in last_errors:
        print(f"  - {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
