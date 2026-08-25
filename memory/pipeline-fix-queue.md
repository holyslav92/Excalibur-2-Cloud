# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260824-1308-cover-qa-tesseract-missing-b10
status: fixed
run_date: 2026-08-24
role: excalibur-blog-cover-qa
topic_id: B10
article_dir: memory/blog/articles/B10-sdelku-zaregistrirovali-deneg-po-faktu-ne-bylo-v-tyumeni-nasledniki-osporili-pok
severity: blocker
category: env

### What went wrong
- Cover-QA pixel gates failed because `tesseract` binary missing in Cloud VM (`pytesseract` installed but `FileNotFoundError`).
- OCR returned empty string → `pixel_hook_title_cyrillic`, `pixel_phone_readable` and related OCR checks failed.
- Cover budget exhausted (2 solo attempts); quad canvas cover restored visually OK.
- `quality-bar-9` blocked on `cover_qa_pass` only.

### How the agent recovered this run
- Pipeline stopped before Publish (B10 not published).
- Quad canvas cover.png kept as best candidate via `cover-budget-result.json`.

### Durable fix needed before next run
- Install `tesseract-ocr` + `tesseract-ocr-rus` in Cloud environment bootstrap.
- Pin `pytesseract` in requirements; doctor preflight must fail loud if OCR deps missing.

### Suggested files to inspect/change
- `.cursor/environment.json`
- `scripts/excalibur_blog_cloud_install_deps.sh`
- `requirements.txt`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_cover_qa_gate.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-24
fix_summary:
- Added idempotent `scripts/excalibur_blog_cloud_install_deps.sh` (apt tesseract-ocr + tesseract-ocr-rus, pip, doctor).
- Wired `.cursor/environment.json` install to the script; pinned `pytesseract` in requirements.txt.
- Doctor + cover_qa_gate `--doctor` now verify tesseract binary + rus lang pack before Cover-QA runs.
- B10 intentionally not published; re-run Cover-QA pixel gate on next agent boot after env rebuild.
files_changed:
- `.cursor/environment.json`
- `scripts/excalibur_blog_cloud_install_deps.sh`
- `requirements.txt`
- `scripts/excalibur_blog_doctor.py`
- `scripts/excalibur_blog_cover_qa_gate.py`
- `CLOUD-FIRST-RUN.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `bash scripts/excalibur_blog_cloud_install_deps.sh` (idempotent re-run)
- `python3 -m py_compile scripts/excalibur_blog_doctor.py scripts/excalibur_blog_cover_qa_gate.py`
- `python3 scripts/excalibur_blog_cover_qa_gate.py --doctor`
- `tesseract --list-langs | grep rus`
commit: d5a7d27

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
- B10 (2026-08-24): повторный METRIKA CREDENTIALS BLOCKER при content-learner post-Indexer.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06 для post-publish behavioral baseline.

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

