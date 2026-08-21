# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260821-0615-content-learner-metrika-credentials
status: needs-human
run_date: 2026-08-21
role: excalibur-blog-content-learner
topic_id: B06, B07
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami; memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER
- Missing `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets/env
- B07 content-learner (2026-08-21 11:09 UTC): same blocker on wp_post_id 8994

### How the agent recovered this run
- B06: Content-learner записал pipeline lessons из run evidence (Derouter 524 chunk, quality-bar PIL sync, html_linter CTA div).
- B07: Content-learner записал B07 lessons (524 validates B06, cover Kie fallback, schema output path); Metrika cohort skipped.
- Metrika cohort analysis пропущен; lessons marked low/medium confidence без behavioral signals.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06/B07 для post-publish behavioral baseline.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded (credentials absent)

### Fixer resolution
status: needs-human
fixed_at: 2026-08-21
reason:
- Missing Yandex Metrika OAuth token and counter id in Cloud Secrets — not fixable in repo code.
needed_decision_or_secret:
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

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

## INC-20260821-1040-schema-output-root
status: fixed
run_date: 2026-08-21
role: excalibur-blog-schema
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
severity: low
category: script

### What went wrong
- `excalibur_blog_derouter_opus_chat.py --output schema.jsonld --article-dir memory/blog/articles/B07-…` записал JSON-LD в `/workspace/schema.jsonld` (корень репо), а не в `--article-dir`.

### How the agent recovered this run
- Переместил `schema.jsonld` в каталог статьи; `schema_gate.py` → PASS.

### Durable fix needed before next run
- Резолвить `--output` относительно `--article-dir`, если задан только basename; или обновить skill/agent prompt на полный repo-relative путь выхода.

### Suggested files to inspect/change
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `resolve_output_path()`: bare `--output` + `--article-dir` → `<article-dir>/<file>`; `memory/...` paths still root-relative.
- Schema skill documents bare output contract (INC-20260821-1040).
files_changed:
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `tests/test_derouter_resolve_model.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_derouter_opus_chat.py`
- `python3 -m unittest tests.test_derouter_resolve_model` → OK
commit: pending-parent-commit

## INC-20260821-1100-publish-notariat-linkverify
status: fixed
run_date: 2026-08-21
role: excalibur-blog-publish
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvu-na-kvartiru-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
severity: medium
category: script

### What went wrong
- `link_verify` hard-FAIL on `https://notariat.ru/` (Cloud egress: TLS timeout or bot 404) despite site live via WebFetch.
- First publish insert created post 8994 with stale draft title/body; live gate BLOCK until republish with `wp_post_id`.
- Inbound interlink skipped: ledger rows lack `post_id`; manual bootstrap with WP IDs 8984/8823/8813.

### How the agent recovered this run
- Added `notariat.ru` to `RF_OFFICIAL_SOFT_EXTERNAL_HOSTS` in `excalibur_blog_link_verify.py`.
- Set `wp_post_id: 8994` in `article.meta.json`; republish → live-page PASS.
- Applied inbound interlink via `excalibur-blog-interlink-once.php` with resolved post IDs.

### Durable fix needed before next run
- Store `post_id` in `shared/published-articles.md` on publish for interlink bootstrap.
- Theme contract deploy: SFTP root `.` — theme path not found on configured root (WARN only if theme already patched).

### Suggested files to inspect/change
- `scripts/excalibur_blog_link_verify.py`
- `scripts/excalibur_blog_wp_publish.py` (ledger post_id column)
- Cloud Secrets: `FTP_ROOT=.` 

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `RF_OFFICIAL_SOFT_EXTERNAL_HOSTS` includes `notariat.ru` (404/timeout soft-pass); unit tests added.
- `upsert_publish_ledger` writes 6th column `post_id`; parses from `OK post=`; persists `wp_post_id` in article.meta.json.
- `parse_ledger` reads post_id; ledger backfilled B02–B07 from wp-publish-log/meta.
- `interlink-contract.md` documents post_id requirement for inbound bootstrap.
- Theme SFTP root mismatch → **needs-human**: set `FTP_ROOT` in Cloud Secrets to WP docroot (not `.`).
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_interlink_lib.py`
- `shared/published-articles.md`
- `shared/interlink-contract.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `tests/test_link_verify_soft_pass.py`
- `tests/test_interlink_ledger_post_id.py`
- `tests/test_wp_categories_interlink.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py scripts/excalibur_blog_interlink_lib.py`
- `python3 -m unittest tests.test_link_verify_soft_pass tests.test_interlink_ledger_post_id tests.test_wp_categories_interlink.WpCategoriesInterlinkTests.test_ledger_upsert_dedupes_legacy_row` → OK
commit: pending-parent-commit

