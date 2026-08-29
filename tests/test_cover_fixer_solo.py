"""Cover fixer solo-path routing — B13 post-budget strip FAIL."""
from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class CoverFixerSoloPathTest(unittest.TestCase):
    def test_is_solo_cover_article_detects_grsai_batch(self) -> None:
        from excalibur_blog_cover_fixer import is_solo_cover_article

        b13 = (
            ROOT
            / "memory/blog/articles/B13-v-tyumeni-obeschali-mashino-mesto-k-kvartire-v-rosreestre-prav-na-nego-ne-nashli"
        )
        if not (b13 / "cover/grsai-solo-batch.json").is_file():
            raise unittest.SkipTest("B13 solo batch missing")
        self.assertTrue(is_solo_cover_article(b13))

    def test_needs_strip_fix_on_query_strips_fail(self) -> None:
        from excalibur_blog_cover_fixer import needs_strip_fix
        from excalibur_blog_cover_qa_pixels import PixelQAResult

        result = PixelQAResult(
            status="FAIL",
            checks={"pixel_no_wordstat_query_strips": False},
        )
        self.assertTrue(needs_strip_fix(result))

    @patch("excalibur_blog_cover_fixer.regen_cover_solo_strip_fix", return_value=True)
    @patch("excalibur_blog_cover_fixer.pixel_qa")
    def test_run_fixer_uses_solo_strip_regen(self, mock_pixel_qa, mock_solo_regen) -> None:
        from excalibur_blog_cover_fixer import run_fixer
        from excalibur_blog_cover_qa_pixels import PixelQAResult

        b13 = (
            ROOT
            / "memory/blog/articles/B13-v-tyumeni-obeschali-mashino-mesto-k-kvartire-v-rosreestre-prav-na-nego-ne-nashli"
        )
        if not b13.is_dir():
            raise unittest.SkipTest("B13 article dir missing")

        fail_result = PixelQAResult(
            status="FAIL",
            checks={
                "pixel_no_wordstat_query_strips": False,
                "pixel_hook_title_present": True,
                "pixel_phone_readable": False,
                "pixel_meme_present": False,
                "pixel_layout_not_collapsed": True,
                "pixel_designed_thumbnail": False,
                "pixel_no_text_on_clothing": True,
                "pixel_no_inpaint_artifacts": True,
                "pixel_host_close_up": True,
                "pixel_host_not_distant_fullbody": True,
            },
            errors=["pixel_no_wordstat_query_strips FAIL"],
        )
        pass_result = PixelQAResult(status="PASS", checks={k: True for k in fail_result.checks})
        mock_pixel_qa.side_effect = [fail_result, pass_result]

        report = run_fixer(b13, ROOT, max_rounds=1, allow_regen=True)
        self.assertTrue(mock_solo_regen.called)
        self.assertEqual(report.get("status"), "PASS")


if __name__ == "__main__":
    unittest.main()
