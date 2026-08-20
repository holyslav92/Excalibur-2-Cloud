"""Tests for spend circuit breaker (no wall-clock kill)."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BudgetGuardTest(unittest.TestCase):
    def test_tenant_run_budget_caps(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        rb = tenant.get("run_budget")
        self.assertIsInstance(rb, dict)
        self.assertEqual(rb.get("cover_qa_image_attempts_max"), 2)
        self.assertEqual(rb.get("derouter_image_jobs_max"), 3)
        self.assertEqual(rb.get("derouter_chat_retries_per_call_max"), 1)
        self.assertEqual(rb.get("kie_image_fallback_max"), 1)
        self.assertEqual(rb.get("wall_clock_soft_note_minutes"), 60)
        self.assertNotIn("wall_clock_max_minutes", rb)

    def test_doctor(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_budget_guard.py"), "--doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_image_jobs_cap(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_budget_guard import (
            BudgetBlocker,
            assert_image_job_allowed,
            ensure_run_started,
            record_image_job,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared/tenant-config.json").write_text(
                json.dumps(
                    {
                        "run_budget": {
                            "derouter_image_jobs_max": 2,
                            "cover_qa_image_attempts_max": 2,
                            "kie_image_fallback_max": 1,
                            "derouter_chat_retries_per_call_max": 1,
                            "wall_clock_soft_note_minutes": 60,
                        }
                    }
                ),
                encoding="utf-8",
            )
            article = root / "memory/blog/articles/B99-test"
            article.mkdir(parents=True)
            ensure_run_started(article, root)
            assert_image_job_allowed(article, root)
            record_image_job(article, root)
            assert_image_job_allowed(article, root)
            record_image_job(article, root)
            with self.assertRaises(BudgetBlocker) as ctx:
                assert_image_job_allowed(article, root)
            self.assertIn("derouter_image_jobs", str(ctx.exception))

    def test_cover_qa_two_rounds_max(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_budget_guard import (
            BudgetBlocker,
            ensure_run_started,
            record_cover_image_round,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared/tenant-config.json").write_text(
                json.dumps({"run_budget": {"cover_qa_image_attempts_max": 2}}),
                encoding="utf-8",
            )
            article = root / "memory/blog/articles/B99-test"
            article.mkdir(parents=True)
            ensure_run_started(article, root)
            record_cover_image_round(article, root, "initial")
            record_cover_image_round(article, root, "panel_regen")
            with self.assertRaises(BudgetBlocker) as ctx:
                record_cover_image_round(article, root, "panel_regen")
            self.assertIn("cover_qa_rounds", str(ctx.exception))

    def test_kie_fallback_once(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_budget_guard import (
            BudgetBlocker,
            assert_kie_fallback_allowed,
            ensure_run_started,
            record_kie_fallback,
        )

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared/tenant-config.json").write_text(
                json.dumps({"run_budget": {"kie_image_fallback_max": 1}}),
                encoding="utf-8",
            )
            article = root / "memory/blog/articles/B99-test"
            article.mkdir(parents=True)
            ensure_run_started(article, root)
            record_kie_fallback(article, root)
            with self.assertRaises(BudgetBlocker):
                assert_kie_fallback_allowed(article, root)

    def test_no_wall_clock_blocker(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_budget_guard import (
            ensure_run_started,
            load_stamp,
            refresh_soft_wall_note,
        )
        from datetime import datetime, timedelta, timezone

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared/tenant-config.json").write_text(
                json.dumps({"run_budget": {"wall_clock_soft_note_minutes": 60}}),
                encoding="utf-8",
            )
            article = root / "memory/blog/articles/B99-test"
            article.mkdir(parents=True)
            stamp = ensure_run_started(article, root)
            old = (datetime.now(timezone.utc) - timedelta(hours=2)).isoformat()
            stamp["started_at"] = old
            from excalibur_blog_budget_guard import save_stamp

            save_stamp(article, stamp)
            refresh_soft_wall_note(article, root)
            stamp2 = load_stamp(article)
            self.assertIsNone(stamp2.get("blocked"))
            self.assertTrue(any("wall_clock_soft" in str(n) for n in stamp2.get("notes") or []))


if __name__ == "__main__":
    unittest.main()
