## LESSON-20260824-0829-B10-grsai-ocr-empty-false-fail
status: proposed
topic_id: B10
category: other
confidence: high

### Evidence
- artifact: cover/cover_qa.json#pixel_hook_title_cyrillic, pixel_phone_readable
  finding: grsai cover.png 1200×675; host face present (pixel_host_face_present=true, face_h_frac=0.44); phone ink=2836 px; hook expected «Сделку отменили — продавец должна вернуть миллионы» from cover-text.json — но OCR returns empty string for both hook and phone (`ocr=''`, `phone_digits=''`, `cyr_ratio=0.0`). Gates fail: pixel_hook_title_cyrillic, pixel_hook_title_not_truncated, pixel_phone_readable, pixel_phone_not_clipped.
- artifact: cover/cover-budget-result.json#attempts[0].tiers
  finding: same empty-OCR pattern on both standard and vip tiers; not attempt-specific flake.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (INC-20260824-0829-content-learner-metrika-credentials-b10)

### Named blockers
- COVER_QA_OCR_EMPTY_ON_GRSAI
- PUBLISH_BLOCKED_COVER_QA
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- cover-text.json hook 5–7 слов кириллицей + phone_cta заданы до генерации — текстовый контракт корректен.
- Pixel QA читает PNG, не prompt (`pixel_qa_reads_png_not_prompt=true`) — правильный источник истины.

### Change
- Когда face+phone ink present, но OCR='' на grsai PNG — не трактовать как «нет текста на обложке»; fallback: visual hook-bar detector или stamp manual review path.
- Расширить `apply_ocr_false_positive_escape` (B08/B09) на кейс **полностью пустого OCR** при наличии designed title bar / phone zone ink (не только truncation/opaque flakes).
- Cover-QA skill: при budget exhausted + empty OCR + visual face/phone → escalate Indexer/manual PASS per cover-budget-result next_steps, не бесконечный regen.

### Never again
- Не считать Publish-ready только потому что cover-text gate PASS — pixel OCR может вернуть '' на grsai и заблокировать publish.
- Не гонять >2 full cover attempts из-за OCR empty (бюджет уже исчерпан на B10).

### Proposed apply
- Fixer: patch `excalibur_blog_cover_qa_pixels.py` — `ocr_empty_with_visual_ink_escape` when host_face + phone_ink_frac + title_bar_luminance pass but tesseract/paddle returns ''.
- После второго run с тем же grsai OCR-empty паттерном — durable gate flag в cover-canon.json.

### Durable applied
- none (первый именованный run B10; B08/B09 escape не покрывает empty OCR)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
publish_status: BLOCKED (cover_qa FAIL)
