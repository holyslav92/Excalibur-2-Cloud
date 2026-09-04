## LESSON-20260904-1311-B23-cover-fixer-solo-no-wordstat-strips
status: proposed
topic_id: B23
category: structure
confidence: medium

### Evidence
- artifact: cover/quad-mcp-batch-01.json
  finding: attempt 1 global prefix still carries «1-3 Wordstat stickers (Тюмень)» despite inline ZERO-strip locks — legacy `quad-style-the-rieltor.json` prefix on cover canvas.
- artifact: cover/quad-solo-batch-cover.json
  finding: fixer round solo regen with hard ban «NO Wordstat query strips on cover — Scout Wordstat is topic-only»; `pipeline: quad_solo_panel_regen`, slot cover only.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true`; flaky overrides: `pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_no_collage_inset`, `pixel_no_wordstat_query_strips`, `pixel_phone_not_clipped`, `pixel_phone_readable`; `wordstat=0 paper-gold regions`.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `wordstat_stickers_not_title_overlap: true`, `no_wordstat_query_strips_on_cover` via pixel path.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-cover-fixer-wordstat-strip-round1 — B23 third live confirmation (B12→B15→B20→B23)

### Named blockers
- COVER_WORDSTAT_STRIP_FIRST_ATTEMPT
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: quad inline batch + solo cover regen (≤2 full attempts) — не pixel-debug loop.
- Short hook 6 слов «Дом готов, ипотеку остановили перед ключами» + sticky «ЕГРН остановил сделку» — KP land-category stakes.
- `apply_ocr_false_positive_escape` when visual core face+hook+phone OK.

### Change
- Director: после quad attempt 1 с strip flakes → solo cover regen с strip-ban (не повторять quad-mcp-batch cover prefix).
- `memory/cover/quad-style-the-rieltor.json` — split cover vs inline Wordstat prefix (review-only; B12 proposal still open).

### Never again
- Quad-mcp-batch cover slot с «1-3 Wordstat stickers» global prefix после strip FAIL.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- B23 — sixth live OCR escape path (B08/B09/B10/B12/B15/B20/B23); canon stable under `cover-canon.json`.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya
wp_post_id: 9653
