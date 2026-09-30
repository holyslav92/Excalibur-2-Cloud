## LESSON-20260930-0811-B34-dvor-bez-mashin-fire-lane-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: research-notes.md
  finding: cluster `newbuild_carfree_yard_fire_lane_tyumen`; rubric novostroyki; plot = маркетинг «двор без машин» vs пожарный/сервисный проезд и парковка до ДДУ; бронь 150k→90k return (editorial casus).
- artifact: quality-score-notes.md + article-quality-score.json
  finding: one Sol repair after LEAD FAIL (15 sentences → 4–6); final PASS, word_count 1540.
- artifact: quality-bar-9.json
  finding: all PASS; `comment_magnet_question`, `spine_once_no_recap`, `no_foreign_slot_rubric_mechanism`, 3 sibling interlinks.
- artifact: wp-publish-result.json
  finding: publish PASS post **11310**, live-page PASS, 7 inline uploads.
- artifact: cover/cover_qa.json
  finding: PASS, grsai solo path (no budget exhaust noted).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no behavioral baseline for post 11310)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (same-day publish)

### Keep
- News-casus spine: бронь + ипотека на кону + «двор без машин» vs документы (проектная декларация, СП 4.13130 ширина проезда по высоте).
- Quality-score single Sol repair для lead length — без self-score loop.
- Разделение пожарный проезд / сервис / парковка у подъезда (research constraints).

### Change
- Scout story-cluster ledger: `newbuild_carfree_yard_fire_lane_tyumen` locked 2026-09-30 (B34).
- После Metrika ingest: cohort tag vs DDU/бронь clusters (B12, B22, B23).

### Never again
- Утверждать, что любой 6 м проезд = «обман» без высоты здания и проектного решения.
- Смешивать бронь с эскроу-ДДУ в финальном takeaway.
- Padding после quality-score repair.

### Proposed apply
- Scout `used-clusters.json`: cluster_id `newbuild_carfree_yard_fire_lane_tyumen`.
- Metrika cohort compare после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-v-novostrojke-tyumeni-v-broni-obeschali-dvor-bez-mashin-v-proekte-poyavilsya-pro
wp_post_id: 11310
