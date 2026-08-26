#!/usr/bin/env python3
"""Cover Fixer (Фиксик) — pixel FAIL → regen cover panel → re-QA bytes.

Никогда не peel/inpaint по человеку. Wordstat query strips на обложке запрещены навсегда.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_cover_qa_pixels import (
    analyze_cover_pixels,
    load_json,
    md5_file,
    stamp_cover_qa_json,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def run_cmd(root: Path, args: list[str]) -> int:
    proc = subprocess.run([sys.executable, *args], cwd=str(root))
    return int(proc.returncode)


def pixel_qa(article_dir: Path, root: Path, manifest: dict[str, Any] | None) -> Any:
    cover = article_dir / "cover" / "cover.png"
    return analyze_cover_pixels(cover, manifest=manifest)


def needs_artifact_fix(result: Any) -> bool:
    checks = result.checks
    return not (
        checks.get("pixel_no_text_on_clothing")
        and checks.get("pixel_no_inpaint_artifacts")
    )


def needs_host_fix(result: Any) -> bool:
    checks = result.checks
    return not (
        checks.get("pixel_host_close_up") and checks.get("pixel_host_not_distant_fullbody")
    )


HOST_CLOSEUP_PROMPT_SUFFIX = (
    "HOST CROP LOCK (mandatory): close-up face+shoulders — host face height ~35–50% of frame, "
    "upper-left or center-left (~35% frame width). NOT distant full-body tiny speck; "
    "face height must exceed 14% of frame. Phone in hand at chest level, fully readable."
)


def regen_cover_panel(article_dir: Path, root: Path) -> bool:
    regen = root / "scripts" / "excalibur_blog_quad_regen_panels.py"
    rel = article_dir.relative_to(root)
    rc = run_cmd(
        root,
        [
            str(regen),
            "--article-dir",
            str(rel),
            "--slots",
            "cover",
        ],
    )
    return rc == 0


def regen_cover_host_closeup(article_dir: Path, root: Path) -> bool:
    """grsai solo i2i with HOST_CROP_LOCK suffix — B10 fixer path (face_h_frac 0.12→0.58)."""
    solo = root / "scripts" / "excalibur_blog_grsai_solo_cover.py"
    rel = article_dir.relative_to(root)
    rc = run_cmd(
        root,
        [
            str(solo),
            "--article-dir",
            str(rel),
            "--prompt-suffix",
            HOST_CLOSEUP_PROMPT_SUFFIX,
        ],
    )
    return rc == 0


def needs_layout_fix(result: Any) -> bool:
    checks = result.checks
    return not (
        checks.get("pixel_hook_title_present")
        and checks.get("pixel_phone_readable")
        and checks.get("pixel_meme_present")
        and checks.get("pixel_layout_not_collapsed")
        and checks.get("pixel_designed_thumbnail")
        and checks.get("pixel_no_wordstat_query_strips")
    )


def run_fixer(
    article_dir: Path,
    root: Path,
    *,
    max_rounds: int = 2,
    allow_regen: bool = True,
) -> dict[str, Any]:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    manifest = load_json(manifest_path) if manifest_path.is_file() else None
    meta_path = article_dir / "article.meta.json"
    topic_id = ""
    if meta_path.is_file():
        try:
            topic_id = str(load_json(meta_path).get("topic_id") or "")
        except json.JSONDecodeError:
            pass
    if manifest:
        topic_id = topic_id or str(manifest.get("topic_id") or "")

    log: list[str] = []
    last_result = None
    for round_idx in range(1, max_rounds + 1):
        last_result = pixel_qa(article_dir, root, manifest)
        log.append(f"round {round_idx}: pixel QA {last_result.status}")
        if last_result.status == "PASS":
            stamp_cover_qa_json(article_dir, last_result, topic_id=topic_id)
            return {
                "status": "PASS",
                "rounds": round_idx,
                "cover_md5": md5_file(article_dir / "cover" / "cover.png"),
                "log": log,
                "pixel_description": last_result.evidence.get("pixel_description"),
            }

        artifact_fail = needs_artifact_fix(last_result)
        host_fail = needs_host_fix(last_result)
        layout_fail = needs_layout_fix(last_result)

        if layout_fail or artifact_fail or host_fail:
            if allow_regen:
                if host_fail and not layout_fail and not artifact_fail:
                    log.append(
                        f"round {round_idx}: host close-up FAIL → grsai solo regen "
                        "(HOST_CROP_LOCK suffix, no peel/inpaint person)"
                    )
                    regen_ok = regen_cover_host_closeup(article_dir, root)
                else:
                    reason = (
                        "layout/hook/phone/meme/wordstat-strip FAIL"
                        if layout_fail
                        else "inpaint/text/host FAIL"
                    )
                    log.append(f"round {round_idx}: {reason} → regen cover panel (no peel/inpaint person)")
                    regen_ok = regen_cover_panel(article_dir, root)
                if regen_ok:
                    if manifest_path.is_file():
                        manifest = load_json(manifest_path)
                    last_result = pixel_qa(article_dir, root, manifest)
                    if last_result.status == "PASS":
                        stamp_cover_qa_json(article_dir, last_result, topic_id=topic_id)
                        return {
                            "status": "PASS",
                            "rounds": round_idx,
                            "cover_md5": md5_file(article_dir / "cover" / "cover.png"),
                            "log": log,
                            "pixel_description": last_result.evidence.get("pixel_description"),
                        }
                else:
                    log.append(f"round {round_idx}: cover regen failed")
            continue

    stamp_cover_qa_json(article_dir, last_result, topic_id=topic_id) if last_result else None
    return {
        "status": "FAIL",
        "rounds": max_rounds,
        "cover_md5": md5_file(article_dir / "cover" / "cover.png"),
        "log": log,
        "errors": last_result.errors if last_result else [],
        "checks": last_result.checks if last_result else {},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--max-rounds", type=int, default=2)
    ap.add_argument("--no-regen", action="store_true")
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    report = run_fixer(
        article_dir,
        root,
        max_rounds=args.max_rounds,
        allow_regen=not args.no_regen,
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
