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

    def test_excalibur_cta_div_allowed(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_html_linter import lint_html_file, ALLOWED_TAGS

        html = (
            '<div class="excalibur-cta-early"><p><a href="https://t.me/Tyumen_Rieltor">TG</a></p></div>'
            '<div class="excalibur-cta-mid"><p><a href="https://max.ru/id561413315447_biz">MAX</a></p></div>'
            '<div class="excalibur-cta-end excalibur-social-cta"><p>fin</p></div>'
        )
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(html)
            path = Path(f.name)
        report = lint_html_file(path, ALLOWED_TAGS)
        path.unlink(missing_ok=True)
        self.assertEqual(report["verdict"], "pass", report.get("errors"))

    def test_plain_div_forbidden(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_html_linter import lint_html_file, ALLOWED_TAGS

        html = '<div class="article-page__footer"><p>x</p></div>'
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(html)
            path = Path(f.name)
        report = lint_html_file(path, ALLOWED_TAGS)
        path.unlink(missing_ok=True)
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("Forbidden <div>" in e for e in report["errors"]))


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


class SolChunkTest(unittest.TestCase):
    def test_split_h2_groups_shared(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_sol_chunk import split_h2_groups

        h2s = [f"H{i}" for i in range(1, 8)]
        groups = split_h2_groups(h2s, 3)
        self.assertEqual(sum(len(g) for g in groups), 7)

    def test_merge_sol_fragments_strips_fences(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_sol_chunk import merge_sol_fragments

        merged = merge_sol_fragments(["```html\n<p>a</p>\n```", "<p>b</p>"])
        self.assertIn("<p>a</p>", merged)
        self.assertIn("<p>b</p>", merged)
        self.assertNotIn("```", merged)


class WordstatOverlayTest(unittest.TestCase):
    def test_overlay_script_import(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_cover_wordstat_overlay import stamp_wordstat_stickers

        with tempfile.TemporaryDirectory() as tmp:
            from PIL import Image

            path = Path(tmp) / "cover.png"
            Image.new("RGB", (400, 225), "#FFFFFF").save(path)
            report = stamp_wordstat_stickers(path, ["ипотека тюмень"])
            self.assertEqual(report["status"], "OK")
            self.assertTrue(path.is_file())


if __name__ == "__main__":
    unittest.main()
