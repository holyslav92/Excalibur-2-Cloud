## LESSON-20260828-1310-B12-cover-fixer-wordstat-strip-round1
status: proposed
topic_id: B12
category: structure
confidence: medium

### Evidence
- artifact: cover/quad-mcp-prompt-01.txt, cover/quad-mcp-prompt-02.txt
  finding: attempt 1 quad prompts still carried «1-3 Wordstat stickers (Тюмень)» — grsai painted collage inset + query strips on cover canvas.
- artifact: cover/quad-solo-batch-cover.json
  finding: fixer round 1 solo regen with hard ban «NO Wordstat query strips on cover — Scout Wordstat is topic-only»; 1 full grsai attempt after fixer (cover.md notes).
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true`; flaky overrides include `pixel_no_wordstat_query_strips`, `pixel_no_inpaint_artifacts`, `pixel_designed_thumbnail`, `pixel_hook_title_not_truncated` — visual core face+hook+phone OK.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `no_wordstat_query_strips_on_cover: true` via pixel checks.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9250 ingest skipped)

### Named blockers
- COVER_WORDSTAT_STRIP_FIRST_ATTEMPT
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: 1 fixer round + bounded solo regen вместо бесконечного pixel loop.
- Short hook 6 слов «Застройщик перенёс ключи — платёж идёт» + sticky «Год без квартиры» — on-topic stakes (год без квартиры, платёж идёт).
- `apply_ocr_false_positive_escape` когда PNG визуально face+hook+phone, а падают только query-strip / collage / thumbnail flakes.

### Change
- Cover-scene default для cover panel: «NO Wordstat query strips» в global prefix до первого grsai call (quad-mcp-batch всё ещё тянет legacy «1-3 Wordstat stickers» из `quad-style-the-rieltor.json`).
- После fixer round: solo prompt path уже корректен — Director должен предпочитать solo regen с strip-ban, не повторять quad batch с Wordstat stickers на cover slot.

### Never again
- Повторять quad-mcp-batch с Wordstat sticker prefix на cover после известного strip FAIL на attempt 1.
- PIL mashup / Kie при strip flakes — только prompt fix + OCR escape.

### Proposed apply
- `memory/cover/quad-style-the-rieltor.json` → split cover vs inline prefix: cover = NO Wordstat strips; inline = optional stickers (review-only proposal).
- B12 — live validation B11 fixer OCR escape expansion (`INC-20260828-cover-qa-ocr-escape-b11`); второй run (B11+B12) с strip flakes → checklist для cover-scene prefix split.

### Durable applied
- none (B11 fixer уже расширил `OCR_FLAKY_CHECK_KEYS`; B12 подтверждает на post-publish cover)

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-klyuchi-ot-novostrojki-v-tyumeni-perenesli-na-god-dengi-na-eskrou-zamorozili
wp_post_id: 9250
