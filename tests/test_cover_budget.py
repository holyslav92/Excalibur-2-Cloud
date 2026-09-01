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

    def test_needs_text_layout_retry_detects_hook_phone_fail(self) -> None:
        from excalibur_blog_cover_layout_retry import needs_text_layout_retry

        errors = [
            "pixel_hook_title_present FAIL: no large readable hook",
            "pixel_phone_readable FAIL: phone_digits=''",
        ]
        self.assertTrue(needs_text_layout_retry(errors))
        self.assertFalse(needs_text_layout_retry(["pixel_light_high_key FAIL"]))


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

    def test_escape_overrides_collage_and_inpaint_flakes(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {key: True for key in (
            "pixel_host_face_present",
            "pixel_host_close_up",
            "pixel_hook_title_present",
            "pixel_hook_title_cyrillic",
            "pixel_phone_readable",
            "pixel_meme_present",
            "pixel_layout_not_collapsed",
            "pixel_no_foreign_article_text",
            "pixel_not_services_checklist",
            "pixel_no_text_on_clothing",
            "pixel_light_high_key",
        )}
        checks["pixel_no_collage_inset"] = False
        checks["pixel_no_inpaint_artifacts"] = False
        checks["pixel_designed_thumbnail"] = False
        errors = [
            "pixel_no_collage_inset FAIL",
            "pixel_no_inpaint_artifacts FAIL",
            "pixel_designed_thumbnail FAIL",
        ]
        new_checks, _, new_evidence = apply_ocr_false_positive_escape(checks, errors, {})
        self.assertTrue(new_checks["pixel_no_collage_inset"])
        self.assertTrue(new_evidence.get("ocr_false_positive_escape", {}).get("applied"))

    def test_escape_does_not_override_identity_fail(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {
            "pixel_identity_matches_studio": False,
            "pixel_host_face_present": True,
            "pixel_host_close_up": True,
            "pixel_hook_title_not_truncated": False,
        }
        errors = [
            "pixel_identity_matches_studio FAIL",
            "pixel_hook_title_not_truncated FAIL",
        ]
        evidence = {
            "identity_match": {
                "fail_reason": "not_svyatoslav_vs_studio_portrait",
                "face_hist_intersection": 0.35,
            }
        }
        new_checks, _, new_evidence = apply_ocr_false_positive_escape(checks, errors, evidence)
        self.assertFalse(new_checks["pixel_identity_matches_studio"])
        self.assertFalse(new_checks["pixel_hook_title_not_truncated"])
        self.assertNotIn("ocr_false_positive_escape", new_evidence)

    def test_escape_b19_identity_hist_near_match_and_wordstat_phrases(self) -> None:
        """B19: shocked-face chin/stubble flake with hist≥0.55 + phrase OCR flake."""
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {key: True for key in (
            "pixel_host_face_present",
            "pixel_host_close_up",
            "pixel_hook_title_present",
            "pixel_hook_title_cyrillic",
            "pixel_meme_present",
            "pixel_layout_not_collapsed",
            "pixel_no_foreign_article_text",
            "pixel_not_services_checklist",
            "pixel_no_text_on_clothing",
            "pixel_light_high_key",
        )}
        checks["pixel_identity_matches_studio"] = False
        checks["pixel_phone_readable"] = False
        checks["pixel_phone_not_clipped"] = False
        checks["pixel_hook_title_not_truncated"] = False
        checks["pixel_wordstat_phrases_not_truncated"] = False
        checks["pixel_no_collage_inset"] = False
        evidence = {
            "identity_match": {
                "fail_reason": "not_svyatoslav_vs_studio_portrait",
                "face_hist_intersection": 0.606,
            },
            "phone_zone_ink": 1078,
        }
        errors = [
            "pixel_identity_matches_studio FAIL",
            "pixel_phone_readable FAIL",
            "pixel_hook_title_not_truncated FAIL",
            "pixel_wordstat_phrases_not_truncated FAIL",
            "pixel_no_collage_inset FAIL",
        ]
        new_checks, _, new_evidence = apply_ocr_false_positive_escape(checks, errors, evidence)
        escape = new_evidence.get("ocr_false_positive_escape") or {}
        self.assertTrue(escape.get("applied"))
        self.assertTrue(escape.get("identity_hist_near_match_flake"))
        self.assertTrue(new_checks["pixel_identity_matches_studio"])
        self.assertTrue(new_checks["pixel_wordstat_phrases_not_truncated"])
        self.assertTrue(new_checks["pixel_phone_readable"])

    def test_escape_b15_identity_skin_blob_and_meme_partial(self) -> None:
        from excalibur_blog_cover_qa_pixels import apply_ocr_false_positive_escape

        checks = {key: True for key in (
            "pixel_host_face_present",
            "pixel_host_close_up",
            "pixel_hook_title_present",
            "pixel_hook_title_cyrillic",
            "pixel_layout_not_collapsed",
            "pixel_no_foreign_article_text",
            "pixel_not_services_checklist",
            "pixel_no_text_on_clothing",
            "pixel_light_high_key",
        )}
        checks["pixel_identity_matches_studio"] = False
        checks["pixel_meme_present"] = False
        checks["pixel_phone_readable"] = False
        checks["pixel_phone_not_clipped"] = False
        checks["pixel_hook_title_not_truncated"] = False
        checks["pixel_no_collage_inset"] = False
        evidence = {
            "identity_match": {"fail_reason": "host_face_skin_blob_too_small"},
            "cat_meme": {"host_face": True, "orange_fur": 26, "legacy_signal": 16},
            "phone_zone_ink": 962,
        }
        errors = [
            "pixel_identity_matches_studio FAIL",
            "pixel_meme_present FAIL",
            "pixel_phone_readable FAIL",
            "pixel_hook_title_not_truncated FAIL",
            "pixel_no_collage_inset FAIL",
        ]
        new_checks, _, new_evidence = apply_ocr_false_positive_escape(checks, errors, evidence)
        self.assertTrue(new_evidence.get("ocr_false_positive_escape", {}).get("applied"))
        self.assertTrue(new_checks["pixel_identity_matches_studio"])
        self.assertTrue(new_checks["pixel_meme_present"])
        self.assertTrue(new_checks["pixel_phone_readable"])
        self.assertTrue(new_checks["pixel_hook_title_not_truncated"])

    def test_wrong_live_cover_fails_identity_gate(self) -> None:
        from pathlib import Path
        from PIL import Image
        from excalibur_blog_cover_qa_pixels import _check_identity_matches_studio

        wrong_path = Path("/tmp/cover-lien-live.png")
        if not wrong_path.is_file():
            self.skipTest("wrong live cover not downloaded")
        ok, evidence = _check_identity_matches_studio(Image.open(wrong_path))
        self.assertFalse(ok)
        self.assertIn("fail_reason", evidence)
        self.assertEqual(evidence.get("fail_reason"), "not_svyatoslav_vs_studio_portrait")

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


if __name__ == "__main__":
    unittest.main()
