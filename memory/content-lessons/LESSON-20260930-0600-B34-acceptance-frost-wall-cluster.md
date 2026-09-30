## LESSON-20260930-0600-B34-acceptance-frost-wall-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs-20260930-0900.md, research-notes.md
  finding: cluster `newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen`; slot rubric novostroyki; P0 «приемка квартиры в новостройке тюмень» **28** (rework from «новостройки тюмень» 3547); sibling B25 clean finish vs B34 frost wall + **40 days** keys.
- artifact: wp-publish-result.json
  finding: publish PASS post **11297**, live-page PASS, 7 inline uploads, categories pokupka-kvartiry + dokumenty + proverka-pered-pokupkoj.
- artifact: quality-bar-9.json
  finding: `no_unrelated_calendar_news_glue: true`, `no_foreign_slot_rubric_mechanism: true`, `word_count` 1528 (target 1400–1600), `comment_magnet_question: true`.
- artifact: article-quality-score.json + quality-score-notes.md
  finding: first Sol FAIL `lead-hit`; one repair Sol PASS (expected ≤1 repair loop).
- artifact: cover-text-gate.json + `.cover-text-retry-user.md`
  finding: Derouter cover-text invalid JSON attempt 1; wrapper retry 2 → PASS.
- artifact: cover/cover_qa.json
  finding: grsai solo quad 2 canvases, QA PASS without budget exhaust (2 canvas split path).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 11297)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Acceptance-casus spine: промёрзшая/мокрая стена → акт не подписан → ключи +40 дней; agency ending (фиксация дефекта), not panic checklist.
- Trend Radar energy only when mechanism matches plot (no family-mortgage 1 Oct calendar glue — gate enforced).
- Quality-score lead repair ≤1 Sol before Description; word band 1400–1600 without padding.
- cover_text_derouter JSON retry before manual edit.

### Change
- Scout cluster ledger: `newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen` locked 2026-09-30 (B34).
- After Metrika ingest: cohort tag `cluster:newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen` vs B25/B12 acceptance siblings.

### Never again
- Drop P0 to generic «новостройки тюмень» without acceptance rework when slot = novostroyki priemka casus.
- Paste unrelated calendar headlines (family mortgage Oct 1) into frost-wall acceptance plot.
- Manual `DEROUTER_POWERFUL_MODEL=gpt-6-astra` when 402 budget_exceeded — use auto fallback (fixer f3fbdd46).

### Proposed apply
- Scout `used-clusters.json`: cluster_id `newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen`.
- Metrika cohort compare after credentials fix (post 11297 baseline).

### Durable applied
- `excalibur_blog_derouter_opus_chat.py` powerful-tier 402 → gpt-6-astra auto fallback (commit f3fbdd46).

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-na-priemke-novostrojki-v-tyumeni-nashli-promerzshuyu-stenu-klyuchi-otlozhili-na-
wp_post_id: 11297
