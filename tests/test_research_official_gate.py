"""Research official source gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResearchOfficialGateTests(unittest.TestCase):
    def test_b02_research_passes_official_gate(self) -> None:
        article_dir = ROOT / "memory/blog/articles/B02-raspisku-na-kvartiru-napisali-deneg-na-schete-net"
        proc = subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_research_official_gate.py"),
                "--article-dir",
                str(article_dir.relative_to(ROOT)),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((article_dir / "research-official-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")

    def test_missing_official_section_blocks(self) -> None:
        fixture = ROOT / "memory/blog/articles/_research_official_fixture"
        if fixture.exists():
            shutil.rmtree(fixture)
        fixture.mkdir(parents=True)
        try:
            (fixture / "research-notes.md").write_text(
                "## practical_facts\n\nСбербанк: комиссия 3 400 ₽ за аккредитив.\n",
                encoding="utf-8",
            )
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_research_official_gate.py"),
                    "--article-dir",
                    str(fixture.relative_to(ROOT)),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 2)
            report = json.loads((fixture / "research-official-gate.json").read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "BLOCK")
        finally:
            shutil.rmtree(fixture, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
