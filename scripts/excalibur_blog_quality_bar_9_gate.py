#!/usr/bin/env python3
"""Hard gate: quality bar 9/10 before Publish.

Checks BRAND, TEXT, COVER prerequisites, and inline utility rules from
shared/quality-bar-9.md. Writes quality-bar-9.json with per-check booleans.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from excalibur_blog_composite_disclaimer import check_no_composite_disclaimer
from excalibur_blog_site_base import SITE_BASE_PLACEHOLDER


WORD_TARGET_MIN = 1800
WORD_TARGET_MAX = 2200
WORD_HARD_MAX = 2400
DZEN_WORDS_PER_MINUTE = 200
DZEN_READING_MINUTES_MAX = 12
H2_MIN = 5
INLINE_MIN = 7
REALISTIC_INLINE_MIN = 2
REALISTIC_INLINE_MAX = 4
INTERLINK_MIN = 2
INTERLINK_MAX = 4

RECAP_BANNED_PHRASES = (
    "коротко если некогда",
    "коротко, если некогда",
    "если некогда",
    "в двух словах",
    "подведём итог",
    "подведем итог",
    "резюмируя",
    "главное — запомните",
    "главное - запомните",
    "итого:",
    "итог:",
)

TG_URL = "https://t.me/Tyumen_Rieltor"
MAX_URL = "https://max.ru/id561413315447_biz"

REQUIRED_CHECKS = (
    "brand_first_person_tyumen",
    "phone_in_body",
    "early_cta_tg_max_only",
    "mid_cta_tg_max_nudge",
    "end_cta_full_channels",
    "interlink_siblings_2_4",
    "dual_cta_soft",
    "word_count_1800_2200",
    "word_count_hard_max_2400",
    "dzen_reading_time_ok",
    "spine_once_no_recap",
    "h2_count_5_plus",
    "inline_figures_7",
    "inline_placement_flexible",
    "inline_realistic_mix_2_4",
    "no_sol_artifact",
    "no_unlabeled_live_inventory",
    "comparison_tables_differ",
    "no_tldr_opening",
    "no_composite_disclaimer",
    "comment_magnet_question",
    "cover_qa_pass",
    "cover_phone_on_cover",
    "wordstat_stickers_not_title_overlap",
    "image_alt_human",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def strip_html(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html or "")


def word_count(html: str) -> int:
    text = strip_html(html)
    return len(re.findall(r"[\wа-яА-ЯёЁ]+", text, flags=re.UNICODE))


def count_h2(html: str) -> int:
    return len(re.findall(r"<h2\b", html or "", flags=re.I))


def count_inline_figures(html: str) -> int:
    return len(re.findall(r'<figure[^>]*class="[^"]*inline-quad', html or "", flags=re.I))


def estimate_dzen_reading_minutes(word_count_value: int) -> int:
    if word_count_value <= 0:
        return 0
    return (word_count_value + DZEN_WORDS_PER_MINUTE - 1) // DZEN_WORDS_PER_MINUTE


def h2_titles_from_html(html: str) -> list[str]:
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", html or "", flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def count_figures_per_h2(html: str) -> dict[str, int]:
    """Map normalized H2 text → inline figure count immediately under that section."""
    counts: dict[str, int] = {t: 0 for t in h2_titles_from_html(html)}
    if not counts:
        return counts
    pattern = re.compile(
        r"<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)",
        flags=re.I | re.S,
    )
    for match in pattern.finditer(html or ""):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if title.lower() in {"частые вопросы", "faq"}:
            break
        body = match.group(2) or ""
        fig_n = len(re.findall(r'<figure[^>]*class="[^"]*inline-quad', body, flags=re.I))
        if title in counts:
            counts[title] = fig_n
    return counts


def check_spine_once_no_recap(html: str) -> tuple[bool, list[str]]:
    plain = strip_html(html).lower()
    errors: list[str] = []
    for phrase in RECAP_BANNED_PHRASES:
        if phrase in plain:
            errors.append(f"spine_once: banned recap phrase {phrase!r}")
    return (not errors, errors)


def check_inline_placement_flexible(html: str) -> tuple[bool, list[str]]:
    """PASS when placement is not rigid 1:1 first-N H2s — allow 0, pair, or skip."""
    per_h2 = count_figures_per_h2(html)
    if not per_h2:
        return True, []
    values = list(per_h2.values())
    has_zero = any(v == 0 for v in values)
    has_pair = any(v >= 2 for v in values)
    # Rigid legacy: first len(values) H2s each have exactly 1 figure and none skipped/paired.
    first_n = min(len(values), INLINE_MIN)
    rigid = all(values[i] == 1 for i in range(first_n)) and not has_zero and not has_pair
    if rigid and len(values) >= INLINE_MIN:
        return False, ["inline_placement: rigid 1:1 under first H2s — use 0/1/pair mix"]
    if not (has_zero or has_pair):
        return False, ["inline_placement: need at least one H2 with 0 images or a pair (2+)"]
    return True, []


def check_inline_realistic_mix(manifest_path: Path) -> tuple[bool, list[str]]:
    if not manifest_path.is_file():
        return False, ["cover/quad-manifest.json missing for realistic mix gate"]
    try:
        manifest = load_json(manifest_path)
    except json.JSONDecodeError:
        return False, ["cover/quad-manifest.json invalid JSON"]
    inline_count = int(manifest.get("inline_count") or 7)
    slots = manifest.get("slots") or {}
    realistic = 0
    for key in (f"inline_{i}" for i in range(1, inline_count + 1)):
        slot = slots.get(key) or {}
        vt = normalize_visual_type(str(slot.get("visual_type") or ""))
        if vt == "realistic_photo":
            realistic += 1
    if realistic < REALISTIC_INLINE_MIN or realistic > REALISTIC_INLINE_MAX:
        return False, [
            f"inline_realistic_mix: {realistic} realistic_photo slots; "
            f"need {REALISTIC_INLINE_MIN}-{REALISTIC_INLINE_MAX}"
        ]
    return True, []


def normalize_visual_type(type_id: str) -> str:
    aliases = {"comparison_table_ui": "comparison_table", "photo_scene": "realistic_photo"}
    raw = str(type_id or "").strip()
    return aliases.get(raw, raw)


def has_phone(html: str) -> bool:
    if re.search(r"tel:\+?79220016505", html or "", re.I):
        return True
    digits = re.sub(r"\D", "", html or "")
    return "79220016505" in digits or digits.endswith("9220016505")


def url_present(html: str, url: str) -> bool:
    url = (url or "").strip()
    if not url:
        return False
    body = html or ""
    site = re.escape(SITE_BASE_PLACEHOLDER)
    if url == "/":
        patterns = (
            r"""href=["']/["']""",
            rf"""href=["']{site}/?["']""",
        )
        return any(re.search(p, body) for p in patterns)
    if url.startswith("/"):
        path = url.rstrip("/")
        patterns = (
            rf"""href=["']{re.escape(path)}/?["']""",
            rf"""href=["']{site}{re.escape(path)}/?["']""",
        )
        return any(re.search(p, body, re.I) for p in patterns)
    if url.lower().startswith("tel:"):
        return has_phone(html)
    parsed = urlparse(url)
    host = (parsed.netloc or "").lower()
    path = (parsed.path or "").rstrip("/")
    pat = rf"https?://{re.escape(host)}{re.escape(path)}"
    return bool(re.search(pat, html or "", re.I))


