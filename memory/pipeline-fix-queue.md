# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260822-1110-cover-regen-wordstat-strip-b08
status: fixed
run_date: 2026-08-22
role: excalibur-blog-fixer
topic_id: B08
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
severity: medium
category: script

### What went wrong
- Cover-QA initial FAIL: `pixel_host_close_up`, `pixel_meme_present`, `pixel_no_wordstat_query_strips`.
- `quad_regen_panels` for cover used `build_prompt` (quad canvas) because B08 manifest lacked `wordstat_pil_only: true` (B05–B07 had it).
- `quad-solo-batch-cover.json` prompt still contained `1-3 Wordstat stickers (Тюмень)` from `quad-style-the-rieltor.json` global_prefix → model painted query strips.

### How the agent recovered this run
- Z-Image MCP generated solo cover; pixel QA PASS; publish wp_post_id 9073.

### Durable fix needed before next run
- Default `wordstat_pil_only: true` in `apply_quad_canon_to_manifest`.
- Cover panel regen always via `build_solo_cover_prompt` (solo 16:9, no Wordstat strips).
- Strip Wordstat-on-cover phrasing from shared style prefix in `build_prompt`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_quad_slots.py`
- `scripts/excalibur_blog_quad_regen_panels.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-22
fix_summary:
- `apply_quad_canon_to_manifest` sets `wordstat_pil_only: true` for 7-inline manifests.
- Cover regen always uses `build_solo_cover_prompt`; `strip_wordstat_from_style_prefix` in quad + solo prompts.
files_changed:
- `scripts/excalibur_blog_quad_slots.py`
- `scripts/excalibur_blog_quad_regen_panels.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`
checks_run:
- `python3 -m py_compile` on changed scripts
- `python3 -m unittest tests.test_fixer_b08` → OK
commit: pending

## INC-20260822-1110-derouter-image-discontinued-b08
status: fixed
run_date: 2026-08-22
role: excalibur-blog-cover
topic_id: B08
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
severity: high
category: api

### What went wrong
- `excalibur_blog_derouter_gpt_image2_api.py` on cover panel regen → HTTP 400 «model discontinued».
- Kie fallback attempted next.

### How the agent recovered this run
- Kie also failed (402 credits); Z-Image MCP emergency cover regen.

### Durable fix needed before next run
- Detect HTTP 400 discontinued/invalid model; explicit `DEROUTER_IMAGE_MODEL` update hint; immediate Kie fallback without pointless retries.
- Document owner action: refresh `DEROUTER_IMAGE_MODEL` from GET `/v1/models`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_derouter_gpt_image2_api.py`
- `shared/derouter-gpt-image-api-contract.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-22
fix_summary:
- `is_derouter_model_terminal_error` + `format_derouter_http_error` for discontinued/invalid model HTTP 400.
- Contract documents fast Kie fallback + owner must update `DEROUTER_IMAGE_MODEL`.
files_changed:
- `scripts/excalibur_blog_derouter_gpt_image2_api.py`
- `shared/derouter-gpt-image-api-contract.md`
checks_run:
- `python3 -m unittest tests.test_fixer_b08.DerouterDiscontinuedTest` → OK
commit: pending

## INC-20260822-1110-kie-credits-402-b08
status: needs-human
run_date: 2026-08-22
role: excalibur-blog-cover
topic_id: B08
article_dir: memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
severity: blocker
category: env

### What went wrong
- After Derouter HTTP 400 discontinued, `excalibur_blog_kie_gpt_image2_api.py` → HTTP 402 insufficient Kie credits on cover regen.

### How the agent recovered this run
- Fixer/Cover agent used MCP-KV `z-image` for solo cover panel; pixel QA PASS.

### Durable fix needed before next run
- Top up Kie account credits in dashboard.
- Script now emits `KIE CREDITS BLOCKER` with explicit message.
- Fixer skill documents z-image emergency for solo cover only when both APIs fail.

### Suggested files to inspect/change
- Cloud Secrets / Kie dashboard billing
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `shared/kie-gpt-image-api-contract.md`
- `skills/fixer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
reason:
- Kie credit balance is owner/env configuration; cannot fix in repo code.
needed_decision_or_secret:
- Top up Kie credits; verify `KIE_API_KEY` account has balance for 2× quad + regen jobs per run.
fix_summary:
- `kie_blocker_message` / `is_kie_credits_exhausted` for HTTP 402; contract + fixer emergency z-image path documented.
files_changed:
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `shared/kie-gpt-image-api-contract.md`
- `skills/fixer-excalibur-blog/SKILL.md`
- `.cursor/skills/fixer-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m unittest tests.test_fixer_b08.KieCreditsTest` → OK

## INC-20260821-0615-content-learner-metrika-credentials
status: open
run_date: 2026-08-21
role: excalibur-blog-content-learner
topic_id: B06, B08
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami; memory/blog/articles/B08-skazali-v-brake-ne-byl-a-v-tyumeni-pered-avansom-vsplyla-umershaya-zhena-i-neofo
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER
- Missing `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets/env
- Повтор на B08 content-learner (2026-08-22): exit 2, тот же blocker

### How the agent recovered this run
- B06: Content-learner записал pipeline lessons из run evidence (Derouter 524 chunk, quality-bar PIL sync, html_linter CTA div).
- B08: Content-learner записал 3 lessons (sibling anti-dup, ZAGS period utility, Writer/Sol compression) без Metrika cohort.
- Metrika cohort analysis пропущен; lessons marked low/medium confidence без behavioral signals.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06/B08 для post-publish behavioral baseline.

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

