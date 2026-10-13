"""Owner lock 2026-08-29 — one-breath text + flexible inline placement."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class OneBreathCanonTest(unittest.TestCase):
    def test_pipeline_canon_word_targets(self) -> None:
        canon = json.loads((ROOT / "shared/pipeline-canon.json").read_text(encoding="utf-8"))
        qb = canon.get("quality_bar_9") or {}
        self.assertEqual(qb.get("word_count_target_min"), 1800)
        self.assertEqual(qb.get("word_count_target_max"), 2200)
        self.assertEqual(qb.get("word_count_hard_max"), 2400)
        pillars = (canon.get("owner_lock_permanent") or {}).get("pillars") or {}
        self.assertIn("one_breath_v1", pillars)

    def test_spine_once_bans_recap(self) -> None:
        from excalibur_blog_quality_bar_9_gate import check_spine_once_no_recap

        ok, _ = check_spine_once_no_recap("<p>Нормальный текст без recap.</p>")
        self.assertTrue(ok)
        bad, errors = check_spine_once_no_recap("<p>Коротко если некогда — вот суть.</p>")
        self.assertFalse(bad)
        self.assertTrue(errors)

    def test_word_count_hard_max(self) -> None:
        from excalibur_blog_quality_bar_9_gate import WORD_HARD_MAX, WORD_TARGET_MAX, WORD_TARGET_MIN

        self.assertEqual(WORD_TARGET_MIN, 1800)
        self.assertEqual(WORD_TARGET_MAX, 2200)
        self.assertEqual(WORD_HARD_MAX, 2400)

    def test_cover_adjacent_stack_gate_pass(self) -> None:
        from excalibur_blog_quality_bar_9_gate import check_no_cover_adjacent_image_stack

        html = """
        <p>лид</p>
        <h2>H1</h2><p>текст</p>
        <h2>H2</h2><p>текст</p>
        <h2>H3</h2><p>абзац</p>
        <figure class="inline-quad" data-slot="inline_1"><img src="a.png" alt="схема"></figure>
        """
        ok, errors = check_no_cover_adjacent_image_stack(html)
        self.assertTrue(ok, errors)

    def test_cover_adjacent_stack_fails_first_h2_figure(self) -> None:
        from excalibur_blog_quality_bar_9_gate import check_no_cover_adjacent_image_stack

        parts = []
        for i in range(1, 8):
            parts.append(f"<h2>H{i}</h2>")
            if i == 1:
                parts.append(
                    f'<figure class="inline-quad" data-slot="inline_{i}">'
                    f'<img src="inline-{i:02d}.png" alt="x"></figure>'
                )
            parts.append("<p>текст</p>")
        ok, errors = check_no_cover_adjacent_image_stack("".join(parts))
        self.assertFalse(ok)
        self.assertTrue(errors)

    def test_realistic_mix_manifest_gate(self) -> None:
        from excalibur_blog_quality_bar_9_gate import check_inline_realistic_mix

        with tempfile.TemporaryDirectory() as td:
            cover_dir = Path(td) / "cover"
            cover_dir.mkdir()
            manifest = {
                "inline_count": 7,
                "slots": {
                    f"inline_{i}": {
                        "visual_type": "realistic_photo" if i <= 3 else "comparison_table"
                    }
                    for i in range(1, 8)
                },
            }
            (cover_dir / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            ok, errors = check_inline_realistic_mix(cover_dir / "quad-manifest.json")
            self.assertTrue(ok, errors)

            manifest["slots"]["inline_1"]["visual_type"] = "comparison_table"
            manifest["slots"]["inline_2"]["visual_type"] = "comparison_table"
            (cover_dir / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            ok, errors = check_inline_realistic_mix(cover_dir / "quad-manifest.json")
            self.assertFalse(ok)
            self.assertTrue(errors)

    def test_manifest_assigns_realistic_photo_types(self) -> None:
        from excalibur_blog_quad_manifest import assign_inline_placements

        h2s = [f"Секция {i}" for i in range(1, 11)]
        inline_keys = tuple(f"inline_{i}" for i in range(1, 8))
        types_catalog = json.loads(
            (ROOT / "memory/cover/inline-visual-types.json").read_text(encoding="utf-8")
        )
        plan = assign_inline_placements(h2s, inline_keys, types_catalog)
        self.assertEqual(len(plan), 7)
        realistic = sum(1 for p in plan if p["visual_type"] == "realistic_photo")
        self.assertGreaterEqual(realistic, 2)
        self.assertLessEqual(realistic, 4)
        pairs = [p for p in plan if p.get("placement_group") == "pair"]
        self.assertEqual(len(pairs), 0)
        anchors = [p["h2_anchor"] for p in plan]
        self.assertEqual(len(anchors), len(set(anchors)))


if __name__ == "__main__":
    unittest.main()
