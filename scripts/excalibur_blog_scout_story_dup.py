#!/usr/bin/env python3
"""HARD Scout story-duplicate gate — refuse near-clone legal risk + plot vs published siblings."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_published_rows(root: Path) -> list[dict[str, str]]:
    ledger_path = root / "shared/published-articles.md"
    rows: list[dict[str, str]] = []
    if not ledger_path.is_file():
        return rows
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| 20"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        rows.append(
            {
                "date": cells[0],
                "topic_id": cells[1].upper(),
                "slug": cells[2],
                "url": cells[3],
                "status": cells[4].lower(),
            }
        )
    return rows


def fetch_recent_wp_topics(limit: int = 40) -> list[dict[str, str]]:
    site_url = (os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or "").strip()
    if not site_url:
        return []
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=date,slug,title",
    )
    try:
        with urlopen(Request(endpoint, headers={"User-Agent": "ExcaliburScoutStoryDup/1.0"}), timeout=12) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception:
        return []

    topics: list[dict[str, str]] = []
    for item in payload:
        title = item.get("title", {}).get("rendered", "") if isinstance(item.get("title"), dict) else ""
        title = re.sub(r"<[^>]+>", " ", str(title))
        slug = str(item.get("slug") or "")
        if not slug:
            continue
        topics.append(
            {
                "topic_id": f"LIVE-{slug[:24]}".upper(),
                "primary_query": " ".join([slug.replace("-", " "), title]).strip(),
                "slug": slug,
                "priority": "live",
            }
        )
    return topics


def topic_comparable_text(topic: dict[str, str]) -> str:
    return " ".join(
        [
            str(topic.get("primary_query") or "").strip(),
            str(topic.get("slug") or "").strip().replace("-", " "),
            str(topic.get("title") or "").strip(),
        ]
    ).strip()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_story_clusters(root: Path) -> list[dict[str, Any]]:
    path = root / "shared" / "scout-story-clusters.json"
    if not path.is_file():
        return []
    data = load_json(path)
    return [c for c in (data.get("clusters") or []) if isinstance(c, dict) and c.get("id")]


def normalize_story_blob(text: str) -> str:
    text = (text or "").lower().replace("-", " ")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
    # Latin slug tokens → Cyrillic stems for cluster regex (nasledstvo → наследство)
    latin_to_ru = {
        "nasledstvo": "наследство",
        "naslednik": "наследник",
        "nasled": "наслед",
        "syn": "сын",
        "otkaz": "отказ",
        "braka": "брака",
        "pervogo": "первого",
        "avans": "аванс",
        "matkapital": "маткапитал",
        "doverennost": "доверенность",
        "svo": "сво",
        "zadatok": "задаток",
        "torg": "торг",
        "million": "миллион",
        "milliona": "миллиона",
    }
    tokens = text.split()
    expanded: list[str] = []
    for tok in tokens:
        expanded.append(tok)
        if tok in latin_to_ru:
            expanded.append(latin_to_ru[tok])
    return " ".join(expanded)


def cluster_matches(text: str, cluster: dict[str, Any]) -> bool:
    blob = normalize_story_blob(text)
    if not blob:
        return False
    for group in cluster.get("required_groups") or []:
        if not isinstance(group, list) or not group:
            return False
        if not any(re.search(str(pat), blob, flags=re.IGNORECASE) for pat in group):
            return False
    return True


def detect_story_clusters(text: str, clusters: list[dict[str, Any]]) -> list[str]:
    return [str(c["id"]) for c in clusters if cluster_matches(text, c)]


def load_published_titles_only(root: Path) -> list[str]:
    titles: list[str] = []
    for rel in ("shared/published-titles.md", "published-titles-only.md"):
        path = root / rel
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or not line or line.startswith("|"):
                continue
            titles.append(line.lstrip("- ").strip())
    return titles


def load_article_meta_texts(root: Path) -> list[dict[str, str]]:
    articles_dir = root / "memory" / "blog" / "articles"
    rows: list[dict[str, str]] = []
    if not articles_dir.is_dir():
        return rows
    for path in sorted(articles_dir.iterdir()):
        if not path.is_dir():
            continue
        meta_path = path / "article.meta.json"
        if not meta_path.is_file():
            continue
        try:
            meta = load_json(meta_path)
        except json.JSONDecodeError:
            continue
        status = str(meta.get("status") or "").lower()
        if status and status not in {"published", "in_progress", "draft_ready"}:
            continue
        rows.append(
            {
                "topic_id": str(meta.get("topic_id") or path.name.split("-", 1)[0]).upper(),
                "slug": str(meta.get("slug") or ""),
                "title": " ".join(
                    str(meta.get(k) or "")
                    for k in ("h1", "title", "primary_query", "description")
                ).strip(),
                "source": "article_meta",
            }
        )
    return rows


def build_published_story_sources(root: Path, *, live_limit: int = 40) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def _add(topic_id: str, slug: str, title: str, source: str) -> None:
        slug = slug.strip().strip("/").lower()
        topic_id = topic_id.strip().upper() or f"LIVE-{slug[:24]}".upper()
        key = (topic_id, slug)
        if key in seen:
            return
        seen.add(key)
        text = topic_comparable_text({"primary_query": title, "slug": slug})
        sources.append(
            {
                "topic_id": topic_id,
                "slug": slug,
                "title": title.strip(),
                "text": text,
                "source": source,
            }
        )

    for row in load_published_rows(root):
        if row.get("status") not in {"published", "in_progress", "draft_ready"}:
            continue
        _add(row.get("topic_id") or "", row.get("slug") or "", row.get("slug", "").replace("-", " "), "ledger")

    for row in load_article_meta_texts(root):
        _add(row["topic_id"], row["slug"], row["title"], row["source"])

    for title in load_published_titles_only(root):
        _add("TITLE", "", title, "published_titles")

    for item in fetch_recent_wp_topics(limit=live_limit):
        slug = str(item.get("slug") or "")
        title = str(item.get("primary_query") or slug.replace("-", " "))
        _add(str(item.get("topic_id") or ""), slug, title, "live_wp")

    return sources


def check_story_duplicate(
    new_text: str,
    published_sources: list[dict[str, str]],
    clusters: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    new_ids = detect_story_clusters(new_text, clusters)
    if not new_ids:
        return []

    cluster_by_id = {str(c["id"]): c for c in clusters}
    warnings: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    for src in published_sources:
        existing_ids = detect_story_clusters(src.get("text") or "", clusters)
        shared = sorted(set(new_ids).intersection(existing_ids))
        for cluster_id in shared:
            key = (cluster_id, str(src.get("topic_id") or src.get("slug") or ""))
            if key in seen:
                continue
            seen.add(key)
            cluster = cluster_by_id.get(cluster_id) or {}
            warnings.append(
                {
                    "severity": "CRITICAL",
                    "cluster_id": cluster_id,
                    "cluster_label": cluster.get("label_ru") or cluster_id,
                    "topic_id": src.get("topic_id") or "",
                    "slug": src.get("slug") or "",
                    "source": src.get("source") or "",
                    "message": (
                        f"STORY DUPLICATE: new topic matches published sibling cluster "
                        f"«{cluster.get('label_ru') or cluster_id}» "
                        f"({src.get('topic_id') or src.get('slug')} via {src.get('source')}). "
                        "Wordstat may refine phrasing but must NOT recycle the same legal risk + plot."
                    ),
                }
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description="HARD Scout story-duplicate gate")
    ap.add_argument("--text", required=True, help="title draft + hook + primary_query + slug")
    ap.add_argument("--live-limit", type=int, default=40)
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = project_root()
    clusters = load_story_clusters(root)
    if not clusters:
        print("WARN: scout-story-clusters.json missing — gate skipped")
        return 0

    sources = build_published_story_sources(root, live_limit=max(1, min(args.live_limit, 100)))
    new_ids = detect_story_clusters(args.text, clusters)
    if not new_ids:
        print("✅ STORY DUP PASS: no published plot cluster detected in candidate text")
        return 0

    print(f"Candidate story clusters: {', '.join(new_ids)}")
    warnings = check_story_duplicate(args.text, sources, clusters)
    if not warnings:
        print("✅ STORY DUP PASS: cluster(s) detected but no published sibling match")
        return 0

    print("❌ STORY DUPLICATE BLOCKER:")
    for w in warnings:
        print(f"  [{w['severity']}] {w['cluster_id']} | {w['topic_id']} ({w['source']})")
        print(f"  {w['message']}")
    print(
        "BLOCKER: SCOUT STORY DUPLICATE — pick a distinct legal risk + plot "
        "(see shared/scout-story-clusters.json). Wordstat rework ≠ same story."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