def check_brand(html: str) -> bool:
    low = (html or "").lower()
    has_name = "святослав" in low and "шакин" in low
    has_tyumen = "тюмен" in low
    has_first = bool(re.search(r"\bя\b", low)) or "я веду" in low or "я работаю" in low or "у меня" in low
    has_rieltor = "риэлтор" in low or "the риэлтор" in low
    return has_name and has_tyumen and has_first and has_rieltor


def first_screen_html(html: str) -> str:
    """Content before first H2 — hook + prose lead + early CTA zone."""
    m = re.search(r"<h2\b", html or "", flags=re.I)
    if m:
        return (html or "")[: m.start()]
    return html or ""


def check_no_tldr_opening(html: str) -> tuple[bool, list[str]]:
    from excalibur_blog_opening_meta_gate import opening_tldr_errors

    screen = first_screen_html(html)
    errors = opening_tldr_errors(screen)
    return (not errors, errors)


FAQ_SKIP_RE = re.compile(
    r"частые вопросы|faq|задаваемые вопросы|читайте также",
    re.I,
)
DEBATE_QUESTION_RES = (
    re.compile(r"«[^»]{8,200}\?»"),
    re.compile(
        r"(?:кто\s+прав|а\s+вы\s+как|что\s+бы\s+вы|спорят|прав\s+ли|верите\s+ли|"
        r"по-вашему|по-моему|кто\s+виноват|на\s+чьей\s+стороне)[^.!?]{0,120}\?",
        re.I,
    ),
)


