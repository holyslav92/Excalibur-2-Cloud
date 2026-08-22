"""Blocker stubs: Kie and PIL mashup must never run."""
from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


class ImageProviderBlockerTest(unittest.TestCase):
    def _run_script(self, name: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / name)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_kie_script_blocked(self) -> None:
        proc = self._run_script("excalibur_blog_kie_gpt_image2_api.py")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("KIE IMAGE BLOCKER", proc.stderr)

    def test_pil_compose_blocked(self) -> None:
        proc = self._run_script("excalibur_blog_cover_pil_compose.py")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("PIL MASHUP BLOCKER", proc.stderr)

    def test_resolve_image_base_urls_default_order(self) -> None:
        from excalibur_blog_derouter_gpt_image2_api import (
            DEFAULT_IMAGE_BASE_URLS,
            resolve_image_base_urls,
        )

        urls = resolve_image_base_urls()
        self.assertEqual(urls[:4], DEFAULT_IMAGE_BASE_URLS)

    def test_resolve_image_base_urls_env_override(self) -> None:
        from excalibur_blog_derouter_gpt_image2_api import resolve_image_base_urls

        with mock.patch.dict(
            os.environ,
            {"DEROUTER_IMAGE_BASE_URL": "https://api.example.com,https://api-direct.example.com"},
        ):
            urls = resolve_image_base_urls()
        self.assertEqual(
            urls,
            [
                "https://api.example.com/openai/v1",
                "https://api-direct.example.com/openai/v1",
            ],
        )

    def test_parse_size_wh(self) -> None:
        from excalibur_blog_derouter_gpt_image2_api import parse_size_wh

        self.assertEqual(parse_size_wh("2048x1152"), (2048, 1152))
        self.assertEqual(parse_size_wh("1200x675"), (1200, 675))

    def test_default_responses_model(self) -> None:
        from excalibur_blog_derouter_gpt_image2_api import (
            DEFAULT_RESPONSES_MODEL,
            default_responses_model,
        )

        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("DEROUTER_RESPONSES_IMAGE_MODEL", None)
            self.assertEqual(default_responses_model(), DEFAULT_RESPONSES_MODEL)


if __name__ == "__main__":
    unittest.main()
