---
name: writer-excalibur-blog
description: Write meaning draft drafts/writer.html; Sol applies tenant SOUL style.
---

# Writer Skill — смысл статьи (черновик)

## Модель (HARD) — thin conductor

**Не пиши прозу моделью Cursor.** Собери `--user-file` из research/title-brief и вызови Derouter powerful tier (claude-opus-5):

```bash
python3 scripts/excalibur_blog_writer_chunk.py \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file <assembled-writer-inputs.md> \
  --output drafts/writer.html \
  --article-dir <article_dir>
```

Longform (7 inline): **3 части на первом проходе** — не ждать HTTP 524. `--single-shot` только для коротких статей.

Контракт: `shared/derouter-opus-brain-contract.md`.
`DEROUTER WRITER BLOCKER` → стоп. Запрещён тихий fallback на Composer/Auto.

Тон Klyshin (кейс, короткие абзацы) допустим; **автор фактов** — Святослав / Тюмень.

Ты пишешь **смысл**: факты, тезисы, ограничения, CTA.  
Финал слога делает **Sol** (`excalibur-blog-sol`) по SOUL + examples.

Выход: **`drafts/writer.html`** (чистый HTML-фрагмент без `<h1>`).  
**Quality bar:** ориентир `shared/quality-bar-9.md` — 2000–2600 слов после Sol, brand+phone в теле, таблицы с разными колонками, лоты только из research или «как пример».
Можно положить ту же копию во временный `article.html`, но канон —
`drafts/writer.html`. Sol перепишет `article.html`.

## Читаешь

1. `shared/writer-master-prompt.md` (секция Writer / смысл)
2. `research-notes.md`
3. `title-brief.json`
4. `published-titles-only.md`
5. `shared/published-articles.md` — **только** `status=published` для outbound interlink
6. `shared/dzen-content-rules.md` + RF (не герой Meta/…) — кратко

## Не обязан читать (это зона Sol)

`shared/SOUL.md`, `shared/soul-examples/*` — Sol применит слог сам.
Можешь писать ясно по-русски без SEO; не трать ход на косплей тенанта.

## Правила смысла

- Все факты только из research; не выдумывай.
- Структура: открытие + TL;DR (`<p><b>Коротко…</b></p>` + список, **не** `<h2>`) → **early CTA (TG+MAX only, до первого H2)** → H2 с мыслями → главный чеклист → **mid CTA** → практика → **end CTA** (dual + полный набор каналов; внутренние ссылки `/blog/...`, `/gajdy/`, `/` — без `{{SITE_BASE}}`).
- Без research-даты / Wordstat в открытии (Sol всё равно вычистит, но не засоряй).
- CTA conversion: early/mid/end по `shared/quality-bar-9.md`; PRIMARY — Telegram + MAX URL из `cta_channels`; телефон один раз в теле.
- **Interlink (если `interlink_old_articles=true`):** **2–4** контекстные `<a href="/blog/...">` на
  опубликованные sibling из ledger; якорь по смыслу H2, не «читайте также» в каждом абзаце.
- **Реестры (reestr-nasled.ru):** plain text в prose, не `<a href>` — link_verify падает на DNS из Cloud.
- Не читай чужие article.html / live-сайт / уже опубликованные статьи сайта / topics.

## Handoff

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
