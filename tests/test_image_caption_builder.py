#!/usr/bin/env python3
"""Tests for human image alt/caption builder and gate."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.excalibur_blog_image_caption_builder import (
    apply_article_captions,
    build_cover_alt,
    build_inline_alt,
    collect_article_alts,
    is_prompt_like_alt,
    resolve_slot_alt,
)


class ImageCaptionBuilderTests(unittest.TestCase):
    def test_detects_prompt_like_cover_alt(self) -> None:
        bad = "Святослав в кардигане смотрит на телефон продавца; hook; CTA; стикер."
        prompt_like, errors = is_prompt_like_alt(bad)
        self.assertTrue(prompt_like)
        self.assertTrue(any("banned" in e or "semicolon" in e for e in errors))

    def test_accepts_human_inline_alt(self) -> None:
        good = "Таблица норма vs осмотр: цена, аванс, пауза, «как сказали»."
        prompt_like, errors = is_prompt_like_alt(good)
        self.assertFalse(prompt_like, msg=str(errors))

    def test_build_cover_alt_from_bad_raw(self) -> None:
        manifest = {
            "cover_hook": "Родственники остановили продажу до аванса",
            "cover_motifs": {"outfit": "sage_olive_cardigan"},
            "slots": {
                "cover": {
                    "alt": "Святослав в кардигане смотрит на телефон продавца; hook; CTA; стикер.",
                    "cover_emotion": "насторожённость",
                    "sticky": "Хорошо, что не внесли аванс",
                }
            },
        }
        meta = {
            "h1": "Пожилого продавца вели по телефону — родственники сорвали сделку",
            "slug": "v-tyumeni-rodstvenniki-ostanovili-prodazhu",
        }
        alt = build_cover_alt(manifest, meta, host_name="Святослав Шакин")
        prompt_like, errors = is_prompt_like_alt(alt)
        self.assertFalse(prompt_like, msg=f"{alt!r} errors={errors}")
        self.assertIn("Святослав", alt)
        self.assertIn("Тюмени", alt)
        self.assertNotIn("hook", alt.casefold())
        self.assertNotIn("cta", alt.casefold())

    def test_build_inline_alt_from_labels(self) -> None:
        slot = {
            "visual_type": "comparison_table",
            "h2_anchor": "Цена согласована — и внезапно телефон не отпускали",
            "alt": "comparison_table Норма vs Осмотр; labels facts; NO human",
            "labels": ["Цена согласована", "«Как сказали»", "Кто решает"],
        }
        alt = build_inline_alt(slot, labels_map={"comparison_table": "Сравнительная таблица"})
        prompt_like, _ = is_prompt_like_alt(alt)
        self.assertFalse(prompt_like)
        self.assertIn("Сравнительная таблица", alt)
        self.assertIn("Цена согласована", alt)

    def test_cover_alt_idempotent_when_hook_already_present(self) -> None:
        hook = "Договор подписали — квартиру продали другим"
        visual = (
            "Святослав Шакин в терракотовом поло рвёт предварительный договор "
            "в переговорной в Тюмени. Договор подписали — квартиру продали другим."
        )
        manifest = {
            "cover_hook": hook,
            "slots": {"cover": {"alt": visual}},
        }
        meta = {
            "h1": "В Тюмени подписали предварительный — продавец продал квартиру другим",
            "slug": "v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim",
        }
        alt = build_cover_alt(manifest, meta, host_name="Святослав Шакин")
        self.assertEqual(alt, visual)
        self.assertEqual(alt.count("Договор подписали"), 1)

    def test_cover_alt_dedupes_repeated_hook_sentences(self) -> None:
        hook = "Договор подписали — квартиру продали другим"
        bloated = (
            "Святослав Шакин в терракотовом поло рвёт предварительный договор в Тюмени. "
            f"{hook}. {hook}. {hook}."
        )
        manifest = {"cover_hook": hook, "slots": {"cover": {"alt": bloated}}}
        meta = {"slug": "v-tyumeni-podpisali-predvaritelnyj"}
        alt = build_cover_alt(manifest, meta, host_name="Святослав Шакин")
        self.assertEqual(alt.count("Договор подписали"), 1)
        self.assertFalse(is_prompt_like_alt(alt)[0], msg=alt)

    def test_apply_cover_alt_twice_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp) / "B15-test"
            cover_dir = article_dir / "cover"
            cover_dir.mkdir(parents=True)
            hook = "Договор подписали — квартиру продали другим"
            visual = (
                "Святослав Шакин в терракотовом поло рвёт предварительный договор "
                f"в переговорной в Тюмени. {hook}."
            )
            manifest = {"cover_hook": hook, "slots": {"cover": {"alt": visual}}}
            (cover_dir / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            (article_dir / "article.meta.json").write_text(
                json.dumps(
                    {
                        "h1": "В Тюмени подписали предварительный — продавец продал квартиру другим",
                        "slug": "v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            root = Path(__file__).resolve().parents[1]
            apply_article_captions(article_dir, root)
            second = apply_article_captions(article_dir, root)
            cover_alt = json.loads((cover_dir / "quad-manifest.json").read_text(encoding="utf-8"))[
                "slots"
            ]["cover"]["alt"]
            self.assertEqual(cover_alt.count("Договор подписали"), 1)
            self.assertFalse(any("cover:" in c for c in second["changes"]))
            self.assertTrue(second["gate"]["all_pass"])

    def test_apply_updates_manifest_and_html(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp) / "B10-test"
            cover_dir = article_dir / "cover"
            cover_dir.mkdir(parents=True)
            manifest = {
                "cover_hook": "Стоп до аванса",
                "slots": {
                    "cover": {
                        "alt": "Святослав в жилете; hook; CTA; мемы.",
                        "cover_emotion": "тревога",
                    },
                    "inline_1": {
                        "h2_anchor": "Финал: сделку остановили",
                        "visual_type": "process_flow",
                        "alt": "process_flow 5 steps; NO human",
                        "labels": ["Стоп до аванса", "Без денег"],
                    },
                },
            }
            (cover_dir / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2),
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
                    '  <img src="cover/inline-01.png" alt="process_flow 5 steps; NO human" loading="lazy">\n'
                    "</figure>\n"
                ),
                encoding="utf-8",
            )

            root = Path(__file__).resolve().parents[1]
            result = apply_article_captions(article_dir, root)
            self.assertTrue(result["changes"])
            updated = json.loads((cover_dir / "quad-manifest.json").read_text(encoding="utf-8"))
            cover_alt = updated["slots"]["cover"]["alt"]
            self.assertFalse(is_prompt_like_alt(cover_alt)[0], msg=cover_alt)
            html = (article_dir / "article.html").read_text(encoding="utf-8")
            self.assertNotIn("NO human", html)
            gate = collect_article_alts(article_dir, root)
            self.assertTrue(gate["all_pass"])


if __name__ == "__main__":
    unittest.main()
