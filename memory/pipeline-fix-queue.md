# Excalibur BLOG — pipeline fix queue

Durable incident memory. Fixer closes `status: open` → `fixed` | `needs-human`.

## INC-20260821-0836-b07-topic-focus-inheritance
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: blocker
category: script

### What went wrong
- `research_start` TOPIC FOCUS BLOCKER: title «Наследству два года…» без «квартир» — `REAL_ESTATE_ALLOW_PATTERNS` не содержал наследство/наследники.

### How the agent recovered this run
- Title patched with «квартиру» / «квартиры» before `research_start` retry.

### Durable fix needed before next run
- Добавить `наследств` / `наследник` в real-estate ALLOW patterns.

### Suggested files to inspect/change
- `scripts/excalibur_blog_topic_focus.py`
- `shared/topic-focus-contract.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `REAL_ESTATE_ALLOW_PATTERNS` += наследств/наследник/отказ от наследства.
files_changed:
- `scripts/excalibur_blog_topic_focus.py`
- `shared/topic-focus-contract.md`
checks_run:
- `python3 scripts/excalibur_blog_topic_focus.py --text "Наследству два года…"` → PASS
- `tests/test_fixer_b07.py`
commit: 559e218

## INC-20260821-0836-b07-early-cta-tldr-h2
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: script

### What went wrong
- `quality-bar-9` `early_cta_tg_max_only` FAIL: Sol поставил TL;DR первым `<h2>`, early CTA оказался после первого H2.

### How the agent recovered this run
- Sol patch: TL;DR в `<p><b>`, early CTA перед первым H2.

### Durable fix needed before next run
- Gate `early_cta_before_first_h2` + Writer/Sol contract: TL;DR не H2.

### Suggested files to inspect/change
- `scripts/excalibur_blog_quality_bar_9_gate.py`
- `shared/quality-bar-9.md`
- `skills/sol-excalibur-blog/SKILL.md`
- `skills/writer-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- New gate checks `early_cta_before_first_h2`; quality-bar-9 + Writer/Sol skills document TL;DR zone.
files_changed:
- `scripts/excalibur_blog_quality_bar_9_gate.py`
- `shared/quality-bar-9.md`
- `skills/sol-excalibur-blog/SKILL.md`
- `skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
checks_run:
- `tests/test_fixer_b07.py`
commit: 2a20eb7

## INC-20260821-0836-b07-site-base-end-cta
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: prompt

### What went wrong
- `end_cta_full_channels` FAIL: Sol оставил `{{SITE_BASE}}` в href end CTA; gate ожидает `/`, `/gajdy/`.

### How the agent recovered this run
- Sol patch: relative paths `/`, `/gajdy/`, `/rieltor-tyumen/`.

### Durable fix needed before next run
- Gate `no_site_base_placeholder_in_article` + Sol skill ban `{{SITE_BASE}}` in article.html.

### Suggested files to inspect/change
- `scripts/excalibur_blog_quality_bar_9_gate.py`
- `shared/quality-bar-9.md`
- `skills/sol-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `check_no_site_base_placeholder`; quality-bar-9 + Sol: article.html uses `/path` only.
files_changed:
- `scripts/excalibur_blog_quality_bar_9_gate.py`
- `shared/quality-bar-9.md`
- `skills/sol-excalibur-blog/SKILL.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`
checks_run:
- `tests/test_fixer_b07.py`
commit: 2a20eb7

## INC-20260821-0836-b07-cover-qa-gold-band
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: docs

### What went wrong
- `cover_qa` pixel FAIL: gold horizontal band under highlight + blazer default outfit.

### How the agent recovered this run
- Cover retry (cream henley, gold letters only) → cover_qa PASS.

### Durable fix needed before next run
- Cover skill: gold letters only, no brush band; variety lock reminder.

