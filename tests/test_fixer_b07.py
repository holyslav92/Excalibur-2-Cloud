"""Durable fixes from pipeline run B07 (2026-08-21)."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_link_verify import known_bad_external_href_reason  # noqa: E402
from excalibur_blog_quality_bar_9_gate import (  # noqa: E402
    check_early_cta_before_first_h2,
    check_no_site_base_placeholder,
)
from excalibur_blog_topic_focus import focus_check  # noqa: E402

B07_DIR = ROOT / "memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya"


class TopicFocusInheritanceTest(unittest.TestCase):
    def test_inheritance_title_without_kvartir_passes(self) -> None:
        verdict = focus_check(
            "Наследству два года. Сын от первого брака отказ не писал "
            "nasledstvo-syn-ot-pervogo-braka"
        )
        self.assertEqual(verdict["status"], "PASS")
        self.assertIn("наслед", verdict.get("allow_hit") or "")


class QualityBarB07StructureTest(unittest.TestCase):
    def test_b07_article_passes_new_cta_checks(self) -> None:
        html = (B07_DIR / "article.html").read_text(encoding="utf-8")
        self.assertTrue(check_early_cta_before_first_h2(html))
        self.assertTrue(check_no_site_base_placeholder(html))

    def test_tldr_as_first_h2_fails_early_cta_zone(self) -> None:
        bad = (
            "<p>hook</p><h2>Коротко</h2><div class=\"excalibur-cta-early\">"
            "<a href=\"https://t.me/Tyumen_Rieltor\">TG</a>"
            "<a href=\"https://max.ru/id561413315447_biz\">MAX</a></div>"
        )
        self.assertFalse(check_early_cta_before_first_h2(bad))

    def test_site_base_placeholder_fails(self) -> None:
        self.assertFalse(check_no_site_base_placeholder('<a href="{{SITE_BASE}}/gajdy/">'))

    def test_b07_quality_gate_all_pass(self) -> None:
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/excalibur_blog_quality_bar_9_gate.py"),
                "--article-dir",
                str(B07_DIR),
                "--skip-cover-qa",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stdout + proc.stderr)


class LinkVerifyRegistryTest(unittest.TestCase):
    def test_reestr_nasled_href_denied(self) -> None:
        reason = known_bad_external_href_reason("https://reestr-nasled.ru/")
        self.assertIsNotNone(reason)
        self.assertIn("plain text", reason or "")


if __name__ == "__main__":
    unittest.main()
