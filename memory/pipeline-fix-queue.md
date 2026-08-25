# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260825-0500-quad-prompt-budget-b10
status: fixed
run_date: 2026-08-25
role: excalibur-blog-fixer
topic_id: B10
article_dir: memory/blog/articles/B10-dogovor-podpisali-a-deneg-ne-bylo-v-tyumeni-nasledniki-zabrali-kvartiru
severity: blocker
category: script

### What went wrong
- `excalibur_blog_cover_quad_prompt.py --write-batch` → MCP prompt 3564 chars > 3500.
- Quad canvas batches never created; 7 inline PNG missing.

### How the agent recovered this run
- Compacted shared ban_line, reference_line, wordstat_line in build_prompt (~250 chars reclaimed).
- B10 canvas 1 prompt 3317 chars; canvas 2 2782 — batch JSON written.

### Durable fix needed before next run
- Keep shared lock text compact; scene_hint targets unchanged.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-25
fix_summary:
- Reclaimed chars from shared ban/reference/wordstat locks; pick_identity_reference import already present.
files_changed:
- `scripts/excalibur_blog_cover_quad_prompt.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_quad_prompt.py`
- `excalibur_blog_cover_quad_prompt.py --write-batch --canvas-index 1/2` → PASS ≤3500
commit: 16557d2

## INC-20260825-0500-cover-solo-ocr-b10
status: needs-human
run_date: 2026-08-25
role: excalibur-blog-cover
topic_id: B10
article_dir: memory/blog/articles/B10-dogovor-podpisali-a-deneg-ne-bylo-v-tyumeni-nasledniki-zabrali-kvartiru
severity: blocker
category: cover

### What went wrong
- grsai solo cover budget exhausted (2 attempts); OCR cannot read Cyrillic hook or phone on best_candidate PNG.
- cover_qa FAIL → quality-bar-9 cover_qa_pass false → publish blocked.

### How the agent recovered this run
- Per canon: proceed Indexer after budget exhaustion; draft status in article.meta.json.

### Durable fix needed before next run
- Regenerate cover via quad canvas (now unblocked) or tighten solo cover TEXT LOCK for OCR-readable hook+phone.
- Manual cover regen or `--media-refresh --featured-only` after PASS.

### Suggested files to inspect/change
- `scripts/excalibur_blog_grsai_solo_cover.py`
- `scripts/excalibur_blog_cover_qa_gate.py`

### Secrets
- none recorded

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

