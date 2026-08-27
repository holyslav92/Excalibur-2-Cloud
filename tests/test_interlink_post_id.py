"""Interlink post_id ledger + WP REST slug resolve (B11 fixer)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class InterlinkPostIdTest(unittest.TestCase):
    def test_parse_ledger_reads_wp_post_id_column(self) -> None:
        from excalibur_blog_interlink_lib import parse_ledger

        with tempfile.TemporaryDirectory() as tmp:
            ledger = Path(tmp) / "published-articles.md"
            ledger.write_text(
                "| date | topic_id | slug | url | status | wp_post_id |\n"
                "|------|----------|------|-----|--------|------------|\n"
                "| 2026-08-27 | B11 | sample-slug | /blog/vtorichka-i-riski/sample-slug/ | published | 9201 |\n",
                encoding="utf-8",
            )
            rows = parse_ledger(ledger)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["post_id"], "9201")
            self.assertEqual(rows[0]["slug"], "sample-slug")

    def test_enrich_candidates_resolves_missing_post_id(self) -> None:
        from excalibur_blog_interlink_lib import enrich_candidates_post_ids

        candidates = [{"slug": "foo-bar", "title": "Foo"}]
        with patch(
            "excalibur_blog_interlink_lib.fetch_wp_post_id_by_slug",
            return_value=8984,
        ):
            enriched = enrich_candidates_post_ids(
                candidates,
                public_site_url="https://example.com",
            )
        self.assertEqual(enriched[0]["post_id"], 8984)
        self.assertEqual(enriched[0]["post_id_source"], "wp_rest")

    def test_parse_publish_post_id_from_bootstrap_output(self) -> None:
        from excalibur_blog_wp_publish import parse_publish_post_id

        out = "OK post=9201 slug=rodstvenniki-osporili\npermalink=/blog/foo/\n"
        self.assertEqual(parse_publish_post_id(out), 9201)

    def test_normalize_visual_type_maps_legacy_alias(self) -> None:
        from excalibur_blog_quad_slots import normalize_visual_type

        self.assertEqual(normalize_visual_type("comparison_table_ui"), "comparison_table")
        self.assertEqual(normalize_visual_type("comparison_table"), "comparison_table")


if __name__ == "__main__":
    unittest.main()
