"""Interlink ledger post_id column parsing."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path


class InterlinkLedgerPostIdTests(unittest.TestCase):
    def test_parse_ledger_reads_post_id_column(self) -> None:
        from scripts.excalibur_blog_interlink_lib import parse_ledger

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "published-articles.md"
            path.write_text(
                "# ledger\n\n"
                "| date | topic_id | slug | url | status | post_id |\n"
                "|------|----------|------|-----|--------|--------|\n"
                "| 2026-08-21 | B07 | fixture-slug | /blog/x/fixture-slug/ | published | 8994 |\n",
                encoding="utf-8",
            )
            rows = parse_ledger(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["post_id"], 8994)


if __name__ == "__main__":
    unittest.main()
