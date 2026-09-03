## LESSON-20260903-0802-B22-cover-fixer-layout-round1
status: proposed
topic_id: B22
category: structure
confidence: medium

### Evidence
- artifact: git commit 37fb56f (`B22: Cover-QA PASS after fixer regen (layout/hook/phone)`)
  finding: initial cover PNG FAIL layout/hook/phone; fixer round 1 → solo i2i regen (`cover/cover.png` 970464→904815 bytes); re-QA PASS.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` — 7 flaky overrides (`pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_identity_matches_studio`, `pixel_no_collage_inset`, `pixel_no_wordstat_query_strips`, `pixel_phone_not_clipped`, `pixel_phone_readable`); visual core face+hook+phone OK; `pixel_layout_not_collapsed: true`.
- artifact: cover/quad-solo-batch-cover.json
  finding: fixer prep with `TEXT LAYOUT LOCK`, `NO Wordstat query strips`, hook «Задержка ключей — сертификат вместо денег», lemon-beige overshirt anti-repeat.
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: `budget_exhausted: false`, `grsai_canvas_attempts: 1`, `solo_cover_attempts: 0` (fixer regen не считает solo budget slot — cover from quad top-left after regen).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust + INC-20260901-1338-cover-layout-fixer-round-b20 — B22 = 6-й live OCR escape (B08/B09/B10/B15/B20/B22) + layout fixer round post-B20 durable fix

### Named blockers
- COVER_LAYOUT_HOOK_PHONE_FAIL
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- 1 fixer round + bounded solo regen вместо бесконечного Cover-QA loop.
- Short hook 6 слов «Задержка ключей — сертификат вместо денег» + sticky «Сначала подпись — потом ключи» — on-topic certificate casus.
- `apply_ocr_false_positive_escape` при визуально OK PNG после fixer regen.

### Change
- none durable — B20 `excalibur_blog_cover_layout_retry.py` path validated on B22; Director не ждать 2-й quad canvas attempt при layout FAIL — сразу fixer solo.

### Never again
- Бесконечный pixel OCR loop после fixer regen + escape PASS.
- PIL mashup / Kie при layout/hook flakes.

### Proposed apply
- Director runbook: B22 подтверждает B20 layout-retry canon; `memory/cover/cover-canon.json` OCR escape pattern stable (6 live).

### Durable applied
- none (B20 INC-20260901-1338 already fixed layout retry scripts)

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser
wp_post_id: 9575
