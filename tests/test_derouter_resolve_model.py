"""Unit tests for Derouter role→tier model resolution."""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]

CANON_WRITING_MODEL = {
    "powerful": {
        "model": "gpt-6-astra",
        "model_env": "DEROUTER_POWERFUL_MODEL",
        "roles": ["writer", "sol", "title", "description", "cover-text"],
    },
    "utility": {
        "model": "gpt-5.6-terra",
        "model_env": "DEROUTER_TERRA_MODEL",
        "roles": [
            "scout",
            "research",
            "schema",
            "cover-scene",
        ],
    },
}


class DerouterResolveModelTests(unittest.TestCase):
    def test_powerful_role_requires_astra_family(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps({"writing_model": CANON_WRITING_MODEL}),
                encoding="utf-8",
            )
            model, tier = resolve_model("writer", None, root)
            self.assertEqual(tier, "powerful")
            self.assertEqual(model, "gpt-6-astra")

            model, tier = resolve_model("sol", None, root)
            self.assertEqual(tier, "powerful")
            self.assertEqual(model, "gpt-6-astra")

            model, tier = resolve_model("research", None, root)
            self.assertEqual(tier, "utility")
            self.assertEqual(model, "gpt-5.6-terra")

    def test_engagement_copy_roles_use_powerful_tier(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps({"writing_model": CANON_WRITING_MODEL}),
                encoding="utf-8",
            )
            for role in ("title", "description", "cover-text"):
                model, tier = resolve_model(role, None, root)
                self.assertEqual(tier, "powerful", role)
                self.assertEqual(model, "gpt-6-astra", role)

    def test_scout_and_research_use_utility_tier(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps({"writing_model": CANON_WRITING_MODEL}),
                encoding="utf-8",
            )
            for role in ("scout", "research", "schema", "cover-scene"):
                model, tier = resolve_model(role, None, root)
                self.assertEqual(tier, "utility", role)
                self.assertEqual(model, "gpt-5.6-terra", role)

    def test_legacy_text_model_does_not_override_powerful_to_non_astra(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps(
                    {
                        "writing_model": {
                            "powerful": {"model": "gpt-6-astra", "roles": ["writer"]},
                            "utility": {"model": "gpt-5.6-terra", "roles": ["research"]},
                        }
                    }
                ),
                encoding="utf-8",
            )
            with mock.patch.dict(os.environ, {"DEROUTER_TEXT_MODEL": "gpt-5.6-terra"}, clear=False):
                model, tier = resolve_model("writer", None, root)
                self.assertEqual(tier, "powerful")
                self.assertIn("astra", model.lower())


class DerouterBudgetFallbackTests(unittest.TestCase):
    def test_budget_exceeded_detection(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import (
            DerouterChatError,
            is_powerful_budget_exceeded_error,
        )

        exc = DerouterChatError(
            "Derouter HTTP 402 budget_exceeded: 0 concurrent claude-opus-5-5 slots",
            status=402,
        )
        self.assertTrue(is_powerful_budget_exceeded_error(exc))
        self.assertFalse(is_powerful_budget_exceeded_error(DerouterChatError("HTTP 500", status=500)))

    def test_powerful_fallback_model_from_tenant(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import powerful_fallback_model_id

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps(
                    {
                        "writing_model": {
                            "powerful": {
                                "model": "claude-opus-5-5",
                                "fallback_model": "gpt-6-astra",
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(powerful_fallback_model_id(root), "gpt-6-astra")


if __name__ == "__main__":
    unittest.main()
