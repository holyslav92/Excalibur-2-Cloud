"""FAIL-CLOSED owner runtime lock drift guard tests."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_owner_runtime_lock import (  # noqa: E402
    extract_automation_instructions,
    load_lock,
    validate_owner_runtime_lock,
    validate_writing_model,
)


class OwnerRuntimeLockTests(unittest.TestCase):
    def test_lock_file_exists_and_has_core_keys(self) -> None:
        lock = load_lock(ROOT)
        self.assertEqual(lock.get("status"), "LOCKED_ON_MAIN")
        self.assertEqual((lock.get("schedule") or {}).get("runs_per_day"), 4)
        self.assertEqual(
            (lock.get("writing_model") or {}).get("powerful", {}).get("model"),
            "gpt-6-astra",
        )
        self.assertTrue((lock.get("scout") or {}).get("anti_dupe_hard", {}).get("enabled"))
        self.assertEqual(
            (lock.get("article_quality_score") or {}).get("word_count_hard_max"),
            1750,
        )

    def test_repo_passes_owner_runtime_lock(self) -> None:
        errors = validate_owner_runtime_lock(ROOT)
        self.assertEqual(errors, [], "\n".join(errors))

    def test_doctor_integrates_lock_validator(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_doctor.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("owner-runtime-lock drift guard", proc.stdout)

    def test_owner_runtime_lock_cli_passes(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_owner_runtime_lock.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)

    def test_automation_instructions_block_has_markers(self) -> None:
        lock = load_lock(ROOT)
        ai = lock["automation_instructions"]
        doc = (ROOT / "CLOUD-AUTOMATION.md").read_text(encoding="utf-8")
        block = extract_automation_instructions(doc, ai["block_start"], ai["block_end"])
        for marker in ai["required_markers"]:
            self.assertIn(marker, block, marker)
        for forbidden in ai["forbidden_markers"]:
            self.assertNotIn(forbidden, block, forbidden)

    def test_tenant_schedule_four_slots(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        sched = tenant["publish_schedule"]
        self.assertEqual(sched["runs_per_day"], 4)
        self.assertEqual(sched["slots_local"], ["09:00", "12:00", "15:00", "17:00"])

    def test_forbidden_opus_model_in_tenant_fails(self) -> None:
        lock = load_lock(ROOT)
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        bad = json.loads(json.dumps(tenant))
        bad["writing_model"]["powerful"]["model"] = "claude-opus-5"
        errors = validate_writing_model(lock, bad)
        self.assertTrue(any("forbidden" in e or "gpt-6-astra" in e for e in errors))

    def test_forbidden_opus_env_fails(self) -> None:
        lock = load_lock(ROOT)
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        with mock.patch.dict(os.environ, {"DEROUTER_POWERFUL_MODEL": "claude-opus-5"}, clear=False):
            errors = validate_writing_model(lock, tenant)
        self.assertTrue(any("Opus" in e for e in errors))

    def test_drift_two_slots_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in ("shared", "scripts", "memory/cover", "agents", "skills"):
                (root / rel).mkdir(parents=True)
            for src in (
                "shared/owner-runtime-lock.json",
                "shared/tenant-config.json",
                "shared/pipeline-canon.json",
                "shared/scout-story-clusters.json",
                "shared/dzen-top-angle-newbuild-lock.md",
                "shared/newbuild-focus-lock.md",
                "scripts/excalibur_blog_structure_gate.py",
                "scripts/excalibur_blog_wp_publish.py",
                "scripts/excalibur_blog_research_start.py",
                "scripts/excalibur_blog_grsai_gpt_image2_api.py",
                "scripts/excalibur_blog_image_caption_builder.py",
                "scripts/excalibur_blog_topic_focus.py",
                "scripts/excalibur_blog_scout_story_dup.py",
                "scripts/excalibur_blog_scout_helper.py",
                "scripts/excalibur_blog_stylo.py",
                "scripts/excalibur_blog_quality_score_gate.py",
                "shared/article-quality-score-lock.md",
                "AGENTS.md",
                "CLOUD-AUTOMATION.md",
            ):
                src_path = ROOT / src
                dst_path = root / src
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                dst_path.write_text(src_path.read_text(encoding="utf-8"), encoding="utf-8")
            tenant = json.loads((root / "shared/tenant-config.json").read_text(encoding="utf-8"))
            tenant["publish_schedule"]["runs_per_day"] = 2
            tenant["publish_schedule"]["slots_local"] = ["09:00", "17:00"]
            (root / "shared/tenant-config.json").write_text(
                json.dumps(tenant, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            (root / "memory/cover/cover-canon.json").write_text(
                '{"image_model_tier":"standard_only"}\n',
                encoding="utf-8",
            )
            errors = validate_owner_runtime_lock(root)
            self.assertTrue(any("runs_per_day" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