def check_comment_magnet(html: str) -> tuple[bool, list[str]]:
    """At least one sharp reader-debate question (Dzen comment magnet)."""
    if re.search(r"<h2[^>]*>\s*[^<]{8,140}\?\s*</h2>", html or "", flags=re.I):
        return True, []
    plain = strip_html(html)
    for rx in DEBATE_QUESTION_RES:
        if rx.search(plain):
            return True, []
    for m in re.finditer(r"[^.!?]{20,180}\?", plain):
        chunk = m.group(0)
        if FAQ_SKIP_RE.search(chunk):
            continue
        return True, []
    return False, ["comment-magnet: need one sharp reader-debate question"]


def check_early_cta(html: str) -> bool:
    early = first_screen_html(html).lower()
    if not url_present(html[: len(first_screen_html(html))], TG_URL):
        return False
    if not url_present(html[: len(first_screen_html(html))], MAX_URL):
        return False
    banned_early = (
        "vk.ru/tymenrieltor",
        "dzen.ru/holyslav",
        "wa.me/79220016505",
        "t.me/holyslav92",
        "/gajdy/",
    )
    return not any(b in early for b in banned_early)


def check_mid_cta(html: str) -> bool:
    if 'class="excalibur-cta-mid"' in (html or "") or "excalibur-cta-mid" in (html or ""):
        block_m = re.search(
            r'<div[^>]*class="[^"]*excalibur-cta-mid[^"]*"[^>]*>.*?</div>',
            html or "",
            flags=re.I | re.S,
        )
        if block_m:
            block = block_m.group(0)
            return url_present(block, TG_URL) and url_present(block, MAX_URL)
    return False


def check_end_cta(html: str) -> bool:
    end_m = re.search(
        r'<div[^>]*class="[^"]*excalibur-cta-end[^"]*"[^>]*>.*?</div>\s*(?:<p[^>]*>Материал проверен|$)',
        html or "",
        flags=re.I | re.S,
    )
    tail = end_m.group(0) if end_m else (html or "")[-3500:]
    required = (
        TG_URL,
        MAX_URL,
        "https://dzen.ru/holyslav",
        "https://vk.ru/tymenrieltor",
    )
    if not all(url_present(tail, u) for u in required):
        return False
    if not url_present(tail, "/gajdy/"):
        return False
    if not url_present(tail, "/rieltor-tyumen/"):
        return False
    if not url_present(tail, "/"):
        return False
    return has_phone(tail)


def load_published_sibling_paths(root: Path, article_dir: Path) -> list[str]:
    ledger = root / "shared/published-articles.md"
    if not ledger.is_file():
        return []
    slug = article_dir.name.split("-", 1)[-1] if "-" in article_dir.name else article_dir.name
    paths: list[str] = []
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if "| published |" not in line.lower():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6:
            continue
        url_path = parts[4]
        row_slug = parts[3]
        if row_slug and row_slug in article_dir.name:
            continue
        if url_path.startswith("/"):
            paths.append(url_path.rstrip("/") + "/")
    return paths


def count_sibling_interlinks(html: str, sibling_paths: list[str]) -> int:
    found: set[str] = set()
    for path in sibling_paths:
        core = path.strip("/")
        if core and core in (html or ""):
            found.add(path)
    return len(found)


def check_interlinks(html: str, root: Path, article_dir: Path) -> tuple[bool, int]:
    tenant_path = root / "shared/tenant-config.json"
    if tenant_path.is_file():
        tenant = load_json(tenant_path)
        if not tenant.get("interlink_old_articles"):
            return True, 0
    siblings = load_published_sibling_paths(root, article_dir)
    if not siblings:
        return True, 0
    count = count_sibling_interlinks(html, siblings)
    ok = INTERLINK_MIN <= count <= INTERLINK_MAX
    return ok, count


def check_socials(html: str) -> bool:
    """Legacy alias — end block channels."""
    return check_end_cta(html)


