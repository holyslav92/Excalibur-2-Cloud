## LESSON-20260827-0801-B11-cover-ocr-empty-publish-blocked
status: proposed
topic_id: B11
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2/2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL — `pixel_hook_title_cyrillic` cyr_ratio=0.0 ocr='' and `pixel_phone_readable` phone_digits='' on hook «Чистая выписка не спасла аванс» + phone +7 922 001 65 05. Model also painted Wordstat-like strips / collage inset despite `cover-text.json` `wordstat_stickers` absent.
- artifact: cover/cover_qa.json
  finding: status FAIL after cover fixer regen (~6 min); OCR still empty on hook and phone — **not** B08/B09/B10 false-positive escape case (no readable Cyrillic on PNG for escape predicate). `pixel_designed_thumbnail` FAIL; `wordstat_stickers_1_3` FAIL.
- artifact: quality-bar-9.json
  finding: text gates all PASS (word_count 2197, h2 7, inline_figures 7, interlinks 4, comment_magnet, early_cta, no_tldr_opening); sole FAIL `cover_qa_pass: false` → `all_pass: false` → Publish STOPPED.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post not published; no behavioral baseline)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_EMPTY_HOOK_PHONE
- OCR_ESCAPE_NOT_APPLICABLE
- WORDSTAT_STRIPS_DESPITE_EMPTY_MANIFEST
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Indexer, не бесконечный Cover-QA loop.
- Text pipeline PASS без publish: Sol 2197 слов, description/cover-text/schema/opening gates PASS — контент готов, блокер только cover.
- Hook 6 слов в cover-text gate PASS; sticky «Проверяйте договоры» on-topic для double-sale casus.
- `apply_ocr_false_positive_escape` только когда на PNG визуально face+hook+phone (B10); при ocr='' escape не применять.

### Change
- Cover-scene prompt: явный suffix «NO Wordstat query strips / paper bars when wordstat_stickers empty» — B11 оба attempt нарушили manifest.
- Cover-text: для OCR-критичных hook — 5 слов max, каждое ≥5 букв, без «не» как отдельного короткого слова между длинными (пример fail: «Чистая выписка не спасла аванс» → propose «Выписка чистая аванс сгорел»).
- Cover fixer: при budget exhausted + ocr='' (не flakes) — не regen внутри бюджета; escalate manual review / phone-in-hand close-up prompt **до** quality-bar publish gate, не после.
- Director: при `quality-bar-9` all_pass=false только из-за cover — не ослаблять text gates; чинить cover path.

### Never again
- Stamp `ocr_false_positive_escape` когда ocr='' и phone_digits='' — это total OCR miss, не flake.
- PIL mashup / Kie / VIP tier при publish block из-за cover OCR.
- Deep-dive `cover_qa_pixels.py` после budget exhaust при designed_thumbnail FAIL.

### Proposed apply
- **B10+B11 repeat (2 runs):** checklist в cover-scene default — (1) NO query strips if manifest empty, (2) phone-in-hand close-up suffix on attempt 2, (3) hook ≤5 words OCR-safe. Review in `skills/cover-text-excalibur-blog/SKILL.md` + `memory/cover/cover-canon.json` — human decision, не auto Writer.
- Cover-QA skill note: escape predicate requires non-empty OCR baseline; B11 = negative control vs B10 escape.

### Durable applied
- none (proposals only; Writer/cover skills protected)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-kvartiru-prodali-dvazhdy-vtoroj-pokupatel-v-tyumeni-poteryal-avans
wp_post_id: none (publish stopped)
