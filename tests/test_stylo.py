"""Stylo voice coach: gold parse, delta calibration."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_stylo import (  # noqa: E402
    DELTA_PASS_THRESHOLD,
    burrows_delta,
    extract_features,
    load_gold_texts,
    load_profile,
)


GOLD_DIR = ROOT / "memory/stylo/gold"
PROFILE_PATH = ROOT / "memory/stylo/profile.json"

VERBOSE_LECTURE_HTML = """
<article>
<p>Необходимо отметить, что безусловно данный случай собирательный и таким образом
иллюстрирует реквизиты правового поля. Следовательно, покупатель должен осознавать,
что обременение в выписке ЕГРН, акт приёма-передачи, договор долевого участия и эскроу-счёт
являются юридически значимыми институтами. Иными словами, необходимо провести комплексную
экспертизу документов. Подведём итог: риски существуют повсеместно.</p>
<p>Во-первых, следует проверить выписку. Во-вторых, необходимо уточнить статус продавца.
В-третьих, безусловно требуется консультация специалиста. В-четвёртых, таким образом
минимизируются правовые риски. В-пятых, необходимо зафиксировать все договорённости.</p>
<p>Резюмируя вышеизложенное, покупатель обязан действовать осмотрительно и не полагаться
на устные обещания, поскольку регистрация в Росреестре, нотариальное удостоверение и
банковская ипотека образуют многоуровневую систему контроля, которую необходимо изучить
до внесения аванса и подписания договора купли-продажи вторичного жилья в Тюмени.</p>
</article>
"""


class StyloGoldTest(unittest.TestCase):
    def test_gold_files_parse(self) -> None:
        entries = load_gold_texts(GOLD_DIR)
        self.assertGreaterEqual(len(entries), 10)
        for entry in entries:
            feats = extract_features(f"<article>{entry['text']}</article>")
            self.assertGreater(feats["sent_len_mean"], 3.0)
            self.assertGreater(feats["para_len_mean"], 10.0)

    def test_gold_delta_low(self) -> None:
        profile = load_profile(PROFILE_PATH, GOLD_DIR)
        entries = load_gold_texts(GOLD_DIR)
        deltas = []
        for entry in entries:
            feats = extract_features(f"<article>{entry['text']}</article>")
            deltas.append(burrows_delta(feats, profile))
        max_gold = max(deltas)
        self.assertLess(max_gold, DELTA_PASS_THRESHOLD, msg=f"max gold delta {max_gold}")
        self.assertLess(sum(deltas) / len(deltas), DELTA_PASS_THRESHOLD * 0.85)

    def test_verbose_lecture_delta_high(self) -> None:
        profile = load_profile(PROFILE_PATH, GOLD_DIR)
        feats = extract_features(VERBOSE_LECTURE_HTML)
        delta = burrows_delta(feats, profile)
        self.assertGreater(delta, DELTA_PASS_THRESHOLD)
        self.assertGreater(feats["hedge_per_1k"], profile["mean"]["hedge_per_1k"])


if __name__ == "__main__":
    unittest.main()
