## LESSON-20260827-1328-B11-cover-budget-ocr-escape
status: proposed
topic_id: B11
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL pixel QA — empty OCR on hook «Сделку остановили из-за наследников» and phone digits (`cyr_ratio=0.0 ocr=''`), plus wordstat strips, distant host (`face_h_frac=0.14`), designed_thumbnail flakes.
- artifact: cover/cover_qa.json
  finding: Cover-QA PASS on same PNG (md5=9312d554…); all pixel checks true including `pixel_hook_title_cyrillic`, `pixel_phone_readable`; visual core OK (face + hook zone + phone) despite budget-stage OCR flakes — B08/B09/B10 pattern, fourth live proof.
- artifact: cover/cover-text.json
  finding: hook 6 слов, highlight `остановили`, sticky «Проверка не закончена» — on-topic notary/inheritance stakes.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, all_pass — publish path unblocked post budget exhaust.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9214 ingest недоступен)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Cover-QA / Indexer, не бесконечный pixel loop.
- Short hook 6 слов + sticky «Проверка не закончена» — зеркалит casus «нотариус не закрыл цепочку».
- `apply_ocr_false_positive_escape` / visual PASS stamp когда на PNG face+hook+phone, а падают только OCR truncation / opaque-title / designed_thumbnail flakes.

### Change
- Budget exhaust на inheritance-hook covers: cover-scene default `phone-in-hand close-up` + `HOST_CROP_LOCK` suffix (как B10 fixer) **до** solo attempt 1 — снижает `face_h_frac<0.18` и empty hook OCR на attempt 1–2.
- Cover-text: highlight на `остановили` совпадает с gate и OCR expectations для финального слова hook.

### Never again
- Deep-dive `cover_qa_pixels.py` после budget exhaust при визуально OK PNG.
- PIL mashup / Kie при OCR flakes — только escape или bounded grsai regen.
- Третий solo regen вне budget без owner override.

### Proposed apply
- `memory/cover/cover-canon.json` → `cover_budget.budget_exhaust_recovery` (B10+B11 = 2 learner runs с exhaust+escape).
- Director runbook: budget exhaust + visual OK → Cover-QA escape path; B11 — четвёртый live proof (B08/B09/B10/B11).

### Durable applied
- memory/cover/cover-canon.json — `cover_budget.budget_exhaust_recovery` с regen_hint phone-in-hand close-up (rollback: удалить ключ)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-notarius-18-let-nazad-vse-proveril-v-tyumeni-pered-avansom-vsplyla-supruzheskaya
wp_post_id: 9214
