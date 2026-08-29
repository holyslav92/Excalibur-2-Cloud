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


def is_prompt_like_alt(text: str) -> tuple[bool, list[str]]:
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
    if len(raw) > 240:
        errors.append(f"alt too long ({len(raw)} chars)")
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
    slot = slot or (manifest.get("slots") or {}).get("cover") or {}
    motifs = manifest.get("cover_motifs") or {}
    raw_alt = normalize_text(slot.get("alt"))

    visual = ""
    if raw_alt and not is_prompt_like_alt(raw_alt)[0]:
        visual = raw_alt.rstrip(".")
    else:
        visual = extract_visual_segment(raw_alt)
        if not visual:
            outfit = outfit_phrase_from_motifs(motifs)
            emotion = normalize_text(slot.get("cover_emotion"))
            sticky = normalize_text(slot.get("sticky"))
            chunks: list[str] = []
            if host_name.split()[0].casefold() not in (emotion + sticky).casefold():
                chunks.append(host_name)
            if outfit:
                chunks.append(outfit)
            if emotion:
                chunks.append(f"с эмоцией «{emotion}»")
            if sticky:
                chunks.append(f"со стикером «{sticky}»")
            visual = " ".join(chunks).strip() or f"{host_name} на обложке кейса"

    first_name = host_name.split()[0]
    if first_name.casefold() not in visual.casefold():
        visual = f"{host_name} {visual[0].lower() + visual[1:]}" if visual else host_name

    if article_has_tyumen(meta) and "тюмен" not in visual.casefold():
        visual = f"{visual.rstrip('.')} в Тюмени"

    stakes = hook_stakes_sentence(manifest, meta)
    stakes_plain = stakes.rstrip(".") if stakes else ""
    if stakes_plain:
        # Не дублировать hook при повторных --apply (raw alt уже содержит stakes).
        while visual.casefold().endswith(stakes_plain.casefold()):
            visual = visual[: -len(stakes_plain)].rstrip(" .,")
        if stakes_plain.casefold() not in visual.casefold():
            return f"{visual.rstrip('.')}. {stakes}"
    return f"{visual.rstrip('.')}."


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
) -> str:
    raw_alt = normalize_text(slot.get("alt"))
    if raw_alt and not is_prompt_like_alt(raw_alt)[0]:
        return raw_alt if raw_alt.endswith((".", "!", "?")) else f"{raw_alt}."

    visual_type = normalize_text(slot.get("visual_type"))
    label_ru = visual_type_label(visual_type, labels_map)
    h2 = normalize_text(slot.get("h2_anchor"))
    panel_labels = [normalize_text(x) for x in (slot.get("labels") or []) if normalize_text(x)]

    if panel_labels:
        facts = ", ".join(panel_labels[:4])
        return f"{label_ru}: {facts}."
    if h2:
        return f"{label_ru} к разделу «{shorten_h2(h2)}»."
    return f"{label_ru} по теме статьи."


def resolve_slot_alt(
    slot_key: str,
    slot: dict[str, Any],
    manifest: dict[str, Any],
    meta: dict[str, Any],
    *,
    host_name: str,
    labels_map: dict[str, str],
) -> str:
    if slot_key == "cover":
        return build_cover_alt(manifest, meta, host_name=host_name, slot=slot)
    return build_inline_alt(slot, labels_map=labels_map)


def collect_article_alts(article_dir: Path, root: Path) -> dict[str, Any]:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    registry_path = article_dir / "cover" / "cover-registry.json"
    html_path = article_dir / "article.html"
    meta_path = article_dir / "article.meta.json"

    manifest = load_json(manifest_path) if manifest_path.is_file() else {}
    meta = load_json(meta_path) if meta_path.is_file() else {}
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)

    slots_out: dict[str, dict[str, Any]] = {}
    for slot_key, slot in (manifest.get("slots") or {}).items():
        if not isinstance(slot, dict):
            continue
        if slot_key != "cover" and not slot.get("h2_anchor") and not slot.get("alt"):
            continue
        raw = normalize_text(slot.get("alt"))
        resolved = resolve_slot_alt(
            slot_key, slot, manifest, meta, host_name=host_name, labels_map=labels_map
        )
        ok, errors = is_prompt_like_alt(resolved)
        slots_out[slot_key] = {
            "raw_alt": raw,
            "resolved_alt": resolved,
            "pass": not ok,
            "errors": errors,
        }

    html_alts: list[dict[str, str]] = []
    if html_path.is_file():
        from excalibur_blog_wp_publish import parse_local_img_tags

        for img in parse_local_img_tags(html_path.read_text(encoding="utf-8")):
            alt = normalize_text(img.get("alt"))
            ok, errors = is_prompt_like_alt(alt)
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
            ok, errors = is_prompt_like_alt(alt)
            registry_alts.append(
                {
                    "file": str(asset.get("file") or ""),
                    "slot": str(asset.get("slot") or ""),
                    "alt": alt,
                    "pass": not ok,
                    "errors": errors,
                }
            )
        cover_alt = normalize_text(registry.get("alt"))
        if cover_alt:
            ok, errors = is_prompt_like_alt(cover_alt)
            registry_alts.append(
                {"file": "cover/cover.png", "slot": "cover", "alt": cover_alt, "pass": not ok, "errors": errors}
            )

    all_items = list(slots_out.values()) + html_alts + registry_alts
    all_pass = all(item.get("pass") for item in all_items) if all_items else False
    return {
        "status": "PASS" if all_pass else "FAIL",
        "all_pass": all_pass,
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

    changes: list[str] = []
    slot_alts: dict[str, str] = {}
    for slot_key, slot in (manifest.get("slots") or {}).items():
        if not isinstance(slot, dict):
            continue
        if slot_key != "cover" and not slot.get("h2_anchor"):
            continue
        resolved = resolve_slot_alt(
            slot_key, slot, manifest, meta, host_name=host_name, labels_map=labels_map
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
                asset["caption"] = slot_alts[slot_key]
                asset["description"] = slot_alts[slot_key]
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


def ensure_human_alt(text: str, *, slot_key: str, manifest: dict[str, Any], meta: dict[str, Any], root: Path) -> str:
    """Publish-time safety net: never return prompt-like alt."""
    raw = normalize_text(text)
    host_name = load_hero_name(root)
    labels_map = load_visual_type_labels(root)
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
