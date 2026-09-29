## LESSON-20260929-1700-B34-derouter-402-astra-writer-sol
status: active
topic_id: B34
category: other
confidence: medium

### Evidence
- artifact: derouter-opus-budget-blocker.json
  finding: Sol hit Derouter HTTP 402 `budget_exceeded: 0 concurrent claude-opus-5-5 slots` (req_98c537d6e7dc42b7ba74344e); continuation stamped as manual retry on `gpt-6-astra` (powerful tier, not Composer).
- artifact: derouter-opus-stamp-writer-part{1,2,3}.json + derouter-opus-stamp-sol-part{1,2,3}.json + derouter-opus-stamp-sol.json
  finding: Writer and Sol chunks completed on `gpt-6-astra`; utility roles (research, title, description, cover-text, schema) on terra tier unchanged.
- artifact: article-quality-score.json + quality-bar-9.json + stylo-report.json
  finding: quality score PASS (1516 words, spine_overlap 0.07); quality-bar-9 all checks PASS; stylo PASS (delta 2.59, no stylo-driven Sol rewrite).
- artifact: wp-publish-result.json
  finding: publish PASS post **11284**, slot 2026-09-29 17:00 YEKT vtorichka, live-page PASS, 7 inline.
- artifact: research-notes.md#cluster_id
  finding: `registered_lease_rosreestr_blocks_secondary_before_advance` — distinct vtorichka casus (ЕГРН-найм 3 года vs устное «съедет к ключам»).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no behavioral baseline for post 11284)

### Named blockers
- DEROUTER_HTTP_402_BUDGET_EXCEEDED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish)

### Keep
- Writer/Sol longform via 3-part chunk on powerful tier; merge → article.html without Composer prose.
- При исчерпании opus-слотов — **astra на powerful tier**, не utility terra и не Cursor fallback.
- Gates после astra-path: stylo + quality-bar + publish без дополнительного opus retry в том же слоте.

### Change
- Директор: не ставить ручной `DEROUTER_POWERFUL_MODEL=gpt-6-astra` — скрипт должен auto-retry 402 (см. durable apply).
- После credentials fix: Metrika cohort `cluster:registered_lease_rosreestr_blocks_secondary_before_advance` vs B09/B10/B14 sibling interlinks.

### Never again
- Composer или terra для Writer/Sol при 402 на opus.
- Повторный Sol на opus в том же run после budget_exceeded без слота fixer/owner.

### Proposed apply
- Подтвердить в director runbook: 402 на powerful → ожидать `derouter-opus-budget-fallback.json` (auto) или legacy `derouter-opus-budget-blocker.json` (manual B34).
- Scout cluster ledger: `registered_lease_rosreestr_blocks_secondary_before_advance` locked 2026-09-29 (B34).

### Durable applied
- `scripts/excalibur_blog_derouter_opus_chat.py` — auto-retry powerful tier HTTP 402 `budget_exceeded` → `fallback_model` (`gpt-6-astra`); stamp `derouter-opus-budget-fallback.json` on success (fixer INC-20260929-1400-sol-writer-derouter-402-budget-b34, commit e12154e0).
- Rollback: revert 402 auto-retry block in `excalibur_blog_derouter_opus_chat.py` and contract note in `shared/derouter-opus-brain-contract.md`.

### Resolution
status: recorded
article_dir: memory/blog/articles/B34-v-tyumeni-zaregistrirovannaya-arenda-na-tri-goda-ostanovila-pokupku-vtorichki-za
wp_post_id: 11284
