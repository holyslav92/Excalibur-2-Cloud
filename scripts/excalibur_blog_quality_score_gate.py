#!/usr/bin/env python3
"""Structural article quality score gate (Grok Bot 7.5–9 bar).

Runs after Stylo on final prose. Writes article-quality-score.json with per-section
pass/fail. Optional --repair triggers at most one Derouter Sol pass with gate notes.

Contract: shared/article-quality-score-lock.md
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from excalibur_blog_composite_disclaimer import check_no_composite_disclaimer
from excalibur_blog_opening_meta_gate import count_prose_sentences, opening_tldr_errors, strip_early_cta
from excalibur_blog_quality_bar_9_gate import (
    check_comment_magnet,
    check_spine_once_no_recap,
    first_screen_html,
    strip_html,
    word_count,
)
from excalibur_blog_stylo import lead_block, spine_overlap, tokenize_words


WORD_TARGET_MIN = 1400
WORD_TARGET_MAX = 1600
WORD_HARD_MAX = 1750
DZEN_WORDS_PER_MINUTE = 200
DZEN_READING_MINUTES_MAX = 10

PROSE_LEAD_MIN = 4
PROSE_LEAD_MAX = 6

CALM_H1_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"как\s+устроен", re.I),
    re.compile(r"что\s+такое", re.I),
    re.compile(r"полный\s+гайд", re.I),
    re.compile(r"\bгайд\b", re.I),
    re.compile(r"чеклист", re.I),
    re.compile(r"\d+\s+шаг", re.I),
    re.compile(r"стоит\s+ли\s+покупать", re.I),
    re.compile(r"разбор\s+схем", re.I),
    re.compile(r"и\s+как\s+", re.I),
    re.compile(r"как\s+купить\s+без", re.I),
)

H1_PUNCH_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(r"[—–-]\s*\S", re.I),
    re.compile(
        r"\b(сгорел|остановил|отказал|заморозил|потерял|вернули|не\s+вернули|"
        r"развернул|поднял|вырос|исчез|задержал|отменил)\w*\b",
        re.I,
    ),
)

CONSEQUENCE_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b(сгорел|потеря|отказ|не\s+вернули|заморозил|остановил|развернул)\w*\b", re.I),
    re.compile(r"[—–-]\s*\S", re.I),
)

LAWYER_PHRASES: tuple[re.Pattern[str], ...] = (
    re.compile(r"профессиональн\w+\s+участник", re.I),
    re.compile(r"досудебн\w+\s+плоскост", re.I),
    re.compile(r"досудебн\w+\s+порядок", re.I),
    re.compile(r"императив\s+норм", re.I),
    re.compile(r"в\s+силу\s+положени", re.I),
    re.compile(r"следует\s+констатировать", re.I),
    re.compile(r"случай\s+собирательн", re.I),
    re.compile(r"собирательн\w+\s+(?:случа|сюжет)", re.I),
)

LECTURE_TAIL_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\d{1,3}[-‑]ФЗ", re.I),
    re.compile(r"главный\s+вывод", re.I),
    re.compile(r"итоговая\s+таблиц", re.I),
    re.compile(r"шпаргалк", re.I),
)

PANIC_ONLY_MARKERS: tuple[str, ...] = (
    "бегите",
    "никогда не покупайте",
    "вторичка — мина",
    "риски везде",
    "как вообще покупать",
)

AGENCY_MARKERS: tuple[str, ...] = (
    "до аванса",
    "до брони",
    "подключусь",
    "напишите",
    "разберём",
    "разложу",
    "остановились до",
    "проверка спасла",
)

SPINE_OVERLAP_FAIL = 0.32


@dataclass
class SectionResult:
    name: str
    pass_: bool
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"pass": self.pass_, "reasons": self.reasons}


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def resolve_h1(article_dir: Path) -> str:
    for rel in ("title-brief.json", "article.meta.json"):
        data = load_json(article_dir / rel)
        if not data:
            continue
        for key in ("h1", "title"):
            val = str(data.get(key) or "").strip()
            if val:
                return val
    return ""


def prose_lead_html(html: str) -> str:
    screen = first_screen_html(html)
    return strip_early_cta(screen)


def split_sentences(text: str) -> list[str]:
    plain = re.sub(r"\s+", " ", text or "").strip()
    if not plain:
        return []
    parts = re.split(r"(?<=[.!?…])\s+", plain)
    return [p.strip() for p in parts if len(p.strip()) >= 8]


def extract_body_sections(html: str) -> dict[str, str]:
    """lead | middle | finale as plain text zones."""
    body = html or ""
    h2_parts = re.split(r"<h2[^>]*>", body, flags=re.I)
    if len(h2_parts) <= 1:
        return {"lead": strip_html(body), "middle": "", "finale": ""}

    lead_zone = strip_html(h2_parts[0])
    sections_html = re.findall(
        r"<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|$)",
        body,
        flags=re.I | re.S,
    )
    if not sections_html:
        return {"lead": lead_zone, "middle": "", "finale": ""}

    middle_chunks: list[str] = []
    finale_chunks: list[str] = []
    for i, (_title, chunk) in enumerate(sections_html):
        plain = strip_html(chunk)
        if re.search(r"excalibur-cta-end", chunk, re.I):
            continue
        if i < max(0, len(sections_html) - 2):
            middle_chunks.append(plain)
        else:
            finale_chunks.append(plain)

    return {
        "lead": lead_zone,
        "middle": " ".join(middle_chunks),
        "finale": " ".join(finale_chunks),
    }


def ngram_phrases(text: str, n: int = 4) -> set[str]:
    words = [w for w in tokenize_words(text) if len(w) >= 3]
    if len(words) < n:
        return set()
    return {" ".join(words[i : i + n]) for i in range(len(words) - n + 1)}


def triple_retell_phrases(zones: dict[str, str]) -> list[str]:
    lead_p = ngram_phrases(zones.get("lead", ""))
    mid_p = ngram_phrases(zones.get("middle", ""))
    fin_p = ngram_phrases(zones.get("finale", ""))
    if not lead_p or not mid_p or not fin_p:
        return []
    common = lead_p & mid_p & fin_p
    stop = {"в тюмени", "по новостройке", "в этом случае", "на руках"}
    hits = [p for p in sorted(common, key=len, reverse=True) if p not in stop and len(p) > 18]
    return hits[:5]


def tail_before_end_cta(html: str) -> str:
    end_m = re.search(r'<div[^>]*class="[^"]*excalibur-cta-end', html or "", flags=re.I)
    if not end_m:
        return (html or "")[-2500:]
    return (html or "")[: end_m.start()][-2500:]


def check_h1(h1: str) -> SectionResult:
    reasons: list[str] = []
    text = (h1 or "").strip()
    if not text:
        return SectionResult("h1", False, ["h1: missing (title-brief.json / article.meta.json)"])

    for rx in CALM_H1_PATTERNS:
        if rx.search(text):
            reasons.append(f"h1-calm-guide:{rx.pattern[:40]}")

    if not re.search(r"\d", text):
        reasons.append("h1: no number or deadline in H1")

    if not any(rx.search(text) for rx in H1_PUNCH_MARKERS):
        reasons.append("h1: missing punch beat (em-dash or consequence verb) in second beat")

    return SectionResult("h1", not reasons, reasons)


def check_lead(html: str) -> SectionResult:
    reasons: list[str] = []
    screen = prose_lead_html(html)
    tldr_errors = opening_tldr_errors(screen)
    if tldr_errors:
        reasons.extend(tldr_errors)

    sentences = count_prose_sentences(screen)
    if sentences < PROSE_LEAD_MIN:
        reasons.append(f"lead: prose too short ({sentences} sentences, need {PROSE_LEAD_MIN}-{PROSE_LEAD_MAX})")
    elif sentences > PROSE_LEAD_MAX:
        reasons.append(f"lead: prose too long ({sentences} sentences, need {PROSE_LEAD_MIN}-{PROSE_LEAD_MAX})")

    plain_lead = strip_html(screen)
    sents = split_sentences(plain_lead)
    hit_zone = " ".join(sents[:2]) if sents else plain_lead[:400]
    if not re.search(r"\d", hit_zone):
        reasons.append("lead-hit: first 1-2 sentences missing number/deadline")
    if not any(rx.search(hit_zone) for rx in CONSEQUENCE_MARKERS):
        reasons.append("lead-hit: first 1-2 sentences missing consequence beat")

    composite_ok, composite_errors = check_no_composite_disclaimer(screen)
    if not composite_ok:
        reasons.extend(composite_errors)

    paras = [p for p in re.split(r"</p>\s*<p", screen, flags=re.I) if strip_html(p).strip()]
    short_para_count = sum(1 for p in paras if len(split_sentences(strip_html(p))) <= 2)
    if len(paras) >= 6 and short_para_count / len(paras) > 0.75:
        reasons.append("lead-style: mandatory 1-2 sentence paragraph chopping (>75% short paras)")

    return SectionResult("lead", not reasons, reasons)


def check_middle(html: str, zones: dict[str, str]) -> SectionResult:
    reasons: list[str] = []
    spine_ok, spine_errors = check_spine_once_no_recap(html)
    if not spine_ok:
        reasons.extend(spine_errors)

    plain = strip_html(html)
    lead = lead_block(html)
    overlap = spine_overlap(plain, lead)
    if overlap >= SPINE_OVERLAP_FAIL:
        reasons.append(f"spine-once: lead↔tail overlap {overlap:.2f} >= {SPINE_OVERLAP_FAIL}")

    triple = triple_retell_phrases(zones)
    if triple:
        reasons.append(f"triple-retell: shared phrase in lead+middle+finale: «{triple[0]}»")
        for extra in triple[1:3]:
            reasons.append(f"triple-retell-extra: «{extra}»")

    return SectionResult("middle", not reasons, reasons)


def check_finale(html: str, zones: dict[str, str]) -> SectionResult:
    reasons: list[str] = []
    tail_html = tail_before_end_cta(html)
    tail_plain = strip_html(tail_html).lower()

    magnet_ok, magnet_errors = check_comment_magnet(html)
    if not magnet_ok:
        reasons.extend(magnet_errors)

    panic = any(m in tail_plain for m in PANIC_ONLY_MARKERS)
    agency = any(m in tail_plain for m in AGENCY_MARKERS)
    if panic and not agency:
        reasons.append("finale: panic landing without agency handle")

    triple_fin = triple_retell_phrases(
        {
            "lead": zones.get("middle", ""),
            "middle": zones.get("middle", ""),
            "finale": zones.get("finale", ""),
        }
    )
    if triple_fin:
        reasons.append(f"finale-third-retell: middle scene repeated in closing: «{triple_fin[0]}»")

    for rx in LECTURE_TAIL_PATTERNS:
        if rx.search(tail_plain):
            reasons.append(f"lecture-tail:{rx.pattern[:32]}")

    list_items = len(re.findall(r"<li\b", tail_html, flags=re.I))
    tables = len(re.findall(r"<table\b", tail_html, flags=re.I))
    if list_items >= 6 or tables >= 2:
        reasons.append(f"lecture-tail: {list_items} list items / {tables} tables after casus before end CTA")

    closing_checklist = re.search(
        r"(?:шаг\s*\d|сначала\s+.*потом\s+.*затем).{0,200}(?:excalibur-cta-end|$)",
        tail_plain,
        re.I | re.S,
    )
    if closing_checklist:
        reasons.append("finale: checklist-as-emotional-landing before end CTA")

    return SectionResult("finale", not reasons, reasons)


def check_length(html: str) -> SectionResult:
    reasons: list[str] = []
    wc = word_count(html)
    reading_min = (wc + DZEN_WORDS_PER_MINUTE - 1) // DZEN_WORDS_PER_MINUTE if wc else 0

    if wc > WORD_HARD_MAX:
        reasons.append(f"length-hard: {wc} words > {WORD_HARD_MAX}")
    elif wc > WORD_TARGET_MAX:
        reasons.append(f"length-over: {wc} words above target {WORD_TARGET_MIN}-{WORD_TARGET_MAX}")

    if reading_min > DZEN_READING_MINUTES_MAX:
        reasons.append(f"dzen-minutes: ~{reading_min} min > {DZEN_READING_MINUTES_MAX}")

    if wc < WORD_TARGET_MIN:
        reasons.append(f"length-short: {wc} words below target {WORD_TARGET_MIN}-{WORD_TARGET_MAX} (warn only)")

    hard_fail = wc > WORD_HARD_MAX or reading_min > DZEN_READING_MINUTES_MAX
    soft_fail = wc > WORD_TARGET_MAX
    fail = hard_fail or soft_fail

    return SectionResult("length", not fail, reasons)


def check_tone(html: str) -> SectionResult:
    reasons: list[str] = []
    plain = strip_html(html).lower()
    for rx in LAWYER_PHRASES:
        m = rx.search(plain)
        if m:
            reasons.append(f"lawyer-tone:{m.group(0)[:48]}")

    screen = prose_lead_html(html)
    if re.search(r"^\s*<(?:ul|ol)\b", screen, re.I):
        reasons.append("tone: checklist-first opening (list before prose)")

    return SectionResult("tone", not reasons, reasons)


def build_quality_score_notes(sections: dict[str, SectionResult], h1: str) -> str:
    lines = [
        "# Quality score notes (для Sol, один проход)",
        "",
        f"H1: {h1}",
        "",
        "Исправь **только** структуру/тон по FAIL ниже. Факты из drafts/writer.html не менять.",
        "Без self-score loop. Без padding до 1800+. Target 1400–1600 слов.",
        "",
    ]
    for key in ("h1", "lead", "middle", "finale", "length", "tone"):
        sec = sections[key]
        if sec.pass_:
            continue
        lines.append(f"## {key.upper()} FAIL")
        for r in sec.reasons:
            lines.append(f"- {r}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def evaluate(
    article_dir: Path,
    root: Path,
    *,
    sol_rewrite_applied: bool = False,
) -> dict[str, Any]:
    html_path = article_dir / "article.html"
    if not html_path.is_file():
        return {
            "status": "FAIL",
            "all_pass": False,
            "gate": "article-quality-score",
            "contract": "shared/article-quality-score-lock.md",
            "errors": ["article.html missing"],
            "sections": {},
        }

    html = html_path.read_text(encoding="utf-8")
    h1 = resolve_h1(article_dir)
    zones = extract_body_sections(html)

    sections: dict[str, SectionResult] = {
        "h1": check_h1(h1),
        "lead": check_lead(html),
        "middle": check_middle(html, zones),
        "finale": check_finale(html, zones),
        "length": check_length(html),
        "tone": check_tone(html),
    }

    all_pass = all(s.pass_ for s in sections.values())
    errors: list[str] = []
    for sec in sections.values():
        if not sec.pass_:
            errors.extend(sec.reasons)

    try:
        article_rel = str(article_dir.relative_to(root)).replace("\\", "/")
    except ValueError:
        article_rel = str(article_dir)

    wc = word_count(html)
    return {
        "status": "PASS" if all_pass else "FAIL",
        "all_pass": all_pass,
        "gate": "article-quality-score",
        "contract": "shared/article-quality-score-lock.md",
        "article_dir": article_rel,
        "sol_rewrite_applied": sol_rewrite_applied,
        "h1": h1,
        "sections": {k: v.to_dict() for k, v in sections.items()},
        "errors": errors,
        "metrics": {
            "word_count": wc,
            "word_target": f"{WORD_TARGET_MIN}-{WORD_TARGET_MAX}",
            "word_hard_max": WORD_HARD_MAX,
            "dzen_reading_minutes_est": (wc + DZEN_WORDS_PER_MINUTE - 1) // DZEN_WORDS_PER_MINUTE
            if wc
            else 0,
            "spine_overlap": round(spine_overlap(strip_html(html), lead_block(html)), 4),
        },
    }


def write_notes(article_dir: Path, notes: str) -> Path:
    path = article_dir / "quality-score-notes.md"
    path.write_text(notes, encoding="utf-8")
    return path


def build_sol_input(article_dir: Path, notes_path: Path) -> Path:
    drafts = article_dir / "drafts"
    drafts.mkdir(parents=True, exist_ok=True)
    out = drafts / "quality-score-sol-input.md"
    parts: list[str] = [
        "# Quality score repair — один Sol pass",
        "",
        "Прочитай quality-score-notes.md и исправь article.html.",
        "Факты — только из drafts/writer.html. Без self-score 9.0 loop.",
        "",
    ]
    if notes_path.is_file():
        parts.append(notes_path.read_text(encoding="utf-8"))
        parts.append("")
    writer = article_dir / "drafts" / "writer.html"
    if writer.is_file():
        parts.append("## Writer facts (не менять)")
        parts.append(writer.read_text(encoding="utf-8")[:12000])
        parts.append("")
    current = article_dir / "article.html"
    if current.is_file():
        parts.append("## Current article.html (перепиши слогом Sol)")
        parts.append(current.read_text(encoding="utf-8")[:20000])
    out.write_text("\n".join(parts), encoding="utf-8")
    return out


def run_repair_sol(article_dir: Path, root: Path, user_file: Path) -> int:
    agent = root / "agents" / "excalibur-blog-sol.md"
    if not agent.is_file():
        agent = root / ".cursor" / "agents" / "excalibur-blog-sol.md"
    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_derouter_opus_chat.py"),
        "--role",
        "sol",
        "--system-file",
        str(agent),
        "--user-file",
        str(user_file),
        "--output",
        "article.html",
        "--article-dir",
        str(article_dir),
    ]
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    if proc.returncode != 0:
        print(proc.stdout, file=sys.stdout)
        print(proc.stderr, file=sys.stderr)
    return int(proc.returncode)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--root", default=".")
    ap.add_argument("-o", "--output", default="article-quality-score.json")
    ap.add_argument("--repair", action="store_true", help="At most one Derouter Sol pass on FAIL")
    ap.add_argument("--sol-rewrite", action="store_true", help="Mark sol_rewrite_applied in report")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = (root / article_dir).resolve()

    prior = load_json(article_dir / Path(args.output).name)
    sol_applied = bool(args.sol_rewrite or (prior or {}).get("sol_rewrite_applied"))

    report = evaluate(article_dir, root, sol_rewrite_applied=sol_applied)

    if not report.get("all_pass"):
        sections_raw = report.get("sections") or {}
        section_objs = {
            k: SectionResult(k, bool(v.get("pass")), list(v.get("reasons") or []))
            for k, v in sections_raw.items()
        }
        notes = build_quality_score_notes(section_objs, str(report.get("h1") or ""))
        write_notes(article_dir, notes)

        if args.repair and not sol_applied:
            user_file = build_sol_input(article_dir, article_dir / "quality-score-notes.md")
            rc = run_repair_sol(article_dir, root, user_file)
            if rc != 0:
                report["repair_error"] = f"derouter sol exit={rc}"
            else:
                report = evaluate(article_dir, root, sol_rewrite_applied=True)
                report["repair_attempted"] = True

    out = article_dir / Path(args.output).name
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("all_pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
