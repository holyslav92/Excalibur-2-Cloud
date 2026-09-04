#!/usr/bin/env python3
"""Tests for human image alt/caption builder and gate."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.excalibur_blog_image_caption_builder import (
    ALT_SEO_MAX,
    ALT_SEO_MIN,
    apply_article_captions,
    build_cover_alt,
    build_inline_alt,
    collect_article_alts,
    cover_caption_must_be_empty,
    is_prompt_like_alt,
    resolve_slot_alt,
    scene_painting_hits,
)


class ImageCaptionBuilderTests(unittest.TestCase):
    def test_detects_prompt_like_cover_alt(self) -> None:
        bad = "Святослав в кардигане смотрит на телефон продавца; hook; CTA; стикер."
        prompt_like, errors = is_prompt_like_alt(bad, seo_length=False)
        self.assertTrue(prompt_like)
        self.assertTrue(any("banned" in e or "semicolon" in e for e in errors))

    def test_detects_b20_scene_hint_dump(self) -> None:
        bad = (
            "Святослав Шакин покупатель сравнивает два договора и реквизиты застройщика "
            "у стойки регистрации, рядом лежит папка с документами и отображается таймер брони "
            "в Тюмени. Застройщик сменил компанию — бронь зависла."
        )
        hits = scene_painting_hits(
            bad,
            host_name="Святослав Шакин",
            scene_hint="Светлый МФЦ: герой сравнивает два ДДУ, рядом таймер 72 часа",
        )
        self.assertTrue(hits)
        prompt_like, errors = is_prompt_like_alt(
            bad,
            host_name="Святослав Шакин",
            seo_length=True,
        )
        self.assertTrue(prompt_like, msg=str(errors))

    def test_accepts_human_seo_cover_alt(self) -> None:
        good = (
            "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу: "
            "что проверить в новом ДДУ перед подписью."
        )
        prompt_like, errors = is_prompt_like_alt(good, seo_length=True)
        self.assertFalse(prompt_like, msg=str(errors))
        self.assertGreaterEqual(len(good), ALT_SEO_MIN)
        self.assertLessEqual(len(good), ALT_SEO_MAX)

    def test_build_cover_alt_empty_for_theme_leak(self) -> None:
        manifest = {
            "cover_hook": "Застройщик сменил компанию — бронь зависла",
            "slots": {
                "cover": {
                    "alt": "Святослав Шакин покупатель сравнивает два договора у стойки регистрации, рядом лежит папка",
                    "scene_hint": "МФЦ: два ДДУ, таймер брони",
                }
            },
        }
        meta = {
            "h1": "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу",
            "slug": "v-tyumeni-zastrojschik-smenil-yurlico",
        }
        alt = build_cover_alt(manifest, meta, host_name="Святослав Шакин")
        self.assertEqual(alt, "")
        prompt_like, errors = is_prompt_like_alt(alt, allow_empty=True, seo_length=False)
        self.assertFalse(prompt_like, msg=str(errors))

    def test_build_inline_alt_from_labels(self) -> None:
        slot = {
            "visual_type": "comparison_table",
            "h2_anchor": "Цена согласована — и внезапно телефон не отпускали",
            "alt": "comparison_table Норма vs Осмотр; labels facts; NO human",
            "labels": ["Цена согласована", "«Как сказали»", "Кто решает"],
        }
        alt = build_inline_alt(slot, labels_map={"comparison_table": "Сравнительная таблица"}, meta={"h1": "Тюмень"})
        prompt_like, _ = is_prompt_like_alt(alt, seo_length=True)
        self.assertFalse(prompt_like)
        self.assertNotIn("иллюстрация", alt.casefold())
        self.assertNotIn("сравнительная таблица с колонками", alt.casefold())

    def test_cover_caption_must_be_empty(self) -> None:
        ok, errors = cover_caption_must_be_empty("Подпись, которую Дзен покажет как текст")
        self.assertFalse(ok)
        self.assertTrue(errors)
        ok2, _ = cover_caption_must_be_empty("")
        self.assertTrue(ok2)

    def test_apply_updates_manifest_registry_and_html(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp) / "B10-test"
            cover_dir = article_dir / "cover"
            cover_dir.mkdir(parents=True)
            manifest = {
                "cover_hook": "Стоп до аванса",
                "slots": {
                    "cover": {
                        "alt": "Святослав у стойки регистрации, рядом лежит папка с документами",
                        "cover_emotion": "тревога",
                        "scene_hint": "МФЦ, два договора",
                    },
                    "inline_1": {
                        "h2_anchor": "Финал: сделку остановили",
                        "visual_type": "process_flow",
                        "alt": "На стойке продаж лежат ДДУ, рядом таймер 72 часа",
                        "labels": ["Стоп до аванса", "Без денег"],
                    },
                },
            }
            (cover_dir / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            (cover_dir / "cover-registry.json").write_text(
                json.dumps(
                    {
                        "alt": manifest["slots"]["cover"]["alt"],
                        "assets": [
                            {
                                "role": "cover",
                                "slot": "cover",
                                "file": "cover/cover.png",
                                "alt": manifest["slots"]["cover"]["alt"],
                                "caption": manifest["slots"]["cover"]["alt"],
                            }
                        ],
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            (article_dir / "article.meta.json").write_text(
                json.dumps(
                    {
                        "h1": "Четыре месяца искали квартиру — суд оспорил сделку",
                        "slug": "v-tyumeni-chetyre-mesyaca-iskali-kvartiru",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            (article_dir / "article.html").write_text(
                (
                    '<h2>Финал: сделку остановили</h2>\n'
                    '<figure class="inline-quad" data-slot="inline_1">\n'
                    '  <img src="cover/inline-01.png" alt="На стойке продаж лежат ДДУ" loading="lazy">\n'
                    "</figure>\n"
                ),
                encoding="utf-8",
            )

            root = Path(__file__).resolve().parents[1]
            result = apply_article_captions(article_dir, root)
            self.assertTrue(result["changes"])
            updated = json.loads((cover_dir / "quad-manifest.json").read_text(encoding="utf-8"))
            cover_alt = updated["slots"]["cover"]["alt"]
            self.assertEqual(cover_alt, "")
            registry = json.loads((cover_dir / "cover-registry.json").read_text(encoding="utf-8"))
            self.assertEqual(registry["assets"][0].get("caption"), "")
            html = (article_dir / "article.html").read_text(encoding="utf-8")
            self.assertNotIn("На стойке продаж", html)
            gate = collect_article_alts(article_dir, root)
            self.assertTrue(gate["all_pass"])


if __name__ == "__main__":
    unittest.main()
