#!/usr/bin/env python3
"""Download TWO 2K quad canvases, save canvas-quad-01/02.png, split + inject.

``--inject-html`` delegates to ``excalibur_blog_cover_quad_split.py``.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from asset_download import download_url_bytes  # noqa: E402
from excalibur_blog_cover_slots import CANVAS_FILES  # noqa: E402


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url", default="", help="MCP result URL (or read cover/quad-mcp-result.json)")
    ap.add_argument("--inject-html", action="store_true")
    ap.add_argument("--output-size", default="1200x675")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    urls: list[str] = []
    if args.url.strip():
        urls = [args.url.strip()]
    result_path = cover_dir / "quad-mcp-result.json"
    if result_path.is_file():
        payload = json.loads(result_path.read_text(encoding="utf-8"))
        listed = payload.get("urls")
        if isinstance(listed, list) and listed:
            urls = [str(x).strip() for x in listed if str(x).strip()]
        elif payload.get("url") and not urls:
            urls = [str(payload.get("url") or "").strip()]
    if len(urls) < 2:
        print(
            "❌ QUAD APPLY BLOCKER: нужны 2 URL (Derouter, 2 кадра 2K) в cover/quad-mcp-result.json → urls",
            file=sys.stderr,
        )
        return 1

    for rel, url in zip(CANVAS_FILES, urls[:2]):
        canvas_path = article_dir / rel
        data, _evidence = download_url_bytes(url)
        canvas_path.write_bytes(data)
        print(f"OK canvas={canvas_path}")

    result_json = cover_dir / "quad-mcp-result.json"
    result_json.write_text(
        json.dumps({"provider": "derouter", "urls": urls[:2]}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_cover_quad_split.py"),
        "--article-dir",
        str(article_dir),
        "--manifest",
        "cover/quad-manifest.json",
        "--output-size",
        args.output_size,
    ]
    if args.inject_html:
        cmd.append("--inject-html")
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
