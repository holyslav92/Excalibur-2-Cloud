# Excalibur BLOG — pipeline fix queue

## INC-20260820-1015-sol-524-chunk
status: fixed
run_date: 2026-08-20
role: excalibur-blog-sol
topic_id: B03
article_dir: memory/blog/articles/B03-doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero
severity: high
category: api

### What went wrong
- Single-shot Derouter Sol call timed out (HTTP 524) on longform B03.
- Conductor manually split Sol into 3 parts and merged HTML.

### How the agent recovered this run
- Manual 3-part Sol (`sol-part-1/2/3-out.html`) merged into `article.html` + `drafts/variant-a.html`.

### Durable fix needed before next run
- Automate 3-part Sol chunking like Writer (`excalibur_blog_writer_chunk.py`).

### Suggested files to inspect/change
- `scripts/excalibur_blog_sol_chunk.py`
- `skills/sol-excalibur-blog/SKILL.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-20
fix_summary:
- Added `scripts/excalibur_blog_sol_chunk.py` (3 Derouter Opus parts, merge + variant-a copy).
- Updated Sol skill runbook: longform uses chunk script first; `--single-shot` for short only.
files_changed:
- `scripts/excalibur_blog_sol_chunk.py`
- `skills/sol-excalibur-blog/SKILL.md`
- `.cursor/skills/sol-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_sol_chunk.py`
commit: 9fe3715

---

## INC-20260820-1030-h2-anchor-inject-mismatch
status: fixed
run_date: 2026-08-20
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero
severity: medium
category: script

### What went wrong
- `quad_apply --inject-html` failed: manifest preserved shortened `h2_anchor` from `--merge` instead of full H2 from `article.html`.
- Conductor injected 7 `<figure data-slot>` manually via Python.

### How the agent recovered this run
- Manual figure inject after reading full H2 from `article.html`.

### Durable fix needed before next run
- `quad-manifest.py` must always sync `h2_anchor` from article H2 (not preserve stale shortened anchors).

### Suggested files to inspect/change
- `scripts/excalibur_blog_quad_manifest.py`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-20
fix_summary:
- `build_manifest`: inline `h2_anchor` always taken from `article.html` extract, never from preserved old value.
files_changed:
- `scripts/excalibur_blog_quad_manifest.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_quad_manifest.py`
commit: 9fe3715

---

## INC-20260820-1045-derouter-images-exhausted
status: needs-human
run_date: 2026-08-20
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero
severity: medium
category: api

### What went wrong
- Derouter REST image API quota/exhausted on both quad canvases B03.
- Kie fallback used for cover + inline generation.

### How the agent recovered this run
- `excalibur_blog_quad_regen_panels.py` / Kie path; `cover_qa.json` PASS with `regeneration: kie_fallback_derouter_exhausted`.

### Durable fix needed before next run
- Monitor Derouter image quota; confirm `api-direct.derouter.ai` host and DEROUTER_API_KEY limits in Cloud Secrets.

### Suggested files to inspect/change
- `shared/derouter-gpt-image-api-contract.md`
- `skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
reason:
- Env/API quota issue; Kie fallback already documented and worked. No code change required beyond monitoring.
needed_decision_or_secret:
- Derouter image tier quota / billing review for daily cron volume (2 canvases × 2K per article).

---

## INC-20260820-1050-cover-text-schema-derouter-refusal
status: needs-human
run_date: 2026-08-20
role: excalibur-blog-cover-text
topic_id: B03
article_dir: memory/blog/articles/B03-doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero
severity: medium
category: api

### What went wrong
- Derouter terra roles `cover-text` and `schema` returned refusal (no shell output) on first attempt.
- Conductor assembled `cover-text.json` and `schema.jsonld` from template/B02 pattern; gates PASS.

### How the agent recovered this run
- Manual JSON assembly per cover-text gate contract; schema without FAQPage (no FAQ H2 in article).

### Durable fix needed before next run
- Retry Derouter utility calls before manual assembly; log refusal reason in stamp files.

### Suggested files to inspect/change
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `shared/derouter-opus-brain-contract.md`

### Secrets
- none recorded

### Fixer resolution
reason:
- One-off Derouter refusal; article shipped with valid gates. Retry policy already in derouter chat (5xx retry).
needed_decision_or_secret:
- If refusals repeat, inspect Derouter utility tier policy for JSON-only roles.

---

## INC-20260820-1100-metrika-credentials-missing
status: needs-human
run_date: 2026-08-20
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero
severity: medium
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → `METRIKA CREDENTIALS BLOCKER`.
- `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` not in Cloud Secrets.

### How the agent recovered this run
- Content-learner recorded low-confidence Metrika-only lesson; evidence gate SKIP (no report file).

### Durable fix needed before next run
- Add Metrika OAuth + counter id to Cloud Secrets for cron content-learner.

### Suggested files to inspect/change
- Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`

### Secrets
- none recorded

### Fixer resolution
reason:
- Credentials outside repo scope; cannot fix in code without secrets.
needed_decision_or_secret:
- Yandex Metrika OAuth token (metrika:read) + counter id for tenant site (PUBLIC_SITE_URL)
