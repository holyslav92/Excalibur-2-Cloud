#!/usr/bin/env python3
"""Trend Radar: ViralDzen → trend-radar.json (3–5 hot angles per rubric)."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from excalibur_blog_slot_rubric import RUBRIC_LABELS, current_slot_local, rubric_for_slot

RUBRIC_PATTERNS: dict[str, tuple[str, ...]] = {
    "novostroyki": (
        r"новострой",
        r"дду",
        r"эскроу",
        r"застройщик",
        r"жк\b",
        r"сдач",
        r"переуступ",
        r"долгострой",
        r"ипотек",
    ),
    "vtorichka": (
        r"вторич",
        r"продав",
        r"покупател",
        r"егрн",
        r"обремен",
        r"банкрот",
        r"опек",
        r"маткапитал",
        r"сделк",
        r"нотариус",
    ),
    "arenda": (
        r"аренд",
        r"съём",
        r"съем",
        r"найм",
        r"квартирант",
        r"залог",
        r"выселен",
        r"сосед",
    ),
}


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def classify_rubric(title: str) -> str | None:
    blob = (title or "").lower()
    scores: dict[str, int] = {}
    for rubric, pats in RUBRIC_PATTERNS.items():
        score = sum(1 for p in pats if re.search(p, blob))
        if score:
            scores[rubric] = score
    if not scores:
        return None
    return max(scores, key=scores.get)


def headline_formula(title: str) -> str:
    t = re.sub(r"\s+", " ", (title or "").strip())
    # убрать хвост после тире для формулы
    parts = re.split(r"\s+[—–-]\s+", t, maxsplit=1)
    core = parts[0]
    words = core.split()
    if len(words) > 8:
        core = " ".join(words[:8]) + "…"
    return f"casus+число: «{core}»"


def first_line_hook(title: str) -> str:
    t = (title or "").strip()
    return t[:120] + ("…" if len(t) > 120 else "")


def mechanism_from_title(title: str) -> str:
    t = (title or "").lower()
    if re.search(r"ипотек|ставк|банк", t):
        return "деньги/ипотека на столе"
    if re.search(r"егрн|обремен|документ", t):
        return "бумага чистая — потом ломается"
    if re.search(r"аренд|залог|высел", t):
        return "договор vs реальность"
    if re.search(r"срок|сдач|дду|эскроу", t):
        return "часы/срок съели аванс"
    return "almost lost перед ключами/деньгами"


def run_collect(root: Path, out_dir: Path, source: dict[str, Any], defaults: dict) -> None:
    wrapper = root / "scripts" / "excalibur_blog_viraldzen_wrapper.py"
    delay = max(0.7, float(defaults.get("delay") or 0.7))
    pages = int(defaults.get("pages") or 1)
    top = int(defaults.get("top") or 15)
    kind = source.get("collect") or "topic"
    slug = source.get("slug") or ""
    url = source.get("url") or ""
    args: list[str]
    if kind == "channel-only" and url:
        args = [
            "collect",
            "--url",
            url,
            "--channel-only",
            "--pages",
            str(pages),
            "--top",
            str(top),
            "--out-dir",
            str(out_dir),
            "--delay",
            str(delay),
        ]
    elif slug:
        args = [
            "collect",
            "--slug",
            slug,
            "--pages",
            str(pages),
            "--top",
            str(top),
            "--out-dir",
            str(out_dir),
            "--delay",
            str(delay),
            "--pick",
            "1",
        ]
    else:
        return
    subprocess.run([sys.executable, str(wrapper), *args], cwd=root, check=False)


def load_rows(db_path: Path) -> list[dict[str, Any]]:
    if not db_path.is_file():
        return []
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    try:
        cur = conn.execute(
            "SELECT title, url, views, read_through, viral_score, channel_name, topic "
            "FROM viral_items ORDER BY viral_score DESC, views DESC LIMIT 500"
        )
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()


def pick_angles(rows: list[dict[str, Any]], rubric: str, limit: int = 5) -> list[dict[str, Any]]:
    picked: list[dict[str, Any]] = []
    seen_formulas: set[str] = set()
    for row in rows:
        title = str(row.get("title") or "")
        if classify_rubric(title) != rubric:
            continue
        formula = headline_formula(title)
        if formula in seen_formulas:
            continue
        seen_formulas.add(formula)
        picked.append(
            {
                "headline_formula": formula,
                "first_line_hook": first_line_hook(title),
                "mechanism": mechanism_from_title(title),
                "views": int(row.get("views") or 0),
                "read_through": float(row.get("read_through") or 0),
                "viral_score": float(row.get("viral_score") or 0),
                "source_url": str(row.get("url") or ""),
                "channel": str(row.get("channel_name") or row.get("topic") or ""),
            }
        )
        if len(picked) >= limit:
            break
    return picked


def main() -> int:
    ap = argparse.ArgumentParser(description="Trend Radar (ViralDzen → trend-radar.json)")
    ap.add_argument("--slot", help="YEKT slot HH:MM")
    ap.add_argument("--max-sources", type=int, default=5, help="Limit ViralDzen collects per run")
    ap.add_argument("--skip-collect", action="store_true", help="Only rebuild JSON from latest data dir")
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Handoff JSON (default memory/blog/trend-radar/trend-radar.json)",
    )
    args = ap.parse_args()
    root = project_root()
    radar_dir = root / "memory" / "blog" / "trend-radar"
    channels_path = radar_dir / "channels.json"
    hubs_path = radar_dir / "topics-hubs.json"
    channels_doc = json.loads(channels_path.read_text(encoding="utf-8"))
    hubs_doc = json.loads(hubs_path.read_text(encoding="utf-8")) if hubs_path.is_file() else {}
    defaults = hubs_doc.get("collect_defaults") or {"delay": 0.7, "pages": 1, "top": 15}

    slot = args.slot or current_slot_local(root)
    slot_rubric = rubric_for_slot(slot, root)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    data_dir = radar_dir / "data" / ts
    data_dir.mkdir(parents=True, exist_ok=True)

    sources = list(channels_doc.get("channels") or [])[: max(1, args.max_sources)]
    if not args.skip_collect:
        for src in sources:
            run_collect(root, data_dir, src, defaults)

    db_path = data_dir / "viral.sqlite"
    if not db_path.is_file():
        # fallback: latest data subdir
        data_root = radar_dir / "data"
        if data_root.is_dir():
            subs = sorted([p for p in data_root.iterdir() if p.is_dir()], reverse=True)
            for sub in subs:
                candidate = sub / "viral.sqlite"
                if candidate.is_file():
                    db_path = candidate
                    break

    rows = load_rows(db_path)
    rubrics_out: dict[str, Any] = {}
    for rubric in ("novostroyki", "vtorichka", "arenda"):
        angles = pick_angles(rows, rubric, limit=5)
        rubrics_out[rubric] = {
            "label": RUBRIC_LABELS.get(rubric, rubric),
            "angles": angles,
            "count": len(angles),
        }

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "slot_local": slot,
        "slot_rubric": slot_rubric,
        "slot_rubric_label": RUBRIC_LABELS.get(slot_rubric, slot_rubric),
        "data_dir": str(data_dir.relative_to(root)) if data_dir.is_dir() else "",
        "viral_db": str(db_path.relative_to(root)) if db_path.is_file() else "",
        "sources_used": [s.get("slug") for s in sources],
        "rubrics": rubrics_out,
        "policy": "MECHANICS_AND_ENERGY_ONLY — do not copy plots or body text",
    }

    out_path = args.output or (radar_dir / "trend-radar.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    history = radar_dir / "history"
    history.mkdir(parents=True, exist_ok=True)
    hist_copy = history / f"trend-radar-{ts}.json"
    hist_copy.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")

    print(f"OK trend-radar → {out_path.relative_to(root)} rubric={slot_rubric} rows={len(rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
