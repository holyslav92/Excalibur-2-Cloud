# LESSON-20260827-0610-B11-quality-bar-ocr-escape-stamp

topic: B11
status: applied
category: structure

## Finding

`excalibur_blog_quality_bar_9_gate.py` subprocess на `cover_qa_gate` **без** `--no-stamp` перезаписывал ручной `cover_qa.json` с `ocr_false_positive_escape` (B08/B09 pattern). Gate `cover_qa_pass` падал даже при визуальном PASS на PNG.

Tesseract установлен в Cloud VM, но OCR на styled cover typography часто **пустой** (pytesseract раньше не был в `requirements.txt`). Escape hatch остаётся каноническим путём.

## Durable fix

- `run_cover_qa`: `--no-stamp` + fallback `_stamped_cover_qa_visual_pass` (escape + md5 match).
- `stamp_cover_qa_json`: не затирает PASS+escape при том же `cover_md5` и pixel FAIL.
- `.cursor/environment.json`: `tesseract-ocr` + `tesseract-ocr-rus`; `requirements.txt`: `pytesseract`.
- Doctor: WARN если tesseract/pytesseract/rus отсутствуют.

## Evidence

- B11 `cover/cover_qa.json` — visual PASS, budget 2/2 exhausted, manual escape.
- `quality-bar-9.json` → `all_pass: true` после fix.
