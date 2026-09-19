#!/usr/bin/env python3
"""Post-Sol draft gate on article.html (before Stylo / full quality-bar-9)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from excalibur_blog_html_linter import ALLOWED_TAGS, lint_html_file
from excalibur_blog_quality_bar_9_gate import (
    WORD_HARD_MAX,
    WORD_TARGET_MAX,
    WORD_TARGET_MIN,
    check_comment_magnet,
    check_no_composite_disclaimer,
    check_spine_once_no_recap,
    count_h2,
    count_inline_figures,
    word_count,
)

H2_EXPECT = 6
INLINE_MIN = 7


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("-o", "--output", default="sol-draft-gate.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    article_dir = (
        root / args.article_dir
        if not Path(args.article_dir).is_absolute()
        else Path(args.article_dir)
    )
    html_path = article_dir / "article.html"
    errors: list[str] = []

    if not html_path.is_file():
        errors.append("missing article.html")
        report = {
            "gate": "sol-draft",
            "status": "BLOCK",
            "all_pass": False,
            "checks": {},
            "errors": errors,
            "metrics": {},
        }
        out = article_dir / Path(args.output).name
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 1

    lint = lint_html_file(html_path, ALLOWED_TAGS)
    html = html_path.read_text(encoding="utf-8")
    wc = word_count(html)
    h2c = count_h2(html)
    inlines = count_inline_figures(html)

    spine_ok, spine_errors = check_spine_once_no_recap(html)
    composite_ok, composite_errors = check_no_composite_disclaimer(html)
    magnet_ok, magnet_errors = check_comment_magnet(html)

    checks = {
        "html_linter": lint.get("verdict") == "pass",
        "word_count_1400_1600": WORD_TARGET_MIN <= wc <= WORD_TARGET_MAX,
        "word_count_hard_max_1750": wc <= WORD_HARD_MAX,
        "spine_once_no_recap": spine_ok,
        "comment_magnet_question": magnet_ok,
        "no_composite_disclaimer": composite_ok,
        "inline_figures_7": inlines >= INLINE_MIN,
        "h2_count_6": h2c >= H2_EXPECT,
    }

    if not checks["html_linter"]:
        for err in lint.get("errors") or []:
            errors.append(f"html_linter: {err}")
    if not checks["word_count_1400_1600"]:
        errors.append(f"word_count {wc} outside {WORD_TARGET_MIN}-{WORD_TARGET_MAX}")
    if not checks["word_count_hard_max_1750"]:
        errors.append(f"word_count {wc} exceeds hard max {WORD_HARD_MAX}")
    if spine_errors:
        errors.extend(spine_errors)
    if composite_errors:
        errors.extend(composite_errors)
    if magnet_errors:
        errors.extend(magnet_errors)
    if not checks["inline_figures_7"]:
        errors.append(f"inline figures {inlines}, need >={INLINE_MIN}")
    if not checks["h2_count_6"]:
        errors.append(f"h2_count {h2c}, need >={H2_EXPECT}")

    all_pass = all(checks.values()) and not errors
    report = {
        "gate": "sol-draft",
        "status": "PASS" if all_pass else "BLOCK",
        "all_pass": all_pass,
        "checks": checks,
        "errors": errors,
        "metrics": {
            "word_count": wc,
            "inline_figures": inlines,
            "h2_count": h2c,
        },
    }
    out = article_dir / Path(args.output).name
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