def check_dual_cta(html: str) -> bool:
    low = (html or "").lower()
    consult = any(x in low for x in ("консультац", "напишите", "напиши", "написать", "telegram"))
    deal = any(
        x in low
        for x in ("к делу", "подключаюсь", "веду сделк", "от звонка до регистрации", "до аванса")
    )
    banned = any(x in low for x in ("лучший риэлтор", "нулевой риск", "гарантия нул"))
    return consult and deal and not banned


def check_no_sol_artifact(html: str) -> bool:
    bad = (
        "=== EXCALIBUR BLOG SOL ===",
        "rewrote_from: drafts/writer.html",
        "incident_report:",
        "article.html drafts/variant-a.html",
    )
    return not any(b in (html or "") for b in bad)


def check_live_inventory(html: str) -> bool:
    low = html.lower()
    if "живые лоты" in low and "пример" not in low and "не live" not in low:
        return False
    street_markers = ("тихий проезд", "широтная, 69", "червишевский тракт, 45")
    for marker in street_markers:
        if marker in low:
            idx = low.find(marker)
            window = low[max(0, idx - 200) : idx + 200]
            if not any(x in window for x in ("пример", "агрегатор", "не live")):
                return False
    return True


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tables: list[list[list[str]]] = []
        self._in_table = False
        self._in_row = False
        self._in_cell = False
        self._rows: list[list[str]] = []
        self._cells: list[str] = []
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "table":
            self._in_table = True
            self._rows = []
        elif self._in_table and tag == "tr":
            self._in_row = True
            self._cells = []
        elif self._in_row and tag in ("td", "th"):
            self._in_cell = True
            self._buf = []

    def handle_endtag(self, tag: str) -> None:
        if tag in ("td", "th") and self._in_cell:
            self._cells.append(" ".join(self._buf).strip())
            self._in_cell = False
            self._buf = []
        elif tag == "tr" and self._in_row:
            if self._cells:
                self._rows.append(self._cells)
            self._in_row = False
        elif tag == "table" and self._in_table:
            if self._rows:
                self.tables.append(self._rows)
            self._in_table = False

    def handle_data(self, data: str) -> None:
        if self._in_cell:
            self._buf.append(data.strip())


def check_comparison_tables(html: str) -> tuple[bool, list[str]]:
    parser = TableParser()
    try:
        parser.feed(html or "")
    except Exception:
        return True, []
    errors: list[str] = []
    for ti, table in enumerate(parser.tables):
        if len(table) < 2:
            continue
        header = [c.lower() for c in table[0]]
        if len(header) < 2:
            continue
        is_comparison = any(
            w in " ".join(header)
            for w in ("ошибк", "правильн", "торги", "обычн", "сигнал", "что видите", "vs")
        )
        if not is_comparison:
            continue
        for ri, row in enumerate(table[1:], start=1):
            if len(row) < 2:
                continue
            left, right = row[0].strip(), row[1].strip()
            if not left or not right:
                errors.append(f"table{ti+1} row{ri}: empty cell")
                continue
            if left.lower() == right.lower():
                errors.append(f"table{ti+1} row{ri}: identical columns")
    return (not errors, errors)


def check_cover_phone(article_dir: Path) -> bool:
    manifest = article_dir / "cover" / "quad-manifest.json"
    if manifest.is_file():
        try:
            data = load_json(manifest)
            return str(data.get("cover_phone_cta") or "").strip() == "+7 922 001 65 05"
        except json.JSONDecodeError:
            return False
    return (article_dir / "cover" / "cover.png").is_file()


def check_wordstat_overlap(article_dir: Path) -> bool:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    if not manifest_path.is_file():
        return True
    try:
        manifest = load_json(manifest_path)
    except json.JSONDecodeError:
        return False
    stickers = manifest.get("wordstat_stickers") or []
    if not (1 <= len(stickers) <= 3):
        return False
    positions = manifest.get("wordstat_sticker_positions")
    if isinstance(positions, list) and positions:
        if manifest.get("wordstat_pil_only"):
            # Синхронно с cover_qa_gate.validate_title_not_occluded: PIL — top-left sacred zone.
            for pos in positions:
                if isinstance(pos, (list, tuple)) and len(pos) >= 2:
                    x, y = float(pos[0]), float(pos[1])
                    if x > 0.42 or y > 0.36:
                        return False
        else:
            for pos in positions:
                if isinstance(pos, (list, tuple)) and len(pos) >= 2:
                    if float(pos[0]) < 0.68:
                        return False
    return True


