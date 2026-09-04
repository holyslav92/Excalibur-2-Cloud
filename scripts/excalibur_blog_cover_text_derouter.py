#!/usr/bin/env python3
"""Derouter cover-text with gate validation and one retry on BLOCK.

Wraps excalibur_blog_derouter_opus_chat.py → parse JSON → cover_text_gate.
On BLOCK, appends gate errors to the user prompt and retries once (max 2 calls).
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from excalibur_blog_cover_text_gate import validate_cover_text
from excalibur_blog_meme_canon import load_meme_catalog, normalize_meme_picks, resolve_meme_id
from excalibur_blog_quad_slots import inline_count_from_tenant

MAX_ATTEMPTS = 2
FENCE_RE = re.compile(r"^```(?:json)?\s*|\s*```$", re.MULTILINE)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_json_payload(text: str) -> dict:
    raw = (text or "").strip()
    if raw.startswith("```"):
        raw = FENCE_RE.sub("", raw).strip()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("cover-text output must be a JSON object")
    return data


def canonicalize_meme_picks(data: dict, catalog: dict) -> dict:
    picks = normalize_meme_picks(data.get("meme_picks"))
    if not picks:
        return data
    out: dict[str, list[str]] = {}
    for slot, ids in picks.items():
        canon: list[str] = []
        for mid in ids:
            resolved, err = resolve_meme_id(mid, catalog)
            if err or not resolved:
                continue
            canon.append(resolved)
        if canon:
            out[slot] = canon
    if out:
        data = dict(data)
        data["meme_picks"] = out
    return data


def write_cover_text(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


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
        "cover-text",
        "--system-file",
        str(system_file),
        "--user-file",
        str(user_file),
        "--output",
        str(output_path),
        "--article-dir",
        str(article_dir),
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

    cover_text_path = article_dir / "cover" / "cover-text.json"
    gate_out = article_dir / "cover-text-gate.json"
    base_user = user_file.read_text(encoding="utf-8")
    retry_user_path = article_dir / ".cover-text-retry-user.md"
    catalog = load_meme_catalog(root)

    tenant_path = root / "shared/tenant-config.json"
    tenant = json.loads(tenant_path.read_text(encoding="utf-8")) if tenant_path.is_file() else {}
    inline_count = inline_count_from_tenant(tenant)

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
            system_file=system_file,
            user_file=active_user,
            output_path=cover_text_path,
        )
        if rc != 0:
            print(f"❌ COVER-TEXT BLOCKER: Derouter failed on attempt {attempt}", file=sys.stderr)
            return rc

        try:
            raw_text = cover_text_path.read_text(encoding="utf-8")
            data = parse_json_payload(raw_text)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            last_errors = [f"invalid JSON: {exc}"]
            user_prompt = (
                f"{base_user}\n\n"
                f"## Gate retry {attempt} — fix JSON\n"
                f"- {'; '.join(last_errors)}\n"
                "Output ONLY valid JSON (no markdown fences)."
            )
            continue

        data = canonicalize_meme_picks(data, catalog)
        write_cover_text(cover_text_path, data)

        verdict = validate_cover_text(data, inline_count=inline_count)
        gate_out.write_text(json.dumps(verdict, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK gate={gate_out.relative_to(root)} status={verdict['status']} attempt={attempt}")

        if verdict["status"] == "PASS":
            return 0

        last_errors = list(verdict.get("errors") or [])
        for err in last_errors:
            print(f"  - {err}")
        if attempt >= args.max_attempts:
            break
        user_prompt = (
            f"{base_user}\n\n"
            f"## Gate retry {attempt} — fix these errors\n"
            + "\n".join(f"- {e}" for e in last_errors)
            + "\n\nBANNED meme ids (never use): drake, drake_no_yes, salt_bae, stock_handsome_man.\n"
            "Use only allowed ids from memory/cover/meme-top100.json.\n"
            "Output ONLY valid JSON (no markdown fences)."
        )

    print("❌ COVER-TEXT BLOCKER: gate FAIL after retries", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
