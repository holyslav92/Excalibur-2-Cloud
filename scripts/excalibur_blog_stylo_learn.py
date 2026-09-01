#!/usr/bin/env python3
"""Self-learn: пометка good/bad и пересчёт centroid memory/stylo/profile.json."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_stylo import FEATURE_KEYS, compute_profile, load_gold_texts, project_root  # noqa: E402


def read_history(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def write_history(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def recompute_profile(gold_dir: Path, history_path: Path) -> dict:
    """Centroid: gold txt + history good=true; bad снижает вес через исключение."""
    gold_entries = load_gold_texts(gold_dir)
    from excalibur_blog_stylo import extract_features  # noqa: WPS433

    feature_rows: list[dict[str, float]] = [
        extract_features(f"<article>{e['text']}</article>") for e in gold_entries
    ]

    history = read_history(history_path)
    for row in history:
        if row.get("good") is True and isinstance(row.get("features"), dict):
            feature_rows.append({k: float(row["features"][k]) for k in FEATURE_KEYS if k in row["features"]})
        # good=false — anti-centroid: не добавляем (можно расширить весами позже)

    profile = compute_profile(feature_rows)
    profile["sources"] = {
        "gold_files": len(gold_entries),
        "history_good": sum(1 for r in history if r.get("good") is True),
        "history_bad": sum(1 for r in history if r.get("good") is False),
    }
    return profile


def mark_topic(history_path: Path, topic_id: str, label: str) -> int:
    rows = read_history(history_path)
    if not rows:
        print(f"FAIL нет history в {history_path}", file=sys.stderr)
        return 2
    updated = False
    good_val = label == "good"
    for row in reversed(rows):
        if str(row.get("topic_id")) == topic_id:
            row["good"] = good_val
            updated = True
            break
    if not updated:
        print(f"FAIL topic_id {topic_id} не найден в history", file=sys.stderr)
        return 2
    write_history(history_path, rows)
    print(f"OK marked {topic_id} good={good_val}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Stylo self-learn profile update")
    parser.add_argument("--mark", nargs=2, metavar=("TOPIC_ID", "good|bad"), help="пометить последнюю запись topic_id")
    parser.add_argument("--recompute", action="store_true", help="пересчитать profile.json")
    parser.add_argument("--gold-dir", type=Path, default=project_root() / "memory/stylo/gold")
    parser.add_argument("--history", type=Path, default=project_root() / "memory/stylo/history.jsonl")
    parser.add_argument("--profile-out", type=Path, default=project_root() / "memory/stylo/profile.json")
    args = parser.parse_args()

    if args.mark:
        topic_id, label = args.mark
        if label not in {"good", "bad"}:
            print("FAIL label must be good|bad", file=sys.stderr)
            return 2
        rc = mark_topic(args.history, topic_id, label)
        if rc != 0:
            return rc
        args.recompute = True

    if args.recompute:
        profile = recompute_profile(args.gold_dir, args.history)
        args.profile_out.parent.mkdir(parents=True, exist_ok=True)
        args.profile_out.write_text(json.dumps(profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK profile -> {args.profile_out} (n={profile.get('n_gold')})")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
