## LESSON-20260829-1309-B15-sol-near-wordcount-cap
status: proposed
topic_id: B15
category: structure
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: `word_count_2000_2600: true`, metrics word_count **2588** (12 words below cap); h2_count 9, inline_figures 7 — all PASS.
- artifact: drafts/writer.html vs article.html
  finding: Sol expanded legal-practice blocks (ст.429/380/381/445, таблица мифов, 8-point checklist in H2) while keeping prose lead and ending landing; no second rewrite loop.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- Legal utility in H2 (таблица «миф vs факт», checklist) — не в первом экране; прозаический лид + early TG/MAX сохранены.
- Sol single pass: no rewrite-loop over Sol output.

### Change
- Writer brief: для clusters с heavy legal spine (ПДКП, задаток, ЕГРН) target writer draft ≤2400 words so Sol headroom stays ≥200 words under 2600 cap.
- Sol: при writer >2500 — tighten таблицу/ol в part3 до 6 rows max before final stamp.

### Never again
- Добавлять второй авторский проход поверх Sol для ужатия объёма.
- Bullet-dump или TL;DR в opening при legal-heavy topics.

### Proposed apply
- Track word_count at writer-ready gate; flag `near_cap_warning` when writer.html >2500 (review-only in content-lessons until second article confirms).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B15-v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim
wp_post_id: 9310
