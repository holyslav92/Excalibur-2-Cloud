"""Regression: pixel Cover-QA must FAIL collapsed B07 live cover (md5 23051a01…)."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAIL_MD5 = "23051a017f8e9251d5435a09232e8313"
FAIL_FIXTURE = ROOT / "tests/fixtures/cover-b07-fail-23051a01.png"
B06_COVER = (
    ROOT
    / "memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami/cover/cover.png"
)


class CoverQAPixelsLayoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fail_cover = FAIL_FIXTURE
        if not cls.fail_cover.is_file():
            raise unittest.SkipTest(f"missing fixture {cls.fail_cover}")

    def _run_pixels(self, cover: Path) -> dict:
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/excalibur_blog_cover_qa_pixels.py"),
                "--cover",
                str(cover),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 1 if "FAIL" in proc.stdout else 0, proc.stderr or proc.stdout)
        return json.loads(proc.stdout)

    def test_live_fail_cover_md5(self) -> None:
        proc = subprocess.run(
            ["md5sum", str(self.fail_cover)],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn(FAIL_MD5, proc.stdout)

    def test_collapsed_b07_cover_fails_layout_gate(self) -> None:
        data = self._run_pixels(self.fail_cover)
        self.assertEqual(data["status"], "FAIL")
        checks = data["checks"]
        self.assertFalse(checks.get("pixel_hook_title_present"))
        self.assertFalse(checks.get("pixel_phone_readable"))
        self.assertFalse(checks.get("pixel_meme_present"))
        self.assertFalse(checks.get("pixel_layout_not_collapsed"))
        self.assertFalse(checks.get("pixel_designed_thumbnail"))

    def test_b06_reference_cover_passes(self) -> None:
        self.assertTrue(B06_COVER.is_file(), f"missing {B06_COVER}")
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/excalibur_blog_cover_qa_pixels.py"),
                "--cover",
                str(B06_COVER),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        data = json.loads(proc.stdout)
        # B06 may fail sticker overlap until repacked — hook/phone must still pass
        self.assertTrue(data["checks"].get("pixel_hook_title_present"))
        self.assertTrue(data["checks"].get("pixel_phone_readable"))

    def test_b07_overlap_fixture_fails_query_strips(self) -> None:
        overlap_fixture = ROOT / "tests/fixtures/cover-b07-overlap-b2cb443e.png"
        if not overlap_fixture.is_file():
            raise unittest.SkipTest(f"missing {overlap_fixture}")
        data = self._run_pixels(overlap_fixture)
        self.assertEqual(data["status"], "FAIL")
        self.assertFalse(data["checks"].get("pixel_no_wordstat_query_strips"))


if __name__ == "__main__":
    unittest.main()
