## LESSON-20261002-0610-B34-presentation-ddu-maintenance-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `newbuild_management_fee_ddu_appendix_vs_sales_tyumen`; story_dup PASS vs B27/B25/B31/B32; Klyshin none (fresh Tyumen newbuild casus).
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: final P0 «новостройки тюмень» regions 55+11176 freq **4360** (compare RU225 **8336**); narrow probes «плата за содержание жилья» 6, «УК новостройка» 2, «ДДУ тюмень» 3 — rework to P0 newbuild spine + tariff conflict in H1/body.
- artifact: research-notes.md
  finding: plot = презентация 35 ₽/м² содержание vs приложение ДДУ 89 ₽/м² + индексация + капремонт; банк урезал одобрение ~620 тыс. ₽; бронь 150 тыс. возврат после отказа от ДДУ.
- artifact: wp-publish-result.json
  finding: publish PASS post **11398**, live-page PASS, 7 inline uploads, categories=32,36,34.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `spine_once_no_recap: true`, `word_count` 1454 (target 1400–1600), `no_composite_disclaimer: true`, slot rubric novostroyki PASS.
- artifact: article-quality-score.json
  finding: PASS after one quality-score Sol rewrite (`sol_rewrite_applied: true`).
- artifact: stylo-report.json
  finding: `stylo_pass: true`, `sol_rewrite_applied: false` (delta 2.44 < 2.85).
- artifact: cover/cover_qa.json
  finding: PASS, no OCR escape / budget exhaust flags.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 11398)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: при слабом exact по УК/содержанию (6/2/3) — P0 «новостройки тюмень» 4360; hook через презентация vs приложение ДДУ + ипотечный пересчёт.
- Dzen news-casus: event (презентация 35 ₽) + risk (89 ₽ в ДДУ → банк режет лимит) + agency finale (отказ от ДДУ, возврат брони).
- Scout anti-repeat: distinct от escrow/страховки/приёмки/аренды земли clusters.

### Change
- Scout story-cluster ledger: `newbuild_management_fee_ddu_appendix_vs_sales_tyumen` locked 2026-10-02 (B34).
- После Metrika ingest: cohort tag `cluster:newbuild_management_fee_ddu_appendix_vs_sales_tyumen` vs sibling newbuild DDU clusters.

### Never again
- Брать «плата за содержание жилья» 6 как P0 без rework на newbuild spine.
- Смешивать plot с B31 insurance-before-DDU или B32 escrow entity mismatch.

### Proposed apply
- Scout `used-clusters.json`: cluster_id `newbuild_management_fee_ddu_appendix_vs_sales_tyumen`.
- Metrika cohort compare после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-v-tyumeni-v-prezentacii-zhk-vznos-35-v-ddu-89-ipoteku-urezali
wp_post_id: 11398
