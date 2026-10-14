"""Cover + inline stack gates (theme featured under H1)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_inline_cover_separation import (
    check_inline_no_cover_stack,
    figure_insert_after_paragraphs,
)
from excalibur_blog_quad_manifest import assign_inline_placements


class InlineCoverSeparationTest(unittest.TestCase):
    def test_fails_first_h2_inline(self) -> None:
        html = """
        <p>лид</p>
        <h2>Первый раздел</h2>
        <p>абзац</p>
        <figure class="inline-quad" data-slot="inline_1"><img src="a.png" alt="x"></figure>
        <h2>Второй</h2>
        <p>текст</p>
        """
        ok, errors = check_inline_no_cover_stack(html)
        self.assertFalse(ok)
        self.assertTrue(any("H2 #1" in e for e in errors))

    def test_passes_from_second_h2_with_prose(self) -> None:
        html = """
        <p>лид</p>
        <h2>Первый раздел</h2>
        <p>только текст без картинки в первом разделе.</p>
        <h2>Второй</h2>
        <p>Достаточно длинный абзац перед картинкой, чтобы не липнуть к обложке темы.</p>
        <figure class="inline-quad" data-slot="inline_1"><img src="a.png" alt="схема раздела"></figure>
        """
        ok, errors = check_inline_no_cover_stack(html)
        self.assertTrue(ok, errors)

    def test_fails_adjacent_figures(self) -> None:
        html = """
        <h2>А</h2><p>пропускаем</p>
        <h2>Б</h2>
        <p>Длинный абзац перед парой картинок в середине статьи для отступа от обложки.</p>
        <figure class="inline-quad"><img alt="a"></figure>
        <figure class="inline-quad"><img alt="b"></figure>
        """
        ok, errors = check_inline_no_cover_stack(html)
        self.assertFalse(ok)
        self.assertTrue(any("adjacent" in e for e in errors))

    def test_insert_after_paragraph_not_h2_flush(self) -> None:
        html = """
        <h2>Раздел</h2>
        <p>Первый абзац.</p>
        <p>Второй абзац.</p>
        """
        pos = figure_insert_after_paragraphs(html, "Раздел", paragraphs_after=1)
        self.assertIsNotNone(pos)
        self.assertIn("Первый абзац.", html[:pos])

    def test_manifest_skips_first_h2(self) -> None:
        h2s = ["Лид-история", "Документы", "Финал", "Практика", "Ещё"]
        inline_keys = tuple(f"inline_{i}" for i in range(1, 8))
        types_catalog = __import__("json").loads(
            (ROOT / "memory/cover/inline-visual-types.json").read_text(encoding="utf-8")
        )
        plan = assign_inline_placements(h2s, inline_keys, types_catalog)
        first_h2 = h2s[0]
        for item in plan:
            self.assertNotEqual(
                item["h2_anchor"],
                first_h2,
                "first H2 must not get inline (cover stack under theme featured)",
            )


if __name__ == "__main__":
    unittest.main()
