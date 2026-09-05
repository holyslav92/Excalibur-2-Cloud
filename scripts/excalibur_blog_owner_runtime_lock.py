#!/usr/bin/env python3
"""FAIL-CLOSED drift guard: repo config must match shared/owner-runtime-lock.json."""
from __future__ import annotations

import fnmatch
import json
import os
from pathlib import Path
from typing import Any


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_lock(root: Path | None = None) -> dict[str, Any]:
    root = root or project_root()
    path = root / "shared" / "owner-runtime-lock.json"
    if not path.is_file():
        raise FileNotFoundError(f"missing {path.relative_to(root)}")
    return json.loads(path.read_text(encoding="utf-8"))


def _read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _glob_paths(root: Path, pattern: str) -> list[Path]:
    if "**" in pattern:
        return sorted(root.glob(pattern))
    return [root / pattern] if (root / pattern).is_file() else []


def extract_automation_instructions(doc_text: str, block_start: str, block_end: str) -> str:
    """Return the paste-ready Automation Instructions block (last ```text fence in doc)."""
    section = doc_text
    marker = "## Automation prompt"
    if marker in doc_text:
        section = doc_text.split(marker, 1)[1]
    start = section.rfind(block_start)
    if start < 0:
        return ""
    start += len(block_start)
    if section[start : start + 1] == "\n":
        start += 1
    end = section.find(block_end, start)
    if end < 0:
        return ""
    return section[start:end]


