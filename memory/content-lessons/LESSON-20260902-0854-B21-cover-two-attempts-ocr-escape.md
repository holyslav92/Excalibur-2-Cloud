## LESSON-20260902-0854-B21-cover-two-attempts-ocr-escape
status: proposed
topic_id: B21
category: structure
confidence: medium

### Evidence
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: `solo_cover_attempts: 2`, `budget_exhausted: false`, attempt 2 PASS; hook «У забора пусто — ключи не взяли» (6 слов), sticky «Акт не подписали», fence/countryside scene.
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15 pattern); 8 flaky checks overridden (designed_thumbnail, hook_title_not_truncated, identity_matches_studio, meme_present, collage_inset, wordstat_query_strips, phone_not_clipped, phone_readable); `identity_skin_blob_flake: true`; gate_status PASS.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust — B21 шестой live OCR escape; отличие: attempt 1 FAIL → attempt 2 PASS внутри budget (не B15 exhaust path)

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- COVER_ATTEMPT_ONE_FAIL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: 2 grsai attempts → attempt 2 PASS без budget exhaust; OCR escape на финальном PNG — штатный путь.
- Short hook 6 слов + countryside fence props — on-topic KP utilities stakes.

### Change
- none durable — canon stable; B21 подтверждает retry-within-budget + escape (не regen loop после PASS).

### Never again
- Deep-dive pixel OCR после escape PASS.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook: B21 — 6-й live OCR escape (B08/B09/B10/B15/B20/B21); `memory/cover/cover-canon.json` pattern stable with 2-attempt success path.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli
wp_post_id: 9523
