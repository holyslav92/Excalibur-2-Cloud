## LESSON-20261003-0630-B34-bti-area-surcharge-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: memory/blog/scout/excalibur-blog-handoff-b34.md
  finding: new cluster `newbuild_bti_area_surcharge_before_keys_tyumen`; slot rubric novostroyki; story_dup PASS; anti_dupe_hard PASS; trend mirror `paper_clean_then_broke`.
- artifact: memory/scout/assembled-scout-inputs-b34-09slot.md
  finding: Wordstat rework weak probes «бти новостройка» 1 / «дду новостройка» 17 → spine P0 «новостройки тюмень» **4394** (regions 55+11176).
- artifact: research-notes.md
  finding: casus = +4 кв.м на приёмке БТИ, доплата 380 000 ₽ до ключей; contrast note — зеркальный SERP «БТИ съело 4,2 кв.м» (уменьшение) — другая механика.
- artifact: wp-publish-result.json
  finding: publish PASS post **11450**, live-page PASS, 7 inline uploads, categories=31 (`vtorichka-i-riski` per publish log).
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `spine_once_no_recap: true`, `no_unrelated_calendar_news_glue: true`, `word_count` **1564** (target 1400–1600), `no_composite_disclaimer: true`.
- artifact: stylo-report.json
  finding: `stylo_pass: true`, delta 2.09 < 2.85; elevated `legal_per_1k` ~52.6 within gate.
- artifact: cover/cover_qa.json + `.cursor/excalibur-blog-fragments/cover.md`
  finding: `ocr_false_positive_escape: true` (5 flaky overrides); `budget_exhausted: false`, grsai_canvas_attempts=1 — canonical escape, no fixer regen.
- artifact: article-quality-score.json
  finding: PASS all sections; `sol_rewrite_applied: true` (quality-score path).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 11450)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat spine: при нулевом exact «бти новостройка» — P0 «новостройки тюмень» 4394; hook через приёмку+ДДУ+доплату до актa.
- Dzen news-casus: event (приёмка с ипотекой и детьми) + risk (380k + двойной дедлайн банк/неустойка) + finale agency (ключи отложены, сверка с ДДУ) + comment magnet «подписываете акт в тот же день?».
- Scout formula_spam PASS vs last-3 (cellar 190k, deposit 35/89, school declaration) — distinct BTI+area plot.
- `no_unrelated_calendar_news_glue` PASS — не цеплять семейную ипотеку 01.10 как spine кейса.

### Change
- Scout story-cluster ledger: lock `newbuild_bti_area_surcharge_before_keys_tyumen` (B34, 2026-10-03).
- После Metrika ingest: cohort tag `cluster:newbuild_bti_area_surcharge_before_keys_tyumen` vs B23 apartments-in-DDU и B12 escrow-delay clusters.

### Never again
- Брать «бти новостройка» 1 как P0 без rework на newbuild spine.
- Смешивать с зеркальным «БТИ уменьшило площадь» как тот же cluster.
- Fixer regen cover при OCR escape PASS + budget not exhausted.

### Proposed apply
- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` after publish (cluster row).
- Metrika cohort compare после credentials fix (post 11450).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-v-tyumeni-v-novostrojke-na-priemke-bti-4-kv-m-doplata-380-tysyach-do-klyuchej
wp_post_id: 11450
