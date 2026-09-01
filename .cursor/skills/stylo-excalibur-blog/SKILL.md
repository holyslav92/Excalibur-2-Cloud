---
name: stylo-excalibur-blog
description: "Stylo: measure voice vs gold; at most one Sol pass with numeric notes."
---

# Stylo — voice coach (стилометрия)

## Когда

**После Sol** (`article.html` готов). **До** `pipeline_canon --stamp` и Description.  
Не публикует. Не трогает Scout/Research.

Контракт: `shared/stylo-voice-lock.md`.

## Шаг 1 — измерить

```bash
python3 scripts/excalibur_blog_stylo.py \
  --article-dir <article_dir> \
  --gold-dir memory/stylo/gold \
  --output <article_dir>/stylo-report.json
```

Читает `stylo-report.json` → `stylo_pass`, `delta`, `stylo-notes.md`.

## Шаг 2 — при FAIL: один Sol (не больше)

Только если `stylo_pass: false` **и** ещё не было `sol_rewrite` в этом run:

1. Собери `drafts/stylo-sol-input.md`:
   - `stylo-notes.md`
   - `drafts/writer.html` (факты — не менять)
   - текущий `article.html`
   - явная инструкция: править **только ритм/голос** по осям notes; не факты, не сюжет, не newbuild→вторичка.

2. Один вызов Derouter:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role sol \
  --system-file agents/excalibur-blog-sol.md \
  --user-file drafts/stylo-sol-input.md \
  --output article.html \
  --article-dir <article_dir>
```

3. Повтори measure с `--sol-rewrite`:

```bash
python3 scripts/excalibur_blog_stylo.py \
  --article-dir <article_dir> \
  --gold-dir memory/stylo/gold \
  --output <article_dir>/stylo-report.json \
  --sol-rewrite
```

4. **Стоп.** Даже при повторном FAIL — только лог; не третий Sol. Директор идёт дальше (stamp / quality-bar).

## Запрещено

- 2+ stylo-driven Sol за один пост
- Менять факты, H2-смысл, newbuild-фокус
- Подтягивать сюжеты из `memory/stylo/gold` в Scout
- Ослаблять composite disclaimer / 1400–1600 kitchen-table / quality-bar 9
- Писать прозу Cursor-моделью (только Derouter `--role sol`)

## Self-learn (опционально, post-publish)

```bash
python3 scripts/excalibur_blog_stylo_learn.py --mark <topic_id> good
python3 scripts/excalibur_blog_stylo_learn.py --recompute
```

Agent: `agents/excalibur-blog-stylo.md`
