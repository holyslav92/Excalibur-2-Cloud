"""Tests for cover motif anti-repeat and Wordstat gates."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CoverMotifGateTest(unittest.TestCase):
    def test_doctor_on_repo_log(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_cover_motif_gate.py"), "doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_collision_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory/cover").mkdir(parents=True)
            (root / "memory/cover/cover-canon.json").write_text("{}", encoding="utf-8")
            log = {
                "schema_version": 1,
                "window_days": 14,
                "entries": [
                    {
                        "date": "2026-08-17",
                        "topic_id": "B100",
                        "motifs": {"location": "лестничная клетка подъезда"},
                    }
                ],
            }
            (root / "memory/cover/used-motifs.json").write_text(
                json.dumps(log, ensure_ascii=False), encoding="utf-8"
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(root)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_cover_motif_gate.py"),
                    "check",
                    "--topic-id",
                    "B101",
                    "--location",
                    "лестничная клетка подъезда",
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertIn("COLLISION", proc.stderr)


class WordstatGateTest(unittest.TestCase):
    def test_geo_doctor(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"), "doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_handoff_rejects_skip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            handoff = Path(tmp) / "handoff.md"
            handoff.write_text(
                "=== SCOUT ===\nwordstat: skip\n",
                encoding="utf-8",
            )
            env = {
                "WORDSTAT_API_KEY": "test",
                "WORDSTAT_FOLDER_ID": "folder",
            }
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"),
                    "handoff",
                    "--handoff",
                    str(handoff),
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1)
            self.assertIn("skip", proc.stderr.lower())

    def test_scout_skill_hard_gate(self) -> None:
        s = (ROOT / "skills/scout-excalibur-blog/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("HARD GATE", s)
        self.assertIn("11176", s)
        self.assertNotIn("не blocker", s.lower())

    def test_cover_canon_rejects_daypart(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertTrue(canon["forbidden_daypart_formula"]["never_use"])


if __name__ == "__main__":
    unittest.main()
