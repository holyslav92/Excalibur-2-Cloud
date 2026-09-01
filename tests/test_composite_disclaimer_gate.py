"""Gate: ban composite-case meta-disclaimers in article body."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_composite_disclaimer import (  # noqa: E402
    check_no_composite_disclaimer,
    composite_disclaimer_hits,
)


class CompositeDisclaimerGateTest(unittest.TestCase):
    def test_clean_casus_passes(self) -> None:
        html = (
            "<p>В среду утром семья сидела на кухне: банк прислал смс, "
            "что оформление приостановлено до проверки долей.</p>"
        )
        ok, errors = check_no_composite_disclaimer(html)
        self.assertTrue(ok)
        self.assertEqual(errors, [])

    def test_banned_phrases_fail(self) -> None:
        samples = [
            "Случай собирательный, без фамилий и адреса ЖК.",
            "Механика в Тюмени повторяется из месяца в месяц.",
            "Это моделируемый финал, а не репортаж.",
        ]
        for text in samples:
            hits = composite_disclaimer_hits(text)
            self.assertTrue(hits, msg=text)
            ok, errors = check_no_composite_disclaimer(f"<p>{text}</p>")
            self.assertFalse(ok)
            self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
