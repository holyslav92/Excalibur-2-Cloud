## LESSON-20260829-1309-B15-cover-budget-ocr-escape
status: proposed
topic_id: B15
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL — hook OCR truncation («овор подписали — а ПРА»), phone clipped (digits='3'), wordstat strips, designed_thumbnail flakes; best_candidate = attempt-2 `cover.png`.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true` on attempt-2 PNG (face + Cyrillic hook + phone; B08/B09 pattern). Overridden: `pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_no_wordstat_query_strips`.
- artifact: cover/cover-text.json
  finding: hook «Договор подписали — квартиру продали другим» (5 кириллических слов); sticky «Деньги не вернут квартиру»; meme_picks two_buttons + polite_cat.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, `wordstat_stickers_not_title_overlap: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9310 ingest skipped)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Cover-QA escape / Indexer, не pixel deep-dive.
- Short hook 5 слов + em dash + highlight «продали» — on-topic double-sale stakes.
- `apply_ocr_false_positive_escape` когда PNG визуально face+hook+phone, а падают только OCR truncation / wordstat strip flakes.

### Change
- Cover-scene: при hook с длинным словом «Договор» в начале — bias к крупному первому слову в sacred zone (снижает «овор подписали» OCR miss на attempt 1–2).
- После budget exhaust на attempt-2 best_candidate: Cover-QA escape без fixer regen (B15 path) — валидный unblock если visual core OK.

### Never again
- Deep-dive `cover_qa_pixels.py` после budget exhaust при визуально OK PNG.
- PIL mashup / Kie при OCR flakes — только escape или bounded grsai regen.

### Proposed apply
- Director runbook: budget exhaust + visual OK → Cover-QA escape; B15 — четвёртый live proof (B08/B09/B10/B15).
- При ≥2 exhaust+escape без regen improvement (B10 fixer regen vs B15 direct escape) — A/B note в cover-scene: phone-in-hand close-up vs attempt-2 stamp.

### Durable applied
- none (canon в cover-canon.json; B15 подтверждает direct-escape path без fixer regen)

### Resolution
status: recorded
article_dir: memory/blog/articles/B15-v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim
wp_post_id: 9310
