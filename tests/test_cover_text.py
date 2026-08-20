"""Guard cover-text gate and prompt TEXT LOCK (no overlay: network draws text)."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CoverTextTest(unittest.TestCase):
    def test_gate_pass_on_clear_russian_strings(self) -> None:
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_text_gate import validate_cover_text

        verdict = validate_cover_text(
            {
                "hook": "Cursor стал дешевле на треть",
                "highlight": "дешевле",
                "sticky": "новой модели нет",
                "inline_labels": {
                    "inline_1": ["заявление 3 августа", "минус 20–30%", "без новой модели"],
                    "inline_2": ["с экраном", "без экрана", "до 80%"],
                    "inline_3": ["MCP", "навыки", "экран"],
                },
            },
            inline_count=3,
        )
        self.assertEqual(verdict["status"], "PASS")

    def test_gate_blocks_english_headline(self) -> None:
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_text_gate import validate_cover_text

        verdict = validate_cover_text(
            {
                "hook": "Token burn rate",
                "highlight": "burn",
                "sticky": "",
                "inline_labels": {
                    "inline_1": ["токены", "экран"],
                    "inline_2": ["токены", "экран"],
                    "inline_3": ["токены", "экран"],
                },
            },
            inline_count=3,
        )
        self.assertEqual(verdict["status"], "BLOCK")
        self.assertTrue(any("Latin words" in e for e in verdict["errors"]))

    def test_gate_blocks_highlight_outside_hook(self) -> None:
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_text_gate import validate_cover_text

        verdict = validate_cover_text(
            {
                "hook": "Cursor стал дешевле на треть",
                "highlight": "бюджет",
                "sticky": "",
                "inline_labels": {
                    "inline_1": ["токены", "экран"],
                    "inline_2": ["токены", "экран"],
                    "inline_3": ["токены", "экран"],
                },
            },
            inline_count=3,
        )
        self.assertEqual(verdict["status"], "BLOCK")

    def test_prompt_has_text_lock_and_russian_hook(self) -> None:
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_quad_prompt import build_solo_cover_collage_prompt

        manifest = {
            "cover_hook": "Cursor стал дешевле на треть",
            "cover_hook_highlight": "дешевле",
            "wordstat_stickers": ["купить квартиру в тюмени"],
            "slots": {
                "cover": {
                    "scene_hint": "side-eye at receipt",
                    "sticky": "новой модели нет",
                    "cover_emotion": "bewildered shock",
                },
            },
        }
        style = {
            "global_prompt_prefix": "Host LARGE left = same 28yo man i2i face-studio-2026-06-23"
        }
        prompt = build_solo_cover_collage_prompt(manifest, style, {})
        self.assertIn("TEXT LANGUAGE LOCK", prompt)
        self.assertIn("«Cursor стал дешевле на треть»", prompt)
        self.assertIn("Host i2i LARGE LEFT", prompt)
        self.assertIn("«новой модели нет»", prompt)
        self.assertIn("NOT a 2x2 grid", prompt)
        self.assertNotIn("PHOTO ONLY", prompt)

    def test_overlay_script_removed(self) -> None:
        self.assertFalse(
            (ROOT / "scripts/excalibur_blog_cover_text_overlay.py").exists(),
            "banner overlay was rejected by user — network must draw the text",
        )
        apply_src = (ROOT / "scripts/excalibur_blog_quad_apply.py").read_text(encoding="utf-8")
        self.assertNotIn("cover_text_overlay", apply_src)


if __name__ == "__main__":
    unittest.main()
