# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260826-0629-cover-qa-pixel-b10
status: open
run_date: 2026-08-26
role: excalibur-blog-cover-qa
topic_id: B10
article_dir: memory/blog/articles/B10-kupili-kvartiru-v-tyumeni-cherez-god-finupravlyayuschij-osporil-sdelku
severity: high
category: qa

### What went wrong
- Cover-QA pixel FAIL after cover budget exhausted (2 solo grsai attempts).
- Fails: `pixel_no_collage_inset`, `pixel_designed_thumbnail`, `pixel_phone_readable`, `pixel_hook_title_not_truncated`, `pixel_no_wordstat_query_strips`.
- grsai generated polaroid/inset collage layout; phone clipped; hook OCR incomplete; Wordstat-like strip on PNG.

### How the agent recovered this run
- `cover-budget-result.json` stamped; best candidate kept as cover.png; pipeline proceeded toward Indexer per fail-fast canon.

### Durable fix needed before next run
- Strengthen solo/quad cover prompt: designed thumbnail, NO polaroid inset, phone full frame not clipped.
- Sanitize stale Wordstat-on-cover language in design-code/style prefix.
- Preflight: wordstat_stickers topic-log only; block scene_hint echo of query phrases.
- Fixer: one regen round via `excalibur_blog_cover_fixer.py`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `scripts/excalibur_blog_cover_budget.py`
- `scripts/excalibur_blog_quad_manifest_preflight.py`
- `memory/cover/cover-design-code.json`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
status: needs-human
fixed_at: 2026-08-26
fix_summary:
- Prompt contract: `designed_thumbnail_prompt_block`, `phone_full_frame_prompt_block`, `collage_inset_ban_prompt_block` in solo/quad cover prompts.
- Sanitized stale Wordstat-on-cover language in `cover-design-code.json` + `sanitize_cover_style_prefix`.
- Preflight: wordstat_stickers topic-log only; warn on hook drift vs cover-text.json.
- `sync_manifest_hook_from_cover_text` before solo/regen prompt build (manifest had longer hook than cover-text).
- Fixer one round: regen 2× grsai still FAIL pixel QA; kept prior cover.png (md5 d56d3698…).
files_changed:
- `scripts/excalibur_blog_cover_budget.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `scripts/excalibur_blog_quad_manifest_preflight.py`
- `scripts/excalibur_blog_grsai_solo_cover.py`
- `scripts/excalibur_blog_quad_regen_panels.py`
- `memory/cover/cover-design-code.json`
- `shared/blog-cover-quad-canvas-contract.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-text-excalibur-blog/SKILL.md`
- `tests/test_cover_budget.py`
checks_run:
- `python3 -m py_compile` on changed scripts
- `python3 -m unittest tests.test_cover_budget` → OK
- `python3 scripts/excalibur_blog_cover_fixer.py --max-rounds 1` B10 → FAIL (pixel QA unchanged)
commit: 7fe8c61 (+ follow-up hook-sync)
reason:
- grsai standard tier still emits collage-inset layout + clipped phone on B10 after budget+fixer; visual manual PASS or owner regen with shorter hook may be needed.
needed_decision_or_secret:
- Human review B10 cover.png; optional manual stamp PASS if visual OK (B08/B09 OCR escape pattern) or re-run Cover with merged cover-text hook.

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

