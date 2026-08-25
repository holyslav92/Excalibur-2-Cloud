## LESSON-20260824-1308-B10-tesseract-missing-cover-qa-blocked
status: proposed
topic_id: B10
category: other
confidence: high

### Evidence
- artifact: cover/cover_qa.json + cover/cover-budget-result.json
  finding: Cover-QA pixel gate FAIL на всех 4 tier-попытках (2× standard→vip). OCR-зависимые checks (`pixel_hook_title_cyrillic`, `pixel_hook_title_not_truncated`, `pixel_phone_readable`, `pixel_phone_not_clipped`) возвращают `ocr=''`, `cyr_ratio=0.0`, `phone_digits=''` — типичный паттерн при отсутствии tesseract binary, не обязательно дефект PNG.
- artifact: env probe — `which tesseract` → not found; `pytesseract.get_tesseract_version()` → `TesseractNotFoundError`
- artifact: cover_qa_pixels.py `_ocr_image_zone` — пустая строка при ImportError/Exception (tesseract missing маскируется под «нет текста на обложке»)
- artifact: cover/cover-text.json — hook «Квартиру оформили, но деньги не дошли» (6 слов, канон 5–7)
- artifact: quality-bar-9.json — все editorial checks PASS кроме `cover_qa_pass: false`; word_count=2475, h2=9, interlinks=4
- artifact: opening-meta-gate.json — PASS (news-casus shape, comment magnet)
- artifact: cover-budget-result.json — `reason: cover_budget_exhausted`, max_attempts=2; next_steps указывают Indexer (не deep-dive Cover-QA)
- artifact: memory/blog/llms.txt — B10 проиндексирован (Indexer завершён без publish)
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID)

### Named blockers
- TESSERACT_BINARY_MISSING
- COVER_QA_OCR_BLIND
- COVER_BUDGET_EXHAUSTED
- PUBLISH_BLOCKED_COVER_QA
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast canon: после исчерпания 2 full attempts → `cover-budget-result.json` → **Indexer**, не бесконечный Cover-QA loop.
- Контентный контур B10 до Cover: research P0 «купить квартиру в тюмени» 22660, opening-meta PASS, engagement shape (2475 слов, comment magnet, 4 sibling interlinks).
- Publish корректно **не** запущен при `cover_qa.json` status=FAIL.

### Change
- Cloud environment: установить `tesseract-ocr` + `tesseract-ocr-rus` (или эквивалент) до Cover-QA.
- `excalibur_blog_doctor.py`: preflight `tesseract --version` → явный ENV BLOCKER до Cover/Publish.
- `cover_qa_pixels.py` / gate: при отсутствии tesseract — `TESSERACT_ENV_BLOCKER`, не каскад pixel_hook_title_* FAIL с пустым OCR.

### Never again
- Не трактовать `ocr=''` + `cyr_ratio=0.0` как дефект grsai cover без проверки tesseract в env.
- Не публиковать при cover_qa FAIL (даже если editorial quality-bar-9 иначе зелёный).
- Не копать pixel OCR source как дебаг-хобби после cover budget exhausted — handoff Indexer.

### Proposed apply
- Fixer INC-20260824-1308-cover-qa-tesseract-missing-b10 помечен fixed, но на pod content-learner tesseract всё ещё отсутствует — нужен env rebuild / `bash scripts/excalibur_blog_cloud_install_deps.sh`.
- Metrika credentials — закрыть INC-20260821-0615-content-learner-metrika-credentials.

### Durable applied
- none (env fix → Fixer; первый именованный run с tesseract gap)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-sdelku-zaregistrirovali-deneg-po-faktu-ne-bylo-v-tyumeni-nasledniki-osporili-pok
publish: skipped (cover_qa FAIL)
