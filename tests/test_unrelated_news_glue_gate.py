"""Тесты gate no_unrelated_calendar_news_glue (B34 INC)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_unrelated_news_glue import check_no_unrelated_calendar_news_glue


class UnrelatedNewsGlueGateTests(unittest.TestCase):
    def _article_dir(self, title_brief: dict) -> Path:
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
                    "wp_category_slugs": ["vtorichka-i-riski"],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        return ad

    def test_fail_secondary_gift_deed_with_family_mortgage_news(self) -> None:
        brief = {
            "h1": "В Тюмени дарственная остановила сделку за 7 дней до аванса",
            "subject": "тюменская вторичная квартира с недавней дарственной",
            "angle": "Юрист нашёл недавний подарок до аванса.",
        }
        ad = self._article_dir(brief)
        html = (
            "<p>Сроки подталкивали. В тюменских новостях обсуждали изменение условий "
            "семейной ипотеки с 1 октября 2026 года, и семья считала дни.</p>"
        )
        ok, errors = check_no_unrelated_calendar_news_glue(html, article_dir=ad)
        self.assertFalse(ok)
        self.assertTrue(errors)

    def test_pass_secondary_without_calendar_glue(self) -> None:
        brief = {
            "h1": "В Тюмени дарственная остановила сделку за 7 дней до аванса",
            "subject": "дарственная на вторичке",
            "angle": "аванс не внесли",
        }
        ad = self._article_dir(brief)
        html = "<p>До аванса оставалась неделя, и проверка казалась рискованной.</p>"
        ok, errors = check_no_unrelated_calendar_news_glue(html, article_dir=ad)
        self.assertTrue(ok)
        self.assertFalse(errors)

    def test_pass_when_family_mortgage_is_declared_casus(self) -> None:
        brief = {
            "h1": "19 дней до 1 октября: банк пересчитал семейную ипотеку",
            "subject": "семейная ипотека на новостройку",
            "angle": "дедлайн программы до 1 октября 2026",
        }
        ad = self._article_dir(brief)
        html = "<p>С 1 октября 2026 в Тюмени меняются условия семейной ипотеки.</p>"
        ok, errors = check_no_unrelated_calendar_news_glue(html, article_dir=ad)
        self.assertTrue(ok)
        self.assertFalse(errors)


if __name__ == "__main__":
    unittest.main()