### Suggested files to inspect/change
- `skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- Cover skill §Gold highlight (B07): letters only, no horizontal band.
files_changed:
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
checks_run:
- manual run evidence (cover_qa PASS after retry)
commit: 2a20eb7

## INC-20260821-0836-b07-link-verify-reestr-nasled
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: script

### What went wrong
- `link_verify` FAIL: `<a href="https://reestr-nasled.ru">` DNS error from Cloud egress.

### How the agent recovered this run
- Removed href; plain text `reestr-nasled.ru` in article.html.

### Durable fix needed before next run
- Early denylist in link_verify + Writer/Sol plain-text rule for registry hosts.

### Suggested files to inspect/change
- `scripts/excalibur_blog_link_verify.py`
- `skills/writer-excalibur-blog/SKILL.md`
- `skills/sol-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- `known_bad_registry_plain_text_reason` for reestr-nasled.ru; Writer/Sol cite plain text.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
- `skills/writer-excalibur-blog/SKILL.md`
- `skills/sol-excalibur-blog/SKILL.md`
- `.cursor/skills/writer-excalibur-blog/SKILL.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`
checks_run:
- `tests/test_fixer_b07.py`
commit: 2a20eb7

## INC-20260821-0836-b07-theme-deploy-ftp-root
status: fixed
run_date: 2026-08-21
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: env

### What went wrong
- `theme_contract_deploy` SFTP ENOENT on configured `FTP_ROOT` before publish (fallback `.` worked).

### How the agent recovered this run
- Publish continued with root fallback `.`; wp-publish-log recommends `FTP_ROOT=.`.

### Durable fix needed before next run
- WARN on theme deploy fallback; doctor WARN when FTP_ROOT ≠ `.`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `scripts/excalibur_blog_doctor.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-21
fix_summary:
- theme_contract_deploy logs WARN on root fallback; doctor warns non-dot FTP_ROOT/SSH_ROOT.
files_changed:
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `scripts/excalibur_blog_doctor.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_theme_contract_deploy.py`
commit: 2a20eb7

## INC-20260821-0615-content-learner-metrika-credentials
status: open
run_date: 2026-08-21
role: excalibur-blog-content-learner
topic_id: B06,B07
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami; memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER
- Missing `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets/env
- Reproduced on B07 content-learner (2026-08-21 08:36 UTC) — post_id 8994

### How the agent recovered this run
- Content-learner B06: pipeline lessons из run evidence (Derouter 524 chunk, quality-bar PIL sync, html_linter CTA div).
- Content-learner B07: 3 named lessons из pipeline evidence (topic focus marker, early CTA position, reestr-nasled DNS); Metrika cohort skipped.
- Lessons marked high confidence on pipeline artifacts; behavioral signals absent.

### Durable fix needed before next run
- Добавить Yandex Metrika OAuth + counter id в Cloud Secrets.
- Повторить ingest после publish B06/B07 для post-publish behavioral baseline.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded (credentials absent)

## INC-20260821-0836-reestr-nasled-cloud-dns-b07
status: open
run_date: 2026-08-21
role: excalibur-blog-content-learner
topic_id: B07
article_dir: memory/blog/articles/B07-nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
severity: medium
category: env

### What went wrong
- `curl https://reestr-nasled.ru/` from Cloud → `Could not resolve host` (DNS, no HTTP status).
- Writer draft variant-a with `<a href="https://reestr-nasled.ru">` would FAIL link_verify; final article.html uses plain text only.

### How the agent recovered this run
- Sol/final article keeps plain-text `reestr-nasled.ru`; link-verify PASS; publish PASS post_id 8994.

### Durable fix needed before next run
- Document plain-text policy for FNP registry in research/writer guidance OR add reestr-nasled.ru to DNS-soft path in link_verify (mirror SOFT_EXTERNAL_HOSTS pattern).

### Suggested files to inspect/change
- `scripts/excalibur_blog_link_verify.py`
- `shared/excalibur-research/SKILL.md` or research skill notes

### Secrets
- none recorded

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

