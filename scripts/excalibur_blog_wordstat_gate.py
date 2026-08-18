#!/usr/bin/env python3
"""Wordstat configuration + Scout handoff hard gate for Excalibur BLOG."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


PARTIAL_RE = re.compile(r"wordstat\s*:\s*.*partial", re.IGNORECASE)
SKIP_RE = re.compile(r"wordstat\s*:\s*.*\bskip\b", re.IGNORECASE)
FREQ_RE = re.compile(r"\d[\d\s]*")


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def wordstat_env_configured() -> tuple[bool, list[str]]:
    """Return (configured, missing_keys). Accept official API or MCP token paths."""
    keys_primary = ("WORDSTAT_API_KEY", "WORDSTAT_FOLDER_ID")
    keys_alt = ("YANDEX_SEARCH_API_KEY", "YANDEX_FOLDER_ID")
    env = os.environ
    missing: list[str] = []
    if env.get("WORDSTAT_API_KEY") and env.get("WORDSTAT_FOLDER_ID"):
        return True, []
    if env.get("YANDEX_SEARCH_API_KEY") and env.get("YANDEX_FOLDER_ID"):
        return True, []
    for key in keys_primary:
        if not env.get(key):
            missing.append(key)
    return False, missing


def parse_handoff_wordstat(handoff_text: str) -> str:
    for line in handoff_text.splitlines():
        if line.strip().lower().startswith("wordstat:"):
            return line.split(":", 1)[1].strip()
    return ""


def handoff_has_live_wordstat(handoff_text: str) -> tuple[bool, str]:
    value = parse_handoff_wordstat(handoff_text)
    if not value:
        return False, "wordstat field missing in handoff"
    if SKIP_RE.search(f"wordstat: {value}"):
        return False, "wordstat: skip is forbidden for Scout"
    if PARTIAL_RE.search(f"wordstat: {value}"):
        return False, "wordstat PARTIAL is forbidden — need live top phrases + frequencies"
    if not FREQ_RE.search(value):
        return False, "wordstat handoff must include numeric frequencies"
    low = value.casefold()
    if "тюмен" not in low and "11176" not in low and "region" not in low:
        return False, "wordstat handoff must show Tyumen/region affinity (Тюмень or region ids)"
    return True, value


def cmd_config(_: Path) -> int:
    ok, missing = wordstat_env_configured()
    if ok:
        print("OK wordstat env configured (API key + folder id)")
        return 0
    print("FAIL WORDSTAT NOT CONFIGURED — Scout must not proceed:", file=sys.stderr)
    for key in missing:
        print(f"  missing env: {key}", file=sys.stderr)
    print(
        "  set WORDSTAT_API_KEY + WORDSTAT_FOLDER_ID "
        "or YANDEX_SEARCH_API_KEY + YANDEX_FOLDER_ID in Cloud Secrets",
        file=sys.stderr,
    )
    print("  wire MCP: .cursor/mcp.json.example → user MCP (mcp-yandex-wordstat)", file=sys.stderr)
    return 1


def cmd_handoff(root: Path, args: argparse.Namespace) -> int:
    handoff_path = Path(args.handoff)
    if not handoff_path.is_absolute():
        handoff_path = root / handoff_path
    if not handoff_path.is_file():
        print(f"FAIL handoff not found: {handoff_path}", file=sys.stderr)
        return 1

    ok_env, missing = wordstat_env_configured()
    if not ok_env:
        print("FAIL WORDSTAT NOT CONFIGURED:", file=sys.stderr)
        for key in missing:
            print(f"  missing env: {key}", file=sys.stderr)
        return 1

    text = handoff_path.read_text(encoding="utf-8")
    ok_handoff, reason = handoff_has_live_wordstat(text)
    if not ok_handoff:
        print(f"FAIL SCOUT WORDSTAT GATE: {reason}", file=sys.stderr)
        return 1

    geo_path = root / "memory/cover/wordstat-geo.json"
    if geo_path.is_file():
        geo = load_json(geo_path)
        ids = geo.get("scout_required_region_ids") or []
        print(f"OK scout wordstat handoff; required_region_ids={ids}")
    else:
        print("OK scout wordstat handoff")
    return 0


def cmd_doctor(root: Path) -> int:
    geo_path = root / "memory/cover/wordstat-geo.json"
    if not geo_path.is_file():
        print("FAIL wordstat-geo.json missing", file=sys.stderr)
        return 1
    geo = load_json(geo_path)
    ids = geo.get("scout_required_region_ids") or []
    if 55 not in ids or 11176 not in ids:
        print("FAIL wordstat-geo must include Tyumen city 55 and oblast 11176", file=sys.stderr)
        return 1
    ok_env, _ = wordstat_env_configured()
    if ok_env:
        print("OK wordstat env present")
    else:
        print("WARN wordstat env not set (expected in Cloud Secrets, not git)")
    print("OK wordstat-geo canon")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Wordstat configuration and Scout gate")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("config", help="Fail if Wordstat API env is not configured")
    handoff = sub.add_parser("handoff", help="Validate Scout handoff wordstat field")
    handoff.add_argument("--handoff", default=".cursor/excalibur-blog-handoff.md")
    sub.add_parser("doctor", help="Validate wordstat-geo canon")
    args = parser.parse_args()
    root = project_root()
    if args.command == "config":
        return cmd_config(root)
    if args.command == "handoff":
        return cmd_handoff(root, args)
    if args.command == "doctor":
        return cmd_doctor(root)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
