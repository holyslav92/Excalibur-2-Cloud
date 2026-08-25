# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260824-0648-cover-qa-pixels-b10-no-tesseract
status: fixed
run_date: 2026-08-24
role: excalibur-blog-fixer
topic_id: B10
article_dir: memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-po-povestke
severity: blocker
category: script

### What went wrong
- Cloud Cover-QA без tesseract: OCR-пустые зоны → FAIL на `pixel_hook_title_cyrillic`, `pixel_phone_not_clipped`, `pixel_hook_title_not_truncated` для легитимной high-key B10 cover.
- `smudge_cat` (grey cat) не детектировался — только orange_fur heuristic.
- Hook-sticky (жёлтый квадрат) ложно считался Wordstat query strip (`paper_frac` 0.012).
- High-key bright covers (white_frac ~0.72) ложно FAIL `pixel_no_collage_inset` (threshold 0.22).
- PIL mashup templates (B08/B09/zags) не должны проходить ink-fallback без tesseract.

### How the agent recovered this run
- Cover-QA OCR escape + manual re-run после partial script fixes; publish B10 с cover_qa PASS.

### Durable fix needed before next run
- Ink-based fallbacks только когда tesseract недоступен и не mashup-template suspect.
- Grey cat (`MEME_GREY_CAT_MIN_SIGNAL`) + hook-sticky filter в Wordstat strip detector.
- Collage inset: phone-zone inset + high white_frac без host only; mashup guard `_pil_mashup_template_suspect`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `tests/test_cover_qa_pixels_layout.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-24
fix_summary:
- `_tesseract_ocr_available()` + ink fallbacks (hook complete, cyrillic hook, phone) gated by `not _pil_mashup_template_suspect`.
- `_pil_mashup_template_suspect` / `_second_face_inset_present`; collage inset uses phone inset + white_frac≥0.88 erase mask.
- `MEME_GREY_CAT_MIN_SIGNAL` grey fur heuristic for smudge_cat; hook-sticky size filter in `_filter_wordstat_strip_components`.
- Foreign leak fails on mashup-template when no OCR; blank-sticky scan when mashup + cyrillic FAIL without tesseract.
files_changed:
- `scripts/excalibur_blog_cover_qa_pixels.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_qa_pixels.py`
- `python3 -m unittest tests.test_cover_qa_pixels_layout` → OK (10 tests)
- B10 cover.png pixel QA → PASS (no tesseract)
commit: c484cb0

## INC-20260824-0648-cover-quad-prompt-import-budget
status: fixed
run_date: 2026-08-24
role: excalibur-blog-cover
topic_id: B10
article_dir: memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-po-povestke
severity: blocker
category: script

### What went wrong
- `excalibur_blog_cover_quad_prompt.py` NameError: `pick_identity_reference` not imported.
- 7-inline longform MCP prompt ~4050 chars blocked at `MAX_MCP_PROMPT_CHARS=3500`.

### How the agent recovered this run
- Cover subagent hit import error; fix committed before quad batch regen.

### Durable fix needed before next run
- Import `pick_identity_reference` from `excalibur_blog_identity_real`.
- Raise `MAX_MCP_PROMPT_CHARS` to 4200 for 7-inline canvases.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-24
fix_summary:
- Added `from excalibur_blog_identity_real import pick_identity_reference`.
- `MAX_MCP_PROMPT_CHARS = 4200` for longform 7-inline (~4000–4150 chars).
files_changed:
- `scripts/excalibur_blog_cover_quad_prompt.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
commit: 4a012cb

## INC-20260821-0615-content-learner-metrika-credentials
status: open
run_date: 2026-08-21
role: excalibur-blog-content-learner
topic_id: B06
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER
- Missing `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets/env

### How the agent recovered this run
- Content-learner записал pipeline lessons из run evidence (Derouter 524 chunk, quality-bar PIL sync, html_linter CTA div).
- Metrika cohort analysis пропущен; lessons marked low/medium confidence без behavioral signals.
- **B10 (2026-08-24):** тот же METRIKA CREDENTIALS BLOCKER; content-learner записал B10 lessons без behavioral cohort.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06/B10 для post-publish behavioral baseline.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded (credentials absent)

## INC-20260821-0614-quality-bar-wordstat-pil-b06
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B06
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
severity: medium
category: script

### What went wrong
- `quality-bar-9` gate `wordstat_stickers_not_title_overlap` required sticker x≥0.68 for all manifests.
- With `wordstat_pil_only` + top-left PIL positions (x≤0.42), `cover_qa` PASS but quality-bar-9 FAIL — conflicting thresholds.

### How the agent recovered this run
- Patched `check_wordstat_overlap` to branch on `wordstat_pil_only`: top-left sacred zone (x≤0.42, y≤0.36) aligned with `cover_qa_gate`.

### Durable fix needed before next run
- Sync quality-bar-9 wordstat position rules with cover_qa for PIL overlay path.

### Suggested files to inspect/change
- `scripts/excalibur_blog_quality_bar_9_gate.py`
- `scripts/excalibur_blog_cover_qa_gate.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `check_wordstat_overlap` branches on `wordstat_pil_only`: PIL top-left zone x≤0.42/y≤0.36; legacy overlay path keeps x≥0.68.
files_changed:
- `scripts/excalibur_blog_quality_bar_9_gate.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_quality_bar_9_gate.py`
- `python3 scripts/excalibur_blog_quality_bar_9_gate.py --article-dir memory/blog/articles/B06-...` → all_pass
commit: 493ea27

## INC-20260821-0614-html-linter-cta-div-b06
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B06
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
severity: blocker
category: script

### What went wrong
- B03–B06 Sol output wraps conversion CTA in `<div class="excalibur-cta-*">` per `shared/quality-bar-9.md`.
- `html_linter` ALLOWED_TAGS had no `div` → structure_gate FAIL on `html_linter` while quality-bar-9 regex expects `<div>` CTA blocks.

### How the agent recovered this run
- structure_gate blocked publish path until fixer; quality-bar-9 already passed CTA div markup.

### Durable fix needed before next run
- Class-aware `<div>` whitelist in html_linter for excalibur-cta-early|mid|end and excalibur-social-cta.

### Suggested files to inspect/change
- `scripts/excalibur_blog_html_linter.py`
- `shared/article-style.md`
- `tests/test_pipeline_speed_b03.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- Added `ALLOWED_DIV_CLASSES` + `is_allowed_div()` in html_linter; plain `<div>` still forbidden.
- Documented CTA div rule in `shared/article-style.md`; unit tests for allow/forbid.
files_changed:
- `scripts/excalibur_blog_html_linter.py`
- `shared/article-style.md`
- `tests/test_pipeline_speed_b03.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_html_linter.py`
- `python3 scripts/excalibur_blog_html_linter.py B06/article.html` → PASS
- `python3 scripts/excalibur_blog_structure_gate.py --article-dir B06` → PASS
- `python3 -m unittest tests.test_pipeline_speed_b03.HtmlAutofixTest` → OK
commit: 35ab34b

