"""Meme canon validators — top-100 catalog, variety, sacred zones docs."""
from __future__ import annotations

import unittest
from pathlib import Path

from scripts.excalibur_blog_meme_canon import (
    load_meme_catalog,
    validate_meme_picks,
    validate_manifest_meme_canon,
)

ROOT = Path(__file__).resolve().parents[1]


class MemeCanonTest(unittest.TestCase):
    def test_catalog_loads(self) -> None:
        catalog = load_meme_catalog(ROOT)
        self.assertTrue(catalog.get("entries"))
        self.assertIn("usage_rules", catalog)

    def test_valid_people_plus_cats(self) -> None:
        catalog = load_meme_catalog(ROOT)
        picks = {"cover": ["roll_safe", "smudge_cat"]}
        self.assertEqual(validate_meme_picks(picks, catalog), [])

    def test_rejects_cats_only(self) -> None:
        catalog = load_meme_catalog(ROOT)
        picks = {"cover": ["smudge_cat", "grumpy_cat"]}
        errs = validate_meme_picks(picks, catalog)
        self.assertTrue(any("cats-only" in e for e in errs))

    def test_rejects_unknown_id(self) -> None:
        catalog = load_meme_catalog(ROOT)
        picks = {"cover": ["fake_meme_id"]}
        errs = validate_meme_picks(picks, catalog)
        self.assertTrue(any("not in meme-top100" in e for e in errs))

    def test_cover_canon_meme_system(self) -> None:
        import json

        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        meme = canon.get("meme_system") or {}
        self.assertEqual(meme.get("locked_canon"), "meme_canon_v1")
        self.assertTrue(meme.get("variety", {}).get("forbid_cats_only_article"))


if __name__ == "__main__":
    unittest.main()
