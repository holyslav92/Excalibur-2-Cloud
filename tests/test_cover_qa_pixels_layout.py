"""Regression: pixel Cover-QA must FAIL owner live broken covers + collapsed B07."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_cover_qa_pixels import _ocr_runtime_available  # noqa: E402
FAIL_MD5 = "23051a017f8e9251d5435a09232e8313"
FAIL_FIXTURE = ROOT / "tests/fixtures/cover-b07-fail-23051a01.png"
ZAGS_FAIL = ROOT / "tests/fixtures/cover-fail-zags-adbb30d1.png"
ZAGS_FAIL_MD5 = "adbb30d185c911094e9a80a3d0b77963"
IPOTEKA_FAIL = ROOT / "tests/fixtures/cover-fail-ipoteka-a519f93f.png"
IPOTEKA_FAIL_MD5 = "a519f93fde507b73e715c4b4ccc3f424"
MASHUP_B08 = ROOT / "tests/fixtures/cover-fail-mashup-b08-80aebe7c.png"
MASHUP_B08_MD5 = "80aebe7cc0b5228a41863531e4c9891e"
MASHUP_B09 = ROOT / "tests/fixtures/cover-fail-mashup-b09-e0824319.png"
MASHUP_B09_MD5 = "e08243196b07b1461f15d94d1a0d8de9"
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

    def _run_pixels(self, cover: Path, *, article_dir: Path | None = None) -> dict:
        cmd = [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_cover_qa_pixels.py"),
            "--cover",
            str(cover),
        ]
        if article_dir is not None:
            cmd.extend(["--article-dir", str(article_dir)])
        proc = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        payload = proc.stdout.strip() or proc.stderr.strip()
        self.assertTrue(payload.startswith("{"), proc.stderr or proc.stdout)
        data = json.loads(payload)
        self.assertEqual(proc.returncode, 1 if data["status"] == "FAIL" else 0, proc.stderr or proc.stdout)
        return data

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
        self.assertFalse(checks.get("pixel_layout_not_collapsed"))
        self.assertFalse(checks.get("pixel_designed_thumbnail"))

    def test_zags_live_fail_cover_blocked(self) -> None:
        if not ZAGS_FAIL.is_file():
            raise unittest.SkipTest(f"missing {ZAGS_FAIL}")
        proc = subprocess.run(["md5sum", str(ZAGS_FAIL)], capture_output=True, text=True, check=True)
        self.assertIn(ZAGS_FAIL_MD5, proc.stdout)
        data = self._run_pixels(ZAGS_FAIL)
        self.assertEqual(data["status"], "FAIL")
        checks = data["checks"]
        if _ocr_runtime_available():
            self.assertFalse(checks.get("pixel_hook_title_cyrillic"))
            self.assertFalse(checks.get("pixel_no_blank_sticky_notes"))
        else:
            self.assertFalse(checks.get("pixel_no_collage_inset"))
        self.assertTrue(checks.get("pixel_host_face_present"))

    def test_ipoteka_services_card_fail_cover_blocked(self) -> None:
        if not IPOTEKA_FAIL.is_file():
            raise unittest.SkipTest(f"missing {IPOTEKA_FAIL}")
        proc = subprocess.run(["md5sum", str(IPOTEKA_FAIL)], capture_output=True, text=True, check=True)
        self.assertIn(IPOTEKA_FAIL_MD5, proc.stdout)
        data = self._run_pixels(IPOTEKA_FAIL)
        self.assertEqual(data["status"], "FAIL")
        checks = data["checks"]
        self.assertFalse(checks.get("pixel_host_face_present"))
        self.assertFalse(checks.get("pixel_not_services_checklist"))
        self.assertFalse(checks.get("pixel_phone_readable"))
        self.assertFalse(checks.get("pixel_meme_present"))

    def test_mashup_b08_pil_template_blocked(self) -> None:
        if not MASHUP_B08.is_file():
            raise unittest.SkipTest(f"missing {MASHUP_B08}")
        proc = subprocess.run(["md5sum", str(MASHUP_B08)], capture_output=True, text=True, check=True)
        self.assertIn(MASHUP_B08_MD5, proc.stdout)
        data = self._run_pixels(MASHUP_B08)
        self.assertEqual(data["status"], "FAIL")
        checks = data["checks"]
        if _ocr_runtime_available():
            self.assertFalse(checks.get("pixel_no_foreign_article_text"))
            self.assertFalse(checks.get("pixel_phone_not_clipped"))
        self.assertFalse(checks.get("pixel_no_collage_inset"))
        self.assertFalse(checks.get("pixel_designed_thumbnail"))

    def test_mashup_b09_pil_template_blocked(self) -> None:
        if not MASHUP_B09.is_file():
            raise unittest.SkipTest(f"missing {MASHUP_B09}")
        proc = subprocess.run(["md5sum", str(MASHUP_B09)], capture_output=True, text=True, check=True)
        self.assertIn(MASHUP_B09_MD5, proc.stdout)
        data = self._run_pixels(MASHUP_B09)
        self.assertEqual(data["status"], "FAIL")
        checks = data["checks"]
        if _ocr_runtime_available():
            self.assertFalse(checks.get("pixel_no_foreign_article_text"))
            self.assertFalse(checks.get("pixel_phone_not_clipped"))
        self.assertFalse(checks.get("pixel_no_collage_inset"))
        self.assertFalse(checks.get("pixel_designed_thumbnail"))

    def test_mashup_b08_hook_truncation_with_manifest(self) -> None:
        if not MASHUP_B08.is_file():
            raise unittest.SkipTest(f"missing {MASHUP_B08}")
        if not _ocr_runtime_available():
            raise unittest.SkipTest("tesseract unavailable — truncation gate needs OCR")
        data = self._run_pixels(MASHUP_B08, article_dir=ROOT / "tests/fixtures/cover-qa-b08")
        self.assertFalse(data["checks"].get("pixel_hook_title_not_truncated"))

    def test_mashup_b09_hook_truncation_with_manifest(self) -> None:
        if not MASHUP_B09.is_file():
            raise unittest.SkipTest(f"missing {MASHUP_B09}")
        if not _ocr_runtime_available():
            raise unittest.SkipTest("tesseract unavailable — truncation gate needs OCR")
        data = self._run_pixels(MASHUP_B09, article_dir=ROOT / "tests/fixtures/cover-qa-b09")
        self.assertFalse(data["checks"].get("pixel_hook_title_not_truncated"))

    def test_b06_reference_cover_passes_core_gates(self) -> None:
        self.assertTrue(B06_COVER.is_file(), f"missing {B06_COVER}")
        b06_dir = B06_COVER.parents[1]
        data = self._run_pixels(B06_COVER, article_dir=b06_dir)
        self.assertTrue(data["checks"].get("pixel_hook_title_present"))
        self.assertTrue(data["checks"].get("pixel_hook_title_cyrillic"))
        self.assertTrue(data["checks"].get("pixel_host_face_present"))
        self.assertTrue(data["checks"].get("pixel_phone_readable"))
        self.assertTrue(data["checks"].get("pixel_meme_present"))

    def test_b07_overlap_fixture_fails_query_strips(self) -> None:
        overlap_fixture = ROOT / "tests/fixtures/cover-b07-overlap-b2cb443e.png"
        if not overlap_fixture.is_file():
            raise unittest.SkipTest(f"missing {overlap_fixture}")
        data = self._run_pixels(overlap_fixture)
        self.assertEqual(data["status"], "FAIL")
        self.assertFalse(data["checks"].get("pixel_no_wordstat_query_strips"))


if __name__ == "__main__":
    unittest.main()
