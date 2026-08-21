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

## INC-20260821-1223-derouter-budget-b08-sol
status: open
run_date: 2026-08-21
role: excalibur-blog-sol
topic_id: B08
article_dir: memory/blog/articles/B08-tri-mesyaca-iskali-kvartiru-v-tyumeni-i-soglasilis-na-risk
severity: blocker
category: env

### What went wrong
- `excalibur_blog_derouter_opus_chat.py --role sol` → DEROUTER SOL BLOCKER (parts 2–3)
- Derouter HTTP 402: `budget_exceeded` — API key budget exhausted (primary + fallback endpoints)
- Smoke test also fails with same 402 (utility tier too)

### How the agent recovered this run
- Собран `assembled-sol-inputs.md` (trim 2000–2600, 7 inline slots, 4 interlinks, 3 CTA zones).
- 3-part chunk user files: `sol-part{1,2,3}-user.md`.
- **Sol part 1/3 PASS** → `sol-part1.html` + `derouter-opus-stamp-sol-part1.json` (~8248 chars).
- **Sol parts 2–3 BLOCKER** (402 immediately after part 1).
- `article.html` **не** создан — запрещён Composer fallback для Sol prose.

### Durable fix needed before next run
- Пополнить бюджет `DEROUTER_API_KEY` или поднять лимит ключа в Derouter / apikey.cloud.
- Resume Sol chunk (do NOT single-shot — 524 risk):
```bash
ART=memory/blog/articles/B08-tri-mesyaca-iskali-kvartiru-v-tyumeni-i-soglasilis-na-risk
for p in 2 3; do
  python3 scripts/excalibur_blog_derouter_opus_chat.py --role sol \
    --system-file skills/sol-excalibur-blog/SKILL.md \
    --user-file "$ART/sol-part${p}-user.md" \
    --output "$ART/sol-part${p}.html" \
    --article-dir "$ART" \
    --stamp-path "$ART/derouter-opus-stamp-sol-part${p}.json"
done
cat "$ART/sol-part1.html" "$ART/sol-part2.html" "$ART/sol-part3.html" > "$ART/article.html"
cp "$ART/article.html" "$ART/drafts/variant-a.html"
# gates → Description → Cover-text || Schema → Cover → Cover-QA → Indexer → Publish
```

### Suggested files to inspect/change
- Cloud Secrets: `DEROUTER_API_KEY`
- `shared/derouter-opus-brain-contract.md`

### Secrets
- none recorded (budget issue, not missing key)

