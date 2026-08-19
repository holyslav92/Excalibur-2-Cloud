#!/usr/bin/env python3
"""Сохранить 2 URL Derouter MCP и разрезать на cover + 7 inline.

Сам MCP вызывается Cover-агентом (server DEROOTER). Этот скрипт — apply path.
Kie API здесь не вызывается.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from excalibur_blog_cover_slots import CANVAS_COUNT, CANVAS_FILES, PIPELINE_ID  # noqa: E402


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url-1", default="")
    ap.add_argument("--url-2", default="")
    ap.add_argument("--inject-html", action="store_true", default=True)
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    urls = [args.url_1.strip(), args.url_2.strip()]
    if not all(urls):
        result_path = cover_dir / "quad-mcp-result.json"
        if result_path.is_file():
            data = json.loads(result_path.read_text(encoding="utf-8"))
            existing = data.get("urls") or []
            if isinstance(existing, list) and len(existing) >= CANVAS_COUNT:
                urls = [str(existing[0]).strip(), str(existing[1]).strip()]
            elif data.get("url"):
                print(
                    "❌ DEROUTER IMAGE BLOCKER: нужен массив urls из 2 кадров, не один url",
                    file=sys.stderr,
                )
                return 1
    if not all(urls):
        print(
            "❌ DEROUTER IMAGE BLOCKER: передай --url-1 и --url-2 после MCP DEROOTER",
            file=sys.stderr,
        )
        return 1

    payload = {
        "provider": "derouter",
        "pipeline": PIPELINE_ID,
        "urls": urls,
        "canvases": list(CANVAS_FILES),
        "resolution": "2K",
        "jobs": CANVAS_COUNT,
    }
    (cover_dir / "quad-mcp-result.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"OK result={cover_dir / 'quad-mcp-result.json'} jobs={CANVAS_COUNT}")

    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_quad_apply.py"),
        "--article-dir",
        str(article_dir),
    ]
    if args.inject_html:
        cmd.append("--inject-html")
    return subprocess.run(cmd, cwd=str(root)).returncode


if __name__ == "__main__":
    raise SystemExit(main())
