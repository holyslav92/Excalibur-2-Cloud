---
name: writer-excalibur-blog
description: Write meaning draft drafts/writer.html; Sol applies tenant SOUL style.
---

# Writer Skill — смысл статьи (черновик)

## OWNER LOCK (permanent)

1. **Dzen engagement** — читай `shared/dzen-engagement-lock.md`: CTR (Title), read-through (один casus, ~1400–1600 слов), comments (bipolar-вопрос после финала), subs (голос Святослава, early TG+MAX, agency ending). **Newbuild focus:** `shared/newbuild-focus-lock.md`. **Запрещено:** TL;DR, «Быстрый инсайт», bullets до первого H2, checklist/how-to в лиде; table+list+«главный вывод» в хвосте; self-score 9.0 loop; квота 1800+ слов.
2. Meme/cover — не зона Writer; см. Cover skill + `meme_canon_v1`.
3. Cover fail-fast — не зона Writer; Cover agent: max 2 attempts, ≤15–20 min.

Канон: `shared/pipeline-canon.json` → `owner_lock_permanent`, `shared/dzen-engagement-lock.md`, `shared/newbuild-focus-lock.md`, `shared/dzen-news-casus.md`.

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
**Dzen engagement lock:** `shared/dzen-engagement-lock.md` — **~1400–1600 слов** (~10 мин Дзен max), **spine once**, brand+phone в теле, таблицы с разными колонками, лоты только из research или «как пример». **Без** self-score 9.0 loop и critic-таблицы в HTML.
Можно положить ту же копию во временный `article.html`, но канон —
`drafts/writer.html`. Sol перепишет `article.html`.

## Читаешь

1. `shared/writer-master-prompt.md` (секция Writer / смысл)
2. `shared/dzen-engagement-lock.md` — **HARD** read-through / comments / subs
3. `shared/newbuild-focus-lock.md`
4. `research-notes.md`
5. `title-brief.json`
6. `published-titles-only.md`
7. `shared/published-articles.md` — **только** `status=published` для outbound interlink
8. `shared/dzen-content-rules.md` + RF (не герой Meta/…) — кратко
9. `shared/dzen-news-casus.md` — **default news-casus shape** (история → финал → практика после)

## Не обязан читать (это зона Sol)

`shared/SOUL.md`, `shared/soul-examples/*` — Sol применит слог сам.
Можешь писать ясно по-русски без SEO; не трать ход на косплей тенанта.

## Правила смысла

- Все факты только из research; не выдумывай.
- **Default shape = новость-казус** (`shared/dzen-news-casus.md`): лид — завершённое событие; середина — хронология; **финал обязателен** (суд, отмена, деньги не вернули). Без финала — FAIL (урок «Расписку написали»).
- **Практика после истории**, не вместо неё: «что проверить теперь» — разбор последствий casus, не сухой how-to в лиде.
- **Spine once (one-breath):** casus **один раз** — лид → развитие → финал → **практика один раз** → agency ending. **Не** пересказывать ту же сцену в лиде, середине и «итоге». **Вырезать:** recap («коротко если некогда»), повтор одних цифр/флагов трижды, lecture-хвосты. **Запрещено в хвосте:** table + list + «главный вывод» подряд.
- Структура: **hook + прозаический лид (4–6 предложений, news-casus)** → **early CTA (TG+MAX only)** → H2 развитие casus → H2 **финал** → H2 практика (ol/таблица — aftermath, **один блок**, не главный hook) → **comment magnet (bipolar-вопрос сразу после финала casus)** → **ending landing (1–2 абзаца: agency, not panic)** → **end CTA**. **5–8 H2** — не раздувать ради картинок.
- **Ending landing (owner lock):** casus остаётся горячим; последние 1–2 абзаца **до** end CTA — читатель уходит с **ручкой**: остановили бронь/ДДУ до денег / проверка эскроу спасла / разобрали договор до аванса. **Не** «все риэлторы плохие», «вторичка — мина», «риски везде — как покупать». Редко: жёсткая потеря OK, если вилка «если бы X до аванса — не потеряли»; never pure dread без действия. **Ban:** sugar happy ending; чеклист N шагов как эмоциональный финал.
- **Запрещено в первом экране:** английский TL;DR; «Быстрый инсайт» / «быстрый инсайдер»; bullet-списки `<ul>/<ol>` до первого H2.
- **Comment magnet:** один острый **bipolar**-вопрос — **сразу после** финала casus (`title-brief.json` → `comment_magnet_angle` если есть). Не «а вы как считаете, друзья».
- **Запрещено как каркас:** открытие «чеклист / N шагов / как купить без риелтора» без завершённого события.
- Без research-даты / Wordstat в открытии (Sol всё равно вычистит, но не засоряй).
- CTA conversion: early после лида (TG+MAX); телефон **+7 922 001 65 05** один раз в теле; ending agency not panic.
- **Interlink (если `interlink_old_articles=true`):** **2–4** контекстные `<a href="/blog/...">` на
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
