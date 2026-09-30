#!/usr/bin/env python3
"""Indexer: regenerate blog llms.txt artifacts and stamp indexer-gate.json.

Does not edit article.html. Wraps excalibur_blog_llms_generator.py + secret-scan.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.excalibur_blog_site_base import (  # noqa: E402
    SITE_BASE_PLACEHOLDER,
    find_secret_scan_hits,
)
from scripts.excalibur_repo_paths import (  # noqa: E402
    repo_relative,
    resolve_article_dir,
    resolve_article_output,
)


def project_root() -> Path:
    return ROOT


def load_meta(article_dir: Path) -> dict:
    path = article_dir / "article.meta.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def cover_qa_status(article_dir: Path) -> str | None:
    qa_path = article_dir / "cover" / "cover_qa.json"
    if not qa_path.is_file():
        return None
    try:
        data = json.loads(qa_path.read_text(encoding="utf-8"))
        return str(data.get("status") or "").strip() or None
    except json.JSONDecodeError:
        return None


def run_llms_generator(root: Path, blog_path: str) -> tuple[int, str]:
    script = root / "scripts/excalibur_blog_llms_generator.py"
    cmd = [
        sys.executable,
        str(script),
        "--blog-dir",
        "memory/blog/articles",
        "--blog-path",
        blog_path,
        "--out-dir",
        "memory/blog",
    ]
    proc = subprocess.run(
        cmd,
        cwd=root,
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def secret_scan_files(paths: list[Path]) -> tuple[str, list[str]]:
    errors: list[str] = []
    for path in paths:
        if not path.is_file():
            errors.append(f"missing llms artifact {path}")
            continue
        hits = find_secret_scan_hits(path.read_text(encoding="utf-8"))
        if hits:
            errors.append(f"{path.name}: secret-scan hits {hits}")
    status = "PASS" if not errors else "FAIL"
    return status, errors


def slug_in_llms(slug: str, llms_txt: str) -> bool:
    slug = (slug or "").strip().strip("/")
    if not slug:
        return False
    return slug in llms_txt


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True, help="memory/blog/articles/<id>-<slug>")
    ap.add_argument("--blog-path", default="/", help="URL prefix for posts (default /)")
    ap.add_argument("-o", "--output", default=None, help="indexer-gate.json path")
    ap.add_argument("--root", default=".", help="Repo root")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    article_dir = resolve_article_dir(args.article_dir, root)
    out_path = resolve_article_output(
        args.output,
        article_dir=article_dir,
        root=root,
        default_name="indexer-gate.json",
    )

    errors: list[str] = []
    html_path = article_dir / "article.html"
    if not article_dir.is_dir():
        errors.append(f"article-dir not found: {article_dir}")
    if not html_path.is_file():
        errors.append(f"missing {html_path.name}")

    meta = load_meta(article_dir)
    topic_id = str(meta.get("topic_id") or "").strip()
    slug = str(meta.get("slug") or "").strip()
    if not slug and article_dir.name.startswith("B"):
        slug = article_dir.name.split("-", 1)[-1] if "-" in article_dir.name else article_dir.name

    gen_rc, gen_log = run_llms_generator(root, args.blog_path)
    if gen_rc != 0:
        errors.append(f"llms_generator exited {gen_rc}")
        if gen_log.strip():
            errors.append(gen_log.strip()[-2000:])

    llms_dir = root / "memory/blog"
    llms_paths = [llms_dir / "llms.txt", llms_dir / "llms-full.txt"]
    secret_status, scan_errors = secret_scan_files(llms_paths)
    errors.extend(scan_errors)

    has_placeholder = False
    llms_txt_path = llms_paths[0]
    if llms_txt_path.is_file():
        llms_text = llms_txt_path.read_text(encoding="utf-8")
        has_placeholder = SITE_BASE_PLACEHOLDER in llms_text
        if not has_placeholder:
            errors.append(f"llms.txt must contain {SITE_BASE_PLACEHOLDER}")
        if slug and not slug_in_llms(slug, llms_text):
            errors.append(f"slug {slug!r} not found in llms.txt")

    status = "PASS" if not errors else "FAIL"
    report: dict = {
        "agent": "excalibur-blog-indexer",
        "status": status,
        "checked_at": date.today().isoformat(),
        "topic_id": topic_id,
        "article_dir": repo_relative(article_dir, root),
        "slug": slug,
        "llms_artifacts": [
            "memory/blog/llms.txt",
            "memory/blog/llms-full.txt",
        ],
        "secret_scan": secret_status,
        "has_site_base_placeholder": has_placeholder,
        "article_html_edited": False,
        "errors": errors,
    }
    cover_status = cover_qa_status(article_dir)
    if cover_status:
        report["cover_qa_status"] = cover_status

    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if status == "PASS":
        print(f"INDEXER PASS → {repo_relative(out_path, root)}")
        if gen_log.strip():
            for line in gen_log.strip().splitlines()[-5:]:
                print(line)
        return 0

    print(f"INDEXER FAIL → {repo_relative(out_path, root)}", file=sys.stderr)
    for err in errors:
        print(f"  - {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