def validate_schedule(lock: dict[str, Any], tenant: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    sched_lock = lock.get("schedule") or {}
    sched = tenant.get("publish_schedule") or {}
    if sched.get("timezone") != sched_lock.get("timezone"):
        errors.append("tenant publish_schedule.timezone != owner-runtime-lock")
    if int(sched.get("runs_per_day") or 0) != int(sched_lock.get("runs_per_day") or 0):
        errors.append(
            f"tenant publish_schedule.runs_per_day={sched.get('runs_per_day')} "
            f"!= lock {sched_lock.get('runs_per_day')}"
        )
    if list(sched.get("slots_local") or []) != list(sched_lock.get("slots_local") or []):
        errors.append("tenant publish_schedule.slots_local != owner-runtime-lock slots")
    if sched.get("weekdays_only") is not True:
        errors.append("tenant publish_schedule.weekdays_only must be true")
    return errors


def validate_writing_model(lock: dict[str, Any], tenant: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    wm_lock = lock.get("writing_model") or {}
    wm = tenant.get("writing_model") or {}
    if wm.get("script") != wm_lock.get("script"):
        errors.append("tenant writing_model.script != owner-runtime-lock")
    if wm.get("contract") != wm_lock.get("contract"):
        errors.append("tenant writing_model.contract != owner-runtime-lock")
    if wm.get("fail_loud_if_unavailable") is not wm_lock.get("fail_loud_if_unavailable"):
        errors.append("tenant writing_model.fail_loud_if_unavailable != owner-runtime-lock")

    powerful_lock = wm_lock.get("powerful") or {}
    powerful = wm.get("powerful") or {}
    model = str(powerful.get("model") or "")
    if model != powerful_lock.get("model"):
        errors.append(f"tenant powerful model {model!r} != lock {powerful_lock.get('model')!r}")
    forbidden = {m.lower() for m in (powerful_lock.get("forbidden_powerful_models") or [])}
    if model.lower() in forbidden or "opus" in model.lower():
        errors.append(f"forbidden powerful model active in tenant: {model}")

    if set(powerful.get("roles") or []) != set(powerful_lock.get("roles") or []):
        errors.append("tenant powerful.roles != owner-runtime-lock")

    utility_lock = wm_lock.get("utility") or {}
    utility = wm.get("utility") or {}
    if str(utility.get("model") or "") != utility_lock.get("model"):
        errors.append("tenant utility model != owner-runtime-lock")
    if set(utility.get("roles") or []) != set(utility_lock.get("roles") or []):
        errors.append("tenant utility.roles != owner-runtime-lock")

    legacy_env = str(powerful_lock.get("legacy_env") or "DEROUTER_OPUS_MODEL")
    legacy_val = os.environ.get(legacy_env, "").strip()
    if legacy_val:
        if "opus" in legacy_val.lower() and "astra" not in legacy_val.lower():
            errors.append(f"{legacy_env}={legacy_val} forbids Opus as active Writer/Sol model")
    powerful_env = os.environ.get(str(powerful_lock.get("model_env") or "DEROUTER_POWERFUL_MODEL"), "").strip()
    if powerful_env:
        if "opus" in powerful_env.lower() and "astra" not in powerful_env.lower():
            errors.append(
                f"{powerful_lock.get('model_env')}={powerful_env} forbids Opus as active Writer/Sol model"
            )
        if powerful_env != powerful_lock.get("model"):
            errors.append(
                f"{powerful_lock.get('model_env')}={powerful_env} != lock {powerful_lock.get('model')}"
            )
    return errors


def validate_pipeline_canon(lock: dict[str, Any], canon: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    qs_lock = lock.get("article_quality_score") or {}
    qs = canon.get("article_quality_score") or {}
    for key in (
        "gate",
        "output",
        "placement",
        "word_count_target_min",
        "word_count_target_max",
        "word_count_hard_max",
        "max_sol_rewrites",
        "repair_flag",
        "required_before_publish",
    ):
        if qs.get(key) != qs_lock.get(key):
            errors.append(f"pipeline-canon article_quality_score.{key} != owner-runtime-lock")
    if qs.get("contract") != qs_lock.get("contract"):
        errors.append("pipeline-canon article_quality_score.contract != owner-runtime-lock")

    qb_lock = lock.get("quality_bar_9") or {}
    qb = canon.get("quality_bar_9") or {}
    if qb.get("gate") != qb_lock.get("gate"):
        errors.append("pipeline-canon quality_bar_9.gate != owner-runtime-lock")
    if qb.get("required_before_publish") is not True:
        errors.append("pipeline-canon quality_bar_9.required_before_publish must be true")

    scout_lock = lock.get("scout") or {}
    scout = canon.get("scout_anti_repeat") or {}
    hard_lock = scout_lock.get("anti_dupe_hard") or {}
    hard = scout.get("anti_dupe_hard") or {}
    if hard.get("enabled") is not hard_lock.get("enabled"):
        errors.append("pipeline-canon scout_anti_repeat.anti_dupe_hard.enabled != owner-runtime-lock")
    if hard.get("gate_script") != hard_lock.get("gate_script"):
        errors.append("pipeline-canon anti_dupe gate_script != owner-runtime-lock")
    if hard.get("fail_before_writer") is not hard_lock.get("fail_before_writer"):
        errors.append("pipeline-canon anti_dupe fail_before_writer != owner-runtime-lock")
    if scout.get("angle_lock_doc") != scout_lock.get("angle_lock_doc"):
        errors.append("pipeline-canon scout angle_lock_doc != owner-runtime-lock")
    return errors


def validate_scout_clusters(lock: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    scout_lock = lock.get("scout") or {}
    hard_lock = scout_lock.get("anti_dupe_hard") or {}
    clusters_path = root / "shared" / "scout-story-clusters.json"
    clusters = _read_json(clusters_path)
    hard = clusters.get("anti_dupe_hard") or {}
    if hard.get("enabled") is not hard_lock.get("enabled"):
        errors.append("scout-story-clusters anti_dupe_hard.enabled != owner-runtime-lock")
    if int(clusters.get("anti_repeat_days") or 0) != int(scout_lock.get("anti_dupe_hard", {}).get("cluster_days") or 30):
        errors.append("scout-story-clusters anti_repeat_days != owner-runtime-lock cluster_days")
    for rel in (
        scout_lock.get("angle_lock_doc"),
        scout_lock.get("newbuild_lock_doc"),
        scout_lock.get("topic_focus_script"),
        hard_lock.get("gate_script"),
        hard_lock.get("helper_script"),
    ):
        if rel and not (root / str(rel)).is_file():
            errors.append(f"scout lock file missing: {rel}")
    return errors


def validate_pipeline_wiring(lock: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    wiring = lock.get("pipeline_wiring") or {}
    qs_gate = lock.get("article_quality_score", {}).get("gate")
    qs_gate_name = Path(str(qs_gate or "")).name
    struct_path = root / str(wiring.get("structure_gate_quality_score") or "")
    if struct_path.is_file():
        body = struct_path.read_text(encoding="utf-8")
        if not qs_gate_name or qs_gate_name not in body:
            errors.append("structure_gate missing quality_score_gate wiring")
    else:
        errors.append("structure_gate script missing")

    publish_path = root / str(wiring.get("wp_publish_quality_score_check") or "")
    if publish_path.is_file():
        body = publish_path.read_text(encoding="utf-8")
        if "article-quality-score.json" not in body:
            errors.append("wp_publish missing article-quality-score.json check")
        if "quality-bar-9.json" not in body:
            errors.append("wp_publish missing quality-bar-9.json check")
        allow_env = (lock.get("publish") or {}).get("allow_publish_env")
        if allow_env and allow_env not in body:
            errors.append(f"wp_publish missing {allow_env} check")
    else:
        errors.append("wp_publish script missing")

    research_path = root / str(wiring.get("research_start_anti_dupe") or "")
    assert_fn = (lock.get("scout") or {}).get("anti_dupe_hard", {}).get("research_start_assert")
    if research_path.is_file():
        body = research_path.read_text(encoding="utf-8")
        if not assert_fn or assert_fn not in body:
            errors.append("research_start missing assert_anti_dupe_hard wiring")
    else:
        errors.append("research_start script missing")
    return errors


def validate_images(lock: dict[str, Any], tenant: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    img_lock = lock.get("images") or {}
    img = tenant.get("image_generation") or {}
    if img.get("provider") != img_lock.get("provider"):
        errors.append("tenant image_generation.provider != owner-runtime-lock")
    if img.get("script") != img_lock.get("script"):
        errors.append("tenant image_generation.script != owner-runtime-lock")
    for forbidden in img_lock.get("forbidden_scripts") or []:
        if (root / str(forbidden)).is_file() and "kie" in str(forbidden).lower():
            # Kie stub may exist as forbidden reference — only fail if tenant points to it
            if img.get("script") == forbidden:
                errors.append(f"tenant image_generation.script forbidden: {forbidden}")
    cover_canon = _read_json(root / "memory/cover/cover-canon.json")
    if cover_canon:
        model_policy = str(cover_canon.get("image_model_tier") or cover_canon.get("model_tier") or "").lower()
        if "vip" in model_policy and "never" not in model_policy:
            errors.append("cover-canon allows VIP image tier")
    grsai_path = root / "scripts/excalibur_blog_grsai_gpt_image2_api.py"
    if grsai_path.is_file():
        grsai = grsai_path.read_text(encoding="utf-8")
        if '"vip_disabled": True' not in grsai and "vip_disabled" not in grsai:
            errors.append("grsai image script missing vip_disabled guard")
    caption = img_lock.get("caption_builder")
    if caption and not (root / str(caption)).is_file():
        errors.append(f"image caption builder missing: {caption}")
    return errors


def validate_automation_instructions(lock: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    ai = lock.get("automation_instructions") or {}
    doc_path = root / str(ai.get("doc") or "CLOUD-AUTOMATION.md")
    if not doc_path.is_file():
        return ["CLOUD-AUTOMATION.md missing"]
    doc = doc_path.read_text(encoding="utf-8")
    block = extract_automation_instructions(
        doc, str(ai.get("block_start") or "```text"), str(ai.get("block_end") or "```")
    )
    if not block.strip():
        errors.append("CLOUD-AUTOMATION automation Instructions block missing")
        return errors
    for marker in ai.get("required_markers") or []:
        if marker not in block:
            errors.append(f"automation Instructions missing marker: {marker!r}")
    for forbidden in ai.get("forbidden_markers") or []:
        if forbidden in block:
            errors.append(f"automation Instructions forbidden marker: {forbidden!r}")
    if "OWNER: re-save" not in doc and "owner must re-save" not in doc.lower():
        errors.append("CLOUD-AUTOMATION missing owner re-save notice for Cursor Automations UI")
    return errors


def validate_forbidden_active_phrases(lock: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    phrases = lock.get("forbidden_active_doc_phrases") or []
    ai = lock.get("automation_instructions") or {}
    automation_doc = str(ai.get("doc") or "CLOUD-AUTOMATION.md")
    automation_exempt: set[str] = set()
    automation_path = root / automation_doc
    if automation_path.is_file():
        automation_body = automation_path.read_text(encoding="utf-8")
        block = extract_automation_instructions(
            automation_body,
            str(ai.get("block_start") or "```text"),
            str(ai.get("block_end") or "```"),
        )
        for phrase in phrases:
            if phrase in block:
                automation_exempt.add(phrase)
    seen: set[str] = set()
    for pattern in lock.get("forbidden_active_doc_globs") or []:
        for path in _glob_paths(root, pattern):
            if not path.is_file():
                continue
            rel = str(path.relative_to(root)).replace("\\", "/")
            if rel.startswith("memory/") or rel.startswith("tests/"):
                continue
            if rel in {"scripts/excalibur_blog_owner_runtime_lock.py", "shared/owner-runtime-lock.json"}:
                continue
            try:
                body = path.read_text(encoding="utf-8")
            except OSError:
                continue
            for phrase in phrases:
                if phrase in automation_exempt and rel == automation_doc:
                    continue
                if phrase in body:
                    key = f"{rel}:{phrase}"
                    if key not in seen:
                        seen.add(key)
                        errors.append(f"forbidden phrase {phrase!r} in {rel}")
    return errors


def validate_owner_runtime_lock(root: Path | None = None) -> list[str]:
    root = root or project_root()
    errors: list[str] = []
    try:
        lock = load_lock(root)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        return [str(exc)]

    lock_path = root / "shared" / "owner-runtime-lock.json"
    if not lock_path.is_file():
        errors.append("shared/owner-runtime-lock.json missing")
        return errors

    tenant = _read_json(root / "shared" / "tenant-config.json")
    canon = _read_json(root / "shared" / "pipeline-canon.json")

    errors.extend(validate_schedule(lock, tenant))
    errors.extend(validate_writing_model(lock, tenant))
    errors.extend(validate_pipeline_canon(lock, canon))
    errors.extend(validate_scout_clusters(lock, root))
    errors.extend(validate_pipeline_wiring(lock, root))
    errors.extend(validate_images(lock, tenant, root))
    errors.extend(validate_automation_instructions(lock, root))
    errors.extend(validate_forbidden_active_phrases(lock, root))

    for rel in (
        lock.get("article_quality_score", {}).get("gate"),
        lock.get("article_quality_score", {}).get("contract"),
        lock.get("scout", {}).get("angle_lock_doc"),
        lock.get("stylo", {}).get("gate"),
    ):
        if rel and not (root / str(rel)).is_file():
            errors.append(f"owner-runtime-lock referenced file missing: {rel}")

    agents = (root / "AGENTS.md").read_text(encoding="utf-8") if (root / "AGENTS.md").is_file() else ""
    if "owner-runtime-lock.json" not in agents:
        errors.append("AGENTS.md missing owner-runtime-lock.json reference")

    return errors


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate repo against owner-runtime-lock.json")
    parser.add_argument("--json", action="store_true", help="Emit JSON report")
    args = parser.parse_args()
    root = project_root()
    errors = validate_owner_runtime_lock(root)
    if args.json:
        print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    else:
        for err in errors:
            print(f"FAIL {err}")
        print(f"SUMMARY errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
