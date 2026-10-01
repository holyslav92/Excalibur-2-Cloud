## LESSON-20261001-0844-B34-family-mortgage-rental-before-escrow-cluster
status: proposed
topic_id: B34
category: geo
confidence: low

### Evidence
- artifact: research-notes.md#cluster_id
  finding: `newbuild_family_mortgage_rental_listing_before_escrow_tyumen` — «сдам» до эскроу vs семейная ипотека/предодобрение; не смешивать с уступкой/маткапиталом.
- artifact: quality-bar-9.json
  finding: PASS, word_count **1510**, `comment_magnet_question`, `spine_once_no_recap`, `no_foreign_slot_rubric_mechanism`.
- artifact: wp-publish-result.json
  finding: post **11372**, live-page PASS, 7 inline.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape` PASS (1 grsai attempt path).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 11372)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- P0 через семейная ипотека + новостройка; hook = публичное «сдам» до эскроу, не «банк запретил аренду».
- Oct-2026 rate-change context без универсальных ставок; agency = сверка лота + банк до подписи.

### Change
- Scout ledger: cluster `newbuild_family_mortgage_rental_listing_before_escrow_tyumen` (B34, 2026-10-01).

### Never again
- Причинно связывать объявление и отказ ипотеки без оговорок.
- Раздувать арендный рынок вместо pre-escrow newbuild casus.

### Proposed apply
- `used-clusters.json` + Metrika cohort после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke
wp_post_id: 11372
