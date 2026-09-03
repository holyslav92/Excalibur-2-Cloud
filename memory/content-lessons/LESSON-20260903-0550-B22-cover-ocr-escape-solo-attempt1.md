## LESSON-20260903-0550-B22-cover-ocr-escape-solo-attempt1
status: proposed
topic_id: B22
category: structure
confidence: medium

### Evidence
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15/B20 pattern); `identity_hist_near_match_flake: true`; 7 flaky checks overridden (designed_thumbnail, hook_title_not_truncated, identity_matches_studio, collage_inset, wordstat_query_strips, phone_not_clipped, phone_readable); visual core OK — face + Cyrillic hook + phone + disaster_girl/capybara memes; gate_status PASS.
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: `budget_exhausted: false`, `solo_attempts: 1` — cover passed on first grsai standard attempt (не B15 exhaust path).
- artifact: cover/cover-text.json
  finding: short hook 5 слов «В квартире пропали два метра»; gold highlight «пропали»; sticky «Это не допуск» on-topic area-mismatch stakes.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, `all_pass: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9562 ingest недоступен)
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust — B22 шестой live OCR escape без budget exhaust (B08/B09/B10/B15/B20/B22)

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: solo attempt 1/2 → Cover-QA OCR escape → Publish; не regen loop при визуально OK PNG.
- Short hook 5–7 слов + sticky on-topic («Это не допуск») + people+cats meme canon (disaster_girl, capybara_indifference).
- `apply_ocr_false_positive_escape` при face + Cyrillic hook + phone; identity_hist_near_match_flake — штатный override.

### Change
- none durable — canon validated на 6-м live run; отличие от B15: escape без `cover_budget_exhausted`.

### Never again
- Fixer regen при escape PASS и solo_attempts 1/2.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook: B22 — шестой live OCR escape path; `memory/cover/cover-canon.json` pattern stable.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry
wp_post_id: 9562
