## LESSON-20260824-0648-B10-cover-budget-exhausted-fail-fast
status: proposed
topic_id: B10
category: other
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: `cover_budget_exhausted` после 2 full attempts (standard→vip × 2); last_errors — OCR/pixel gates на grsai candidates; `best_candidate` = cover.png vip attempt 2.
- artifact: cover/cover_qa.json — status PASS, pixel_qa true, cover_md5=29955e0577b6c065fca2f05bcc1ae007
- artifact: wp-publish-result.json — publish pass, featured_image=9122, 7 inline uploads OK
- artifact: memory/cover/cover-canon.json#cover_budget — fail_fast owner lock pillar
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- COVER_BUDGET_EXHAUSTED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Owner lock **cover fail-fast**: max 2 attempts → `cover-budget-result.json` → Cover-QA stamp → Indexer → Publish (не бесконечный Cover-QA loop).
- Best candidate vip tier bytes=1013665 сохранён; publish с existing_file decode_verified.
- Short hook 5–7 слов: «Аванс внесли — сделка встала внезапно» (cover-text.json).

### Change
- Директор: при `cover_budget_exhausted` + visual OK на best_candidate — сразу Cover-QA agent stamp PASS, не тратить >15–20 мин на regen.
- Cover-text: для OCR-хрупких hookов prefer слова ≥5 букв (канон B08-style) — «внезапно» в hook совпадает с missing list в budget errors.

### Never again
- Не запускать 3+ full grsai attempts (нарушение EXCALIBUR_COVER_MAX_ATTEMPTS).
- Не PIL mashup / Kie remediation после budget exhaust.

### Proposed apply
- Director runbook: branch `cover-budget-result.status=FAIL` → Cover-QA visual PASS path (уже в cover-budget next_steps).
- Повтор на B11+ → durable checklist в director skill.

### Durable applied
- none (первый repo artifact `cover-budget-result.json`; канон уже в pipeline-canon owner_lock)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-po-povestke
wp_post_id: 9121
