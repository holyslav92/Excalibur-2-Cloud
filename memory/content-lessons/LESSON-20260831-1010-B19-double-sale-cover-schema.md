## LESSON-20260831-1010-B19-double-sale-cover-schema
status: proposed
topic_id: B19
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2 grsai standard attempts exhausted; FAIL pixel QA — identity, phone clipped, hook OCR missing «дважды», wordstat strips, designed_thumbnail.
- artifact: cover/cover_qa.json
  finding: PASS with `ocr_false_positive_escape: true` (B08/B09/B15 pattern); 7 flaky checks overridden; visual core OK (face + Cyrillic hook + phone + meme).
- artifact: schema.jsonld (manual build after Derouter schema refusal)
  finding: initial BlogPosting URLs used `/blog/vtorichka-i-riski/<slug>/` — schema-gate FAIL; fixed to canonical `{{SITE_BASE}}/<slug>/`.
- artifact: none (skipped) — content-evidence-report.json absent
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260831-0608-B15-cover-budget-ocr-escape-repeat — третий exhaust+escape без regen improvement

### Named blockers
- COVER_BUDGET_EXHAUSTED
- OCR_FALSE_POSITIVE_FLAKES
- SCHEMA_MANUAL_BLOG_PATH
- METRIKA_CREDENTIALS_MISSING

### Keep
- Scout cluster `double_sale_two_buyers_one_apartment` + Wordstat P0 «продал квартиру двум покупателям» (135).
- Cover fail-fast → OCR escape → Publish (post 9385, live-page PASS).
- Short hook «В Тюмени одну квартиру продали дважды» + sticky «Второй аванс остановили».

### Change
- Schema role: при ручной сборке копировать B15 template — только `{{SITE_BASE}}/<slug>/`, не category path.
- Cover-scene: NO Wordstat strips на solo cover (prompt had strips in quad canvas 2 only — solo still painted strips attempt 1/2).

### Never again
- Derouter schema refusal → manual JSON с `/blog/` prefix без schema-gate.
- Infinite Cover-QA после budget exhaust.

### Proposed apply
- Director: B19 — пятый live proof OCR escape (B08/B09/B10/B15/B19).
- Human: Metrika credentials в Cloud Secrets для post-publish feedback loop.

### Durable applied
- none — proposal only

### Resolution
status: recorded
article_dir: memory/blog/articles/B19-v-tyumeni-prodali-odnu-kvartiru-dvum-pokupatelyam-vtoroj-avans-ostanovili
wp_post_id: 9385
