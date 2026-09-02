## LESSON-20260902-1340-B21-cover-ocr-escape-no-budget-exhaust
status: proposed
topic_id: B21
category: structure
confidence: medium

### Evidence
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15/B20 pattern); `cover_budget_exhausted` absent; 7 flaky checks overridden (designed_thumbnail, hook_title_not_truncated, collage_inset, wordstat_query_strips, wordstat_not_edge_truncated, wordstat_not_opaque_bars, wordstat_phrases_not_truncated); visual core OK — face + Cyrillic hook + phone; gate_status PASS.
- artifact: .cursor/excalibur-blog-fragments/cover.md
  finding: `budget_exhausted: false`, `solo_cover_attempts: 2` — cover passed within grsai budget (не B15 exhaust path).
- artifact: cover/cover-text.json + grsai-solo-batch.json
  finding: short hook 6 слов «Кладовка по ДДУ исчезла на ключах»; sticky «Акт подписывать страшно»; meme james_doakes + pop_cat; NO Wordstat strips on cover.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, word_count 1812.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust — B20 escape без budget exhaust; B21 — шестой live proof OCR path (B08/B09/B10/B15/B20/B21)

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `apply_ocr_false_positive_escape` при визуально OK PNG без budget exhaust — штатный путь после 2 grsai attempts, не regen loop.
- Short hook 6 слов on cellar/DDU stakes + meme people+cats (meme_canon_v1); underground storage scene on-topic.
- Cover fail-fast: attempt 2 PASS → Cover-QA escape → Indexer/Publish; no cover-budget-result.json needed.

### Change
- none durable — canon validated; wordstat OCR flakes on gold bands persist (7 overrides vs B20's 4) — monitor, not auto-regen.

### Never again
- Fixer regen при escape PASS и budget not exhausted.
- PIL mashup / Kie при OCR flakes.
- Wordstat query strips on cover (manifest log only).

### Proposed apply
- Director runbook: B21 — шестой live OCR escape (B08/B09/B10/B15/B20/B21); `memory/cover/cover-canon.json` pattern stable.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo
wp_post_id: 9549
