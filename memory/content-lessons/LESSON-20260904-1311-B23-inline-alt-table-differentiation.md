## LESSON-20260904-1311-B23-inline-alt-table-differentiation
status: proposed
topic_id: B23
category: structure
confidence: medium

### Evidence
- artifact: image-alt-gate.json
  finding: pre-publish fix — `inline_2` alt changed from generic «Сравнительная таблица к разделу о подписании договора…» to distinct column labels «Договор подписан, Кредит одобрен, Ключи не выданы»; all 7 inline alts synced to article.html + cover-registry.json.
- artifact: cover/quad-split-report.json vs cover-registry.json
  finding: draft inline_2 columns «Взнос внесён | Деньги на эскроу | Ипотека одобрена» overlapped semantically with inline_5/6/7 schematic labels — caption builder differentiated per-slot TXT.
- artifact: quality-bar-9.json
  finding: `comparison_tables_differ: true`, `image_alt_human: true` after fix.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- ALT_OVERLAP_TABLE_SLOTS
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `excalibur_blog_image_caption_builder.py --apply` post-Cover: human alt from H2 anchor + distinct panel TXT, not duplicate generic «таблица к разделу…».
- Per-slot column triplets for table/schematic/timeline inlines (inline_2 vs inline_5 vs inline_6 vs inline_7).

### Change
- Cover-scene / quad-manifest: assign **unique** TXT column sets per table-like inline at scene-draft time (reduces post-hoc alt gate churn).
- Director: run image caption builder before quality-bar when article has ≥2 table/schematic inlines.

### Never again
- Reuse identical column-label triplets across multiple inline table/schematic slots.
- Generic section-only alt without distinguishing column keywords on comparison-table PNGs.

### Proposed apply
- B23 first explicit alt-overlap lesson; cross-check with `scripts/excalibur_blog_image_caption_builder.py` uniqueness heuristic (review-only).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya
wp_post_id: 9653
