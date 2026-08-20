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

    def test_prompt_cover_is_photo_only_inlines_keep_labels(self) -> None:
        import sys
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_quad_prompt import (
            build_cover_photo_prompt,
            build_prompt,
            cover_photo_prompt_errors,
        )

        manifest = {
            "cover_hook": "Cursor стал дешевле на треть",
            "cover_hook_highlight": "дешевле",
            "cover_motifs": {
                "outfit": "olive overshirt",
                "pose_framing": "host RIGHT",
                "action": "holds blank folder",
            },
            "slots": {
                "cover": {"scene_hint": "Host face LARGE left half", "sticky": "новой модели нет"},
                "inline_1": {
                    "visual_type": "infographic_card",
                    "h2_anchor": "Цифры",
                    "scene_hint": "fact card",
                    "labels": ["минус 20–30%", "заявление вендора"],
                },
                "inline_2": {"visual_type": "comparison_table_ui", "h2_anchor": "Сравнение", "scene_hint": "two columns"},
                "inline_3": {"visual_type": "workflow_diagram", "h2_anchor": "Схема", "scene_hint": "arrows"},
            },
        }
        prompt = build_prompt(manifest, {}, {}, {}, {})
        self.assertIn("TEXT LANGUAGE LOCK", prompt)
        self.assertIn("PHOTO ONLY", prompt)
        self.assertIn("минус 20–30%", prompt)
        self.assertNotIn("COVER TXT", prompt)
        self.assertNotIn("Host LARGE left", prompt)
        self.assertNotIn("«Cursor стал дешевле на треть»", prompt)
        self.assertNotIn("«новой модели нет»", prompt)
        self.assertEqual(cover_photo_prompt_errors(prompt), [])
        solo = build_cover_photo_prompt(manifest, solo=True)
        self.assertIn("ONE single 16:9 photograph", solo)
        self.assertEqual(cover_photo_prompt_errors(solo), [])
        self.assertNotIn("+7 922", solo)

    def test_style_files_do_not_force_left_bust_wordstat(self) -> None:
        style = (ROOT / "memory/cover/quad-style-the-rieltor.json").read_text(encoding="utf-8")
        design = (ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8")
        self.assertNotIn("Host LARGE left", style)
        self.assertNotIn("Host LARGE left", design)

    def test_overlay_script_removed(self) -> None:
        self.assertFalse(
            (ROOT / "scripts/excalibur_blog_cover_text_overlay.py").exists(),
            "banner overlay was rejected by user — network must draw the text",
        )
        apply_src = (ROOT / "scripts/excalibur_blog_quad_apply.py").read_text(encoding="utf-8")
        self.assertNotIn("cover_text_overlay", apply_src)


if __name__ == "__main__":
    unittest.main()
