"""HARD Scout story-duplicate gate — near-clone legal risk + plot vs published siblings."""
from __future__ import annotations

import sys
import unittest
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_scout_story_dup import (  # noqa: E402
    anti_repeat_days,
    build_published_story_sources,
    check_locked_clusters,
    check_story_duplicate,
    detect_story_clusters,
    load_story_clusters,
    parse_iso_date,
    sync_used_clusters,
    within_anti_repeat_window,
)


class ScoutStoryDupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.clusters = load_story_clusters(ROOT)
        cls.sources = build_published_story_sources(ROOT, live_limit=20)

    def test_anti_repeat_window_is_30_days(self) -> None:
        self.assertEqual(anti_repeat_days(ROOT), 30)

    def test_inheritance_cluster_matches_b07_style_hook(self) -> None:
        blob = (
            "Наследству на квартиру два года. Сын от первого брака отказ не писал "
            "nasledstvo-kvartiry-syn-ot-pervogo-braka"
        )
        ids = detect_story_clusters(blob, self.clusters)
        self.assertIn("inheritance_son_first_marriage_no_refusal", ids)

    def test_marital_share_notary_cluster_matches_aug27(self) -> None:
        blob = (
            "Нотариус не выделил супружескую долю — аванс остановили "
            "notarius-18-let-nazad-vse-proveril supruzheskaya"
        )
        ids = detect_story_clusters(blob, self.clusters)
        self.assertIn("marital_share_heirs_notary_checked", ids)

    def test_elderly_phone_cluster_matches_b10(self) -> None:
        blob = "Пожилого продавца вели по телефону — родственники сорвали сделку"
        ids = detect_story_clusters(blob, self.clusters)
        self.assertIn("elderly_seller_led_by_phone", ids)

    def test_near_clone_blocked_against_live_siblings(self) -> None:
        candidate = (
            "Наследство квартиры: сын от первого брака отказ не оформлен "
            "nasledstvo syn pervogo braka otkaz"
        )
        warnings = check_story_duplicate(candidate, self.sources, self.clusters, root=ROOT)
        self.assertTrue(warnings, "expected STORY DUPLICATE vs published/live sibling")
        self.assertTrue(
            any(w["cluster_id"] == "inheritance_son_first_marriage_no_refusal" for w in warnings),
            warnings,
        )

    def test_locked_cluster_blocks_even_new_title(self) -> None:
        candidate = "Новый заголовок: супружеская доля и нотариус всё проверил — аванс стоп"
        locked = check_locked_clusters(
            detect_story_clusters(candidate, self.clusters),
            ROOT,
            today=date(2026, 8, 27),
        )
        self.assertTrue(
            any(w["cluster_id"] == "marital_share_heirs_notary_checked" for w in locked),
            locked,
        )

    def test_unrelated_topic_passes(self) -> None:
        candidate = "Аккредитив в Тюмени: банк отказал перевод без эскроу-счёта"
        warnings = check_story_duplicate(candidate, self.sources, self.clusters, root=ROOT)
        self.assertEqual(warnings, [])

    def test_old_source_outside_window_excluded(self) -> None:
        today = date(2026, 9, 30)
        old = today - timedelta(days=31)
        self.assertFalse(within_anti_repeat_window(old, today, 30))
        sources = build_published_story_sources(ROOT, live_limit=0, window_days=30, today=today)
        ledger_dates = [s.get("date") for s in sources if s.get("source") == "ledger"]
        self.assertTrue(all(d == "" or parse_iso_date(d) >= today - timedelta(days=30) for d in ledger_dates))

    def test_sync_used_clusters_writes_file(self) -> None:
        payload = sync_used_clusters(ROOT, live_limit=20, today=date(2026, 8, 27), dry_run=True)
        self.assertGreaterEqual(len(payload.get("clusters") or []), 9)
        self.assertEqual(payload.get("anti_repeat_days"), 30)


if __name__ == "__main__":
    unittest.main()
