"""Blocker stubs: Kie and PIL mashup must never run."""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


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


if __name__ == "__main__":
    unittest.main()
