# LESSON-20260825-0800-B10-cover-ocr-tesseract-env

- **topic_id:** B10
- **status:** applied
- **category:** cover
- **evidence:** content-evidence SKIP; Metrika credentials absent (METRIKA BLOCKER — no causal claims)

## Finding

Cover-QA pixel gates (`pixel_hook_title_cyrillic`, `pixel_phone_readable`) silently failed when `pytesseract`/system `tesseract-ocr` were missing — OCR returned empty strings while visual ink checks passed.

## Keep

- Quad canvas TL crop as fallback cover when solo regen OCR flakes (B08/B09 OCR escape pattern).
- Empty `wordstat_stickers` in manifest = no Wordstat strips on cover (canon).

## Change (applied)

- `requirements.txt` + `.cursor/environment.json`: install `tesseract-ocr`, `tesseract-ocr-rus`, `pytesseract`.
- `excalibur_blog_cover_qa_pixels.py`: phone OCR invert variants; manifest-empty wordstat strip bypass; OCR escape order fix; collage inset requires dominant inset blob.
- `excalibur_blog_quality_bar_9_gate.py`: empty wordstat_stickers → overlap check PASS.

## Never again

- Run Cover-QA without tesseract in cloud env (doctor should warn).
