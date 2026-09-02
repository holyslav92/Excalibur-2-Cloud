"""Quality bar 9/10 gate contract."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


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

    def test_stamped_cover_qa_visual_pass_accepts_escape(self) -> None:
        from excalibur_blog_quality_bar_9_gate import _stamped_cover_qa_visual_pass

        with tempfile.TemporaryDirectory() as td:
            article = Path(td)
            cover_dir = article / "cover"
            cover_dir.mkdir(parents=True)
            cover_bytes = b"fake-cover-png-bytes"
            (cover_dir / "cover.png").write_bytes(cover_bytes)
            md5 = hashlib.md5(cover_bytes).hexdigest()
            qa = {
                "status": "PASS",
                "gate_status": "PASS",
                "pixel_qa": True,
                "cover_md5": md5,
                "pixel_evidence": {
                    "ocr_false_positive_escape": {"applied": True, "pattern": "B08/B09"},
                },
            }
            (cover_dir / "cover_qa.json").write_text(
                json.dumps(qa, ensure_ascii=False), encoding="utf-8"
            )
            self.assertTrue(_stamped_cover_qa_visual_pass(article))

    def test_stamped_cover_qa_visual_pass_rejects_md5_mismatch(self) -> None:
        from excalibur_blog_quality_bar_9_gate import _stamped_cover_qa_visual_pass

        with tempfile.TemporaryDirectory() as td:
            article = Path(td)
            cover_dir = article / "cover"
            cover_dir.mkdir(parents=True)
            (cover_dir / "cover.png").write_bytes(b"live-bytes")
            qa = {
                "status": "PASS",
                "gate_status": "PASS",
                "pixel_qa": True,
                "cover_md5": "stale-md5",
                "pixel_evidence": {
                    "ocr_false_positive_escape": {"applied": True},
                },
            }
            (cover_dir / "cover_qa.json").write_text(
                json.dumps(qa, ensure_ascii=False), encoding="utf-8"
            )
            self.assertFalse(_stamped_cover_qa_visual_pass(article))


class StampCoverQaEscapePreserveTest(unittest.TestCase):
    def test_stamp_preserves_manual_escape_when_pixel_reruns_fail(self) -> None:
        from excalibur_blog_cover_qa_pixels import PixelQAResult, stamp_cover_qa_json

        with tempfile.TemporaryDirectory() as td:
            article = Path(td)
            cover_dir = article / "cover"
            cover_dir.mkdir(parents=True)
            cover_bytes = b"cover-bytes-for-escape-preserve"
            (cover_dir / "cover.png").write_bytes(cover_bytes)
            md5 = hashlib.md5(cover_bytes).hexdigest()
            escape = {
                "applied": True,
                "mode": "visual_manual_B08_B09",
                "flaky_checks_overridden": ["pixel_hook_title_cyrillic"],
            }
            existing = {
                "status": "PASS",
                "gate_status": "PASS",
                "pixel_qa": True,
                "cover_md5": md5,
                "checks": {"pixel_hook_title_cyrillic": True},
                "pixel_evidence": {"ocr_false_positive_escape": escape},
            }
            qa_path = cover_dir / "cover_qa.json"
            qa_path.write_text(json.dumps(existing, ensure_ascii=False), encoding="utf-8")

            fail_pixel = PixelQAResult(
                "FAIL",
                checks={"pixel_hook_title_cyrillic": False},
                errors=["pixel_hook_title_cyrillic FAIL: empty OCR"],
                evidence={"cover_md5": md5},
            )
            returned = stamp_cover_qa_json(article, fail_pixel, topic_id="B11")
            self.assertEqual(returned, qa_path)
            preserved = json.loads(qa_path.read_text(encoding="utf-8"))
            self.assertEqual(preserved.get("status"), "PASS")
            self.assertTrue(
                (preserved.get("pixel_evidence") or {})
                .get("ocr_false_positive_escape", {})
                .get("applied")
            )

    def test_stamp_sets_gate_status_and_splits_escape_notes(self) -> None:
        from excalibur_blog_cover_qa_pixels import PixelQAResult, stamp_cover_qa_json

        with tempfile.TemporaryDirectory() as td:
            article = Path(td)
            cover_dir = article / "cover"
            cover_dir.mkdir(parents=True)
            (cover_dir / "cover.png").write_bytes(b"cover-stamp-gate")
            pixel_checks = {
                key: True
                for key in (
                    "pixel_identity_matches_studio",
                    "pixel_host_close_up",
                    "pixel_host_not_distant_fullbody",
                    "pixel_title_zone_clear",
                    "pixel_wordstat_not_on_host_chest",
                    "pixel_meme_not_occluded_by_wordstat",
                    "pixel_no_text_on_clothing",
                    "pixel_meme_clearance_80px",
                    "pixel_hook_title_present",
                    "pixel_hook_title_cyrillic",
                    "pixel_hook_title_not_truncated",
                    "pixel_no_foreign_article_text",
                    "pixel_no_wordstat_query_strips",
                    "pixel_no_wordstat_ocr_strips",
                    "pixel_no_collage_inset",
                    "pixel_layout_not_collapsed",
                    "pixel_not_services_checklist",
                    "pixel_manifest_outfit_matches",
                    "pixel_phone_readable",
                    "pixel_wordstat_not_opaque_bars",
                    "pixel_wordstat_phrases_not_truncated",
                    "pixel_light_high_key",
                )
            }
            pass_pixel = PixelQAResult(
                "PASS",
                checks=pixel_checks,
                errors=[
                    "ocr_false_positive_escape PASS: visual core OK; overridden pixel_no_collage_inset"
                ],
                evidence={"cover_md5": "abc", "ocr_false_positive_escape": {"applied": True}},
            )
            stamp_cover_qa_json(article, pass_pixel, topic_id="B21")
            stamped = json.loads((cover_dir / "cover_qa.json").read_text(encoding="utf-8"))
            self.assertEqual(stamped.get("status"), "PASS")
            self.assertEqual(stamped.get("gate_status"), "PASS")
            self.assertEqual(stamped.get("gate_errors"), [])
            self.assertEqual(stamped.get("pixel_errors"), [])
            self.assertEqual(len(stamped.get("pixel_escape_notes") or []), 1)


if __name__ == "__main__":
    unittest.main()
