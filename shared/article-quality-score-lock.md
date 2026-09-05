# Article quality score lock — Grok Bot 7.5–9 bar (HARD)

**Владелец:** Святослав Шакин  
**Дата:** 2026-09-05  
**Статус:** `LOCKED_ON_MAIN` — не ослаблять без явного owner override.

## Мандат

Owner оценивает live-посты по блокам: **H1 / lead / middle / finale / length / tone**.
Этот lock кодирует **структурные FAIL-критерии** в машинный гейт — без self-score-to-9.0 loop
и без бесконечных переписок Writer.

**Один repair:** при FAIL — максимум **один** Derouter `--role sol` (`gpt-6-astra`) с notes гейта,
повторное измерение, **стоп**. Cursor Composer **не** пишет тело.

Синхрон с `shared/dzen-engagement-lock.md` (read-through ~1400–1600, kitchen Russian, HIT lead,
Klyshin H1, agency ending, один bipolar-вопрос).

---

## Гейт

```bash
python3 scripts/excalibur_blog_quality_score_gate.py --article-dir memory/blog/articles/<topic>-<slug>
# опционально один repair-pass (Derouter Sol):
python3 scripts/excalibur_blog_quality_score_gate.py --article-dir <dir> --repair
```

Пишет `article-quality-score.json` с `sections.{h1,lead,middle,finale,length,tone}.pass` + `reasons[]`.
**Publish блокируется** без `all_pass: true` (наряду с `quality-bar-9.json`).

**Точка пайплайна:** после **Stylo** (финальная проза Sol+Stylo), **до** Description / Cover.

---

## 1) H1 — casus + число + удар во втором бите

**PASS:** Klyshin-ритм — событие, цифра/срок, consequence во втором бите (тире, глагол потери/остановки).

**FAIL:**
- спокойные «как устроена / что такое / разбор схемы / полный гайд / N шагов / чеклист / стоит ли покупать»
- SEO-хвосты, label-head без casus
- H1 без цифры/срока и без ударного второго бита

Источник: `title-brief.json` → `h1` / `title`, fallback `article.meta.json`.

---

## 2) Lead — 4–6 предложений, HIT в первых 1–2

**PASS:**
- прозаический лид **4–6 предложений** до первого H2 (early CTA не считается)
- **HIT** в предложении 1 (или первых двух): **casus + число + последствие**
- kitchen-table, конкретный день в комнате

**FAIL:**
- TL;DR / «Быстрый инсайт» / bullet-dump в первом экране
- disclaimer «случай собирательный / без фамилий / механика повторяется» (gate `no_composite_disclaimer`)
- лид <4 или >6 предложений
- первая строка без числа и без consequence-beat
- mandate «рубка» 1–2 предложения на весь текст (короткие удары — только в первой строке)

---

## 3) Middle — spine once (без тройного пересказа)

**PASS:** одна сцена casus проходит **один раз**; практика — **после** истории, коротко.

**FAIL — тройной пересказ (spine):**
- та же сцена/beat в **лиде + середине + финале** (n-gram overlap / spine_overlap)
- recap-маркеры: «коротко если некогда», «в двух словах», «подведём итог», «главное — запомните»
- повтор одних цифр/флагов трижды в разных зонах

---

## 4) Finale — agency not panic + один bipolar-вопрос

**PASS:**
- casus остаётся горячим; посадка = **ручка до аванса**, не «бегите»
- **один** острый bipolar-вопрос **сразу после** финала casus (comment magnet)
- финал не пересказывает середину третий раз

**FAIL:**
- pure dread без действия; takeaway «риски везде — как покупать»
- **учебный хвост** после casus: простыня 214-ФЗ / таблицы-гайды / длинный `<ul>`/`<ol>` **после** story-beat и **до** end CTA
- третий пересказ middle в closing-абзацах
- чеклист N шагов как **эмоциональный** финал

---

## 5) Length — engagement read-through

| Зона | Слова | Дзен |
|------|-------|------|
| Target | **1400–1600** | ~8–10 мин |
| Hard FAIL (новые посты) | **>1750** | >10 мин |

Короткость **не** FAIL, если spine once и heat сохранены. Padding до 1800+ — **FAIL**.

Синхрон: `shared/quality-bar-9.md`, `pipeline-canon.json` → `quality_bar_9` + `owner_lock_permanent.dzen_engagement`.

---

## 6) Tone — kitchen-table, не lawyer-blog

**PASS:** простой русский за кухонным столом; термин (ДДУ, эскроу) → сразу бытовой перевод.

**FAIL — lawyer phrases (примеры):**
- профессиональный участник рынка
- досудебная плоскость / досудебный порядок
- императив нормы / в силу положений
- следует констатировать
- собирательный случай (также lead FAIL)
- преддоговорный этап **без** мгновенного перевода (если звучит как lecture)

**FAIL:** checklist-first opening; English TL;DR.

---

## Repair path (один Sol)

1. Гейт → `article-quality-score.json` + `quality-score-notes.md`
2. Если FAIL и `sol_rewrite_applied != true`:
   - собрать `drafts/quality-score-sol-input.md` (notes + `drafts/writer.html` + `article.html`)
   - `excalibur_blog_derouter_opus_chat.py --role sol` → перезаписать `article.html`
   - повторный гейт с `--sol-rewrite`
3. **Стоп** — даже при повторном FAIL (лог, без цикла)

**Запрещено:** self-score 9.0 loop; Writer re-run; 2+ quality-score Sol за пост.

---

## Кто читает

Writer, Sol, Stylo, Director, `pipeline-canon.json` → `article_quality_score`,
`AGENTS.md`, `CLOUD-AUTOMATION.md`.
