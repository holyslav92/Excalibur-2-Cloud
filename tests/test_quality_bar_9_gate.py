"""Quality bar 9/10 gate contract."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class QualityBar9GateTest(unittest.TestCase):
    def test_contract_file_exists(self) -> None:
        self.assertTrue((ROOT / "shared/quality-bar-9.md").is_file())

    def test_pipeline_canon_references_quality_bar(self) -> None:
        canon = json.loads((ROOT / "shared/pipeline-canon.json").read_text(encoding="utf-8"))
        qb = canon.get("quality_bar_9") or {}
        self.assertEqual(qb.get("contract"), "shared/quality-bar-9.md")
        self.assertEqual(qb.get("gate"), "scripts/excalibur_blog_quality_bar_9_gate.py")

    def test_b03_quality_stamp_pass(self) -> None:
        path = ROOT / "memory/blog/articles/B03-pochti-vnesli-zadatok-za-48-chasov-do-torgov-kvartiru-podarili-docheri/quality-bar-9.json"
        self.assertTrue(path.is_file())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data.get("status"), "PASS")
        self.assertTrue(data.get("all_pass"))


if __name__ == "__main__":
    unittest.main()
