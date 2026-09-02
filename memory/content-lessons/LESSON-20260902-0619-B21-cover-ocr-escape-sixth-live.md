## LESSON-20260902-0619-B21-cover-ocr-escape-sixth-live
status: proposed
topic_id: B21
category: structure
confidence: medium

### Evidence
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape.applied: true` (B08/B09/B15 live pattern); **6** flaky checks overridden (`pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_identity_matches_studio`, `pixel_no_collage_inset`, `pixel_no_wordstat_query_strips`, `pixel_wordstat_not_opaque_bars`); `identity_skin_blob_flake: true`; visual core OK — face + Cyrillic hook + phone; gate_status PASS.
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: solo cover 2 attempts (attempt 2 PASS) + 1 restore after quad split overwrite (PASS); `cover-budget-result.json` not created — budget not exhausted; inline quads 2×1 job OK.
- artifact: cover/cover-text.json
  finding: short hook «Оплатили переуступку — дольщиком не стали» (5–7 words); sticky «Оплата не даёт права»; NO Wordstat strips.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, `wordstat_stickers_not_title_overlap: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust — B20 5th live; B21 **6th** live OCR escape without budget exhaust

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- IDENTITY_SKIN_BLOB_FLAKE
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `apply_ocr_false_positive_escape` при visual core OK (face + hook + phone) без budget exhaust — штатный путь, не regen loop.
- Solo 2-attempt budget + quad restore path без `cover-budget-result.json`.
- Meme people+cats (disappointed_black_guy + doge cover); anti-repeat 14d PASS.

### Change
- none durable — 6-й live proof стабилизирует B08/B09/B15/B20 pattern; `identity_skin_blob_flake` остаётся в override set.

### Never again
- Fixer regen / Kie / PIL mashup при escape PASS и budget not exhausted.
- Novel-length hook на assignment casus (ломает OCR).

### Proposed apply
- Director runbook: B21 — шестой live OCR escape; canon stable in `memory/cover/cover-canon.json`.
- Consider durable apply to cover-qa skill checklist only after human review (≥6 runs documented).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-/
wp_post_id: 9510
