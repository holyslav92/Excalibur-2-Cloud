#!/usr/bin/env python3
"""Human Russian alt/caption builder for cover + inline images.

Production scene_hint / prompt tokens must never leak into alt, figcaption,
or WP Media Library fields. This module builds short Russian sentences from
title, hook, labels, and visual context — and gates prompt-like junk.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")

# English production tokens — banned in alt/caption forever.
BANNED_ALT_TOKEN_RES = (
    re.compile(r"\bhook\b", re.I),
    re.compile(r"\bcta\b", re.I),
    re.compile(r"\bmemes?\b", re.I),
    re.compile(r"\bscene_hint\b", re.I),
    re.compile(r"\bsticky\b", re.I),
    re.compile(r"\bprompt\b", re.I),
    re.compile(r"\bi2i\b", re.I),
    re.compile(r"\bcover\s*slot\b", re.I),
    re.compile(r"\bquad\b", re.I),
    re.compile(r"\binline_\d+\b", re.I),
    re.compile(r"\bwordstat\b", re.I),
    re.compile(r"\bno_host\b", re.I),
    re.compile(r"\bhost\s+large\b", re.I),
)

# «мемы» as a production tag (not natural prose like «мем-стикер»).
MEME_TAG_RE = re.compile(r"(?:^|[;\s])мемы(?:$|[;\s])", re.I)

PHONE_ONLY_RE = re.compile(r"^\+?7[\s\d\-()]{10,}$")

# Short Russian SEO alt for WP/Dzen (owner lock 2026-09-01).
ALT_SEO_MIN = 80
ALT_SEO_MAX = 140

# Scene-painting / scene_hint dump markers — must never appear in alt/caption.
SCENE_PAINTING_RES: tuple[re.Pattern[str], ...] = (
    re.compile(r"рядом\s+лежит", re.I),
    re.compile(r"у\s+стойки", re.I),
    re.compile(r"на\s+столе", re.I),
    re.compile(r"на\s+заднем\s+плане", re.I),
    re.compile(r"без\s+людей\s+в\s+кадре", re.I),
    re.compile(r"в\s+кадре\s+без", re.I),
    re.compile(r"отображается", re.I),
    re.compile(r"сопоставлен", re.I),
    re.compile(r"сидит\s+за", re.I),
    re.compile(r"стоят\s+за", re.I),
    re.compile(r"лежат\s+\w+", re.I),
    re.compile(r"остановивш", re.I),
    re.compile(r"сравнивает\s+два\s+договор", re.I),
    re.compile(r"показывает\s+связь", re.I),
    re.compile(r"временн\w+\s+шкала\s+показывает", re.I),
    re.compile(r"покупатель\s+сравнивает", re.I),
    re.compile(r"у\s+стойки\s+регистраци", re.I),
    re.compile(r"таймер\s+брони", re.I),
    re.compile(r"со\s+стикером\s+«", re.I),
    re.compile(r"с\s+эмоци", re.I),
)

OUTFIT_RU_FRAGMENTS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"cardigan", re.I), "в кардигане"),
    (re.compile(r"sweater|свитер", re.I), "в свитере"),
    (re.compile(r"blazer|пиджак", re.I), "в пиджаке"),
    (re.compile(r"hoodie|худи", re.I), "в худи"),
    (re.compile(r"vest|жилет", re.I), "в жилете"),
    (re.compile(r"terracotta|терракот", re.I), "терракотовом"),
    (re.compile(r"sage|olive", re.I), "оливковом"),
)

VISUAL_TYPE_FALLBACK_RU = {
    "comparison_table": "Сравнительная таблица",
    "comparison_table_ui": "Сравнительная таблица",
    "process_flow": "Схема процесса",
    "workflow_diagram": "Пошаговая схема",
    "bar_timeline_chart": "График и шкала сроков",
    "structure_diagram": "Схема механизма",
    "labeled_checklist": "Чеклист",
    "fact_card": "Карточка фактов",
    "cover_editorial_hero": "Обложка",
}


def project_root() -> Path:
    env_root = __import__("os").environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def normalize_text(value: object) -> str:
    return " ".join(str(value or "").split()).strip()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_cover_text_inline_labels(article_dir: Path) -> dict[str, list[str]]:
    """cover-text.json inline_labels — fallback when manifest slot labels empty (B23)."""
    cover_text_path = article_dir / "cover" / "cover-text.json"
    if not cover_text_path.is_file():
        return {}
    try:
        cover_text = load_json(cover_text_path)
    except json.JSONDecodeError:
        return {}
    raw = cover_text.get("inline_labels") or {}
    out: dict[str, list[str]] = {}
    if not isinstance(raw, dict):
        return out
    for slot_key, labels in raw.items():
        if not isinstance(labels, list):
            continue
        cleaned = [normalize_text(x) for x in labels if normalize_text(x)]
        if cleaned:
            out[str(slot_key)] = cleaned
    return out


def slot_labels_with_fallback(
    slot_key: str,
    slot: dict[str, Any],
    *,
    cover_text_labels: dict[str, list[str]] | None = None,
) -> list[str]:
    panel_labels = [normalize_text(x) for x in (slot.get("labels") or []) if normalize_text(x)]
    if panel_labels:
        return panel_labels
    fallback = (cover_text_labels or {}).get(slot_key) or []
    return [normalize_text(x) for x in fallback if normalize_text(x)]


def load_visual_type_labels(root: Path) -> dict[str, str]:
    catalog_path = root / "memory/cover/inline-visual-types.json"
    labels: dict[str, str] = dict(VISUAL_TYPE_FALLBACK_RU)
    if not catalog_path.is_file():
        return labels
    try:
        catalog = load_json(catalog_path)
    except json.JSONDecodeError:
        return labels
    for key, spec in (catalog.get("types") or {}).items():
        if isinstance(spec, dict) and spec.get("label_ru"):
            labels[str(key)] = str(spec["label_ru"])
    return labels


def load_hero_name(root: Path) -> str:
    hero_path = root / "memory/cover/blog-hero.json"
    if hero_path.is_file():
        try:
            hero = load_json(hero_path)
            name = normalize_text(hero.get("name_ru"))
            if name:
                return name
        except json.JSONDecodeError:
            pass
    return "Святослав Шакин"


def banned_alt_hits(text: str) -> list[str]:
    hits: list[str] = []
    for rx in BANNED_ALT_TOKEN_RES:
        if rx.search(text or ""):
            hits.append(rx.pattern)
    if MEME_TAG_RE.search(text or ""):
        hits.append("мемы-tag")
    return hits


def looks_like_prompt_list(text: str) -> bool:
    """Semicolon-separated production fragments, not one human sentence."""
    raw = normalize_text(text)
    if ";" not in raw:
        return False
    parts = [normalize_text(p) for p in raw.split(";") if normalize_text(p)]
    if len(parts) < 2:
        return False
    junk_parts = 0
    for part in parts:
        if banned_alt_hits(part):
            junk_parts += 1
            continue
        if not CYRILLIC_RE.search(part):
            junk_parts += 1
            continue
        if len(part.split()) <= 2 and part.casefold() in {"стикер", "телефон", "hook", "cta"}:
            junk_parts += 1
    return junk_parts >= 1 and junk_parts >= len(parts) // 2


def host_name_appears_twice(text: str, host_name: str) -> bool:
    """FAIL when hero full name is repeated (scene_hint tail leak)."""
    parts = [p for p in normalize_text(host_name).split() if p]
    if len(parts) < 2:
        return False
    first, last = parts[0].casefold(), parts[-1].casefold()
    blob = normalize_text(text).casefold()
    return blob.count(first) >= 2 and blob.count(last) >= 2


def scene_hint_overlap_ratio(text: str, scene_hint: str) -> float:
    """Share of scene_hint content words present in alt (prompt leak)."""
    hint = normalize_text(scene_hint)
    alt = normalize_text(text)
    if not hint or not alt:
        return 0.0
    stop = {"и", "в", "на", "с", "по", "для", "без", "из", "к", "у", "о", "а", "но", "же", "ли", "то", "не", "что", "как", "это", "тот", "та", "те", "рядом", "лежит"}
    hint_words = [w for w in re.findall(r"[а-яёa-z0-9]+", hint.casefold()) if len(w) > 3 and w not in stop]
    if not hint_words:
        return 0.0
    alt_blob = alt.casefold()
    hits = sum(1 for w in hint_words if w in alt_blob)
    return hits / len(hint_words)


def hook_concatenated_in_alt(text: str, manifest: dict[str, Any], meta: dict[str, Any]) -> bool:
    """Two-sentence alt where second chunk repeats title/hook (Dzen leak pattern)."""
    raw = normalize_text(text)
    if ". " not in raw and " — " not in raw:
        return False
    hook = normalize_text(manifest.get("cover_hook") or meta.get("h1") or meta.get("title"))
    if not hook:
        return False
    hook_plain = hook.rstrip(".!?").casefold()
    parts = re.split(r"\.\s+|—\s+", raw)
    if len(parts) < 2:
        return False
    tail = parts[-1].rstrip(".!?").casefold()
    return hook_plain in tail or tail in hook_plain


def scene_painting_hits(
    text: str,
    *,
    scene_hint: str = "",
    host_name: str = "",
    manifest: dict[str, Any] | None = None,
    meta: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    raw = normalize_text(text)
    if not raw:
        return errors
    for rx in SCENE_PAINTING_RES:
        if rx.search(raw):
            errors.append(f"scene-painting: {rx.pattern}")
    if host_name and host_name_appears_twice(raw, host_name):
        errors.append("host name duplicated in alt")
    if scene_hint and scene_hint_overlap_ratio(raw, scene_hint) >= 0.45:
        errors.append("scene_hint overlap in alt")
    if manifest is not None and meta is not None and hook_concatenated_in_alt(raw, manifest, meta):
        errors.append("hook concatenated in alt")
    return errors


def clamp_seo_alt(text: str, *, min_len: int = ALT_SEO_MIN, max_len: int = ALT_SEO_MAX) -> str:
    raw = normalize_text(text).rstrip(".!?")
    if not raw:
        return raw
    if len(raw) <= max_len and len(raw) >= min_len:
        return f"{raw}."
    if len(raw) > max_len:
        cut = raw[: max_len - 1]
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        return f"{cut.rstrip('.,;:')}…"
    return f"{raw}."


def is_prompt_like_alt(
    text: str,
    *,
    scene_hint: str = "",
    host_name: str = "",
    manifest: dict[str, Any] | None = None,
    meta: dict[str, Any] | None = None,
    seo_length: bool = True,
) -> tuple[bool, list[str]]:
    raw = normalize_text(text)
    errors: list[str] = []
    if not raw:
        errors.append("alt empty")
        return True, errors
    if not CYRILLIC_RE.search(raw):
        errors.append("alt has no Cyrillic")
    hits = banned_alt_hits(raw)
    if hits:
        errors.append(f"banned tokens: {', '.join(hits)}")
    if looks_like_prompt_list(raw):
        errors.append("semicolon prompt list")
    if PHONE_ONLY_RE.match(raw.replace(" ", "")):
        errors.append("phone-only alt")
    errors.extend(
        scene_painting_hits(
            raw,
            scene_hint=scene_hint,
            host_name=host_name,
            manifest=manifest,
            meta=meta,
        )
    )
    if seo_length:
        if len(raw) < ALT_SEO_MIN:
            errors.append(f"alt too short ({len(raw)} < {ALT_SEO_MIN})")
        if len(raw) > ALT_SEO_MAX:
            errors.append(f"alt too long ({len(raw)} > {ALT_SEO_MAX})")
    return bool(errors), errors


def extract_visual_segment(raw_alt: str) -> str:
    """Keep the first human Russian segment from a semicolon prompt list."""
    parts = [normalize_text(p) for p in (raw_alt or "").split(";")]
    for part in parts:
        if not part or not CYRILLIC_RE.search(part):
            continue
        if banned_alt_hits(part):
            continue
        if len(part.split()) < 3:
            continue
        return part.rstrip(".")
    return ""


def outfit_phrase_from_motifs(motifs: dict[str, Any]) -> str:
    outfit = normalize_text(motifs.get("outfit"))
    if not outfit:
        return ""
    for rx, phrase in OUTFIT_RU_FRAGMENTS:
        if rx.search(outfit):
            return phrase
    return ""


def article_has_tyumen(meta: dict[str, Any]) -> bool:
    blob = " ".join(
        str(meta.get(k) or "")
        for k in ("title", "h1", "slug", "description")
    ).casefold()
    return "тюмен" in blob or "tyumen" in blob


def hook_stakes_sentence(manifest: dict[str, Any], meta: dict[str, Any]) -> str:
    hook = normalize_text(manifest.get("cover_hook"))
    if not hook:
        hook = normalize_text(meta.get("h1") or meta.get("title"))
    if not hook:
        return ""
    if hook[-1] not in ".!?":
        hook += "."
    return hook


def build_cover_alt(
    manifest: dict[str, Any],
    meta: dict[str, Any],
    *,
    host_name: str,
    slot: dict[str, Any] | None = None,
) -> str:
    """One short Russian SEO sentence from title/topic — never scene_hint painting."""
    slot = slot or (manifest.get("slots") or {}).get("cover") or {}
    scene_hint = normalize_text(slot.get("scene_hint"))
    title = normalize_text(meta.get("h1") or meta.get("title") or manifest.get("cover_hook"))
    if not title:
        title = "Новостройка в Тюмени: проверка договора перед подписью"
    core = title.rstrip(".!?")
    if article_has_tyumen(meta) and "тюмен" not in core.casefold():
        core = f"{core} в Тюмени"
    if len(core) < ALT_SEO_MIN:
        core = f"{core}: что проверить в договоре и эскроу до подписи"
    alt = clamp_seo_alt(core)
    # Safety: if still scene-like, fall back to title only.
    if is_prompt_like_alt(
        alt,
        scene_hint=scene_hint,
        host_name=host_name,
        manifest=manifest,
        meta=meta,
        seo_length=False,
    )[0]:
        alt = clamp_seo_alt(title)
    return alt


def shorten_h2(h2: str, *, max_len: int = 72) -> str:
    text = normalize_text(h2)
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


def visual_type_label(visual_type: str, labels_map: dict[str, str]) -> str:
    key = normalize_text(visual_type)
    return labels_map.get(key) or VISUAL_TYPE_FALLBACK_RU.get(key) or "Инфографика"


def build_inline_alt(
    slot: dict[str, Any],
    *,
    labels_map: dict[str, str],
    meta: dict[str, Any] | None = None,
    cover_text_labels: dict[str, list[str]] | None = None,
    slot_key: str = "",
) -> str:
    visual_type = normalize_text(slot.get("visual_type"))
    label_ru = visual_type_label(visual_type, labels_map)
    h2 = shorten_h2(normalize_text(slot.get("h2_anchor")), max_len=48)
    panel_labels = slot_labels_with_fallback(
        slot_key,
        slot,
        cover_text_labels=cover_text_labels,
    )

    if panel_labels and visual_type not in {"realistic_photo", "cover_editorial_hero"}:
        facts = ", ".join(panel_labels[:3])
        alt = f"{label_ru} по новостройке в Тюмени: {facts} — иллюстрация к разбору сделки."
    elif h2:
        tyumen = " в Тюмени" if meta and article_has_tyumen(meta) else ""
        alt = f"{label_ru} к разделу «{h2}»{tyumen} — иллюстрация к кейсу о сделке."
    else:
        tyumen = " в Тюмени" if meta and article_has_tyumen(meta) else ""
        alt = f"{label_ru} по новостройке{tyumen} — иллюстрация к материалу."
    return clamp_seo_alt(alt)


def resolve_slot_alt(
    slot_key: str,
    slot: dict[str, Any],
    manifest: dict[str, Any],
    meta: dict[str, Any],
    *,
    host_name: str,
    labels_map: dict[str, str],
    cover_text_labels: dict[str, list[str]] | None = None,
) -> str:
    if slot_key == "cover":
        return build_cover_alt(manifest, meta, host_name=host_name, slot=slot)
    return build_inline_alt(
        slot,
        labels_map=labels_map,
        meta=meta,
        cover_text_labels=cover_text_labels,
        slot_key=slot_key,
    )


def validate_alt_for_gate(
    alt: str,
    *,
    slot_key: str,
    slot: dict[str, Any],
    manifest: dict[str, Any],
    meta: dict[str, Any],
    host_name: str,
) -> tuple[bool, list[str]]:
    scene_hint = normalize_text(slot.get("scene_hint")) if slot_key != "cover" else normalize_text(
        ((manifest.get("slots") or {}).get("cover") or {}).get("scene_hint")
    )
    return is_prompt_like_alt(
        alt,
        scene_hint=scene_hint,
        host_name=host_name if slot_key == "cover" else "",
        manifest=manifest if slot_key == "cover" else None,
        meta=meta if slot_key == "cover" else None,
    )


def cover_caption_must_be_empty(caption: str) -> tuple[bool, list[str]]:
    if normalize_text(caption):
        return False, ["featured caption must be empty (Dzen syndication leak)"]
    return True, []


def collect_article_alts(article_dir: Path, root: Path) -> dict[str, Any]:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    registry_path = article_dir / "cover" / "cover-registry.json"
    html_path = article_dir / "article.html"
    meta_path = article_dir / "article.meta.json"

    manifest = load_json(manifest_path) if manifest_path.is_file() else {}
    meta = load_json(meta_path) if meta_path.is_file() else {}
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)
    cover_text_labels = load_cover_text_inline_labels(article_dir)

    slots_out: dict[str, dict[str, Any]] = {}
    for slot_key, slot in (manifest.get("slots") or {}).items():
        if not isinstance(slot, dict):
            continue
        if slot_key != "cover" and not slot.get("h2_anchor") and not slot.get("alt"):
            continue
        raw = normalize_text(slot.get("alt"))
        resolved = resolve_slot_alt(
            slot_key,
            slot,
            manifest,
            meta,
            host_name=host_name,
            labels_map=labels_map,
            cover_text_labels=cover_text_labels,
        )
        ok, errors = validate_alt_for_gate(
            resolved,
            slot_key=slot_key,
            slot=slot,
            manifest=manifest,
            meta=meta,
            host_name=host_name,
        )
        slots_out[slot_key] = {
            "raw_alt": raw,
            "resolved_alt": resolved,
            "pass": not ok,
            "errors": errors,
        }

    cover_caption_ok = True
    cover_caption_errors: list[str] = []
    if registry_path.is_file():
        try:
            reg_probe = load_json(registry_path)
            cap = ""
            for asset in reg_probe.get("assets") or []:
                if isinstance(asset, dict) and asset.get("role") == "cover":
                    cap = normalize_text(asset.get("caption"))
                    break
            cover_caption_ok, cover_caption_errors = cover_caption_must_be_empty(cap)
        except json.JSONDecodeError:
            cover_caption_ok = False
            cover_caption_errors = ["cover-registry.json invalid JSON"]

    html_alts: list[dict[str, str]] = []
    if html_path.is_file():
        from excalibur_blog_wp_publish import parse_local_img_tags

        for img in parse_local_img_tags(html_path.read_text(encoding="utf-8")):
            alt = normalize_text(img.get("alt"))
            ok, errors = is_prompt_like_alt(alt, seo_length=True)
            html_alts.append({"src": img.get("src", ""), "alt": alt, "pass": not ok, "errors": errors})

    registry_alts: list[dict[str, str]] = []
    if registry_path.is_file():
        try:
            registry = load_json(registry_path)
        except json.JSONDecodeError:
            registry = {}
        for asset in registry.get("assets") or []:
            if not isinstance(asset, dict):
                continue
            alt = normalize_text(asset.get("alt"))
            slot_key = str(asset.get("slot") or "")
            slot = (manifest.get("slots") or {}).get(slot_key) or {}
            ok, errors = validate_alt_for_gate(
                alt,
                slot_key=slot_key or "inline",
                slot=slot if isinstance(slot, dict) else {},
                manifest=manifest,
                meta=meta,
                host_name=host_name,
            )
            cap_ok, cap_errs = (True, [])
            if asset.get("role") == "cover":
                cap_ok, cap_errs = cover_caption_must_be_empty(str(asset.get("caption") or ""))
            registry_alts.append(
                {
                    "file": str(asset.get("file") or ""),
                    "slot": slot_key,
                    "alt": alt,
                    "pass": (not ok) and cap_ok,
                    "errors": errors + cap_errs,
                }
            )
        cover_alt = normalize_text(registry.get("alt"))
        if cover_alt:
            cover_slot = (manifest.get("slots") or {}).get("cover") or {}
            ok, errors = validate_alt_for_gate(
                cover_alt,
                slot_key="cover",
                slot=cover_slot if isinstance(cover_slot, dict) else {},
                manifest=manifest,
                meta=meta,
                host_name=host_name,
            )
            registry_alts.append(
                {"file": "cover/cover.png", "slot": "cover", "alt": cover_alt, "pass": not ok, "errors": errors}
            )

    all_items = list(slots_out.values()) + html_alts + registry_alts
    all_pass = cover_caption_ok and all(item.get("pass") for item in all_items) if all_items else cover_caption_ok
    return {
        "status": "PASS" if all_pass else "FAIL",
        "all_pass": all_pass,
        "cover_caption_empty": cover_caption_ok,
        "cover_caption_errors": cover_caption_errors,
        "slots": slots_out,
        "html_alts": html_alts,
        "registry_alts": registry_alts,
    }


def apply_article_captions(article_dir: Path, root: Path, *, dry_run: bool = False) -> dict[str, Any]:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    registry_path = article_dir / "cover" / "cover-registry.json"
    html_path = article_dir / "article.html"
    meta_path = article_dir / "article.meta.json"

    if not manifest_path.is_file():
        raise FileNotFoundError(f"missing {manifest_path}")

    manifest = load_json(manifest_path)
    meta = load_json(meta_path) if meta_path.is_file() else {}
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)
    cover_text_labels = load_cover_text_inline_labels(article_dir)

    changes: list[str] = []
    slot_alts: dict[str, str] = {}
    for slot_key, slot in (manifest.get("slots") or {}).items():
        if not isinstance(slot, dict):
            continue
        if slot_key != "cover" and not slot.get("h2_anchor"):
            continue
        resolved = resolve_slot_alt(
            slot_key,
            slot,
            manifest,
            meta,
            host_name=host_name,
            labels_map=labels_map,
            cover_text_labels=cover_text_labels,
        )
        old = normalize_text(slot.get("alt"))
        slot_alts[slot_key] = resolved
        if old != resolved:
            changes.append(f"{slot_key}: {old!r} -> {resolved!r}")
            if not dry_run:
                slot["alt"] = resolved

    if changes and not dry_run:
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    if registry_path.is_file() and not dry_run:
        registry = load_json(registry_path)
        cover_alt = slot_alts.get("cover") or registry.get("alt") or ""
        if cover_alt:
            registry["alt"] = cover_alt
        for asset in registry.get("assets") or []:
            if not isinstance(asset, dict):
                continue
            slot_key = str(asset.get("slot") or "")
            if slot_key in slot_alts:
                asset["alt"] = slot_alts[slot_key]
                if asset.get("role") == "cover" or slot_key == "cover":
                    asset["caption"] = ""
                else:
                    asset["caption"] = ""
                asset["description"] = slot_alts[slot_key]
        registry["caption"] = ""
        registry_path.write_text(
            json.dumps(registry, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        changes.append("cover-registry.json updated")

    if html_path.is_file():
        html = html_path.read_text(encoding="utf-8")
        new_html = html
        for slot_key, alt in slot_alts.items():
            if slot_key == "cover":
                continue
            file_name = "cover.png" if slot_key == "cover" else f"inline-{slot_key.split('_')[-1]}.png"
            pattern = re.compile(
                rf'(<figure[^>]*\bdata-slot="{re.escape(slot_key)}"[^>]*>\s*<img\b[^>]*\balt=")([^"]*)(")',
                re.I | re.S,
            )

            def _repl(match: re.Match[str], *, _alt: str = alt) -> str:
                return f"{match.group(1)}{_alt}{match.group(3)}"

            new_html, n = pattern.subn(_repl, new_html, count=1)
            if n:
                changes.append(f"article.html img {slot_key} alt updated")
            else:
                # Fallback: replace by filename when data-slot missing.
                file_pattern = re.compile(
                    rf'(<img\b[^>]*\bsrc="[^"]*{re.escape(file_name)}"[^>]*\balt=")([^"]*)(")',
                    re.I,
                )
                new_html, n2 = file_pattern.subn(_repl, new_html, count=1)
                if n2:
                    changes.append(f"article.html img {file_name} alt updated")

        if new_html != html and not dry_run:
            html_path.write_text(new_html, encoding="utf-8", newline="\n")

    gate = collect_article_alts(article_dir, root)
    return {"changes": changes, "gate": gate, "dry_run": dry_run}


def ensure_human_alt(
    text: str,
    *,
    slot_key: str,
    manifest: dict[str, Any],
    meta: dict[str, Any],
    root: Path,
    article_dir: Path | None = None,
) -> str:
    """Publish-time safety net: never return prompt-like alt."""
    raw = normalize_text(text)
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)
    cover_text_labels = (
        load_cover_text_inline_labels(article_dir)
        if article_dir is not None
        else {}
    )
    slot = (manifest.get("slots") or {}).get(slot_key) or {}
    if raw and not is_prompt_like_alt(raw)[0]:
        return raw
    return resolve_slot_alt(
        slot_key,
        {**slot, "alt": raw},
        manifest,
        meta,
        host_name=host_name,
        labels_map=labels_map,
        cover_text_labels=cover_text_labels,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Build human Russian image alt/caption text")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--apply", action="store_true", help="Write resolved alt into manifest/registry/html")
    ap.add_argument("--gate", action="store_true", help="Validate alts only (writes image-alt-gate.json with --output)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("-o", "--output", default="image-alt-gate.json")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    if args.apply:
        result = apply_article_captions(article_dir, root, dry_run=args.dry_run)
        out_path = article_dir / args.output
        payload = {
            "status": result["gate"]["status"],
            "all_pass": result["gate"]["all_pass"],
            "changes": result["changes"],
            "slots": result["gate"]["slots"],
            "html_alts": result["gate"]["html_alts"],
            "registry_alts": result["gate"]["registry_alts"],
        }
        if not args.dry_run:
            out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if payload["all_pass"] else 1

    gate = collect_article_alts(article_dir, root)
    out_path = article_dir / args.output
    if args.gate and not args.dry_run:
        out_path.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(gate, ensure_ascii=False, indent=2))
    return 0 if gate["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
