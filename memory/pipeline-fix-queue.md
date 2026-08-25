# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260824-0830-cover-qa-b10-pixel-false-positive
status: fixed
run_date: 2026-08-24
role: excalibur-blog-fixer
topic_id: B10
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
severity: high
category: script

### What went wrong
- Cover budget exhausted; pixel QA FAIL on gold hook/phone bars (OCR empty on high-key).
- False positive `pixel_no_wordstat_query_strips` on gold board décor (not buyer-query strips).
- `pixel_meme_present` flake for people memes (roll_safe); `comparison_table_ui` invalid in cover_qa_gate.

### How the agent recovered this run
- Indexer path blocked; `cover-budget-result.json` stamped FAIL.

### Durable fix needed before next run
- Ink-based + `apply_gold_typography_visual_escape` for manifest-backed covers without tesseract.
- Wordstat strip filter: require dark query ink; ghost_frac threshold.
- `comparison_table_ui` alias; gate ignores escape PASS notes in errors.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `scripts/excalibur_blog_cover_qa_gate.py`
- `scripts/excalibur_blog_quad_manifest.py`
- `memory/cover/inline-visual-types.json`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-24
fix_summary:
- Gold typography visual escape (B10) + no-tesseract ink fallbacks; wordstat strip dark-ink filter; meme relaxed signal; collage uses designed_thumbnail_visual_core with manifest.
- `comparison_table_ui` alias in gate, quad_manifest, inline-visual-types catalog.
files_changed:
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `scripts/excalibur_blog_cover_qa_gate.py`
- `scripts/excalibur_blog_quad_manifest.py`
- `memory/cover/inline-visual-types.json`
- `tests/test_cover_qa_pixels_layout.py`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-qa-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile` changed scripts
- `python3 -m unittest tests.test_cover_qa_pixels_layout tests.test_cover_budget tests.test_cover_text`
- `python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir B10...` → OK PASS
commit: 6d1ba33

## INC-20260824-0829-content-learner-metrika-credentials-b10
status: open
run_date: 2026-08-24
role: excalibur-blog-content-learner
topic_id: B10
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER
- Missing `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets/env

### How the agent recovered this run
- Content-learner записал 4 pipeline/editorial lessons из B10 run evidence (OCR empty, hook-bar false positives, budget exhaust flow, phone_scammers_notary angle).
- Metrika cohort analysis пропущен; lessons marked medium confidence без behavioral signals.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B10 для post-publish behavioral baseline.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded (credentials absent)

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

