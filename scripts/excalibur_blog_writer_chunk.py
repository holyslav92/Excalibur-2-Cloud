#!/usr/bin/env python3
"""Writer longform chunking — 3 Derouter Opus parts on first try (avoid HTTP 524).

Thin conductor: splits assembled user inputs by H2 outline into ~3 parts,
calls excalibur_blog_derouter_opus_chat.py per part, merges drafts/writer.html.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def inline_count_from_tenant(root: Path) -> int:
    tenant_path = root / "shared/tenant-config.json"
    if not tenant_path.is_file():
        return 7
    import json

    tenant = json.loads(tenant_path.read_text(encoding="utf-8"))
    if tenant.get("inline_image_count") in (3, 7):
        return int(tenant["inline_image_count"])
    if str(tenant.get("publish_format") or "").casefold() == "longform":
        return 7
    return 7


def extract_h2_outline(user_text: str) -> list[str]:
    """Извлечь плановые H2 из user bundle (title-brief, research, явные маркеры)."""
    titles: list[str] = []
    for line in user_text.splitlines():
        line = line.strip()
        if re.match(r"^#{1,3}\s+", line):
            t = re.sub(r"^#{1,3}\s+", "", line).strip()
            if t and t.lower() not in {"faq", "частые вопросы"}:
                titles.append(t)
        m = re.search(r"<h2[^>]*>(.*?)</h2>", line, re.I)
        if m:
            t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
            if t:
                titles.append(t)
        m = re.match(r"^H2:\s*(.+)$", line, re.I)
        if m:
            titles.append(m.group(1).strip())
    # Дедуп с сохранением порядка
    seen: set[str] = set()
    unique: list[str] = []
    for t in titles:
        key = t.casefold()
        if key not in seen:
            seen.add(key)
            unique.append(t)
    return unique


def split_h2_groups(h2s: list[str], parts: int) -> list[list[str]]:
    if not h2s:
        return [[] for _ in range(parts)]
    n = len(h2s)
    base, rem = divmod(n, parts)
    groups: list[list[str]] = []
    idx = 0
    for p in range(parts):
        size = base + (1 if p < rem else 0)
        groups.append(h2s[idx : idx + size])
        idx += size
    return groups


def build_part_prompt(
    user_text: str,
    part_index: int,
    total_parts: int,
    h2_group: list[str],
) -> str:
    h2_block = "\n".join(f"- {h}" for h in h2_group) if h2_group else "(см. research)"
    scope = (
        "открытие статьи + первые H2 секции"
        if part_index == 1
        else "средние H2 секции"
        if part_index < total_parts
        else "оставшиеся H2 + практика/ограничения + CTA (без FAQ — Sol добавит)"
    )
    opening_note = ""
    if part_index == 1:
        opening_note = (
            "\nОткрытие: hook + прозаический лид 4–6 предложений (news-casus актуалочка, часть истории). "
            "ЗАПРЕЩЕНО: TL;DR, «Быстрый инсайт», bullet-списки <ul>/<ol> до первого H2. "
            "После лида — excalibur-cta-early (TG+MAX only). "
            "В теле: один comment magnet — острый вопрос «…?» после финала или перед mid CTA.\n"
        )
    return (
        f"{user_text}\n\n"
        f"=== WRITER CHUNK {part_index}/{total_parts} ===\n"
        f"Напиши ТОЛЬКО фрагмент HTML для: {scope}.\n"
        f"{opening_note}"
        f"H2 в этом чанке:\n{h2_block}\n"
        "Без <h1>. Чистый HTML-фрагмент. Не дублируй секции из других чанков.\n"
        "HTML whitelist: <b> не <strong>, <i> не <em>.\n"
    )


def merge_writer_fragments(fragments: list[str]) -> str:
    parts: list[str] = []
    for frag in fragments:
        text = frag.strip()
        if not text:
            continue
        # Убрать markdown fences если Opus обернул
        text = re.sub(r"^```(?:html)?\s*", "", text)
        text = re.sub(r"\s*```\s*$", "", text)
        parts.append(text.strip())
    merged = "\n\n".join(parts)
    if merged and not merged.endswith("\n"):
        merged += "\n"
    return merged


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--system-file", required=True)
    ap.add_argument("--user-file", required=True)
    ap.add_argument("--output", default="drafts/writer.html")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--parts", type=int, default=3)
    ap.add_argument(
        "--single-shot",
        action="store_true",
        help="Force one Derouter call (skip chunking even on longform)",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    user_path = Path(args.user_file)
    if not user_path.is_absolute():
        user_path = root / user_path
    system_path = Path(args.system_file)
    if not system_path.is_absolute():
        system_path = root / system_path

    user_text = user_path.read_text(encoding="utf-8")
    inline_count = inline_count_from_tenant(root)
    use_chunk = not args.single_shot and inline_count >= 7

    derouter = root / "scripts/excalibur_blog_derouter_opus_chat.py"
    out_path = Path(args.output)
    if not out_path.is_absolute():
        out_path = article_dir / out_path

    if not use_chunk:
        cmd = [
            sys.executable,
            str(derouter),
            "--role",
            "writer",
            "--system-file",
            str(system_path),
            "--user-file",
            str(user_path),
            "--output",
            str(out_path),
            "--article-dir",
            str(article_dir),
        ]
        return subprocess.call(cmd, cwd=str(root))

    h2s = extract_h2_outline(user_text)
    groups = split_h2_groups(h2s, max(1, args.parts))
    fragments: list[str] = []

    with tempfile.TemporaryDirectory(prefix="writer-chunk-") as tmpdir:
        tmp = Path(tmpdir)
        for i, group in enumerate(groups, start=1):
            part_user = tmp / f"writer-part-{i}-user.md"
            part_out = tmp / f"writer-part-{i}.html"
            part_user.write_text(
                build_part_prompt(user_text, i, len(groups), group),
                encoding="utf-8",
            )
            cmd = [
                sys.executable,
                str(derouter),
                "--role",
                "writer",
                "--system-file",
                str(system_path),
                "--user-file",
                str(part_user),
                "--output",
                str(part_out),
                "--article-dir",
                str(article_dir),
                "--stamp-path",
                str(article_dir / f"derouter-opus-stamp-writer-part{i}.json"),
            ]
            print(f"WRITER chunk {i}/{len(groups)} H2s={group or ['(auto)']}")
            rc = subprocess.call(cmd, cwd=str(root))
            if rc != 0:
                print(f"DEROUTER WRITER BLOCKER chunk {i}/{len(groups)} exit={rc}", file=sys.stderr)
                return rc
            fragments.append(part_out.read_text(encoding="utf-8"))

    merged = merge_writer_fragments(fragments)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(merged, encoding="utf-8")
    print(f"WROTE {out_path} (merged {len(groups)} chunks, {len(merged)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
