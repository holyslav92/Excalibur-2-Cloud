"""HARD Scout story-duplicate gate — near-clone legal risk + plot vs published siblings."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_scout_story_dup import (  # noqa: E402
    build_published_story_sources,
    check_story_duplicate,
    cluster_matches,
    detect_story_clusters,
    load_story_clusters,
)


class ScoutStoryDupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.clusters = load_story_clusters(ROOT)
        cls.sources = build_published_story_sources(ROOT, live_limit=20)

    def test_inheritance_cluster_matches_b07_style_hook(self) -> None:
        blob = (
            "Наследству на квартиру два года. Сын от первого брака отказ не писал "
            "nasledstvo-kvartiry-syn-ot-pervogo-braka"
        )
        ids = detect_story_clusters(blob, self.clusters)
        self.assertIn("inheritance_son_first_marriage_no_refusal", ids)

    def test_inheritance_cluster_matches_aug19_slug_tokens(self) -> None:
        blob = "Сын от первого брака без отказа аванс nasledstvo-ne-proshlo-tri-goda"
        cluster = next(c for c in self.clusters if c["id"] == "inheritance_son_first_marriage_no_refusal")
        self.assertTrue(cluster_matches(blob, cluster))

    def test_near_clone_blocked_against_live_siblings(self) -> None:
        candidate = (
            "Наследство квартиры: сын от первого брака отказ не оформлен "
            "nasledstvo syn pervogo braka otkaz"
        )
        warnings = check_story_duplicate(candidate, self.sources, self.clusters)
        self.assertTrue(warnings, "expected STORY DUPLICATE vs published/live sibling")
        self.assertTrue(
            any(w["cluster_id"] == "inheritance_son_first_marriage_no_refusal" for w in warnings),
            warnings,
        )

    def test_unrelated_topic_passes(self) -> None:
        candidate = "Проверка ЕГРН перед авансом на вторичку в Тюмени"
        warnings = check_story_duplicate(candidate, self.sources, self.clusters)
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
