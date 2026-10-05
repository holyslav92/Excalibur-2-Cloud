## LESSON-20261005-1317-B34-secondary-appraisal-below-dkp-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: research-notes.md#cluster_id
  finding: new cluster `secondary_bank_appraisal_below_dkp_price_tyumen`; plot = предодобрение по доходу + «чистая» ЕГРН → банковская оценка до аванса на 900k ниже цены в проекте ДКП → пересчёт/отзыв предодобрения; аванс не вносился; slot vtorichka (не ДДУ).
- artifact: memory/scout/used-clusters.json (cross-check)
  finding: story_dup PASS vs `bank_appraisal_below_ddu_price` (B07 newbuild 900k ниже ДДУ) — другая рубрика и механика (ДКП/залог vs ДДУ/эскроу); vs B06 autoocenka/CIRC plot; vs B14 справка о закрытии ипотеки/залог.
- artifact: interlink-plan.json
  finding: outbound B06 (оценка/CIRC), B14 (ипотека/залог), B33 (долг за свет до аванса) — vtorichka risk siblings; 3 links quality-bar PASS.
- artifact: wp-publish-result.json
  finding: publish PASS post **11622**, live-page PASS, 7 inline uploads, categories 31,34,36; permalink vtorichka-i-riski slug.
- artifact: quality-bar-9.json
  finding: all_pass; `word_count` 1438 (target 1400–1600); `comment_magnet_question: true`, `spine_once_no_recap: true`, `no_foreign_slot_rubric_mechanism: true`.
- artifact: stylo-report.json + article-quality-score.json
  finding: stylo delta 2.93 > 2.85 → one Sol pass applied; article-quality-score PASS after repair.
- artifact: cover/cover_qa.json
  finding: PASS; `ocr_false_positive_escape` overrides (canonical path, budget not exhausted).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 11622)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Scout anti-repeat: не смешивать с newbuild `bank_appraisal_below_ddu_price` (900k ниже ДДУ) — отдельный cluster_id для вторички/ДКП.
- News-casus spine: «одобрено по доходу» ≠ «одобрен объект»; оценка до аванса; ending agency (письменное подтверждение банка, условия возврата аванса), не panic «банк виноват».
- Wordstat/slot: vtorichka + proverka-pered-pokupkoj rubrics; P0 через вторичка/ипотека жаргон Тюмень (из scout handoff), не newbuild ДДУ tail.
- Interlink к B06/B14/B33 — document + pre-advance risk cluster, не formula spam с последними 3 published.

### Change
- Scout story-cluster ledger (proposed): lock `secondary_bank_appraisal_below_dkp_price_tyumen` after human review of used-clusters sync.
- После Metrika ingest: cohort tag `cluster:secondary_bank_appraisal_below_dkp_price_tyumen` vs B06 appraisal/CIRC и B07 newbuild appraisal.

### Never again
- Recycle B07 «900 тысяч ниже ДДУ» skeleton как vtorichka plot без смены механики (ДКП vs ДДУ).
- Treat предодобрение по личности как гарантию сделки до отчёта оценщика.
- Fixer regen cover при OCR escape PASS + budget not exhausted.

### Proposed apply
- `memory/scout/used-clusters.json`: add cluster_id `secondary_bank_appraisal_below_dkp_price_tyumen` (topic B34, post 11622) via `excalibur_blog_scout_story_dup.py --sync-used-clusters` when owner approves.
- Metrika cohort compare после credentials fix (post 11622).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-v-tyumeni-na-vtorichke-ocenka-na-900-tysyach-nizhe-dkp-bank-snyal-odobrenie
wp_post_id: 11622
