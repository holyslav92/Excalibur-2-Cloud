#!/usr/bin/env python3
"""Еженедельный дайджест трендов Дзена по рубрикам (plain Russian)."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_snapshots(radar_dir: Path, days: int = 7) -> list[dict]:
    history = radar_dir / "history"
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    snaps: list[tuple[datetime, dict]] = []
    if history.is_dir():
        for path in sorted(history.glob("trend-radar-*.json")):
            try:
                ts_str = path.stem.replace("trend-radar-", "")
                ts = datetime.strptime(ts_str, "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
            except ValueError:
                continue
            if ts < cutoff:
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                continue
            snaps.append((ts, data))
    current = radar_dir / "trend-radar.json"
    if current.is_file():
        try:
            data = json.loads(current.read_text(encoding="utf-8"))
            gen = data.get("generated_at") or ""
            ts = datetime.fromisoformat(gen.replace("Z", "+00:00")) if gen else datetime.now(timezone.utc)
            snaps.append((ts, data))
        except (json.JSONDecodeError, ValueError):
            pass
    snaps.sort(key=lambda x: x[0])
    return [d for _, d in snaps]


def aggregate_formulas(snapshots: list[dict]) -> dict[str, list[str]]:
    out: dict[str, set[str]] = {k: set() for k in ("novostroyki", "vtorichka", "arenda")}
    for snap in snapshots:
        rubrics = snap.get("rubrics") or {}
        for rubric, block in rubrics.items():
            if rubric not in out:
                continue
            for angle in block.get("angles") or []:
                formula = str(angle.get("headline_formula") or "")
                if formula:
                    out[rubric].add(formula)
    return {k: sorted(v)[:8] for k, v in out.items()}


def build_digest(snapshots: list[dict], taken_work: list[str]) -> str:
    formulas = aggregate_formulas(snapshots)
    lines = [
        "Дайджест трендов Дзена по недвижимости (The Риэлтор), за последнюю неделю.",
        "",
    ]
    labels = {
        "novostroyki": "Новостройки",
        "vtorichka": "Вторичка",
        "arenda": "Аренда",
    }
    for key in ("novostroyki", "vtorichka", "arenda"):
        lines.append(f"**{labels[key]}** — формулы заголовков, которые сейчас тянут:")
        items = formulas.get(key) or []
        if not items:
            lines.append("  • (мало данных сбора — запустите Trend Radar перед слотом)")
        else:
            for f in items[:5]:
                lines.append(f"  • {f}")
        lines.append("")
    lines.append("Что уже взяли в работу на этой неделе:")
    if taken_work:
        for t in taken_work:
            lines.append(f"  • {t}")
    else:
        lines.append("  • Пока только интеграция Trend Radar; тестовый слот вторички — в прогоне.")
    lines.append("")
    lines.append(
        "Правило для редакции: крадём механику и энергию, не текст. Scout сводит тренд + Wordstat Тюмень + рубрику слота."
    )
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=Path, help="Write digest text file")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = project_root()
    radar_dir = root / "memory" / "blog" / "trend-radar"
    snapshots = load_snapshots(radar_dir)
    taken: list[str] = []
    ledger = root / "shared" / "published-articles.md"
    if ledger.is_file():
        for line in ledger.read_text(encoding="utf-8").splitlines()[-20:]:
            if line.startswith("| 20"):
                taken.append(line.strip())
    digest = build_digest(snapshots, taken[-5:])
    if args.json:
        print(json.dumps({"digest": digest, "snapshots": len(snapshots)}, ensure_ascii=False, indent=2))
    else:
        print(digest)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(digest + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
