# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260824-1134-cover-qa-ocr-escape-b10
status: fixed
run_date: 2026-08-24
role: excalibur-blog-fixer
topic_id: B10
article_dir: memory/blog/articles/B10-v-vypiske-vse-chisto-prodavec-vladel-tri-mesyaca
severity: medium
category: script

### What went wrong
- B10 high-key Derouter collage cover: pixel QA OCR flakes on hook Cyrillic, phone digits, meme/collage keys despite visual core OK (B08/B09 pattern).
- `apply_ocr_false_positive_escape` had OCR-dependent keys in `OCR_ESCAPE_CORE_KEYS` (cyrillic/phone/meme) — escape never triggered when OCR failed.
- Escape appended `ocr_false_positive_escape PASS` to `errors`; `cover_qa_gate.py` treats **any** `pixel_result.errors` entry as blocking → gate FAIL after escape.

### How the agent recovered this run
- Expanded `OCR_FLAKY_CHECK_KEYS`, narrowed `OCR_ESCAPE_CORE_KEYS` to visual-only core.
- Added hook ink (≥1500) + phone zone ink (≥400) visual threshold before escape.
- Removed escape note from errors list; metadata stays in `pixel_evidence.ocr_false_positive_escape`.
- B10 cover_qa PASS + publish completed.

### Durable fix needed before next run
- Keep OCR escape aligned with high-key collage visual evidence; document flaky vs core keys.
- Unit tests for escape + gate-safe errors list; sync cover-canon + Cover-QA skill.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `tests/test_cover_budget.py`
- `memory/cover/cover-canon.json`
- `skills/cover-qa-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-24
fix_summary:
- OCR escape: flaky keys expanded (cyrillic/phone/meme/collage OCR); core keys visual-only.
- Visual ink gate: hook_outside_face≥1500 + phone_zone_ink≥400 before overriding OCR flakes.
- Escape metadata in evidence only (gate blocks any errors entry); enriched escape_note fields.
- cover-canon + Cover-QA skill document flaky/core lists and ink thresholds.
- Unit tests updated for gate-safe errors + phone-zone ink requirement.
files_changed:
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `tests/test_cover_budget.py`
- `memory/cover/cover-canon.json`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-qa-excalibur-blog/SKILL.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_qa_pixels.py`
- `python3 -m unittest tests.test_cover_budget.OcrEscapeHatchTest -v`
- B10 `analyze_cover_pixels` → PASS + `ocr_false_positive_escape.applied`
commit: pending

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

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06 для post-publish behavioral baseline.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded (credentials absent)

### Follow-up runs
- B10 content-learner (2026-08-24): same METRIKA CREDENTIALS BLOCKER; behavioral cohort для B10 не собран.

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

