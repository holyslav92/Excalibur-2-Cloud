"""Visual type alias normalization (B08 Cover-QA fixer)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_quad_slots import (  # noqa: E402
    is_allowed_inline_visual_type,
    normalize_visual_type,
)


class VisualTypeAliasTest(unittest.TestCase):
    def test_comparison_table_ui_normalizes(self) -> None:
        self.assertEqual(normalize_visual_type("comparison_table_ui"), "comparison_table")
        self.assertTrue(is_allowed_inline_visual_type("comparison_table_ui"))

    def test_legacy_aliases_normalize(self) -> None:
        self.assertEqual(normalize_visual_type("workflow_diagram"), "process_flow")
        self.assertEqual(normalize_visual_type("checklist_board"), "labeled_checklist")
        self.assertTrue(is_allowed_inline_visual_type("tool_screenshot"))

    def test_canonical_types_unchanged(self) -> None:
        self.assertEqual(normalize_visual_type("comparison_table"), "comparison_table")
        self.assertTrue(is_allowed_inline_visual_type("fact_card"))

    def test_unknown_type_rejected(self) -> None:
        self.assertFalse(is_allowed_inline_visual_type("decorative_icons_row"))


if __name__ == "__main__":
    unittest.main()
