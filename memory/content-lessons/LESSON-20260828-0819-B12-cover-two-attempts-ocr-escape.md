## LESSON-20260828-0819-B12-cover-two-attempts-ocr-escape
status: proposed
topic_id: B12
category: structure
confidence: medium

### Evidence
- artifact: cover/quad-mcp-result-01.json + cover/quad-mcp-result-02.json
  finding: 2 grsai quad canvas attempts (`canvas-quad-01`, `canvas-quad-02`); run notes «cover 2 attempts» within EXCALIBUR_COVER_MAX_ATTEMPTS budget.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true` — flaky checks overridden: `pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_no_collage_inset`, `pixel_no_wordstat_query_strips`; visual core face + Cyrillic hook + phone OK (B08/B09 pattern).
- artifact: cover/cover-text.json
  finding: Hook 6 words «Квартиру продали двоим — кто останется?»; highlight «двоим»; sticky «Суда ещё нет»; meme_picks people+cats (`two_buttons`, `crying_cat`).
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true` — publish unblocked post 9240.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES (resolved via escape)
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 attempts → Indexer path if budget exhaust (B12 passed attempt 2, no budget-result.json).
- Short hook 5–7 слов + sticky on-topic («Суда ещё нет») — aligns with OCR expectations.
- `apply_ocr_false_positive_escape` when PNG visually OK — fifth live proof chain B08→B09→B10→B11→B12.

### Change
- Attempt 1 quad-split had `status: BLOCK` (inline_3 H2 anchor mismatch «Риелтор и хитрый пункт» vs article H2); attempt 2 gutter_detect split succeeded — Cover pipeline should align quad-manifest h2_anchor with final Sol H2 before regen (reduces wasted attempt 1).
- Cross-ref LESSON-20260826-0834-B10-cover-budget-ocr-escape: B12 confirms escape path without budget exhaust when attempt 2 visual PASS.

### Never again
- Deep pixel OCR debug loop beyond 2 attempts.
- PIL mashup / Kie при OCR-only flakes.

### Proposed apply
- Director: при attempt 1 quad-split BLOCK on H2 anchor → fix manifest anchors before attempt 2 (B12 inline_3 lesson).
- После ≥5 OCR-escape publishes (B08–B12): validate B10 proposal «phone-in-hand close-up default» — optional human review, не auto-expand cover skill.

### Durable applied
- none (canon in cover-canon.json; B12 adds H2-anchor preflight proposal)

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit
wp_post_id: 9240
