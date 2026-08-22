## LESSON-20260822-1109-B08-writer-sol-compression-gap
status: proposed
topic_id: B08
category: structure
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: Sol inputs (sol-part1/2/3-user.md) — Writer ~3243 слов, HARD ceiling 2000–2600; quality-bar-9 итог word_count 2439 (внутри коридора после Sol).
- artifact: sol-part3-user-retry.md — chunk 3 retry с пометкой «СЖАТЬ».
- artifact: quality-bar-9.json — `word_count_2000_2600: true`, metrics.word_count 2439.
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- LOW_SAMPLE (Metrika absent)

### Keep
- Sol chunking + retry на part 3 уложил текст без потери 4 interlinks и 7 inline figures.
- Quality-bar gate как финальный стоппер перегруза — PASS после Sol, не после Writer.

### Change
- Writer assembled inputs: soft target ~2800 слов (не 3200+) на document-heavy casus, чтобы Sol не тратил retry на сжатие.
- Sol brief: при Writer >3000 — приоритет сжатия checklist/повторов, не фактов из research-notes.

### Never again
- Считать Writer draft «готовым к publish» по объёму — только Sol + quality-bar-9.

### Proposed apply
- Мониторить Writer word_count в assembled-writer-inputs / post-Writer lint; alert при >3000 до Sol.
- Durable только после ≥2 runs с тем же gap (B08 — первый задокументированный кейс).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
wp_post_id: 9073
