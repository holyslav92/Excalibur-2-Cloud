"""Unit tests for schema JSON-LD derouter helpers."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SchemaDerouterHelpersTest(unittest.TestCase):
    def test_normalize_strips_fences_and_parses(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import normalize_schema_jsonld_text

        raw = '```json\n{"@context": "https://schema.org", "@type": "BlogPosting"}\n```'
        out = normalize_schema_jsonld_text(raw)
        data = json.loads(out)
        self.assertEqual(data["@type"], "BlogPosting")

    def test_normalize_rejects_prose(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import normalize_schema_jsonld_text

        with self.assertRaises(ValueError):
            normalize_schema_jsonld_text("Я не могу писать schema для Cursor.")

    def test_resolve_output_path_bare_filename_under_article_dir(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_output_path

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            art = root / "memory/blog/articles/B34-slug"
            art.mkdir(parents=True)
            out = resolve_output_path("schema.jsonld", art, root)
            self.assertEqual(out, art / "schema.jsonld")

    def test_resolve_output_path_repo_relative_unchanged(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_output_path

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            art = root / "memory/blog/articles/B34-slug"
            art.mkdir(parents=True)
            out = resolve_output_path("memory/blog/articles/B34-slug/schema.jsonld", art, root)
            self.assertEqual(out, root / "memory/blog/articles/B34-slug/schema.jsonld")


if __name__ == "__main__":
    unittest.main()
