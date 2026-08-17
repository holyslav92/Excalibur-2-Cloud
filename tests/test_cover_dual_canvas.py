"""Два холста 2K → cover + 7 inline."""
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DualCanvasSplitTest(unittest.TestCase):
    def test_demo_split_makes_cover_and_seven_inline(self) -> None:
        tmp = Path(tempfile.mkdtemp())
        try:
            article = tmp / "BTEST-dual"
            cover = article / "cover"
            cover.mkdir(parents=True)
            h2s = "".join(f"<h2>Секция {i}</h2><p>x</p>" for i in range(1, 8))
            (article / "article.html").write_text(
                f"<article><p>лид</p>{h2s}</article>\n", encoding="utf-8"
            )
            (article / "article.meta.json").write_text(
                json.dumps({"topic_id": "BTEST", "h1": "Тест"}, ensure_ascii=False),
                encoding="utf-8",
            )
            slots = {
                "cover": {
                    "quadrant": "top_left",
                    "alt": "Обложка тест",
                    "scene_hint": "host left",
                }
            }
            for i in range(1, 8):
                slots[f"inline_{i}"] = {
                    "h2_anchor": f"Секция {i}",
                    "alt": f"Схема секции {i}",
                    "scene_hint": "card",
                    "visual_type": "infographic_card",
                }
            (cover / "quad-manifest.json").write_text(
                json.dumps({"slots": slots, "cover_hook": "тест хук", "pipeline": "dual_2k_quad_8_panels"}, ensure_ascii=False),
                encoding="utf-8",
            )
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_cover_quad_split.py"),
                    "--article-dir",
                    str(article),
                    "--demo-canvas",
                    "--inject-html",
                ],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertTrue((cover / "cover.png").is_file())
            for i in range(1, 8):
                self.assertTrue((cover / f"inline-{i:02d}.png").is_file(), f"missing inline-{i:02d}")
            html = (article / "article.html").read_text(encoding="utf-8")
            for i in range(1, 8):
                self.assertIn(f'data-slot="inline_{i}"', html)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
