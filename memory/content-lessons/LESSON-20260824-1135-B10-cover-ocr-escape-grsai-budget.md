## LESSON-20260824-1135-B10-cover-ocr-escape-grsai-budget
status: proposed
topic_id: B10
category: other
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: grsai solo 2×(standard+vip) — все попытки FAIL на `pixel_hook_title_cyrillic` (cyr_ratio=0.0, ocr=''), `pixel_phone_readable`, `pixel_hook_title_not_truncated`, wordstat strips, collage inset; budget exhausted.
- artifact: cover/cover_qa.json
  finding: Финальный cover.png PASS все pixel checks включая cyrillic hook + phone; mean_lum=206; host close-up.
- artifact: scripts/excalibur_blog_cover_qa_pixels.py#apply_ocr_false_positive_escape
  finding: Escape hatch B08/B09/B10 — host face + hook ink band + phone zone ink ≥400 без OCR digits; flaky keys only, no PIL/Kie.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_BUDGET_EXHAUSTED
- GRSai_CYRILLIC_OCR_FAIL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 full grsai attempts → `cover-budget-result.json` → не бесконечный Cover-QA loop.
- OCR escape только при core visual present (face + hook ink + phone band) и **только** flaky OCR keys — без PIL mashup/Kie.
- Short hook 5–7 слов из cover-text.json: «Чистая выписка — сделку оспорили позже».

### Change
- После budget exhausted на grsai Cyrillic fail: **сразу** Derouter solo cover regen (см. sibling lesson B10-derouter-cyrillic), не deep-dive pixel source.
- Cover-QA: если grsai candidate визуально OK но OCR пустой — проверить `apply_ocr_false_positive_escape` до ручного stamp.

### Never again
- Не тратить >2 grsai attempts на кириллический hook/phone когда cyr_ratio=0 стабильно на всех tiers.
- Не regen через Kie / PIL mashup при OCR flakes.

### Proposed apply
- Cover skill runbook: grsai budget fail + Cyrillic OCR → Derouter solo fallback chain (уже сработало B10).
- Документировать в cover-canon: escape применим когда ink bands есть, OCR пустой (B10 case в pixels.py comment).

### Durable applied
- none (escape logic уже в pixels.py; Derouter fallback — первый именованный B10 run)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca
wp_post_id: 9141
