# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

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
- **2026-08-26 B10 content-learner:** same METRIKA CREDENTIALS BLOCKER; post 9161 ingest skipped; B10 lessons recorded without behavioral signals.
- **2026-08-27 B11 content-learner:** same METRIKA CREDENTIALS BLOCKER; post 9191 ingest skipped; B11 lessons recorded without behavioral signals.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06, B10 (post 9161) и B11 (post 9191) для post-publish behavioral baseline.

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

## INC-20260826-0830-sol-derouter-524-b10
status: fixed
run_date: 2026-08-26
role: excalibur-blog-sol
topic_id: B10
article_dir: memory/blog/articles/B10-v-tyumeni-rodstvenniki-ostanovili-prodazhu-pozhilogo-prodavca-veli-po-telefonu-v
severity: high
category: api

### What went wrong
- Sol single-shot `excalibur_blog_derouter_opus_chat.py --role sol` → HTTP 524 (Cloudflare timeout) на полном longform HTML.

### How the agent recovered this run
- 3-chunk Sol merge (part1–part3 Derouter calls) → merged `article.html` + stamps `derouter-opus-stamp-sol-part*.json`.

### Durable fix needed before next run
- `excalibur_blog_sol_chunk.py` — mirror `writer_chunk.py`; Sol skill/agent default longform path.

### Suggested files to inspect/change
- `scripts/excalibur_blog_sol_chunk.py`
- `skills/sol-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-sol.md`
- `shared/derouter-opus-brain-contract.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-26
fix_summary:
- Added `excalibur_blog_sol_chunk.py` — 3-part Sol on longform (inline≥7), merge article.html + variant-a.html.
- Sol skill/agent + derouter contract updated; doctor lists script.
files_changed:
- `scripts/excalibur_blog_sol_chunk.py`
- `skills/sol-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-sol.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`
- `.cursor/agents/excalibur-blog-sol.md`
- `shared/derouter-opus-brain-contract.md`
- `scripts/excalibur_blog_doctor.py`
- `tests/test_pipeline_speed_b03.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_sol_chunk.py`
- `python3 -m unittest tests.test_pipeline_speed_b03.SolChunkTest`
commit: 62f1bb2

## INC-20260826-0831-cover-ocr-false-positive-b10
status: fixed
run_date: 2026-08-26
role: excalibur-blog-cover-qa
topic_id: B10
article_dir: memory/blog/articles/B10-v-tyumeni-rodstvenniki-ostanovili-prodazhu-pozhilogo-prodavca-veli-po-telefonu-v
severity: medium
category: qa

### What went wrong
- Pixel QA FAIL on OCR truncation / opaque flakes while visual core OK (face + Cyrillic hook + phone on PNG) — B08/B09 pattern.

### How the agent recovered this run
- `apply_ocr_false_positive_escape` + manual visual PASS stamp in `cover_qa.json` (`ocr_false_positive_escape: true`).

### Durable fix needed before next run
- Escape already in `cover_qa_pixels.py` + cover-qa skill; no code change — document B10 as live proof.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_qa_pixels.py`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `tests/test_cover_budget.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-26
fix_summary:
- Confirmed durable `apply_ocr_false_positive_escape` path; B10 `cover_qa.json` stamped PASS with escape flag (no new code).
files_changed:
- none (contract already canonical)
checks_run:
- `python3 -m unittest tests.test_cover_budget` (OCR escape test)
commit: 62f1bb2

## INC-20260826-0832-cover-fixer-host-closeup-b10
status: fixed
run_date: 2026-08-26
role: excalibur-blog-fixer
topic_id: B10
article_dir: memory/blog/articles/B10-v-tyumeni-rodstvenniki-ostanovili-prodazhu-pozhilogo-prodavca-veli-po-telefonu-v
severity: medium
category: script

### What went wrong
- Cover fixer regen left distant host (`face_h_frac=0.12`) — `pixel_host_close_up` FAIL despite layout OK.

### How the agent recovered this run
- grsai solo regen with close-up prompt → `face_h_frac=0.58`, visual PASS.

### Durable fix needed before next run
- `cover_fixer.py`: host-only FAIL → `grsai_solo_cover` with `HOST_CROP_LOCK` prompt suffix (not quad panel regen).

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_fixer.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-26
fix_summary:
- `regen_cover_host_closeup()` calls `excalibur_blog_grsai_solo_cover.py --prompt-suffix HOST_CROP_LOCK` when host_fail without layout/artifact fail.
files_changed:
- `scripts/excalibur_blog_cover_fixer.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_fixer.py`
commit: 62f1bb2

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