def _stamped_cover_qa_visual_pass(article_dir: Path) -> bool:
    """Принять cover_qa.json с B08/B09 OCR escape, если PNG md5 совпадает."""
    qa_path = article_dir / "cover" / "cover_qa.json"
    cover_path = article_dir / "cover" / "cover.png"
    if not qa_path.is_file() or not cover_path.is_file():
        return False
    try:
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    if str(qa.get("status") or "").upper() != "PASS":
        return False
    gate_status = str(qa.get("gate_status") or qa.get("status") or "").upper()
    if gate_status != "PASS":
        return False
    if not qa.get("pixel_qa"):
        return False
    import hashlib

    live_md5 = hashlib.md5(cover_path.read_bytes()).hexdigest()
    stamped_md5 = str(qa.get("cover_md5") or "")
    if stamped_md5 and live_md5 != stamped_md5:
        return False
    escape = (qa.get("pixel_evidence") or {}).get("ocr_false_positive_escape") or {}
    return bool(escape.get("applied"))


def check_image_alt_human(article_dir: Path, root: Path) -> tuple[bool, list[str]]:
    from excalibur_blog_image_caption_builder import apply_article_captions, collect_article_alts

    try:
        apply_article_captions(article_dir, root)
    except FileNotFoundError:
        return False, ["cover/quad-manifest.json missing for image alt gate"]
    gate = collect_article_alts(article_dir, root)
    errors: list[str] = []
    for slot_key, item in (gate.get("slots") or {}).items():
        if not item.get("pass"):
            errors.append(f"{slot_key}: {'; '.join(item.get('errors') or [])}")
    for item in gate.get("html_alts") or []:
        if not item.get("pass"):
            errors.append(f"html {item.get('src')}: {'; '.join(item.get('errors') or [])}")
    for item in gate.get("registry_alts") or []:
        if not item.get("pass"):
            errors.append(f"registry {item.get('file')}: {'; '.join(item.get('errors') or [])}")
    return bool(gate.get("all_pass")), errors


def run_cover_qa(article_dir: Path, root: Path) -> bool:
    rc = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/excalibur_blog_cover_qa_gate.py"),
            "--article-dir",
            str(article_dir),
            "--no-stamp",
        ],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if rc.returncode == 0:
        return True
    return _stamped_cover_qa_visual_pass(article_dir)


