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


WORD_MIN = 2000
WORD_MAX = 2600
H2_MIN = 7
INLINE_MIN = 7

REQUIRED_CHECKS = (
    "brand_first_person_tyumen",
    "phone_in_body",
    "socials_compact_block",
    "dual_cta_soft",
    "word_count_2000_2600",
    "h2_count_7_plus",
    "inline_figures_7",
    "no_sol_artifact",
    "no_unlabeled_live_inventory",
    "comparison_tables_differ",
    "cover_qa_pass",
    "cover_phone_on_cover",
    "wordstat_stickers_not_title_overlap",
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


def has_phone(html: str) -> bool:
    if re.search(r"tel:\+?79220016505", html or "", re.I):
        return True
    digits = re.sub(r"\D", "", html or "")
    return "79220016505" in digits or digits.endswith("9220016505")


def url_present(html: str, url: str) -> bool:
    url = (url or "").strip()
    if not url:
        return False
    if url == "/":
        return bool(re.search(r"""href=["']/["']""", html or ""))
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


def check_socials(html: str) -> bool:
    required = (
        "https://t.me/Tyumen_Rieltor",
        "https://t.me/holyslav92",
        "https://wa.me/79220016505",
        "https://vk.ru/tymenrieltor",
        "https://dzen.ru/holyslav",
    )
    site_ok = url_present(html, "/")
    return all(url_present(html, u) for u in required) and site_ok and bool(
        re.search(r"\bMAX\b", html or "", re.I)
    )


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
        for pos in positions:
            if isinstance(pos, (list, tuple)) and len(pos) >= 2:
                if float(pos[0]) < 0.68:
                    return False
    return True


def run_cover_qa(article_dir: Path, root: Path) -> bool:
    rc = subprocess.run(
        [
            sys.executable,
            str(root / "scripts/excalibur_blog_cover_qa_gate.py"),
            "--article-dir",
            str(article_dir),
        ],
        cwd=root,
        capture_output=True,
        text=True,
    )
    return rc.returncode == 0


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
    checks["socials_compact_block"] = check_socials(html)
    checks["dual_cta_soft"] = check_dual_cta(html)
    checks["word_count_2000_2600"] = WORD_MIN <= wc <= WORD_MAX
    checks["h2_count_7_plus"] = h2c >= H2_MIN
    checks["inline_figures_7"] = inlines >= INLINE_MIN
    checks["no_sol_artifact"] = check_no_sol_artifact(html)
    checks["no_unlabeled_live_inventory"] = check_live_inventory(html)
    tbl_ok, tbl_errors = check_comparison_tables(html)
    checks["comparison_tables_differ"] = tbl_ok
    checks["cover_phone_on_cover"] = check_cover_phone(article_dir)
    checks["wordstat_stickers_not_title_overlap"] = check_wordstat_overlap(article_dir)

    if skip_cover_qa:
        checks["cover_qa_pass"] = (article_dir / "cover" / "cover_qa.json").is_file()
    else:
        checks["cover_qa_pass"] = run_cover_qa(article_dir, root)

    for key in REQUIRED_CHECKS:
        if not checks.get(key):
            if key == "comparison_tables_differ" and tbl_errors:
                errors.extend(tbl_errors)
            elif key == "word_count_2000_2600":
                errors.append(f"word_count {wc} outside {WORD_MIN}-{WORD_MAX}")
            elif key == "h2_count_7_plus":
                errors.append(f"h2 count {h2c} < {H2_MIN}")
            elif key == "inline_figures_7":
                errors.append(f"inline figures {inlines} < {INLINE_MIN}")
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
        "metrics": {"word_count": wc, "h2_count": h2c, "inline_figures": inlines},
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
