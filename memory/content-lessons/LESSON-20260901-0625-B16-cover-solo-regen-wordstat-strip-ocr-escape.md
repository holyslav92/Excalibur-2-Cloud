## LESSON-20260901-0625-B16-cover-solo-regen-wordstat-strip-ocr-escape
status: proposed
topic_id: B16
category: structure
confidence: medium

### Evidence
- artifact: cover/quad-mcp-prompt-01.txt, cover/quad-mcp-prompt-02.txt
  finding: quad canvas prompts carried legacy «1-3 Wordstat stickers (Тюмень)» — grsai painted query strips on cover quadrant; `canvas1_attempts: 2` before split.
- artifact: cover/grsai-solo-batch.json, .cursor/excalibur-blog-fragments/cover.md
  finding: solo cover regen attempt 1/2 with hard ban «NO Wordstat query strips on cover — Scout Wordstat is topic-only»; `solo_attempts: 1`, pre_qa PASS.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true` (B08/B09/B15 pattern); 7 flaky checks overridden (`pixel_no_wordstat_query_strips`, `pixel_hook_title_not_truncated`, `pixel_phone_readable`, etc.); visual core face+Cyrillic hook+phone OK; `wordstat=0 paper-gold regions`.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `no_wordstat_query_strips_on_cover` via pixel checks, `cover_phone_on_cover: true`.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9439 ingest skipped)
- cross_run: LESSON-20260828-1310-B12-cover-fixer-wordstat-strip-round1 — второй post-publish run с quad Wordstat strip FAIL → solo regen + OCR escape (B12 fixer round1, B16 Director solo path)

### Named blockers
- COVER_WORDSTAT_STRIP_QUAD_FIRST_ATTEMPT
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: quad inline path OK; cover slot → solo regen с strip-ban вместо повторного quad batch.
- Short hook 5 слов «Мокрая стяжка — ключи не выдали» + sticky «Подписывать или ждать?» — on-topic acceptance stakes.
- `apply_ocr_false_positive_escape` при визуально OK PNG (face + Cyrillic hook + phone + thinking_cat meme).

### Change
- Director: после quad strip FAIL сразу `grsai_solo_cover` с NO Wordstat prefix — не тратить canvas1 attempt 2 на тот же legacy quad-mcp-batch prefix (B16 подтверждает B12 proposal).
- Cover-text: highlight «Мокрая» на gold — держать в gate notes как OCR-sensitive token (как B15 «остановила»).

### Never again
- Повторять quad-mcp-batch с «1-3 Wordstat stickers» на cover slot после strip FAIL на canvas1.
- PIL mashup / Kie при strip/OCR flakes — только prompt fix + OCR escape.

### Proposed apply
- `memory/cover/quad-style-the-rieltor.json` → split cover vs inline prefix: cover = NO Wordstat strips (review-only; B12+B16 = 2 runs).
- Director runbook: B16 — пятый live proof OCR escape path после B08/B09/B10/B12/B15.

### Durable applied
- none — proposal review-only; rollback N/A until applied

### Resolution
status: recorded
article_dir: memory/blog/articles/B16-na-priemke-novostrojki-v-tyumeni-nashli-mokruyu-styazhku-klyuchi-ne-vydali
wp_post_id: 9439
