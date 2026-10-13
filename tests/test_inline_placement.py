"""Cover-safe inline placement — owner complaint tymenrieltor.ru 2026-10."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class InlinePlacementTest(unittest.TestCase):
    def test_spread_h2_indices_even(self) -> None:
        from excalibur_blog_inline_placement import spread_h2_indices

        indices = spread_h2_indices(10, 7, first_index=2)
        self.assertEqual(len(indices), 7)
        self.assertEqual(indices[0], 2)
        self.assertEqual(len(set(indices)), 7)

    def test_fail_figure_in_first_h2_section(self) -> None:
        from excalibur_blog_inline_placement import check_no_cover_adjacent_image_stack

        html = """
        <p>lead</p>
        <h2>Первый</h2>
        <figure class="inline-quad" data-slot="inline_1"><img src="a.png" alt="схема"></figure>
        <p>текст</p>
        <h2>Второй</h2>
        <p>текст</p>
        <h2>Третий</h2>
        <p>текст</p>
        """
        ok, errors = check_no_cover_adjacent_image_stack(html)
        self.assertFalse(ok)
        self.assertTrue(any("opening H2" in e for e in errors))

    def test_pass_figure_from_third_section(self) -> None:
        from excalibur_blog_inline_placement import check_no_cover_adjacent_image_stack

        html = """
        <p>lead</p>
        <h2>Первый</h2>
        <p>текст</p>
        <h2>Второй</h2>
        <p>текст</p>
        <h2>Третий</h2>
        <p>абзац перед картинкой</p>
        <figure class="inline-quad" data-slot="inline_1"><img src="a.png" alt="таблица сроков"></figure>
        <p>ещё текст</p>
        """
        ok, errors = check_no_cover_adjacent_image_stack(html)
        self.assertTrue(ok, errors)

    def test_fail_adjacent_figures(self) -> None:
        from excalibur_blog_inline_placement import check_no_cover_adjacent_image_stack

        html = """
        <h2>A</h2><p>x</p>
        <h2>B</h2><p>x</p>
        <h2>C</h2>
        <figure class="inline-quad"><img alt="a"></figure>
        <figure class="inline-quad"><img alt="b"></figure>
        """
        ok, errors = check_no_cover_adjacent_image_stack(html)
        self.assertFalse(ok)
        self.assertTrue(any("adjacent" in e for e in errors))

    def test_manifest_assign_skips_opening_h2(self) -> None:
        from excalibur_blog_quad_manifest import assign_inline_placements
        import json

        h2s = [f"Секция {i}" for i in range(1, 11)]
        inline_keys = tuple(f"inline_{i}" for i in range(1, 8))
        types_catalog = json.loads(
            (ROOT / "memory/cover/inline-visual-types.json").read_text(encoding="utf-8")
        )
        plan = assign_inline_placements(h2s, inline_keys, types_catalog)
        self.assertEqual(len(plan), 7)
        opening = {h2s[0], h2s[1]}
        for item in plan:
            self.assertNotIn(item["h2_anchor"], opening)
            self.assertIsNone(item.get("placement_group"))
        anchors = [p["h2_anchor"] for p in plan]
        self.assertEqual(len(anchors), len(set(anchors)))


if __name__ == "__main__":
    unittest.main()
