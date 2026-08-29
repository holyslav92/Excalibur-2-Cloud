## LESSON-20260829-0740-B13-cover-budget-no-fixer-wordstat-strips
status: proposed
topic_id: B13
category: structure
confidence: high

### Evidence
- artifact: cover/cover-budget-result.json
  finding: 2/2 grsai standard attempts exhausted (`cover_budget_exhausted`); both FAIL — attempt 1 had 1 Wordstat strip + collage inset; attempt 2 had 2 Wordstat strips + opaque gold bar + hook OCR garbage + phone clipped + meme absent.
- artifact: cover/cover_qa.json
  finding: `gate_status: FAIL`; hard fails include `pixel_no_wordstat_query_strips`, `pixel_wordstat_not_opaque_bars`, `pixel_hook_title_not_truncated`, `pixel_phone_readable`, `pixel_meme_present`, `pixel_no_collage_inset`, `pixel_designed_thumbnail`. No fixer round, no OCR escape stamp.
- artifact: cover/grsai-solo-batch.json
  finding: solo prompt already carried «NO Wordstat query strips on cover» + BAN HARD — grsai still painted 2 strips on attempt 2 (model non-compliance despite runtime strip-ban in `cover_quad_prompt.py`).
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: false` — publish correctly blocked; prose gates PASS (word_count 2513, comment_magnet, interlinks 4).
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post not published; ingest skipped)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- COVER_WORDSTAT_STRIP_PERSIST
- COVER_FIXER_SKIPPED
- PUBLISH_BLOCKED_COVER_QA
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Cover fail-fast: max 2 grsai attempts → `cover-budget-result.json` → Indexer (llms) without infinite Cover-QA loop.
- Publish gate: `cover_qa_pass` false blocks WP — correct for B13.
- Short hook 6 слов «Обещанное место исчезло из реестра» + sticky «Проверили до аванса» — on-topic mashino-mesto stakes до аванса.
- Solo prompt strip-ban + BAN HARD already in `cover_quad_prompt.py` — keep runtime replace of legacy «1-3 Wordstat stickers» prefix.

### Change
- После budget exhaust при `pixel_no_wordstat_query_strips` / layout FAIL: **1 cover_fixer round** (как B12) **до** Indexer на publish-intent run — B13 пропустил fixer → publish blocked.
- Director: не трактовать fail-fast Indexer как «cover OK» — quality-bar всё равно требует `cover_qa_pass` или manual escape.
- При strip FAIL после strip-ban prompt: prefer fixer regen (panel/solo) с phone-in-hand close-up, не повторять full-body parking scene (attempt 2 host crop mismatch → hook/phone/meme flakes).

### Never again
- Indexer complete + publish intent без cover_fixer, когда оба grsai attempts FAIL на wordstat strips (B12 fixer path уже canonical).
- PIL mashup / Kie при strip FAIL — только prompt fix + fixer regen + OCR escape.
- Deep-dive `cover_qa_pixels.py` после budget exhaust.

### Proposed apply
- `memory/cover/quad-style-the-rieltor.json` → cover global prefix без Wordstat stickers (durable applied — 2-й run B12+B13).
- `memory/cover/cover-canon.json` → `cover_budget.after_exhaust` note: fixer round before Indexer when strip/layout FAIL (review-only until fixer closes INC).

### Durable applied
- `memory/cover/quad-style-the-rieltor.json` — `global_prompt_prefix`: «1-3 Wordstat stickers» → «NO Wordstat query strips on cover — Scout Wordstat is topic-only» (rollback: restore legacy prefix line 20).
- `memory/cover/cover-canon.json` — `cover_budget.after_exhaust_fixer`: «1 cover_fixer round when pixel_no_wordstat_query_strips or layout FAIL before Indexer on publish intent» (rollback: remove key).

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-v-tyumeni-obeschali-mashino-mesto-k-kvartire-v-rosreestre-prav-na-nego-ne-nashli
publish_status: blocked (cover_qa_pass false)
