## LESSON-20260828-1310-B12-sol-tighten-writer-over-2600
status: proposed
topic_id: B12
category: structure
confidence: medium

### Evidence
- artifact: drafts/writer.html (word count script)
  finding: Writer draft ~2904 words (quality-bar gate would FAIL `word_count_2000_2600` on raw writer).
- artifact: assembled-sol-inputs.md
  finding: explicit Sol brief: «2000–2600 слов (НЕ больше 2600; writer ~2904 — ужать без потери фактов)».
- artifact: quality-bar-9.json
  finding: final `word_count: 2558`, `word_count_2000_2600: true`; 9 H2, 7 inline figures, 3 sibling interlinks — all PASS.
- artifact: article.html
  finding: Sol preserved comment magnet, early TG+MAX, factual spine (эскроу/ДДУ/ипотека/214-ФЗ) after ~346-word trim.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- WRITER_OVER_WORDCOUNT_CAP
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Sol как единственный стилевой слой, который также ужимает объём до quality-bar cap без возврата Writer.
- Жёсткий brief в `assembled-sol-inputs.md` с явным word-count target — Sol сжал без потери 9 H2 / 7 inline / comment magnet.

### Change
- Writer brief: target 2200–2500 слов на research-heavy novostroyka/ДДУ темах, чтобы Sol не тратил токены на массовое сжатие (>300 слов).
- При writer >2800 до Sol — Director flag «pre-sol trim needed» (optional Sol part regen vs Writer one-pass shorten).

### Never again
- Публиковать writer.html напрямую при >2600 слов.
- Расширять Writer master-prompt автоматически — proposals только в content-lessons.

### Proposed apply
- `assembled-writer-inputs.md` template: add «target 2200–2500 words» for article_mode B news-casus with 7+ H2.
- После второго run с writer>2800 + sol-trim>300w без quality loss → human review Writer length guard.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-klyuchi-ot-novostrojki-v-tyumeni-perenesli-na-god-dengi-na-eskrou-zamorozili
wp_post_id: 9250
