"""Тесты gate no_foreign_slot_rubric_mechanism (owner 2026-09-29)."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_slot_rubric_mechanism import (  # noqa: E402
    check_no_foreign_slot_rubric_mechanism,
    foreign_mechanism_hits,
)


class SlotRubricMechanismGateTests(unittest.TestCase):
    def _article_dir(self, title_brief: dict, slot_rubric: str = "vtorichka") -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        ad = Path(tmp.name)
        (ad / "title-brief.json").write_text(
            json.dumps(title_brief, ensure_ascii=False), encoding="utf-8"
        )
        (ad / "article.meta.json").write_text(
            json.dumps(
                {
                    "h1": title_brief.get("h1", ""),
                    "slot_rubric": slot_rubric,
                    "wp_category_slugs": ["vtorichka-i-riski"],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return ad

    def test_fail_secondary_with_newbuild_bron_in_ending(self) -> None:
        brief = {
            "h1": "В Тюмени дарственная остановила сделку за 7 дней до аванса",
            "subject": "дарственная на вторичке",
            "angle": "аванс не внесли",
        }
        ad = self._article_dir(brief)
        html = (
            "<p>До аванса оставалась неделя. Святослав советует: подключиться лучше до брони.</p>"
        )
        with mock.patch.dict(os.environ, {"EXCALIBUR_BLOG_SLOT": "15:00"}, clear=False):
            ok, errors = check_no_foreign_slot_rubric_mechanism(html, article_dir=ad)
        self.assertFalse(ok)
        self.assertTrue(errors)
        self.assertIn("бронь", errors[0].lower())

    def test_pass_clean_secondary_casus(self) -> None:
        brief = {
            "h1": "В Тюмени дарственная остановила сделку за 7 дней до аванса",
            "subject": "вторичка, дарственная, аванс",
            "angle": "проверка перед авансом",
        }
        ad = self._article_dir(brief)
        html = (
            "<p>До аванса оставалась неделя. Ипотека банка одобрена, ЕГРН чистый, "
            "дарственная всплыла в реестре.</p>"
        )
        with mock.patch.dict(os.environ, {"EXCALIBUR_BLOG_SLOT": "15:00"}, clear=False):
            ok, errors = check_no_foreign_slot_rubric_mechanism(html, article_dir=ad)
        self.assertTrue(ok)
        self.assertFalse(errors)

    def test_pass_clean_newbuild_casus(self) -> None:
        brief = {
            "h1": "В Тюмени бронь сгорела за сутки до ДДУ",
            "subject": "новостройка, бронь, эскроу",
            "angle": "застройщик снял бронь",
        }
        ad = self._article_dir(brief, slot_rubric="novostroyki")
        html = (
            "<p>Бронь держалась сутки. ДДУ на эскроу не подписали, застройщик вернул только часть.</p>"
        )
        with mock.patch.dict(os.environ, {"EXCALIBUR_BLOG_SLOT": "09:00"}, clear=False):
            ok, errors = check_no_foreign_slot_rubric_mechanism(html, article_dir=ad)
        self.assertTrue(ok)
        self.assertFalse(errors)

    def test_foreign_hits_detects_bron_for_vtorichka(self) -> None:
        hits = foreign_mechanism_hits("лучше до брони", "vtorichka")
        self.assertTrue(hits)
        self.assertTrue(any("novostroyki" in h for h in hits))

    def test_ipoteka_not_foreign_for_secondary(self) -> None:
        hits = foreign_mechanism_hits("семейная ипотека на вторичку", "vtorichka")
        self.assertFalse(any("novostroyki" in h for h in hits))


if __name__ == "__main__":
    unittest.main()
