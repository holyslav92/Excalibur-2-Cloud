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
    def _run_script(self, name: str, *, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        if extra_env:
            env.update(extra_env)
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts" / name)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )

    def test_kie_script_blocked(self) -> None:
        proc = self._run_script("excalibur_blog_kie_gpt_image2_api.py")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("KIE IMAGE BLOCKER", proc.stderr)

    def test_pil_compose_blocked(self) -> None:
        proc = self._run_script("excalibur_blog_cover_pil_compose.py")
        self.assertEqual(proc.returncode, 1)
        self.assertIn("PIL MASHUP BLOCKER", proc.stderr)

    def test_grsai_dry_run_without_key(self) -> None:
        article = "memory/blog/articles/B02-raspisku-na-kvartiru-napisali-deneg-na-schete-net"
        env = {k: v for k, v in os.environ.items() if k not in {"GRSAI_API_KEY", "GRSAI_KEY"}}
        proc = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "excalibur_blog_grsai_gpt_image2_api.py"),
                "--article-dir",
                article,
                "--batch",
                "cover/quad-mcp-batch-01.json",
                "--dry-run",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )
        self.assertEqual(proc.returncode, 0, msg=proc.stderr)
        self.assertIn("grsaiapi.com", proc.stdout)
        self.assertIn("vip_disabled", proc.stdout)

    def test_resolve_grsai_hosts_default(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import DEFAULT_HOSTS, resolve_hosts

        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GRSAI_API_BASE_URL", None)
            self.assertEqual(resolve_hosts(), DEFAULT_HOSTS)

    def test_resolve_grsai_hosts_env_override(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import resolve_hosts

        with mock.patch.dict(
            os.environ,
            {"GRSAI_API_BASE_URL": "https://api.example.com,https://cn.example.com"},
        ):
            self.assertEqual(
                resolve_hosts(),
                ["https://api.example.com", "https://cn.example.com"],
            )

    def test_default_grsai_model_standard_only(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import (
            default_model,
            grsai_standard_model_id,
            iter_model_tiers,
            model_tier_standard,
        )

        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GRSAI_IMAGE_MODEL", None)
            model = default_model()
            self.assertTrue(model.startswith("gpt"))
            self.assertEqual(model, grsai_standard_model_id())
            self.assertEqual(model, model_tier_standard())
            tiers = iter_model_tiers()
            self.assertEqual(len(tiers), 1)
            self.assertEqual(tiers[0][0], "standard")
            self.assertEqual(tiers[0][1], grsai_standard_model_id())
            self.assertNotIn("vip", tiers[0][1])

    def test_grsai_vip_env_forced_to_standard(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import (
            grsai_standard_model_id,
            model_tier_standard,
            normalize_grsai_model,
            iter_model_tiers,
        )

        vip_id = grsai_standard_model_id() + "-vip"
        with mock.patch.dict(os.environ, {"GRSAI_IMAGE_MODEL": vip_id}):
            standard = model_tier_standard()
            self.assertEqual(standard, grsai_standard_model_id())
            self.assertEqual(normalize_grsai_model(vip_id), grsai_standard_model_id())
            self.assertEqual(iter_model_tiers(), [("standard", grsai_standard_model_id())])

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

    def test_standard_aspect_supports_2k_pixels(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import (
            aspect_ratio_for_grsai,
            grsai_standard_model_id,
            parse_size_wh,
        )

        standard = grsai_standard_model_id()
        self.assertEqual(aspect_ratio_for_grsai("16:9", model=standard), "1672x941")
        self.assertEqual(
            aspect_ratio_for_grsai("16:9", model=standard, resolution="2K"),
            "2048x1152",
        )
        self.assertEqual(aspect_ratio_for_grsai("2048x1152", model=standard), "2048x1152")
        self.assertEqual(parse_size_wh("2048x1152"), (2048, 1152))
        self.assertEqual(parse_size_wh("1200x675"), (1200, 675))

    def test_vip_model_unreachable_from_generate_image(self) -> None:
        import inspect

        from excalibur_blog_grsai_gpt_image2_api import (
            generate_image,
            grsai_standard_model_id,
        )

        source = inspect.getsource(generate_image)
        self.assertNotIn("-vip", source)
        vip_id = grsai_standard_model_id() + "-vip"
        module_path = ROOT / "scripts" / "excalibur_blog_grsai_gpt_image2_api.py"
        module_text = module_path.read_text(encoding="utf-8")
        self.assertNotIn("model_tier_vip_fallback", module_text)
        self.assertNotIn("generate_image_with_model_tier_fallback", module_text)
        self.assertNotIn(f"model={vip_id}", module_text)

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
