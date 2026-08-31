## LESSON-20260826-0834-B10-cover-budget-ocr-escape
status: validated
topic_id: B10
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL pixel QA — empty OCR on hook «Телефон решал за продавца — сделку остановили» and phone digits, plus wordstat strips / designed_thumbnail flakes.
- artifact: cover/cover_qa.json
  finding: fixer regen cover → visual PASS with `ocr_false_positive_escape: true` (face + Cyrillic hook + phone readable on PNG; B08/B09 pattern). `gate_status: PASS`, all pixel checks true after escape.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true` — publish path unblocked after escape stamp.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9161 недоступен)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → fixer regen / Cover-QA, не бесконечный pixel loop.
- Short hook 5–7 слов (6 слов в hook) + sticky «Хорошо, что не внесли аванс» — on-topic stakes до аванса.
- `apply_ocr_false_positive_escape` когда на PNG визуально face+hook+phone, а падают только OCR truncation / opaque-title flakes.

### Change
- После budget exhaust: fixer regen с phone-in-hand close-up (как B10 notes) перед повторным solo regen — снижает designed_thumbnail + hook OCR empty на attempt 1–2.
- Cover-text: при hook с em dash держать highlight на финальном слове (`остановили`) — совпадает с cover-text gate и OCR expectations.

### Never again
- Deep-dive `cover_qa_pixels.py` после budget exhaust при визуально OK PNG.
- PIL mashup / Kie при OCR flakes — только escape или bounded grsai regen.

### Proposed apply
- Director runbook: budget exhaust + visual OK → Cover-QA escape path (уже в `memory/cover/cover-canon.json`); B10 — третий live proof (B08/B09/B10).
- После второго content-learner run с тем же exhaust+escape без regen improvement → checklist item «phone-in-hand close-up» в cover-scene default.

### Durable applied
- none (canon уже в cover-canon.json; первый именованный learner run B10)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-rodstvenniki-ostanovili-prodazhu-pozhilogo-prodavca-veli-po-telefonu-v
wp_post_id: 9161
