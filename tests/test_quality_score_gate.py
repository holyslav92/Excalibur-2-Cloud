"""Tests for article quality score gate (Grok Bot 7.5–9 bar)."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_quality_score_gate import (  # noqa: E402
    check_finale,
    check_h1,
    check_lead,
    check_length,
    check_middle,
    check_tone,
    evaluate,
    extract_body_sections,
)


def _good_lead_paras() -> str:
    return (
        "<p>За двое суток до подписания ДДУ банк прислал семье новый расчёт: ставка выше, "
        "платёж — плюс 18 тысяч в месяц, и бронь на квартиру сгорела. Одобрение лежало на руках "
        "несколько недель, взнос собран до рубля. Письмо пришло в четверг вечером, подписание "
        "стояло на субботу. Утром они сели на кухне с калькулятором и увидели, что новая цифра "
        "не сходится с доходом. ДДУ подписывать не стали — бронь дотикала, квартира ушла в продажу.</p>"
    )


def _minimal_article(extra_body: str = "", h1: str = "Платёж вырос в 8 раз — бронь сгорела") -> str:
    return (
        f"{_good_lead_paras()}"
        '<div class="excalibur-cta-early"><p><a href="https://t.me/Tyumen_Rieltor">TG</a> '
        '<a href="https://max.ru/id561413315447_biz">MAX</a></p></div>'
        "<h2>История</h2><p>Семья выбрала новостройку на севере Тюмени и внесла бронь.</p>"
        f"{extra_body}"
        "<h2>Финал</h2><p>Они остановились до аванса — напишите, разберём до внесения.</p>"
        "<p>Кто прав: банк, который поднял ставку накануне, или семья, что развернулась?</p>"
        '<div class="excalibur-cta-end"><p><a href="https://t.me/Tyumen_Rieltor">TG</a></p></div>'
    )


class QualityScoreGateTest(unittest.TestCase):
    def test_contract_and_canon(self) -> None:
        self.assertTrue((ROOT / "shared/article-quality-score-lock.md").is_file())
        canon = json.loads((ROOT / "shared/pipeline-canon.json").read_text(encoding="utf-8"))
        qs = canon.get("article_quality_score") or {}
        self.assertEqual(qs.get("gate"), "scripts/excalibur_blog_quality_score_gate.py")
        self.assertEqual(qs.get("word_count_hard_max"), 1750)

    def test_weak_calm_h1_fails(self) -> None:
        res = check_h1("Как устроена семейная ипотека на новостройку: полный гайд")
        self.assertFalse(res.pass_)
        self.assertTrue(any("h1-calm-guide" in r for r in res.reasons))

    def test_strong_h1_passes(self) -> None:
        res = check_h1("Платёж по новостройке вырос в 8 раз — бронь сгорела")
        self.assertTrue(res.pass_)

    def test_composite_disclaimer_in_lead_fails(self) -> None:
        html = (
            "<p>Случай собирательный, без фамилий. За 2 дня до ДДУ банк поднял ставку — "
            "платёж вырос, бронь сгорела. Семья сидела на кухне. ДДУ не подписали. "
            "Квартира ушла. Деньги не вернули.</p>"
        )
        res = check_lead(html)
        self.assertFalse(res.pass_)
        self.assertTrue(any("composite" in r for r in res.reasons))

    def test_lawyer_phrase_fails_tone(self) -> None:
        html = "<p>Профессиональный участник рынка в досудебной плоскости следует констатировать риски.</p>"
        res = check_tone(html)
        self.assertFalse(res.pass_)
        self.assertTrue(any("lawyer-tone" in r for r in res.reasons))

    def test_overlong_fails_length(self) -> None:
        words = " ".join(["слово"] * 1800)
        res = check_length(f"<p>{words}</p>")
        self.assertFalse(res.pass_)
        self.assertTrue(any("length-hard" in r or "length-over" in r for r in res.reasons))

    def test_triple_retell_detected(self) -> None:
        phrase = (
            "банк прислал семье новый расчет ставка выше платеж вырос бронь сгорела"
        )
        zones = {
            "lead": phrase,
            "middle": phrase + " в середине истории",
            "finale": "в конце " + phrase,
        }
        html = f"<p>{phrase}</p><h2>A</h2><p>{zones['middle']}</p><h2>B</h2><p>{zones['finale']}</p>"
        res = check_middle(html, zones)
        self.assertFalse(res.pass_)
        self.assertTrue(any("triple-retell" in r for r in res.reasons))

    def test_lecture_tail_214_fz_fails_finale(self) -> None:
        html = _minimal_article().replace(
            '<div class="excalibur-cta-end">',
            "<p>По 214-ФЗ застройщик обязан передать объект в срок.</p>"
            '<div class="excalibur-cta-end">',
        )
        zones = extract_body_sections(html)
        res = check_finale(html, zones)
        self.assertFalse(res.pass_)
        self.assertTrue(any("lecture-tail" in r for r in res.reasons))

    def test_evaluate_writes_report(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            article = Path(td)
            (article / "title-brief.json").write_text(
                json.dumps({"h1": "Платёж вырос в 8 раз — бронь сгорела"}),
                encoding="utf-8",
            )
            body = _minimal_article()
            (article / "article.html").write_text(body, encoding="utf-8")
            report = evaluate(article, ROOT)
            self.assertIn("sections", report)
            self.assertIn("h1", report["sections"])


if __name__ == "__main__":
    unittest.main()
