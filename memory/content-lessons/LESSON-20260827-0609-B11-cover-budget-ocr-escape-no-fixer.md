## LESSON-20260827-0609-B11-cover-budget-ocr-escape-no-fixer
status: proposed
topic_id: B11
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: grsai solo 2/2 exhausted; both attempts FAIL pixel QA — empty Tesseract OCR on hook «Четыре месяца искали — суд оспорил сделку» and phone digits; best_candidate from quad canvas 1 split.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape.applied: true` (B08/B09 pattern); `fixer_skipped: "budget 2/2 — no panel regen"`; visual PASS — face cobalt vest temple-rub, hook Cyrillic readable, phone +7 922 001 65 05, sticky «Жёлтое заключение?», crying cat.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true` — publish unblocked after escape stamp.
- artifact: memory/content-lessons/LESSON-20260826-0834-B10-cover-budget-ocr-escape.md
  finding: B10 — 3rd live proof + fixer regen path; B11 — 4th proof **без fixer** (canon fail-fast → Indexer).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Cover-QA escape → Indexer (не бесконечный pixel loop).
- `apply_ocr_false_positive_escape` когда PNG визуально face+hook+phone, падают только OCR empty / gold-bar / sticky / collage flakes.
- Short hook + highlight «оспорил» + on-topic sticky — stakes жёлтого заключения.

### Change
- B11 vs B10: при budget exhaust и visual OK — **не обязателен fixer regen** перед publish (B10 fixer был optional recovery); director default = escape → Indexer если cover_qa PASS.
- Cover quad split canvas 1 при exhaust — рабочий fallback (B11 proof); не копать solo regen attempt 3+.

### Never again
- Fixer panel regen после budget exhaust при visual PASS + escape stamp (B11 notes: fixer not run).
- PIL mashup / Kie при OCR flakes.
- Deep-dive `cover_qa_pixels.py` как дебаг-хобби после escape.

### Proposed apply
- 2nd content-learner run (B10+B11) с одинаковым exhaust+escape → validate LESSON-20260826-0834-B10-cover-budget-ocr-escape как `validated` после human review.
- Director runbook: budget exhaust + escape PASS → Indexer без fixer round-trip (B11 canonical path).

### Durable applied
- none (canon в cover-canon.json; B11 — 4th live proof)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri
wp_post_id: 9191
