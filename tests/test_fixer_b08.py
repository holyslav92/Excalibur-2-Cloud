"""Regression tests for B08 fixer: cover regen prompts + image API blockers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_cover_quad_prompt import strip_wordstat_from_style_prefix
from excalibur_blog_derouter_gpt_image2_api import (
    format_derouter_http_error,
    is_derouter_model_terminal_error,
)
from excalibur_blog_kie_gpt_image2_api import is_kie_credits_exhausted, kie_blocker_message
from excalibur_blog_quad_slots import apply_quad_canon_to_manifest


class CoverPromptWordstatStripTest(unittest.TestCase):
    def test_strip_wordstat_from_style_prefix(self) -> None:
        raw = (
            "High-key bright RU editorial collage. "
            "1-3 Wordstat stickers (Тюмень). Meme cat/people cutouts."
        )
        out = strip_wordstat_from_style_prefix(raw)
        self.assertNotIn("Wordstat stickers (Тюмень)", out)
        self.assertIn("NO Wordstat query strips", out)

    def test_apply_quad_canon_sets_wordstat_pil_only(self) -> None:
        manifest = {"inline_count": 7, "slots": {"cover": {}}}
        apply_quad_canon_to_manifest(manifest)
        self.assertTrue(manifest.get("wordstat_pil_only"))


class DerouterDiscontinuedTest(unittest.TestCase):
    def test_discontinued_400_is_terminal(self) -> None:
        body = '{"error":{"message":"model gpt-image-1 is discontinued"}}'
        self.assertTrue(is_derouter_model_terminal_error(400, body))

    def test_format_discontinued_hint(self) -> None:
        msg = format_derouter_http_error(400, "model discontinued")
        self.assertIn("DEROUTER_IMAGE_MODEL", msg)


class KieCreditsTest(unittest.TestCase):
    def test_402_is_credits(self) -> None:
        self.assertTrue(is_kie_credits_exhausted(status=402, message=""))

    def test_blocker_message_credits(self) -> None:
        msg = kie_blocker_message(Exception("Kie API HTTP 402: insufficient credits"))
        self.assertIn("KIE CREDITS BLOCKER", msg)


if __name__ == "__main__":
    unittest.main()
