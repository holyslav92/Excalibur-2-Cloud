#!/usr/bin/env python3
"""Стиlометрия голоса: сравнение article.html с GOLD-профилем (ритм/слог, не сюжет).

CLI:
  python3 scripts/excalibur_blog_stylo.py --article-dir DIR --gold-dir memory/stylo/gold --output DIR/stylo-report.json

Пишет stylo-report.json и stylo-notes.md. Exit 0 всегда, кроме отсутствующих файлов.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

# Порог Burrows-like Delta: калиброван на gold vs verbose lecture (см. tests/test_stylo.py).
DELTA_PASS_THRESHOLD = 2.85
AXIS_Z_NOTE = 1.35

FUNCTION_WORDS = (
    "и",
    "а",
    "но",
    "что",
    "как",
    "это",
    "не",
    "на",
    "в",
    "с",
    "по",
    "к",
    "от",
    "за",
    "я",
    "мы",
    "вы",
)

HEDGE_LEXICON = (
    "собирательн",
    "безусловно",
    "необходимо",
    "таким образом",
    "реквизит",
)

LEGAL_TERMS = (
    "дду",
    "егрн",
    "эскроу",
    "акт",
    "обременение",
    "ипотек",
    "залог",
    "нотариус",
    "росреестр",
    "выписк",
    "регистрац",
    "договор",
    "застройщик",
    "переуступк",
    "аккредитив",
    "банкрот",
    "финуправля",
)

FEATURE_KEYS = (
    "sent_len_mean",
    "sent_len_std",
    "para_len_mean",
    "ttr",
    "hapax_rate",
    "punct_em_dash_per_1k",
    "punct_ellipsis_per_1k",
    "punct_guillemet_per_1k",
    "first_person_ya_share",
    "first_person_my_share",
    "hedge_per_1k",
    "legal_per_1k",
    "lead_word_count",
    "lead_has_number",
    "spine_overlap",
    *tuple(f"fw_{w}" for w in FUNCTION_WORDS),
)


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip = False
        if tag in {"p", "br", "h2", "h3", "li"} and not self._skip:
            self._chunks.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip and data.strip():
            self._chunks.append(data)

    def text(self) -> str:
        return re.sub(r"\s+", " ", "".join(self._chunks)).strip()


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def strip_html(html: str) -> str:
    parser = _TextExtractor()
    parser.feed(html or "")
    return parser.text()


def extract_article_body_html(html: str) -> str:
    """Вытащить тело из article.html или live-страницы."""
    if not html:
        return ""
    m = re.search(r"<article[^>]*>(.*?)</article>", html, flags=re.I | re.S)
    if m:
        return m.group(1)
    # article.html без <article> — весь файл
    return html


def split_paragraphs_from_html(html: str) -> list[str]:
    body = extract_article_body_html(html)
    paras: list[str] = []
    for m in re.finditer(r"<p[^>]*>(.*?)</p>", body, flags=re.I | re.S):
        text = strip_html(m.group(1))
        if text:
            paras.append(text)
    if paras:
        return paras
    plain = strip_html(body)
    return [p.strip() for p in re.split(r"\n{2,}", plain) if p.strip()]


def tokenize_words(text: str) -> list[str]:
    return re.findall(r"[а-яёА-ЯЁa-zA-Z0-9]+", text.lower())


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def per_1k(count: float, words: int) -> float:
    if words <= 0:
        return 0.0
    return count * 1000.0 / words


def lead_block(html: str) -> str:
    """Первый блок до H2 или первые 2 предложения."""
    body = extract_article_body_html(html)
    before_h2 = re.split(r"<h2[^>]*>", body, maxsplit=1, flags=re.I)[0]
    paras = split_paragraphs_from_html(before_h2 if before_h2.strip() else body)
    if not paras:
        return strip_html(body)[:600]
    lead = paras[0]
    sents = split_sentences(lead)
    if len(sents) >= 2:
        return " ".join(sents[:2])
    if len(paras) >= 2:
        return f"{paras[0]} {paras[1]}"
    return lead


def spine_overlap(plain: str, lead: str, tail_words: int = 400) -> float:
    lead_tokens = set(tokenize_words(lead))
    words = tokenize_words(plain)
    if not lead_tokens or not words:
        return 0.0
    tail_tokens = set(words[-tail_words:])
    if not tail_tokens:
        return 0.0
    inter = len(lead_tokens & tail_tokens)
    union = len(lead_tokens | tail_tokens)
    return inter / union if union else 0.0


def extract_features(html: str) -> dict[str, float]:
    plain = strip_html(extract_article_body_html(html))
    words = tokenize_words(plain)
    word_count = len(words)
    sentences = split_sentences(plain)
    sent_lens = [len(tokenize_words(s)) for s in sentences] or [0]
    paras = split_paragraphs_from_html(html)
    para_lens = [len(tokenize_words(p)) for p in paras] or [0]

    types = set(words)
    ttr = len(types) / word_count if word_count else 0.0
    freq: dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    hapax = sum(1 for c in freq.values() if c == 1)
    hapax_rate = hapax / len(freq) if freq else 0.0

    raw = plain
    em_dash = raw.count("—") + raw.count("–")
    ellipsis = raw.count("…") + len(re.findall(r"\.\.\.", raw))
    guillemet = raw.count("«") + raw.count("»")

    ya = sum(1 for w in words if w == "я")
    my = sum(1 for w in words if w == "мы")
    vy = sum(1 for w in words if w == "вы")
    fp_total = ya + my + vy
    ya_share = ya / fp_total if fp_total else 0.0
    my_share = my / fp_total if fp_total else 0.0

    lower = plain.lower()
    hedge_hits = sum(lower.count(h) for h in HEDGE_LEXICON)
    legal_hits = sum(len(re.findall(rf"\b{re.escape(t)}", lower)) for t in LEGAL_TERMS)

    lead = lead_block(html)
    lead_words = tokenize_words(lead)
    lead_has_number = 1.0 if re.search(r"\d", lead) else 0.0

    fw_rates: dict[str, float] = {}
    for fw in FUNCTION_WORDS:
        fw_rates[f"fw_{fw}"] = per_1k(sum(1 for w in words if w == fw), word_count)

    features: dict[str, float] = {
        "sent_len_mean": sum(sent_lens) / len(sent_lens),
        "sent_len_std": _std(sent_lens),
        "para_len_mean": sum(para_lens) / len(para_lens),
        "ttr": ttr,
        "hapax_rate": hapax_rate,
        "punct_em_dash_per_1k": per_1k(em_dash, word_count),
        "punct_ellipsis_per_1k": per_1k(ellipsis, word_count),
        "punct_guillemet_per_1k": per_1k(guillemet, word_count),
        "first_person_ya_share": ya_share,
        "first_person_my_share": my_share,
        "hedge_per_1k": per_1k(hedge_hits, word_count),
        "legal_per_1k": per_1k(legal_hits, word_count),
        "lead_word_count": float(len(lead_words)),
        "lead_has_number": lead_has_number,
        "spine_overlap": spine_overlap(plain, lead),
        **fw_rates,
    }
    return features


def _std(values: list[float | int]) -> float:
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    return math.sqrt(var)


def load_gold_texts(gold_dir: Path) -> list[dict[str, Any]]:
    meta_path = gold_dir / "meta.json"
    entries: list[dict[str, Any]] = []
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        for item in meta.get("posts", []):
            slug = item.get("slug", "")
            txt_path = gold_dir / f"{slug}.txt"
            if txt_path.is_file():
                entries.append(
                    {
                        "slug": slug,
                        "title": item.get("title", ""),
                        "url": item.get("url", ""),
                        "text": txt_path.read_text(encoding="utf-8"),
                    }
                )
        if entries:
            return entries
    for path in sorted(gold_dir.glob("*.txt")):
        entries.append({"slug": path.stem, "title": path.stem, "url": "", "text": path.read_text(encoding="utf-8")})
    return entries


def compute_profile(gold_features: list[dict[str, float]]) -> dict[str, Any]:
    if not gold_features:
        raise ValueError("gold_features пуст")
    mean: dict[str, float] = {}
    std: dict[str, float] = {}
    for key in FEATURE_KEYS:
        vals = [f[key] for f in gold_features if key in f]
        mean[key] = sum(vals) / len(vals) if vals else 0.0
        std[key] = _std(vals) if len(vals) > 1 else max(mean[key] * 0.05, 1e-6)
        if std[key] < 1e-9:
            std[key] = 1e-6
    return {"mean": mean, "std": std, "n_gold": len(gold_features), "feature_keys": list(FEATURE_KEYS)}


def load_profile(profile_path: Path, gold_dir: Path) -> dict[str, Any]:
    if profile_path.is_file():
        data = json.loads(profile_path.read_text(encoding="utf-8"))
        if "mean" in data and "std" in data:
            return data
    gold_entries = load_gold_texts(gold_dir)
    gold_features = [extract_features(f"<article>{e['text']}</article>") for e in gold_entries]
    return compute_profile(gold_features)


def burrows_delta(features: dict[str, float], profile: dict[str, Any]) -> float:
    mean = profile["mean"]
    std = profile["std"]
    zs: list[float] = []
    for key in FEATURE_KEYS:
        z = (features.get(key, 0.0) - mean.get(key, 0.0)) / std.get(key, 1.0)
        zs.append(z)
    return math.sqrt(sum(z * z for z in zs) / len(zs)) if zs else 0.0


def axis_z_scores(features: dict[str, float], profile: dict[str, Any]) -> dict[str, float]:
    mean = profile["mean"]
    std = profile["std"]
    return {key: (features.get(key, 0.0) - mean.get(key, 0.0)) / std.get(key, 1.0) for key in FEATURE_KEYS}


AXIS_LABELS_RU: dict[str, str] = {
    "sent_len_mean": "средняя длина предложения (слова)",
    "sent_len_std": "разброс длины предложений",
    "para_len_mean": "средняя длина абзаца",
    "ttr": "лексическое разнообразие (TTR)",
    "hapax_rate": "доля hapax-лексем",
    "punct_em_dash_per_1k": "тире на 1000 слов",
    "punct_ellipsis_per_1k": "многоточие на 1000 слов",
    "punct_guillemet_per_1k": "«ёлочки» на 1000 слов",
    "first_person_ya_share": "доля «я» среди я/мы/вы",
    "first_person_my_share": "доля «мы» среди я/мы/вы",
    "hedge_per_1k": "канцелярит/дисклеймеры на 1000 слов",
    "legal_per_1k": "юртермины на 1000 слов",
    "lead_word_count": "длина лида (слова)",
    "lead_has_number": "число в первых 1–2 предложениях лида",
    "spine_overlap": "перекрытие лид ↔ финал (spine-once)",
}


def build_stylo_notes(
    features: dict[str, float],
    profile: dict[str, Any],
    delta: float,
    *,
    axis_z: float = AXIS_Z_NOTE,
) -> list[str]:
    zmap = axis_z_scores(features, profile)
    notes: list[str] = []
    for key, z in sorted(zmap.items(), key=lambda kv: abs(kv[1]), reverse=True):
        if abs(z) < axis_z:
            continue
        label = AXIS_LABELS_RU.get(key, key)
        if key.startswith("fw_"):
            word = key[3:]
            label = f"частота служебного «{word}»"
        direction = "выше" if z > 0 else "ниже"
        gold_val = profile["mean"].get(key, 0.0)
        cur_val = features.get(key, 0.0)
        notes.append(f"- {label}: {direction} gold (сейчас {cur_val:.3g}, эталон {gold_val:.3g}, z={z:+.2f})")
        if len(notes) >= 8:
            break
    if not notes:
        notes.append(f"- Delta {delta:.2f} в норме; явных отклонений по осям нет.")
    return notes


def append_history(
    history_path: Path,
    *,
    topic_id: str,
    features: dict[str, float],
    delta: float,
    stylo_pass: bool,
    sol_rewrite: bool,
) -> None:
    history_path.parent.mkdir(parents=True, exist_ok=True)
    row = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "topic_id": topic_id,
        "features": features,
        "delta": round(delta, 4),
        "stylo_pass": stylo_pass,
        "sol_rewrite": sol_rewrite,
        "good": None,
    }
    with history_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def measure_article(
    article_dir: Path,
    gold_dir: Path,
    output_path: Path,
    *,
    profile_path: Path | None = None,
    sol_rewrite: bool = False,
    append_hist: bool = True,
) -> dict[str, Any]:
    article_html_path = article_dir / "article.html"
    if not article_html_path.is_file():
        raise FileNotFoundError(f"нет {article_html_path}")

    html = article_html_path.read_text(encoding="utf-8")
    features = extract_features(html)
    prof_path = profile_path or project_root() / "memory/stylo/profile.json"
    profile = load_profile(prof_path, gold_dir)
    delta = burrows_delta(features, profile)
    stylo_pass = delta <= DELTA_PASS_THRESHOLD

    notes = build_stylo_notes(features, profile, delta)
    report: dict[str, Any] = {
        "stylo_pass": stylo_pass,
        "delta": round(delta, 4),
        "delta_threshold": DELTA_PASS_THRESHOLD,
        "features": {k: round(features[k], 6) for k in FEATURE_KEYS},
        "gold_n": profile.get("n_gold"),
        "sol_rewrite_applied": sol_rewrite,
        "notes": notes,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    notes_path = article_dir / "stylo-notes.md"
    notes_body = "\n".join(
        [
            "# Stylo notes (для Sol, один проход)",
            "",
            f"Delta: **{delta:.2f}** (порог {DELTA_PASS_THRESHOLD}); pass: **{stylo_pass}**",
            "",
            "Правь только ритм/голос. Факты, сюжет и newbuild-фокус не трогать.",
            "",
            *notes,
            "",
        ]
    )
    notes_path.write_text(notes_body, encoding="utf-8")

    if append_hist:
        topic_id = article_dir.name.split("-")[0] if "-" in article_dir.name else article_dir.name
        meta_path = article_dir / "article.meta.json"
        if meta_path.is_file():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                topic_id = str(meta.get("topic_id") or topic_id)
            except json.JSONDecodeError:
                pass
        append_history(
            project_root() / "memory/stylo/history.jsonl",
            topic_id=topic_id,
            features={k: round(features[k], 6) for k in FEATURE_KEYS},
            delta=delta,
            stylo_pass=stylo_pass,
            sol_rewrite=sol_rewrite,
        )

    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Excalibur stylo voice measurer")
    parser.add_argument("--article-dir", required=True, type=Path)
    parser.add_argument("--gold-dir", default=project_root() / "memory/stylo/gold", type=Path)
    parser.add_argument("--output", type=Path, help="stylo-report.json (default: article-dir/stylo-report.json)")
    parser.add_argument("--profile", type=Path, help="memory/stylo/profile.json override")
    parser.add_argument("--no-history", action="store_true")
    parser.add_argument("--sol-rewrite", action="store_true", help="пометить history sol_rewrite=true")
    args = parser.parse_args()

    out = args.output or (args.article_dir / "stylo-report.json")
    try:
        report = measure_article(
            args.article_dir,
            args.gold_dir,
            out,
            profile_path=args.profile,
            sol_rewrite=args.sol_rewrite,
            append_hist=not args.no_history,
        )
    except FileNotFoundError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 2

    status = "PASS" if report["stylo_pass"] else "FAIL"
    print(f"STYLO {status} delta={report['delta']} -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
