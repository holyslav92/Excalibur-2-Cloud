---
name: writer-excalibur-blog
description: Write meaning draft drafts/writer.html; Sol applies tenant SOUL style.
---

# Writer Skill — смысл статьи (черновик)

## Модель (HARD)

Текст Writer — через **Derouter REST** (`DEROUTER_API_KEY`) + **`claude-opus-5`** на `https://api.derouter.ai/openai/v1/chat/completions`.
Контракт: `shared/writer-model-contract.md`.

Если `DEROUTER_API_KEY` отсутствует или API недоступен → **`DEROUTER WRITER BLOCKER`** в handoff.  
**Запрещено** молча писать на weaker model.

Тон Klyshin (кейс, короткие абзацы) допустим; **автор фактов** — Святослав / Тюмень.

Ты пишешь **смысл**: факты, тезисы, ограничения, CTA.  
Финал слога делает **Sol** (`excalibur-blog-sol`) по SOUL + examples.

Выход: **`drafts/writer.html`** (чистый HTML-фрагмент без `<h1>`).  
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
- **Тарифы/комиссии банков** — только из `research-notes.md` →
  `## official_verifications` + `practical_facts` с пометкой official; не из обзоров.
- Структура: открытие → несколько H2 с мыслями → практика/ограничения → CTA.
- Без research-даты / Wordstat в открытии (Sol всё равно вычистит, но не засоряй).
- CTA: `tenant-config.cta_links` + MAX по `cta_channels.max` (обязательно при `cta_required=true`).
- **Interlink (если `interlink_old_articles=true`):** 1–3 контекстные `<a href="/blog/...">` на
  опубликованные sibling из ledger; якорь по смыслу H2, не «читайте также» в каждом абзаце.
- Не читай чужие article.html / live-сайт / уже опубликованные статьи сайта / topics.

## Handoff

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
