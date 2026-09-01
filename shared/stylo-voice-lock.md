# Stylo voice lock — голос vs сюжет

**Owner:** Святослав Шакин (The Риэлтор).  
**Статус:** канон пайплайна (код + memory/stylo), **не** ослабляет newbuild-only, quality-bar 9, kitchen-table, composite disclaimer.

## Что это

После **Sol** Python-измеритель сравнивает `article.html` с **GOLD STYLE** — ритм и голос Dzen-hit постов.  
Сюжеты gold-корпуса **заморожены** (вторичные хиты + один ужатый newbuild). Scout **не** берёт оттуда plot.

Максимум **один** дополнительный проход Sol с числовыми заметками, если `stylo_pass: false`.  
Никогда 3+ переписок. Stylo **не** публикует.

## Gold corpus

- Тексты: `memory/stylo/gold/*.txt`
- Мета: `memory/stylo/gold/meta.json` (url, title, `plot_for_scout: false`)
- Профиль: `memory/stylo/profile.json` (centroid + std)
- История: `memory/stylo/history.jsonl`

Обновление gold с live:

```bash
python3 scripts/excalibur_blog_stylo_fetch_gold.py
python3 scripts/excalibur_blog_stylo_learn.py --recompute
```

## Измерение

```bash
python3 scripts/excalibur_blog_stylo.py \
  --article-dir memory/blog/articles/<topic>-<slug> \
  --gold-dir memory/stylo/gold \
  --output memory/blog/articles/<topic>-<slug>/stylo-report.json
```

Пишет `stylo-report.json` и `stylo-notes.md` (короткие русские bullets только по осям с отклонением).

**Оси:** длина предложений/абзацев, служебные слова, TTR/hapax, тире/«ёлочки», я/мы, hedge-лексика, юртермины, лид (число, длина), spine-overlap лид↔финал.

**Gate:** `stylo_pass: true` если Burrows-like Delta ≤ порога (`DELTA_PASS_THRESHOLD` в `excalibur_blog_stylo.py`, калиброван unittest на gold vs verbose lecture).

## Пайплайн

```text
Writer → Sol → Stylo → [≤1 Sol с stylo-notes] → stamp → Description → …
```

Агент: `excalibur-blog-stylo` (`Task`). Skill: `stylo-excalibur-blog`.

При `stylo_pass: false` — **один** вызов Derouter `--role sol` с `stylo-notes.md` + `drafts/writer.html` + текущий `article.html`. Перезаписать `article.html`, снова `excalibur_blog_stylo.py`, **стоп** (даже если снова fail — лог, без цикла).

**Запрещено:** менять факты/сюжет; возвращать вторичный casus; ослаблять newbuild lock; бесконечные rewrite-loop «до 9.0».

## Self-learn

После каждого measure — append в `history.jsonl`:

```json
{"date":"…","topic_id":"B111","features":{…},"delta":1.2,"stylo_pass":true,"sol_rewrite":false,"good":null}
```

Пометка удачного голоса:

```bash
python3 scripts/excalibur_blog_stylo_learn.py --mark B111 good
python3 scripts/excalibur_blog_stylo_learn.py --recompute
```

`good=true` тянет centroid; `bad` не добавляется в centroid (anti-пул на будущее).

## Scout

Gold URL/тексты — **только style-gold**. `plot_for_scout: false` в meta.  
Scout по-прежнему: Wordstat × news-casus × **newbuild_only** × 30d anti-repeat.
