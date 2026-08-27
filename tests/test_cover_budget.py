"""Tests for cover budget + short-hook helpers + OCR escape hatch."""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class CoverBudgetTest(unittest.TestCase):
    def test_default_max_attempts_is_two(self) -> None:
        from excalibur_blog_cover_budget import DEFAULT_COVER_MAX_ATTEMPTS, resolve_cover_max_attempts

        self.assertEqual(DEFAULT_COVER_MAX_ATTEMPTS, 2)
        old = os.environ.pop("EXCALIBUR_COVER_MAX_ATTEMPTS", None)
        try:
            self.assertEqual(resolve_cover_max_attempts(), 2)
            self.assertEqual(resolve_cover_max_attempts(5), 5)
            os.environ["EXCALIBUR_COVER_MAX_ATTEMPTS"] = "3"
            self.assertEqual(resolve_cover_max_attempts(), 3)
        finally:
            if old is not None:
                os.environ["EXCALIBUR_COVER_MAX_ATTEMPTS"] = old
            else:
                os.environ.pop("EXCALIBUR_COVER_MAX_ATTEMPTS", None)

    def test_short_hook_pass_b08_style(self) -> None:
        from excalibur_blog_cover_budget import validate_short_hook

        verdict = validate_short_hook("Справка ЗАГС чистая — банк отказал")
        self.assertEqual(verdict["status"], "PASS")
        self.assertGreaterEqual(verdict["word_count"], 4)

    def test_short_hook_blocks_novel(self) -> None:
        from excalibur_blog_cover_budget import validate_short_hook

        long_hook = " ".join(["слово"] * 10)
        verdict = validate_short_hook(long_hook)
        self.assertEqual(verdict["status"], "BLOCK")
        self.assertTrue(any("words" in e for e in verdict["errors"]))

    def test_short_hook_blocks_multiline(self) -> None:
        from excalibur_blog_cover_budget import validate_short_hook

        verdict = validate_short_hook("первая строка\nвторая строка")
        self.assertEqual(verdict["status"], "BLOCK")

    def test_generate_image_accepts_ref_path_kwarg(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import generate_image
        import inspect

        params = inspect.signature(generate_image).parameters
        self.assertIn("ref_path", params)


class OcrEscapeHatchTest(unittest.TestCase):
    def test_escape_overrides_only_flaky_checks(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {key: True for key in (
            "pixel_host_face_present",
            "pixel_host_close_up",
            "pixel_hook_title_present",
            "pixel_hook_title_cyrillic",
            "pixel_phone_readable",
            "pixel_meme_present",
            "pixel_layout_not_collapsed",
            "pixel_no_collage_inset",
            "pixel_no_foreign_article_text",
            "pixel_no_wordstat_query_strips",
            "pixel_not_services_checklist",
            "pixel_no_text_on_clothing",
            "pixel_light_high_key",
        )}
        checks["pixel_hook_title_not_truncated"] = False
        checks["pixel_wordstat_not_opaque_bars"] = False
        errors = [
            "pixel_hook_title_not_truncated FAIL: truncated=True",
            "pixel_wordstat_not_opaque_bars FAIL: 1 horizontal opaque bar(s)",
        ]
        evidence: dict = {}
        new_checks, new_errors, new_evidence = apply_ocr_false_positive_escape(
            checks, errors, evidence
        )
        self.assertTrue(new_checks["pixel_hook_title_not_truncated"])
        self.assertTrue(new_checks["pixel_wordstat_not_opaque_bars"])
        self.assertTrue(new_evidence.get("ocr_false_positive_escape", {}).get("applied"))
        self.assertTrue(any("ocr_false_positive_escape PASS" in e for e in new_errors))

    def test_escape_does_not_override_hard_fail(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {
            "pixel_host_face_present": False,
            "pixel_hook_title_not_truncated": False,
        }
        errors = ["pixel_host_face_present FAIL", "pixel_hook_title_not_truncated FAIL"]
        new_checks, _, new_evidence = apply_ocr_false_positive_escape(checks, errors, {})
        self.assertFalse(new_checks["pixel_host_face_present"])
        self.assertNotIn("ocr_false_positive_escape", new_evidence)

    def test_paper_collage_hook_escape_overrides_present_when_bands_ok(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_paper_collage_hook_escape

        checks = {
            "pixel_host_face_present": True,
            "pixel_host_close_up": True,
            "pixel_phone_readable": True,
            "pixel_layout_not_collapsed": True,
            "pixel_hook_title_present": False,
            "pixel_hook_title_cyrillic": False,
        }
        evidence = {
            "hook_title": {
                "bands": [{"rows": 14}],
                "ink_outside_face": 120,
            },
            "title_cyrillic": {"cyrillic_ratio": 0.42},
        }
        errors = ["pixel_hook_title_present FAIL: no large readable hook title"]
        new_checks, new_errors, new_evidence = apply_paper_collage_hook_escape(
            checks, errors, evidence
        )
        self.assertTrue(new_checks["pixel_hook_title_present"])
        self.assertTrue(new_checks["pixel_hook_title_cyrillic"])
        self.assertTrue(new_evidence.get("paper_collage_hook_escape", {}).get("applied"))


if __name__ == "__main__":
    unittest.main()
