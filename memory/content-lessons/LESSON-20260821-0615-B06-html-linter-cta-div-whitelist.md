## LESSON-20260821-0615-B06-html-linter-cta-div-whitelist
status: applied
topic_id: B06
category: structure
confidence: high

### Evidence
- artifact: html-linter-report.json (pre-fixer) — 3× Forbidden `<div>` на excalibur-cta-early/mid/end
  finding: Sol оборачивает CTA в `<div class="excalibur-cta-*">` по quality-bar-9, но html_linter не имел class-whitelist для div → structure_gate FAIL html_linter.
- artifact: community-cta-gate.json — PASS (ссылки TG/MAX/tel на месте)
- artifact: wp-publish-result.json + live-page-report.json — PASS после fixer whitelist
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- HTML_LINTER_CTA_DIV_CONFLICT
- EVIDENCE_SKIPPED

### Keep
- CTA zones: excalibur-cta-early / mid / end + excalibur-social-cta на end block (quality-bar-9).
- Publish + live-page PASS с div-обёртками CTA.

### Change
- html_linter: ALLOWED_DIV_CLASSES + `is_allowed_div()` — div только с excalibur-cta-* / excalibur-social-cta.
- HTML_WHITELIST_PROMPT_LINE обновлён для Sol/Writer prompts.

### Never again
- Не блокировать publish-ready статью из-за легитимных CTA div, требуемых quality-bar-9.

### Proposed apply
- Регенерировать stale html-linter-report.json в article_dir после fixer (опционально).

### Durable applied
- `scripts/excalibur_blog_html_linter.py` — ALLOWED_DIV_CLASSES whitelist (rollback: revert + заменить div на p-only CTA)

### Resolution
status: applied
article_dir: memory/blog/articles/B06-avtoocenka-kvartiry-na-dva-milliona-nizhe-rynka-circ-s-prosmotrami
wp_post_id: 8984
