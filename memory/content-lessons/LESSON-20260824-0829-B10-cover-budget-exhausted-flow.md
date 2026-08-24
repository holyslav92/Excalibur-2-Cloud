## LESSON-20260824-0829-B10-cover-budget-exhausted-flow
status: proposed
topic_id: B10
category: other
confidence: high

### Evidence
- artifact: cover/cover-budget-result.json
  finding: `reason: cover_budget_exhausted`, `max_attempts: 1`, standard→vip per attempt, `best_candidate` written to cover.png, `last_errors` preserved, `next_steps` explicitly say proceed Indexer / manual PASS — no infinite Cover-QA loop.
- artifact: cover/cover_qa.json
  finding: FAIL stamped with full pixel_errors list; pipeline did not silently PASS.
- artifact: quality-bar-9.json
  finding: editorial gates PASS (2557 words, 7 inline, 4 interlinks, comment_magnet) except `cover_qa_pass: false` — correct separation editorial vs cover tooling.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- PUBLISH_BLOCKED_COVER_QA
- COVER_BUDGET_EXHAUSTED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Fail-fast cover budget (owner lock pillar 3): 1 full attempt × (standard+vip) → budget result JSON → Indexer allowed.
- `next_steps` in cover-budget-result.json: no PIL mashup/Kie, no deep-dive pixel source as hobby.
- Indexer completed per run handoff; Publish correctly BLOCKED on cover_qa — publish gate integrity.

### Change
- After budget exhausted: director runbook should offer manual cover_qa PASS path when visual OK but OCR/pixel false positives (see LESSON-20260824-0829-B10-grsai-ocr-empty-false-fail).
- Log `cover_budget_exhausted` in content-lessons index for cross-run tracking (repeat pattern → durable OCR escape).

### Never again
- Не превышать EXCALIBUR_COVER_MAX_ATTEMPTS после budget JSON written.
- Не bypass publish cover_qa gate автоматически после budget exhaust — manual stamp or fixer patch only.

### Proposed apply
- none (flow already matches pipeline_canon; validate on next B11+ run)

### Durable applied
- none (behavior validated B10; no code change required for budget flow itself)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-notarius-udostoveril-sdelku-a-cherez-god-sud-otmenil-prodazhu-prodavca
indexer_status: done
publish_status: BLOCKED (cover_qa)
