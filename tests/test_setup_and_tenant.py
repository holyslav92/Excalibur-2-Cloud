"""Excalibur-2-Cloud setup/tenant skeleton contracts."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SetupTenantTests(unittest.TestCase):
    def test_setup_status_complete_after_tenant_fill(self) -> None:
        status = json.loads((ROOT / "memory/setup/status.json").read_text(encoding="utf-8"))
        self.assertTrue(status.get("complete"))
        for phase in ("cloud", "site", "author", "voice", "visual", "cta", "scout"):
            self.assertEqual(status.get("phases", {}).get(phase), "done", phase)

    def test_tenant_config_the_rieltor(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        self.assertTrue(tenant.get("setup_complete"))
        self.assertEqual(tenant.get("brand_name"), "The Риэлтор")
        self.assertEqual(tenant.get("author_id"), "svyatoslav-shakin")
        self.assertEqual(tenant.get("cover_mode"), "host_reference")
        self.assertFalse(tenant.get("cta_required"))
        self.assertIn("https://t.me/Tyumen_Rieltor", tenant.get("cta_links") or [])
        self.assertTrue(tenant.get("dzen_rf_pack"))
        self.assertEqual(tenant.get("image_provider"), "derouter")
        self.assertEqual(tenant.get("inline_panel_count"), 7)
        self.assertEqual(tenant.get("article_text_model"), "claude-opus-5-thinking-high")

    def test_setup_agents_present(self) -> None:
        for rel in (
            "agents/excalibur-blog-setup.md",
            "agents/excalibur-blog-setup-voice.md",
            "agents/excalibur-blog-setup-visual.md",
            "skills/setup-excalibur-blog/SKILL.md",
            "skills/setup-voice-excalibur-blog/SKILL.md",
            "skills/setup-visual-excalibur-blog/SKILL.md",
            ".cursor/agents/excalibur-blog-setup.md",
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_tenant_files_filled_no_setup_required(self) -> None:
        for rel in (
            "shared/SOUL.md",
            "shared/article-style.md",
            "shared/soul-examples/good-outputs.md",
            "memory/brief/site-brief.md",
            "memory/cover/blog-hero.json",
            "shared/authors-registry.json",
        ):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("SETUP_REQUIRED", text, rel)

    def test_no_personal_lebedev_style_file(self) -> None:
        self.assertFalse((ROOT / "shared/lebedev-style.md").exists())
        self.assertTrue((ROOT / "shared/article-style.md").is_file())

    def test_cta_gate_requires_tenant_telegram(self) -> None:
        import shutil
        import subprocess
        import tempfile

        article_dir = ROOT / "memory/blog/articles/_cta_gate_fixture"
        if article_dir.exists():
            shutil.rmtree(article_dir)
        article_dir.mkdir(parents=True, exist_ok=True)
        try:
            (article_dir / "article.html").write_text(
                '<p>Консультация: <a href="https://t.me/Tyumen_Rieltor">Telegram</a></p>\n',
                encoding="utf-8",
            )
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_community_cta_gate.py"),
                    "--article-dir",
                    str(article_dir.relative_to(ROOT)),
                    "--root",
                    str(ROOT),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            report = json.loads((article_dir / "community-cta-gate.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "PASS")
        finally:
            shutil.rmtree(article_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
