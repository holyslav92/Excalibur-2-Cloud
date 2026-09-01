#!/usr/bin/env python3
"""Solo cover regen via grsai standard image model (face i2i from studio portrait).

Builds solo cover prompt from quad-manifest, generates 1200×675 PNG,
stamps cover_qa.json. Kie and PIL mashup FORBIDDEN.

VIP image tier disabled owner 2026-08-25 — standard grsai model only.

Hard budget: default max 2 full attempts (EXCALIBUR_COVER_MAX_ATTEMPTS override).
After budget → clear FAIL with best candidate path; never infinite loop.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_cover_budget import resolve_cover_max_attempts
from excalibur_blog_grsai_gpt_image2_api import (
    DEFAULT_TIMEOUT_SECONDS,
    MIN_TIMEOUT_SECONDS,
    default_quality,
    generate_image,
    model_tier_standard,
    project_root,
    resolve_grsai_api_key,
    resolve_hosts,
)

DEFAULT_REF = "memory/cover/assets/identity-real/face-studio-2026-06-23.jpg"
SOLO_COVER_SIZE = "1200x675"


def build_prompt_for_article(article_dir: Path, root: Path) -> str:
    sys.path.insert(0, str(root / "scripts"))
    from excalibur_blog_cover_quad_prompt import build_solo_cover_prompt, load_json

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    manifest = load_json(manifest_path)
    style = load_json(root / manifest.get("style_file", "memory/cover/quad-style-the-rieltor.json"))
    hero = load_json(root / manifest.get("blog_hero", "memory/cover/blog-hero.json"))
    design = load_json(root / "memory/cover/cover-design-code.json")
    return build_solo_cover_prompt(manifest, style, hero, design)


def stamp_qa(article_dir: Path, root: Path, topic_id: str) -> dict[str, Any]:
    from excalibur_blog_cover_qa_pixels import analyze_cover_pixels, load_json, stamp_cover_qa_json

    cover_path = article_dir / "cover" / "cover.png"
    manifest = load_json(article_dir / "cover" / "quad-manifest.json")
    pixel = analyze_cover_pixels(cover_path, manifest=manifest)
    stamp_cover_qa_json(article_dir, pixel, topic_id=topic_id)
    qa_path = article_dir / "cover" / "cover_qa.json"
    qa = load_json(qa_path)
    qa["gate_status"] = "PASS" if pixel.status == "PASS" else "FAIL"
    qa["gate_errors"] = pixel.errors
    qa_path.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": pixel.status, "errors": pixel.errors, "md5": qa.get("cover_md5")}


def _record_cover_motifs(article_dir: Path, root: Path, topic_id: str) -> None:
    """Append cover motifs to used-motifs.json after successful solo regen."""
    import subprocess

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    if not manifest_path.is_file():
        return
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    motifs = manifest.get("cover_motifs") or {}
    if not motifs:
        return
    meta_path = article_dir / "article.meta.json"
    slug = ""
    if meta_path.is_file():
        slug = str(json.loads(meta_path.read_text(encoding="utf-8")).get("slug") or "")
    cmd = [
        sys.executable,
        str(root / "scripts/excalibur_blog_cover_motif_gate.py"),
        "record",
        "--topic-id",
        topic_id,
        "--slug",
        slug,
    ]
    field_map = {
        "composition": "--composition",
        "location": "--location",
        "meme": "--meme",
        "prop_set": "--prop-set",
        "sticker_set": "--sticker-set",
        "joke": "--joke",
        "outfit": "--outfit",
        "emotion": "--emotion",
        "pose_framing": "--pose-framing",
        "action": "--action",
    }
    for key, flag in field_map.items():
        value = str(motifs.get(key) or "").strip()
        if value:
            cmd.extend([flag, value])
    subprocess.run(cmd, cwd=root, check=False)


def _identity_i2i_reference_paths(root: Path, face_ref: Path) -> list[str]:
    """FACE primary + body-build refs from identity-real (WHO + medium-slim build)."""
    from excalibur_blog_identity_real import BODY_BUILD_FILES, IDENTITY_REAL_DIR

    refs: list[str] = []
    seen: set[str] = set()

    def add(path: Path) -> None:
        if not path.is_file():
            return
        key = str(path.resolve())
        if key in seen:
            return
        seen.add(key)
        try:
            refs.append(str(path.relative_to(root)))
        except ValueError:
            refs.append(str(path))

    add(face_ref)
    for spec in BODY_BUILD_FILES:
        add(root / IDENTITY_REAL_DIR / str(spec["file"]))
    return refs


def write_temp_batch(article_dir: Path, prompt: str, ref_path: Path, root: Path) -> Path:
    identity_locals = _identity_i2i_reference_paths(root, ref_path)
    batch = {
        "pipeline": "grsai_solo_cover",
        "slot": "cover",
        "output_canvas": "cover/cover.png",
        "prefer_local_reference": True,
        "local_reference": identity_locals[0] if identity_locals else str(ref_path),
        "identity_reference_locals": identity_locals,
        "jobs": [
            {
                "slot": "cover",
                "tool": "grsai-rest",
                "mcp_args": {
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "resolution": "2K",
                },
            }
        ],
    }
    batch_path = article_dir / "cover" / "grsai-solo-batch.json"
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return batch_path


def write_budget_exhausted_report(
    article_dir: Path,
    *,
    max_attempts: int,
    last_errors: list[str],
    best_cover_path: Path,
    attempts_log: list[dict[str, Any]],
) -> Path:
    report = {
        "status": "FAIL",
        "reason": "cover_budget_exhausted",
        "max_attempts": max_attempts,
        "best_candidate": str(best_cover_path),
        "last_errors": last_errors,
        "attempts": attempts_log,
        "next_steps": [
            "Re-run cover_qa_gate on best_candidate — analyze_cover_pixels applies OCR escape before verdict",
            "Do NOT deep-dive Cover-QA source — if visual OK after escape, proceed Indexer",
            "Never PIL mashup / Kie; regen only via grsai solo cover within budget",
        ],
    }
    out = article_dir / "cover" / "cover-budget-result.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate solo 1200×675 cover via grsai standard image model")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--ref", default=DEFAULT_REF)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    ap.add_argument("--prompt-suffix", default="", help="Extra prompt lines appended")
    ap.add_argument(
        "--max-attempts",
        type=int,
        default=None,
        help="Full cover attempts (default 2 or EXCALIBUR_COVER_MAX_ATTEMPTS)",
    )
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    max_attempts = resolve_cover_max_attempts(args.max_attempts)

    api_key = resolve_grsai_api_key()
    if not api_key:
        print("GRSAI API KEY MISSING", file=sys.stderr)
        return 1

    quality = default_quality()
    prompt = build_prompt_for_article(article_dir, root)
    if args.prompt_suffix.strip():
        prompt = prompt + "\n" + args.prompt_suffix.strip()
    ref_path = root / args.ref
    from excalibur_blog_identity_real import ensure_identity_reference

    try:
        ref_path = ensure_identity_reference(root)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL identity ref: {exc}", file=sys.stderr)
        return 1
    if not ref_path.is_file():
        print(f"FAIL identity ref missing: {ref_path}", file=sys.stderr)
        return 1

    identity_suffix = (
        "\nIDENTITY LOCK (mandatory): exact same man as reference photo — "
        "28 years old, medium-slim build, round-oval face, dark brown short hair tapered sides, "
        "warm dark brown eyes, full dark brows. "
        "MANDATORY visible dark five-o'clock-shadow stubble on jaw, chin and upper lip — "
        "same density and pattern as reference; NEVER clean-shaven, NEVER fashion-model jaw. "
        "Bone structure, hairline, stubble pattern, eye shape MUST match studio portrait. "
        "NEW invented outfit and emotion/scene — do NOT clone reference blazer/pose/background."
    )
    prompt = prompt + identity_suffix

    timeout = max(MIN_TIMEOUT_SECONDS, int(args.timeout))
    hosts = resolve_hosts()
    model = model_tier_standard()

    print(
        f"prompt_chars={len(prompt)} ref={ref_path.name} max_attempts={max_attempts} "
        f"model={model} hosts={hosts}",
        flush=True,
    )

    meta_json = json.loads((article_dir / "article.meta.json").read_text(encoding="utf-8"))
    topic_id = str(meta_json.get("topic_id") or "")

    last_errors: list[str] = []
    attempts_log: list[dict[str, Any]] = []
    best_cover_path = article_dir / "cover" / "cover.png"

    image_input = {
        "prompt": prompt,
        "aspect_ratio": "16:9",
        "resolution": "2K",
    }

    for attempt in range(1, max_attempts + 1):
        print(f"attempt {attempt}/{max_attempts} model={model}", flush=True)
        batch_path = write_temp_batch(article_dir, prompt, ref_path, root)

        attempt_entry: dict[str, Any] = {"attempt": attempt, "model": model}

        try:
            raw_bytes, gen_meta = generate_image(
                root=root,
                batch_path=batch_path,
                image_input=image_input,
                api_key=api_key,
                model=model,
                quality=quality,
                target_size=SOLO_COVER_SIZE,
                timeout=timeout,
                hosts=hosts,
                max_retries=1,
                retry_wait=5,
                ref_path=ref_path,
            )
        except Exception as exc:  # noqa: BLE001
            attempt_entry["error"] = str(exc)
            attempts_log.append(attempt_entry)
            print(f"FAIL generation: {exc}", file=sys.stderr)
            continue

        gen_meta["model_tier"] = "standard"
        cover_path = article_dir / "cover" / "cover.png"
        cover_path.parent.mkdir(parents=True, exist_ok=True)
        cover_path.write_bytes(raw_bytes)
        best_cover_path = cover_path
        attempt_entry["bytes"] = len(raw_bytes)
        attempt_entry["host"] = gen_meta.get("host")
        print(
            f"OK cover.png bytes={len(raw_bytes)} model={model} "
            f"host={gen_meta.get('host')} endpoint={gen_meta.get('endpoint')}",
        )

        qa = stamp_qa(article_dir, root, topic_id)
        attempt_entry["qa_status"] = qa["status"]
        attempt_entry["qa_errors"] = list(qa["errors"])

        if qa["status"] == "PASS":
            print(f"OK cover_qa PASS md5={qa['md5']}")
            _record_cover_motifs(article_dir, root, topic_id)
            return 0

        last_errors = list(qa["errors"])
        attempt_entry["qa_fail"] = True
        attempts_log.append(attempt_entry)
        print(f"WARN pixel QA fail: {'; '.join(last_errors)}", flush=True)

    report_path = write_budget_exhausted_report(
        article_dir,
        max_attempts=max_attempts,
        last_errors=last_errors,
        best_cover_path=best_cover_path,
        attempts_log=attempts_log,
    )
    print(
        f"FAIL COVER BUDGET EXHAUSTED after {max_attempts} attempt(s). "
        f"best_candidate={best_cover_path} report={report_path}",
        file=sys.stderr,
    )
    print("FAIL pixel QA:", "; ".join(last_errors), file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
