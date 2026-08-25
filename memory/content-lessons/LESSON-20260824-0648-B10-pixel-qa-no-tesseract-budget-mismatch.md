## LESSON-20260824-0648-B10-pixel-qa-no-tesseract-budget-mismatch
status: proposed
topic_id: B10
category: other
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json#attempts — repeated `pixel_hook_title_cyrillic FAIL: cyr_ratio=0.0 ocr=''`, `pixel_phone_readable FAIL: phone_digits=''`, `pixel_hook_title_not_truncated FAIL` с пустым ocr на всех 4 tier runs
- artifact: scripts/excalibur_blog_cover_qa_pixels.py — `_tesseract_ocr_available()` → False в Cloud Agent env; ink-based fallbacks в `_title_cyrillic_metrics`, `_phone_not_clipped_metrics`, `_hook_title_complete_metrics` при отсутствии tesseract
- artifact: cover/cover_qa.json — финальный cover.png PASS все pixel_* checks без ocr_false_positive_escape note (ink fallbacks достаточны на best_candidate)
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- TESSERACT_UNAVAILABLE
- PIXEL_QA_BUDGET_LOOP_STRICT
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Ink-based no-tesseract fallbacks в `cover_qa_pixels.py` — финальная обложка B10 PASS без tesseract.
- `apply_ocr_false_positive_escape` (B08/B09 pattern) остаётся для flaky OCR при наличии tesseract.

### Change
- Cloud env: установить `tesseract-ocr` + `rus` traineddata + `pytesseract` (или документировать как required для cover regen loop).
- Альтернатива: grsai solo cover `stamp_qa` при `not _tesseract_ocr_available()` не считать пустой ocr hard-fail если ink fallbacks PASS (сейчас промежуточные candidates не дотягивают ink thresholds → budget false-negative).

### Never again
- Не интерпретировать `ocr=''` в budget log как «нет кириллицы на PNG» без проверки ink fallbacks на том же файле.
- Не копать pixel OCR source >15–20 мин после budget exhaust (канон fail-fast).

### Proposed apply
- Fixer/env: `tesseract-ocr` в environment.json или setup script.
- После второго run с тем же mismatch (budget FAIL + final PASS без tesseract) — patch grsai loop to reuse escape path.

### Durable applied
- none (первый именованный run; B08/B09 escape был ручной, не в content-lessons)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-po-povestke
wp_post_id: 9121
