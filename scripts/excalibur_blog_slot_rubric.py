#!/usr/bin/env python3
"""Слот YEKT → рубрика Scout (The Риэлтор, 5 слотов/день)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

YEKT = ZoneInfo("Asia/Yekaterinburg")

SLOT_RUBRIC: dict[str, str] = {
    "09:00": "novostroyki",
    "12:00": "novostroyki",
    "15:00": "vtorichka",
    "17:00": "vtorichka",
    "19:00": "arenda",
}

RUBRIC_LABELS = {
    "novostroyki": "новостройки",
    "vtorichka": "вторичка",
    "arenda": "аренда жилья",
}


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_schedule(root: Path) -> dict:
    path = root / "shared" / "tenant-config.json"
    if not path.is_file():
        return {}
    try:
        tenant = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return tenant.get("publish_schedule") or {}


def normalize_slot(slot: str) -> str:
    s = (slot or "").strip()
    if not s:
        return ""
    parts = s.split(":")
    if len(parts) >= 2:
        h, m = parts[0].zfill(2), parts[1].zfill(2)
        return f"{h}:{m}"
    return s


def rubric_for_slot(slot: str, root: Path | None = None) -> str:
    root = root or project_root()
    sched = load_schedule(root)
    override_map = sched.get("slot_rubric_map") or {}
    norm = normalize_slot(slot)
    if norm in override_map:
        return str(override_map[norm])
    if norm in SLOT_RUBRIC:
        return SLOT_RUBRIC[norm]
    # fallback: env or default novostroyki
    env_r = os.environ.get("EXCALIBUR_BLOG_RUBRIC", "").strip()
    if env_r in RUBRIC_LABELS:
        return env_r
    return "novostroyki"


def current_slot_local(root: Path | None = None) -> str:
    root = root or project_root()
    sched = load_schedule(root)
    slots = [normalize_slot(s) for s in (sched.get("slots_local") or list(SLOT_RUBRIC))]
    now = datetime.now(YEKT)
    current = f"{now.hour:02d}:{now.minute:02d}"
    env_slot = os.environ.get("EXCALIBUR_BLOG_SLOT", "").strip()
    if env_slot:
        return normalize_slot(env_slot)
    # ближайший прошедший слот сегодня
    past = [s for s in slots if s <= current]
    if past:
        return past[-1]
    return slots[0] if slots else "09:00"


def rubric_per_slot_tenant(root: Path) -> bool:
    path = root / "shared" / "tenant-config.json"
    if not path.is_file():
        return False
    try:
        tenant = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    focus = str(tenant.get("topic_market_focus") or "").strip().lower()
    return focus in {"rubric_per_slot", "slot_rubric", "multi_rubric"}


def main() -> int:
    ap = argparse.ArgumentParser(description="Slot → rubric for Scout")
    ap.add_argument("--slot", help="YEKT slot HH:MM (default: env or now)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--current", action="store_true", help="Resolve slot from clock/env")
    args = ap.parse_args()
    root = project_root()
    slot = normalize_slot(args.slot or "") if args.slot else ""
    if not slot or args.current:
        slot = current_slot_local(root)
    rubric = rubric_for_slot(slot, root)
    payload = {
        "slot_local": slot,
        "rubric": rubric,
        "rubric_label": RUBRIC_LABELS.get(rubric, rubric),
        "timezone": "Asia/Yekaterinburg",
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(rubric)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
