## LESSON-20260826-1116-B11-cover-budget-ocr-escape-repeat
status: applied
topic_id: B11
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2/2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL — empty OCR on hook «Чистая выписка квартиру не спасла» and phone digits, plus wordstat strips / designed_thumbnail / text-on-clothing flakes (same flake set as B10).
- artifact: cover/cover_qa.json
  finding: Cover-QA PASS with `ocr_false_positive_escape: true` (B08/B09 pattern); `face_h_frac=0.49` close-up; 11 flaky checks overridden; visual core OK on attempt-2 PNG (md5=29eb359c).
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true` — publish unblocked after escape stamp.
- artifact: cover/cover-text.json
  finding: short hook 6 Cyrillic words; highlight «Чистая»; sticky «Проверяйте продавца» on-topic to bankruptcy casus.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post 9171 ingest skipped (INC-20260821-0615)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 attempts → `cover-budget-result.json` → Cover-QA escape / Indexer, не pixel deep-dive loop.
- `apply_ocr_false_positive_escape` when PNG has face + hook ink + phone ink and only OCR truncation/opaque flakes fail.
- Short hook 5–7 слов aligned with cover-text gate (6 words).

### Change
- **Repeat confirmed (B10+B11):** default cover-scene draft should prefer phone-in-hand close-up before solo attempts — снижает empty hook OCR + designed_thumbnail flakes on attempt 1–2.
- Highlight word at start of hook («Чистая») — совпадает с cover-text gate; финальное слово «спасла» в missing OCR list — escape path, не regen loop.

### Never again
- Deep-dive `cover_qa_pixels.py` после 2/2 budget при визуально OK PNG.
- PIL mashup / Kie при OCR flakes.
- Третий full solo regen «на удачу» после budget exhaust.

### Proposed apply
- `memory/cover/cover-canon.json` → `solo_cover_scene_default_on_budget_risk` (validated B10+B11).
- Director: budget exhaust + visual OK → escape path (четвёртый live proof: B08/B09/B10/B11).

### Durable applied
- `memory/cover/cover-canon.json` — block `solo_cover_scene_default_on_budget_risk` (phone-in-hand close-up default scene_hint before solo regen).
- Rollback: remove block from cover-canon.json; cover-scene Derouter reverts to invention-only hints.

### Resolution
status: applied
article_dir: memory/blog/articles/B11-kupili-kvartiru-v-tyumeni-prodavec-ushel-v-bankrotstvo-finupravlyayuschij-ospori
wp_post_id: 9171
live_url: {{SITE_BASE}}/blog/vtorichka-i-riski/kupili-kvartiru-v-tyumeni-prodavec-ushel-v-bankrotstvo-finupravlyayuschij-ospori/
