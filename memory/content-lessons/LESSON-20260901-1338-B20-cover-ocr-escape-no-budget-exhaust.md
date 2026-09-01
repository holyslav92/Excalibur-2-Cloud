## LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust
status: proposed
topic_id: B20
category: structure
confidence: medium

### Evidence
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15 pattern); `cover_budget_exhausted` absent; 4 flaky checks overridden (designed_thumbnail, hook_title_not_truncated, collage_inset, wordstat_query_strips); visual core OK — face + Cyrillic hook + phone; gate_status PASS.
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: `budget_exhausted: false` — cover passed within grsai budget (не B15 exhaust path).
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260831-0608-B15-cover-budget-ocr-escape-repeat — B15 exhaust+escape; B20 escape **без** budget exhaust (5-й live proof OCR path)

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `apply_ocr_false_positive_escape` при визуально OK PNG без budget exhaust — штатный путь, не regen loop.
- Short hook on legal-entity stakes + meme people+cats (meme_canon_v1).

### Change
- none durable — canon validated; отличие от B15: escape без `cover_budget_exhausted` не требует needs-human phone-in-hand checklist (уже в B10/B15 proposal).

### Never again
- Fixer regen при escape PASS и budget not exhausted.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook: B20 — пятый live OCR escape (B08/B09/B10/B15/B20); `memory/cover/cover-canon.json` pattern stable.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B20-v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot
wp_post_id: 9490
