"""HARD Scout anti-dupe: H1 fingerprint, formula spam, frozen secondary recycle."""
from __future__ import annotations

import sys
import unittest
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_scout_story_dup import (  # noqa: E402
    check_anti_dupe_hard,
    check_formula_spam,
    check_frozen_secondary_recycle,
    check_h1_fingerprint_duplicate,
    extract_h1_fingerprint,
    extract_mechanism_signature,
    load_story_clusters,
)


class ScoutAntiDupeHardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.clusters = load_story_clusters(ROOT)
        cls.today = date(2026, 9, 5)

    def test_fingerprint_escrow_mechanism(self) -> None:
        blob = "Семейную ипотеку одобрили — эскроу не открыли до ДДУ в Тюмени"
        self.assertEqual(extract_mechanism_signature(blob), "escrow_blocked")
        self.assertEqual(extract_h1_fingerprint(blob), "escrow_blocked")

    def test_frozen_secondary_grandma_blocked(self) -> None:
        blob = "Бабушка-собственник не пришла на осмотр — старая доверенность перед авансом"
        warnings = check_frozen_secondary_recycle(blob, self.clusters)
        self.assertTrue(
            any(w.get("gate") == "frozen_secondary_recycle" for w in warnings),
            warnings,
        )

    def test_newbuild_escrow_not_frozen_secondary(self) -> None:
        blob = "В Тюмени одобрили семейную ипотеку на новостройку — эскроу не открыли"
        warnings = check_frozen_secondary_recycle(blob, self.clusters)
        frozen = [w for w in warnings if w.get("gate") == "frozen_secondary_recycle"]
        self.assertEqual(frozen, [])

    def test_h1_fingerprint_duplicate_within_30d(self) -> None:
        candidate = "Бронь сгорела — застройщик поднял цену на 500 тысяч в Тюмени"
        self.assertIn(":", extract_h1_fingerprint(candidate))
        prior_date = (self.today - timedelta(days=5)).isoformat()
        sources = [
            {
                "topic_id": "B99",
                "slug": "bron-sgorala-500-tysyach",
                "title": "Бронь сгорела за сутки — цена выросла на 500 тысяч",
                "text": "бронь сгорела 500 тысяч застройщик поднял цену",
                "source": "ledger",
                "date": prior_date,
            }
        ]
        warnings = check_h1_fingerprint_duplicate(
            candidate,
            sources,
            root=ROOT,
            today=self.today,
        )
        self.assertTrue(any(w.get("gate") == "h1_fingerprint" for w in warnings), warnings)

    def test_formula_spam_last_three_same_mechanism(self) -> None:
        candidate = "В Тюмени бронь на новостройку — застройщик изменил условия ДДУ"
        base_date = self.today
        sources = []
        for i in range(3):
            sources.append(
                {
                    "topic_id": f"B{10 + i}",
                    "slug": f"bron-ddu-{i}",
                    "title": f"Бронь и ДДУ застройщик Тюмень {i}",
                    "text": "бронь дду застройщик новостройка тюмень",
                    "source": "ledger",
                    "date": (base_date - timedelta(days=i + 1)).isoformat(),
                }
            )
        warnings = check_formula_spam(candidate, sources, root=ROOT)
        self.assertTrue(any(w.get("gate") == "formula_spam" for w in warnings), warnings)

    def test_anti_dupe_hard_pass_distinct_mechanism(self) -> None:
        candidate = "Trade-in: застройщик не принял старую квартиру — бронь сняли"
        sources = [
            {
                "topic_id": "B19",
                "slug": "eskrou-ne-otkryli",
                "title": "Эскроу не открыли",
                "text": "эскроу не открыли семейная ипотека дду",
                "source": "ledger",
                "date": (self.today - timedelta(days=3)).isoformat(),
            }
        ]
        warnings = check_anti_dupe_hard(
            candidate,
            sources,
            self.clusters,
            root=ROOT,
            today=self.today,
        )
        spam = [w for w in warnings if w.get("gate", "").startswith("formula_spam")]
        self.assertEqual(spam, [])


if __name__ == "__main__":
    unittest.main()
