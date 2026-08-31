## LESSON-20260831-0608-B15-cover-budget-ocr-escape-repeat
status: proposed
topic_id: B15
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL pixel QA — hook OCR truncation («Проверка согласия супруги остановила аванс»), phone OCR `0`, wordstat strips, designed_thumbnail, identity skin_blob, meme orange_fur flakes.
- artifact: cover/cover_qa.json
  finding: visual PASS with `ocr_false_positive_escape: true` (B08/B09 pattern); `cover_budget_exhausted: true`; fixer skipped regen (`budget 2/2`); 9 flaky checks overridden; gate_status PASS.
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `cover_qa_pass: true`, `cover_phone_on_cover: true`, word_count 1968, inline_figures 7.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9368 недоступен)
- cross_run: LESSON-20260826-0834-B10-cover-budget-ocr-escape — второй content-learner run с exhaust+escape без regen improvement (B08/B09 live + B10 named + B15 repeat)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai → `cover-budget-result.json` → Cover-QA OCR escape → Indexer/Publish; не deep-dive pixel loop.
- Short hook 6 слов «Проверка согласия супруги остановила аванс» + sticky «Конверт не доказательство» — on-topic envelope stakes до аванса.
- `apply_ocr_false_positive_escape` при визуально OK PNG (face + Cyrillic hook + phone + polite_cat meme).

### Change
- **needs-human (2nd repeat):** cover-scene default checklist — phone-in-hand close-up LEFT при envelope/document props; снижает attempt-1/2 designed_thumbnail + hook OCR empty (предложено в B10 lesson, подтверждено B15 без regen improvement).
- Cover-text: highlight на «остановила» / финальном слове hook совпадает с gold-band OCR false positive — держать в cover-text gate notes.

### Never again
- Fixer regen после budget exhaust при визуально OK PNG (B15: fixer_skipped no-regen — корректно).
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook: B15 — четвёртый live proof OCR escape path (B08/B09/B10/B15); canon в `memory/cover/cover-canon.json` validated на repeat.
- Human review: добавить `phone_in_hand_close_up_left` в cover-scene default props / assembled-cover-scene checklist (не автоматически в skills).

### Durable applied
- none — proposal `needs-human`; rollback N/A until applied

### Resolution
status: recorded
article_dir: memory/blog/articles/B15-v-tyumeni-poddelnoe-soglasie-suprugi-ostanovilo-sdelku-pered-avansom
wp_post_id: 9368
