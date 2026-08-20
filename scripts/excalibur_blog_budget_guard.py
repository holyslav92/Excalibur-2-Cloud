#!/usr/bin/env python3
"""Circuit breaker: hard caps on billed Derouter/Kie work per article run.

NO wall-clock kill — waiting/SFTP/polls do not count. Soft note if run > N minutes.
Stamp: <article_dir>/budget-stamp.json
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STAMP_FILENAME = "budget-stamp.json"
FIX_QUEUE_REL = "memory/pipeline-fix-queue.md"

DEFAULT_CAPS: dict[str, int] = {
    "wall_clock_soft_note_minutes": 60,
    "cover_qa_image_attempts_max": 2,
    "derouter_image_jobs_max": 3,
    "derouter_chat_retries_per_call_max": 1,
    "kie_image_fallback_max": 1,
}


class BudgetBlocker(RuntimeError):
    """Spend cap exceeded — pipeline must STOP (no retry storm)."""

    def __init__(self, reason: str, detail: str = "") -> None:
        self.reason = reason
        self.detail = detail
        msg = f"BUDGET BLOCKER | {reason}"
        if detail:
            msg += f" | {detail}"
        super().__init__(msg)


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_caps(root: Path) -> dict[str, int]:
    path = root / "shared/tenant-config.json"
    caps = dict(DEFAULT_CAPS)
    if path.is_file():
        try:
            tenant = json.loads(path.read_text(encoding="utf-8"))
            rb = tenant.get("run_budget")
            if isinstance(rb, dict):
                for key in DEFAULT_CAPS:
                    if key in rb and rb[key] is not None:
                        caps[key] = int(rb[key])
        except (json.JSONDecodeError, TypeError, ValueError):
            pass
    return caps


def stamp_path(article_dir: Path) -> Path:
    return article_dir / STAMP_FILENAME


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_iso(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def load_stamp(article_dir: Path) -> dict[str, Any]:
    path = stamp_path(article_dir)
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def save_stamp(article_dir: Path, stamp: dict[str, Any]) -> None:
    path = stamp_path(article_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp["updated_at"] = _now_iso()
    path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _default_stamp(article_dir: Path) -> dict[str, Any]:
    rel = str(article_dir)
    return {
        "started_at": _now_iso(),
        "article_dir": rel,
        "blocked": None,
        "counters": {
            "derouter_chat_calls": 0,
            "derouter_image_jobs": 0,
            "kie_image_fallbacks": 0,
            "cover_image_rounds": [],
        },
        "calls": [],
        "notes": [],
    }


def ensure_run_started(article_dir: Path, root: Path) -> dict[str, Any]:
    stamp = load_stamp(article_dir)
    if not stamp:
        stamp = _default_stamp(article_dir)
        stamp["caps"] = load_caps(root)
        save_stamp(article_dir, stamp)
    elif "caps" not in stamp:
        stamp["caps"] = load_caps(root)
        save_stamp(article_dir, stamp)
    return stamp


def refresh_soft_wall_note(article_dir: Path, root: Path) -> None:
    """Soft note only — never blocks on elapsed time."""
    stamp = ensure_run_started(article_dir, root)
    caps = stamp.get("caps") or load_caps(root)
    started = _parse_iso(str(stamp.get("started_at") or ""))
    if not started:
        return
    soft_min = int(caps.get("wall_clock_soft_note_minutes") or 60)
    elapsed_min = (datetime.now(timezone.utc) - started.astimezone(timezone.utc)).total_seconds() / 60
    if elapsed_min < soft_min:
        return
    note = (
        f"wall_clock_soft: run elapsed {elapsed_min:.0f}m (>{soft_min}m) — "
        "informational only, not a blocker"
    )
    notes = stamp.setdefault("notes", [])
    if not any(str(n).startswith("wall_clock_soft:") for n in notes):
        notes.append(note)
        save_stamp(article_dir, stamp)


def check_not_blocked(article_dir: Path) -> None:
    stamp = load_stamp(article_dir)
    blocked = stamp.get("blocked")
    if isinstance(blocked, dict) and blocked.get("reason"):
        raise BudgetBlocker(str(blocked["reason"]), str(blocked.get("detail") or ""))


def _append_call(stamp: dict[str, Any], entry: dict[str, Any]) -> None:
    calls = stamp.setdefault("calls", [])
    entry = dict(entry)
    entry.setdefault("at", _now_iso())
    calls.append(entry)


def record_chat_call(article_dir: Path, root: Path, *, role: str, meta: dict[str, Any] | None = None) -> None:
    stamp = ensure_run_started(article_dir, root)
    check_not_blocked(article_dir)
    stamp["counters"]["derouter_chat_calls"] = int(stamp["counters"].get("derouter_chat_calls") or 0) + 1
    _append_call(
        stamp,
        {"kind": "derouter_chat", "role": role, **(meta or {})},
    )
    refresh_soft_wall_note(article_dir, root)
    save_stamp(article_dir, stamp)


def max_chat_attempts(root: Path) -> int:
    caps = load_caps(root)
    return int(caps.get("derouter_chat_retries_per_call_max") or 1) + 1


def assert_image_job_allowed(article_dir: Path, root: Path) -> None:
    check_not_blocked(article_dir)
    stamp = ensure_run_started(article_dir, root)
    caps = stamp.get("caps") or load_caps(root)
    used = int(stamp["counters"].get("derouter_image_jobs") or 0)
    limit = int(caps.get("derouter_image_jobs_max") or 3)
    if used >= limit:
        raise BudgetBlocker(
            "derouter_image_jobs",
            f"used {used}/{limit} billed image jobs this run",
        )


def record_image_job(article_dir: Path, root: Path, *, meta: dict[str, Any] | None = None) -> None:
    stamp = ensure_run_started(article_dir, root)
    stamp["counters"]["derouter_image_jobs"] = int(stamp["counters"].get("derouter_image_jobs") or 0) + 1
    _append_call(stamp, {"kind": "derouter_image", **(meta or {})})
    refresh_soft_wall_note(article_dir, root)
    save_stamp(article_dir, stamp)


def assert_kie_fallback_allowed(article_dir: Path, root: Path) -> None:
    check_not_blocked(article_dir)
    stamp = ensure_run_started(article_dir, root)
    caps = stamp.get("caps") or load_caps(root)
    used = int(stamp["counters"].get("kie_image_fallbacks") or 0)
    limit = int(caps.get("kie_image_fallback_max") or 1)
    if used >= limit:
        raise BudgetBlocker(
            "kie_image_fallback",
            f"used {used}/{limit} Kie fallback(s) this run",
        )


def record_kie_fallback(article_dir: Path, root: Path, *, meta: dict[str, Any] | None = None) -> None:
    stamp = ensure_run_started(article_dir, root)
    stamp["counters"]["kie_image_fallbacks"] = int(stamp["counters"].get("kie_image_fallbacks") or 0) + 1
    _append_call(stamp, {"kind": "kie_image_fallback", **(meta or {})})
    save_stamp(article_dir, stamp)


def assert_cover_image_round_allowed(article_dir: Path, root: Path, round_kind: str) -> None:
    """round_kind: 'initial' | 'panel_regen'. Max 2 rounds (initial + one panel regen)."""
    check_not_blocked(article_dir)
    stamp = ensure_run_started(article_dir, root)
    caps = stamp.get("caps") or load_caps(root)
    rounds: list[str] = list(stamp["counters"].get("cover_image_rounds") or [])
    limit = int(caps.get("cover_qa_image_attempts_max") or 2)
    if round_kind in rounds:
        raise BudgetBlocker(
            "cover_qa_rounds",
            f"round {round_kind!r} already recorded",
        )
    if len(rounds) >= limit:
        raise BudgetBlocker(
            "cover_qa_rounds",
            f"{len(rounds)}/{limit} cover image rounds used — third QA cycle forbidden",
        )


def record_cover_image_round(article_dir: Path, root: Path, round_kind: str) -> None:
    assert_cover_image_round_allowed(article_dir, root, round_kind)
    stamp = load_stamp(article_dir)
    rounds: list[str] = list(stamp["counters"].get("cover_image_rounds") or [])
    rounds.append(round_kind)
    stamp["counters"]["cover_image_rounds"] = rounds
    _append_call(stamp, {"kind": "cover_image_round", "round": round_kind})
    save_stamp(article_dir, stamp)


def set_blocked(article_dir: Path, root: Path, reason: str, detail: str = "") -> None:
    stamp = ensure_run_started(article_dir, root)
    stamp["blocked"] = {
        "reason": reason,
        "detail": detail,
        "at": _now_iso(),
    }
    save_stamp(article_dir, stamp)


def append_fix_queue(root: Path, article_dir: Path, reason: str, detail: str) -> None:
    path = root / FIX_QUEUE_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"\n## {_now_iso()} — BUDGET BLOCKER | {reason}\n"
        f"- article: `{article_dir}`\n"
        f"- detail: {detail or '(none)'}\n"
        f"- action: pipeline STOP; no Publish; artifacts kept in repo\n"
    )
    existing = path.read_text(encoding="utf-8") if path.is_file() else "# Pipeline fix queue\n"
    path.write_text(existing.rstrip() + "\n" + line, encoding="utf-8")


def handle_budget_blocker(
    article_dir: Path,
    root: Path,
    exc: BudgetBlocker,
    *,
    exit_code: int = 0,
) -> int:
    set_blocked(article_dir, root, exc.reason, exc.detail)
    append_fix_queue(root, article_dir, exc.reason, exc.detail)
    print(str(exc), file=sys.stderr)
    print(
        "BUDGET: pipeline STOP — no further Derouter/Kie calls; "
        "do not Publish; see memory/pipeline-fix-queue.md",
        file=sys.stderr,
    )
    return exit_code


def cmd_init(article_dir: Path, root: Path) -> int:
    stamp = ensure_run_started(article_dir, root)
    print(f"OK budget init {stamp_path(article_dir)} caps={stamp.get('caps')}")
    return 0


def cmd_check(article_dir: Path, root: Path) -> int:
    try:
        check_not_blocked(article_dir)
    except BudgetBlocker as exc:
        return handle_budget_blocker(article_dir, root, exc)
    refresh_soft_wall_note(article_dir, root)
    stamp = load_stamp(article_dir)
    c = stamp.get("counters") or {}
    print(
        f"OK budget check chat={c.get('derouter_chat_calls')} "
        f"image={c.get('derouter_image_jobs')} "
        f"kie={c.get('kie_image_fallbacks')} "
        f"cover_rounds={c.get('cover_image_rounds')}"
    )
    return 0


def cmd_status(article_dir: Path) -> int:
    stamp = load_stamp(article_dir)
    print(json.dumps(stamp, ensure_ascii=False, indent=2))
    return 0


def cmd_doctor(root: Path) -> int:
    script = root / "scripts/excalibur_blog_budget_guard.py"
    tenant = root / "shared/tenant-config.json"
    if not script.is_file() or not tenant.is_file():
        print("FAIL budget_guard doctor", file=sys.stderr)
        return 1
    data = json.loads(tenant.read_text(encoding="utf-8"))
    rb = data.get("run_budget")
    if not isinstance(rb, dict):
        print("FAIL tenant-config missing run_budget block", file=sys.stderr)
        return 1
    for key in DEFAULT_CAPS:
        if key not in rb:
            print(f"FAIL run_budget missing {key}", file=sys.stderr)
            return 1
    print("OK budget_guard doctor")
    return 0


def resolve_article_dir(root: Path, raw: str) -> Path:
    p = Path(raw)
    if not p.is_absolute():
        p = root / p
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", nargs="?", choices=("init", "check", "status"), default="check")
    ap.add_argument("--article-dir", default="")
    ap.add_argument("--doctor", action="store_true")
    args = ap.parse_args()

    root = project_root()
    if args.doctor:
        return cmd_doctor(root)

    if not args.article_dir:
        print("❌ budget_guard: --article-dir required", file=sys.stderr)
        return 2

    article_dir = resolve_article_dir(root, args.article_dir)
    article_dir.mkdir(parents=True, exist_ok=True)

    if args.command == "init":
        return cmd_init(article_dir, root)
    if args.command == "status":
        return cmd_status(article_dir)
    return cmd_check(article_dir, root)


if __name__ == "__main__":
    raise SystemExit(main())
