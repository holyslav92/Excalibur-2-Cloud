"""Tests for B03 pipeline speed improvements."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HtmlAutofixTest(unittest.TestCase):
    def test_strong_to_b(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_html_linter import autofix_html_aliases, lint_html_file

        html = "<p><strong>тест</strong> и <em>курсив</em></p>"
        fixed, fixes = autofix_html_aliases(html)
        self.assertIn("<b>тест</b>", fixed)
        self.assertIn("<i>курсив</i>", fixed)
        self.assertTrue(fixes)
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(fixed)
            path = Path(f.name)
        report = lint_html_file(path, __import__("excalibur_blog_html_linter", fromlist=["ALLOWED_TAGS"]).ALLOWED_TAGS)
        path.unlink(missing_ok=True)
        self.assertEqual(report["verdict"], "pass")


class QuadManifestCanonTest(unittest.TestCase):
    def test_apply_canon_meme_pattern(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_quad_manifest_preflight import validate_quad_manifest
        from excalibur_blog_quad_slots import apply_quad_canon_to_manifest

        manifest = {
            "inline_count": 7,
            "wordstat_stickers": ["купить квартиру в тюмени", "ипотека тюмень"],
            "cover_phone_cta": "+7 922 001 65 05",
            "slots": {
                "cover": {"scene_hint": "x", "alt": "y"},
                **{
                    f"inline_{i}": {"scene_hint": "s", "alt": "a"}
                    for i in range(1, 8)
                },
            },
        }
        manifest = apply_quad_canon_to_manifest(manifest)
        self.assertTrue(manifest["slots"]["inline_1"]["meme_sticker"])
        self.assertTrue(manifest["slots"]["inline_2"]["no_meme"])
        self.assertTrue(manifest["slots"]["inline_4"]["no_host_face"])
        result = validate_quad_manifest(manifest)
        self.assertEqual(result["status"], "PASS")

    def test_preflight_doctor(self) -> None:
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/excalibur_blog_quad_manifest_preflight.py"),
                "--doctor",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)


class WriterChunkTest(unittest.TestCase):
    def test_split_h2_groups(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_writer_chunk import split_h2_groups

        h2s = [f"H{i}" for i in range(1, 8)]
        groups = split_h2_groups(h2s, 3)
        self.assertEqual(sum(len(g) for g in groups), 7)
        self.assertEqual(len(groups), 3)


class WordstatOverlayTest(unittest.TestCase):
    def test_typography_keeps_stickers_inside_frame(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_typography import compose_cover_typography, RAIL_LEFT

        with tempfile.TemporaryDirectory() as tmp:
            from PIL import Image

            path = Path(tmp) / "cover.png"
            Image.new("RGB", (1200, 675), "#88AACC").save(path)
            report = compose_cover_typography(
                path,
                hook="-2 МЛН уценили",
                highlight="уценили",
                phone="+7 922 001 65 05",
                stickers=["купить квартиру в тюмени", "банкротство продавца"],
                sticky="задаток сегодня",
            )
            self.assertEqual(report["status"], "OK")
            self.assertGreaterEqual(report["rail_left"], 0.68)
            for pos in report["sticker_positions"]:
                self.assertGreaterEqual(pos[0], RAIL_LEFT - 0.01)
                self.assertLess(pos[0], 0.90)
                self.assertLessEqual(pos[0] + 0.26, 1.01)
            img = Image.open(path)
            self.assertEqual(img.size, (1200, 675))


if __name__ == "__main__":
    unittest.main()
