"""Opening canon: prose lead instead of TL;DR / «Быстрый инсайт» bullet-dump."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.excalibur_blog_opening_meta_gate import (
    check_article,
    opening_tldr_errors,
    count_prose_sentences,
)
from scripts.excalibur_blog_quality_bar_9_gate import check_no_tldr_opening

ROOT = Path(__file__).resolve().parents[1]


PROSE_OPENING = (
    "<p>Квартира выглядит чистой. Продавец спокойный.</p>"
    "<p>«А если в выписке одна строка?» — спрашивают покупатели.</p>"
    "<p>Я в Тюмени такие кейсы веду до регистрации: сначала реестр, потом деньги.</p>"
    "<p>Одна строка в реквизите 4 может остановить аванс за сутки.</p>"
    "<p>Дальше разберём, что именно смотреть до подписи.</p>"
)


class OpeningProseLeadTest(unittest.TestCase):
    def test_blocks_tldr_bullets(self) -> None:
        html = (
            "<p>TL;DR</p><ul><li>Сталинка под ремонт</li><li>bullet</li></ul>"
        )
        errors = opening_tldr_errors(html)
        self.assertTrue(any("tldr" in e for e in errors))
        self.assertTrue(any("opening-bullet" in e for e in errors))

    def test_blocks_fast_insight_label(self) -> None:
        html = "<p><b>Быстрый инсайт.</b> Одна строка.</p>"
        errors = opening_tldr_errors(html)
        self.assertTrue(any("fast-insight" in e for e in errors))

    def test_prose_lead_passes(self) -> None:
        errors = opening_tldr_errors(PROSE_OPENING)
        self.assertEqual(errors, [])
        self.assertGreaterEqual(count_prose_sentences(PROSE_OPENING), 4)

    def test_quality_bar_no_tldr_check(self) -> None:
        ok, errors = check_no_tldr_opening(PROSE_OPENING + "<h2>Дальше</h2>")
        self.assertTrue(ok, errors)
        bad_ok, bad_errors = check_no_tldr_opening(
            "<p>TL;DR</p><ul><li>one</li><li>two</li></ul><h2>X</h2>"
        )
        self.assertFalse(bad_ok)
        self.assertTrue(bad_errors)

    def test_opening_meta_gate_blocks_tldr_article(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            (d / "article.html").write_text(
                "<p>TL;DR</p><ul><li>a</li><li>b</li></ul><h2>Разбор</h2>\n",
                encoding="utf-8",
            )
            (d / "article.meta.json").write_text(
                json.dumps({"description": "Карточка без TL;DR."}, ensure_ascii=False),
                encoding="utf-8",
            )
            report = check_article(d)
            self.assertEqual(report["status"], "BLOCK")
            joined = " ".join(report["errors"])
            self.assertIn("tldr", joined.lower())

    def test_pipeline_canon_opening_rules(self) -> None:
        canon = json.loads((ROOT / "shared/pipeline-canon.json").read_text(encoding="utf-8"))
        rules = canon["opening_rules"]
        self.assertTrue(rules.get("no_tldr_opening"))
        self.assertEqual(rules.get("prose_lead_sentences_min"), 4)


if __name__ == "__main__":
    unittest.main()
