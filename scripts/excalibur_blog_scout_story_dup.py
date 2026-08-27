#!/usr/bin/env python3
"""HARD Scout story-duplicate gate — refuse near-clone legal risk + plot vs published siblings."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from urllib.request import Request, urlopen


DEFAULT_ANTI_REPEAT_DAYS = 30
DEFAULT_LIVE_LIMIT = 20


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    text = str(value).strip()
    if not text:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(text[: len(fmt.replace("%", "0"))], fmt).date()
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def load_story_cluster_config(root: Path) -> dict[str, Any]:
    path = root / "shared" / "scout-story-clusters.json"
    if not path.is_file():
        return {"anti_repeat_days": DEFAULT_ANTI_REPEAT_DAYS, "clusters": []}
    return load_json(path)


def anti_repeat_days(root: Path) -> int:
    cfg = load_story_cluster_config(root)
    days = int(cfg.get("anti_repeat_days") or DEFAULT_ANTI_REPEAT_DAYS)
    return max(1, days)


def used_clusters_path(root: Path) -> Path:
    cfg = load_story_cluster_config(root)
    rel = str(cfg.get("used_clusters_log") or "memory/scout/used-clusters.json")
    return root / rel


def load_story_clusters(root: Path) -> list[dict[str, Any]]:
    data = load_story_cluster_config(root)
    return [c for c in (data.get("clusters") or []) if isinstance(c, dict) and c.get("id")]


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


def fetch_recent_wp_topics(limit: int = DEFAULT_LIVE_LIMIT) -> list[dict[str, str]]:
    site_url = (os.environ.get("PUBLIC_SITE_URL") or os.environ.get("WP_SITE_URL") or "").strip()
    if not site_url:
        return []
    endpoint = urljoin(
        site_url.rstrip("/") + "/",
        f"wp-json/wp/v2/posts?per_page={limit}&orderby=date&order=desc&_fields=date,slug,title",
    )
    try:
        with urlopen(Request(endpoint, headers={"User-Agent": "ExcaliburScoutStoryDup/2.0"}), timeout=12) as response:
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
                "title": title.strip(),
                "date": str(item.get("date") or "")[:10],
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


def normalize_story_blob(text: str) -> str:
    text = (text or "").lower().replace("-", " ")
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip()
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
        "notarius": "нотариус",
        "supruzheskaya": "супружеская",
        "opeka": "опека",
        "bankrotstvo": "банкротство",
        "finupravlyayuschij": "финуправляющий",
        "vypiske": "выписке",
        "vypiska": "выписка",
        "chisto": "чисто",
        "chistaya": "чистая",
        "tri": "три",
        "mesyaca": "месяца",
        "mesyacev": "месяцев",
        "torgov": "торгов",
        "torgi": "торги",
        "zadatok": "задаток",
        "pochti": "почти",
        "vnesli": "внесли",
        "chasov": "часов",
        "do": "до",
        "povestka": "повестка",
        "babushka": "бабушка",
        "pnd": "пнд",
        "chetyre": "четыре",
        "mesyaca": "месяца",
        "rodstvenniki": "родственники",
        "osporili": "оспорили",
        "egrn": "егрн",
        "umershaya": "умершая",
        "zhena": "жена",
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


def load_published_titles_only(root: Path) -> list[dict[str, str]]:
    titles: list[dict[str, str]] = []
    for rel in ("shared/published-titles.md", "published-titles-only.md"):
        path = root / rel
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("#") or not line or line.startswith("|"):
                continue
            titles.append({"title": line.lstrip("- ").strip(), "date": ""})
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
                "date": str(meta.get("date") or ""),
                "source": "article_meta",
            }
        )
    return rows


def within_anti_repeat_window(source_date: date | None, today: date, window_days: int) -> bool:
    if source_date is None:
        return True
    cutoff = today - timedelta(days=window_days)
    return source_date >= cutoff


def build_published_story_sources(
    root: Path,
    *,
    live_limit: int = DEFAULT_LIVE_LIMIT,
    window_days: int | None = None,
    today: date | None = None,
) -> list[dict[str, str]]:
    window_days = window_days if window_days is not None else anti_repeat_days(root)
    today = today or date.today()
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def _add(
        topic_id: str,
        slug: str,
        title: str,
        source: str,
        source_date: date | None = None,
    ) -> None:
        if source_date is not None and not within_anti_repeat_window(source_date, today, window_days):
            return
        slug = slug.strip().strip("/").lower()
        topic_id = topic_id.strip().upper() or f"LIVE-{slug[:24]}".upper()
        key = (topic_id, slug)
        if key in seen:
            return
        seen.add(key)
        text = topic_comparable_text({"primary_query": title, "slug": slug, "title": title})
        sources.append(
            {
                "topic_id": topic_id,
                "slug": slug,
                "title": title.strip(),
                "text": text,
                "source": source,
                "date": source_date.isoformat() if source_date else "",
            }
        )

    for row in load_published_rows(root):
        if row.get("status") not in {"published", "in_progress", "draft_ready"}:
            continue
        _add(
            row.get("topic_id") or "",
            row.get("slug") or "",
            row.get("slug", "").replace("-", " "),
            "ledger",
            parse_iso_date(row.get("date")),
        )

    for row in load_article_meta_texts(root):
        _add(row["topic_id"], row["slug"], row["title"], row["source"], parse_iso_date(row.get("date")))

    for item in load_published_titles_only(root):
        _add("TITLE", "", item["title"], "published_titles", parse_iso_date(item.get("date")))

    for item in fetch_recent_wp_topics(limit=live_limit):
        slug = str(item.get("slug") or "")
        title = str(item.get("title") or item.get("primary_query") or slug.replace("-", " "))
        _add(
            str(item.get("topic_id") or ""),
            slug,
            title,
            "live_wp",
            parse_iso_date(item.get("date")),
        )

    return sources


def load_used_clusters(root: Path) -> list[dict[str, Any]]:
    path = used_clusters_path(root)
    if not path.is_file():
        return []
    try:
        data = load_json(path)
    except json.JSONDecodeError:
        return []
    return [c for c in (data.get("clusters") or []) if isinstance(c, dict) and c.get("cluster_id")]


def locked_cluster_ids(root: Path, today: date | None = None) -> dict[str, dict[str, Any]]:
    today = today or date.today()
    locked: dict[str, dict[str, Any]] = {}
    for row in load_used_clusters(root):
        cluster_id = str(row.get("cluster_id") or "")
        if not cluster_id:
            continue
        locked_until = parse_iso_date(str(row.get("locked_until") or ""))
        if locked_until is not None and locked_until < today:
            continue
        locked[cluster_id] = row
    return locked


def check_locked_clusters(
    new_cluster_ids: list[str],
    root: Path,
    today: date | None = None,
) -> list[dict[str, Any]]:
    today = today or date.today()
    locked = locked_cluster_ids(root, today=today)
    cluster_by_id = {str(c["id"]): c for c in load_story_clusters(root)}
    warnings: list[dict[str, Any]] = []
    for cluster_id in new_cluster_ids:
        row = locked.get(cluster_id)
        if not row:
            continue
        cluster = cluster_by_id.get(cluster_id) or {}
        warnings.append(
            {
                "severity": "CRITICAL",
                "cluster_id": cluster_id,
                "cluster_label": cluster.get("label_ru") or cluster_id,
                "topic_id": str(row.get("topic_id") or ""),
                "slug": str(row.get("slug") or ""),
                "source": "used_clusters_lock",
                "locked_until": str(row.get("locked_until") or ""),
                "message": (
                    f"CLUSTER LOCKED until {row.get('locked_until')}: "
                    f"«{cluster.get('label_ru') or cluster_id}» "
                    f"({row.get('topic_id') or row.get('slug')}). "
                    "Same story/cluster = FAIL even if title differs."
                ),
            }
        )
    return warnings


def check_story_duplicate(
    new_text: str,
    published_sources: list[dict[str, str]],
    clusters: list[dict[str, Any]],
    *,
    root: Path | None = None,
    today: date | None = None,
) -> list[dict[str, Any]]:
    new_ids = detect_story_clusters(new_text, clusters)
    if not new_ids:
        return []

    cluster_by_id = {str(c["id"]): c for c in clusters}
    warnings: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    if root is not None:
        for locked_warning in check_locked_clusters(new_ids, root, today=today):
            key = (locked_warning["cluster_id"], locked_warning.get("source") or "lock")
            if key in seen:
                continue
            seen.add(key)
            warnings.append(locked_warning)

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


def sync_used_clusters(
    root: Path,
    *,
    live_limit: int = DEFAULT_LIVE_LIMIT,
    today: date | None = None,
    dry_run: bool = False,
) -> dict[str, Any]:
    today = today or date.today()
    window_days = anti_repeat_days(root)
    clusters = load_story_clusters(root)
    sources = build_published_story_sources(
        root,
        live_limit=live_limit,
        window_days=window_days,
        today=today,
    )
    path = used_clusters_path(root)
    existing_rows = {str(r.get("cluster_id")): r for r in load_used_clusters(root)}
    updated: list[dict[str, Any]] = list(existing_rows.values())

    for src in sources:
        matched = detect_story_clusters(src.get("text") or "", clusters)
        src_date = parse_iso_date(src.get("date")) or today
        locked_until = src_date + timedelta(days=window_days)
        for cluster_id in matched:
            prior = existing_rows.get(cluster_id)
            if prior:
                prior_until = parse_iso_date(str(prior.get("locked_until") or ""))
                if prior_until and prior_until >= locked_until:
                    continue
            row = {
                "cluster_id": cluster_id,
                "first_seen": src_date.isoformat(),
                "locked_until": locked_until.isoformat(),
                "source": src.get("source") or "",
                "slug": src.get("slug") or "",
                "topic_id": src.get("topic_id") or "",
                "title": src.get("title") or "",
            }
            existing_rows[cluster_id] = row

    updated = sorted(existing_rows.values(), key=lambda r: str(r.get("locked_until") or ""), reverse=True)
    payload = {
        "version": 1,
        "anti_repeat_days": window_days,
        "description": (
            "Closed story clusters — Scout must not reuse until locked_until. "
            "Sync via: python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters"
        ),
        "last_sync": today.isoformat(),
        "clusters": updated,
    }
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    ap = argparse.ArgumentParser(description="HARD Scout story-duplicate gate (30-day window)")
    ap.add_argument("--text", default="", help="title draft + hook + primary_query + slug")
    ap.add_argument("--live-limit", type=int, default=DEFAULT_LIVE_LIMIT)
    ap.add_argument(
        "--sync-used-clusters",
        action="store_true",
        help="Scan ledger + live WP (~20) and refresh memory/scout/used-clusters.json",
    )
    ap.add_argument("--dry-run", action="store_true", help="With --sync-used-clusters: print only")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    root = project_root()
    window_days = anti_repeat_days(root)

    if args.sync_used_clusters:
        payload = sync_used_clusters(root, live_limit=max(1, min(args.live_limit, 100)), dry_run=args.dry_run)
        active = [
            c
            for c in payload.get("clusters") or []
            if parse_iso_date(str(c.get("locked_until") or "")) is None
            or parse_iso_date(str(c.get("locked_until") or "")) >= date.today()
        ]
        print(f"✅ used-clusters sync ({window_days}d window): {len(active)} active lock(s)")
        for row in active[:25]:
            print(
                f"  - {row.get('cluster_id')} until {row.get('locked_until')} "
                f"({row.get('topic_id') or row.get('slug')})"
            )
        if args.dry_run:
            print("(dry-run — file not written)")
        return 0

    if not args.text.strip():
        ap.error("--text is required unless --sync-used-clusters")

    clusters = load_story_clusters(root)
    if not clusters:
        print("WARN: scout-story-clusters.json missing — gate skipped")
        return 0

    live_limit = max(1, min(args.live_limit, 100))
    sources = build_published_story_sources(root, live_limit=live_limit, window_days=window_days)
    new_ids = detect_story_clusters(args.text, clusters)
    if not new_ids:
        print(f"✅ STORY DUP PASS ({window_days}d): no published plot cluster detected in candidate text")
        return 0

    print(f"Candidate story clusters: {', '.join(new_ids)}")
    warnings = check_story_duplicate(args.text, sources, clusters, root=root)
    if not warnings:
        print(f"✅ STORY DUP PASS ({window_days}d): cluster(s) detected but no published sibling match")
        return 0

    print(f"❌ STORY DUPLICATE BLOCKER ({window_days}-day anti-repeat):")
    for w in warnings:
        print(f"  [{w['severity']}] {w['cluster_id']} | {w['topic_id']} ({w['source']})")
        print(f"  {w['message']}")
    print(
        "BLOCKER: SCOUT STORY DUPLICATE — pick a distinct legal risk + plot "
        "(see shared/scout-story-clusters.json + memory/scout/used-clusters.json). "
        "Wordstat rework ≠ same story."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