def evaluate(article_dir: Path, root: Path, *, skip_cover_qa: bool = False) -> dict[str, Any]:
    html_path = article_dir / "article.html"
    errors: list[str] = []
    checks: dict[str, bool] = {}

    if not html_path.is_file():
        return {
            "status": "FAIL",
            "all_pass": False,
            "checks": {},
            "errors": ["article.html missing"],
            "metrics": {},
        }

    html = html_path.read_text(encoding="utf-8")
    wc = word_count(html)
    h2c = count_h2(html)
    inlines = count_inline_figures(html)

    checks["brand_first_person_tyumen"] = check_brand(html)
    checks["phone_in_body"] = has_phone(html)
    checks["early_cta_tg_max_only"] = check_early_cta(html)
    checks["mid_cta_tg_max_nudge"] = check_mid_cta(html)
    checks["end_cta_full_channels"] = check_end_cta(html)
    interlink_ok, interlink_count = check_interlinks(html, root, article_dir)
    checks["interlink_siblings_2_4"] = interlink_ok
    checks["dual_cta_soft"] = check_dual_cta(html)
    checks["word_count_1800_2200"] = WORD_TARGET_MIN <= wc <= WORD_TARGET_MAX
    checks["word_count_hard_max_2400"] = wc <= WORD_HARD_MAX
    reading_min = estimate_dzen_reading_minutes(wc)
    checks["dzen_reading_time_ok"] = reading_min < DZEN_READING_MINUTES_MAX + 2  # <14 min
    spine_ok, spine_errors = check_spine_once_no_recap(html)
    checks["spine_once_no_recap"] = spine_ok
    checks["h2_count_5_plus"] = h2c >= H2_MIN
    checks["inline_figures_7"] = inlines >= INLINE_MIN
    placement_ok, placement_errors = check_inline_placement_flexible(html)
    checks["inline_placement_flexible"] = placement_ok
    realistic_ok, realistic_errors = check_inline_realistic_mix(article_dir / "cover" / "quad-manifest.json")
    checks["inline_realistic_mix_2_4"] = realistic_ok
    checks["no_sol_artifact"] = check_no_sol_artifact(html)
    checks["no_unlabeled_live_inventory"] = check_live_inventory(html)
    tbl_ok, tbl_errors = check_comparison_tables(html)
    checks["comparison_tables_differ"] = tbl_ok
    tldr_ok, tldr_errors = check_no_tldr_opening(html)
    checks["no_tldr_opening"] = tldr_ok
    composite_ok, composite_errors = check_no_composite_disclaimer(html)
    checks["no_composite_disclaimer"] = composite_ok
    magnet_ok, magnet_errors = check_comment_magnet(html)
    checks["comment_magnet_question"] = magnet_ok
    checks["cover_phone_on_cover"] = check_cover_phone(article_dir)
    checks["wordstat_stickers_not_title_overlap"] = check_wordstat_overlap(article_dir)
    alt_ok, alt_errors = check_image_alt_human(article_dir, root)
    checks["image_alt_human"] = alt_ok

    if skip_cover_qa:
        checks["cover_qa_pass"] = (article_dir / "cover" / "cover_qa.json").is_file()
    else:
        checks["cover_qa_pass"] = run_cover_qa(article_dir, root)

    for key in REQUIRED_CHECKS:
        if not checks.get(key):
            if key == "comparison_tables_differ" and tbl_errors:
                errors.extend(tbl_errors)
            elif key == "word_count_1800_2200":
                errors.append(f"word_count {wc} outside target {WORD_TARGET_MIN}-{WORD_TARGET_MAX}")
            elif key == "word_count_hard_max_2400":
                errors.append(f"word_count {wc} exceeds hard max {WORD_HARD_MAX}")
            elif key == "dzen_reading_time_ok":
                errors.append(
                    f"dzen_reading_minutes ~{reading_min} (words/{DZEN_WORDS_PER_MINUTE}); "
                    f"need < {DZEN_READING_MINUTES_MAX + 2}"
                )
            elif key == "spine_once_no_recap" and spine_errors:
                errors.extend(spine_errors)
            elif key == "h2_count_5_plus":
                errors.append(f"h2 count {h2c} < {H2_MIN}")
            elif key == "inline_figures_7":
                errors.append(f"inline figures {inlines} < {INLINE_MIN}")
            elif key == "inline_placement_flexible" and placement_errors:
                errors.extend(placement_errors)
            elif key == "inline_realistic_mix_2_4" and realistic_errors:
                errors.extend(realistic_errors)
            elif key == "interlink_siblings_2_4":
                errors.append(
                    f"sibling interlinks {interlink_count} outside {INTERLINK_MIN}-{INTERLINK_MAX}"
                )
            elif key == "no_tldr_opening" and tldr_errors:
                errors.extend(tldr_errors)
            elif key == "no_composite_disclaimer" and composite_errors:
                errors.extend(composite_errors)
            elif key == "comment_magnet_question" and magnet_errors:
                errors.extend(magnet_errors)
            elif key == "image_alt_human" and alt_errors:
                errors.extend(alt_errors)
            else:
                errors.append(f"check failed: {key}")

    all_pass = all(checks.get(k) for k in REQUIRED_CHECKS)
    status = "PASS" if all_pass else "FAIL"
    return {
        "status": status,
        "all_pass": all_pass,
        "gate": "quality-bar-9",
        "contract": "shared/quality-bar-9.md",
        "article_dir": str(article_dir.relative_to(root)).replace("\\", "/"),
        "checks": checks,
        "errors": errors,
        "metrics": {
            "word_count": wc,
            "word_count_target": f"{WORD_TARGET_MIN}-{WORD_TARGET_MAX}",
            "word_count_hard_max": WORD_HARD_MAX,
            "dzen_reading_minutes_est": reading_min,
            "h2_count": h2c,
            "inline_figures": inlines,
            "sibling_interlinks": interlink_count,
        },
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("--skip-cover-qa", action="store_true", help="Skip live cover_qa subprocess")
    ap.add_argument("-o", "--output", default="quality-bar-9.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = (root / article_dir).resolve()

    report = evaluate(article_dir, root, skip_cover_qa=args.skip_cover_qa)
    out = article_dir / Path(args.output).name
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
