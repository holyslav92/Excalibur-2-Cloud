## LESSON-20260829-1254-B13-cover-budget-core-pixel-fail
status: proposed
topic_id: B13
category: structure
confidence: medium

### Evidence
- artifact: cover/cover-budget-result.json
  finding: `cover_budget_exhausted` after 2 grsai standard attempts; both FAIL — `pixel_hook_title_present`, `pixel_phone_readable`, `pixel_no_wordstat_query_strips`, `pixel_layout_not_collapsed`, `pixel_designed_thumbnail`; attempt 2 OCR gibberish (`бтлнприп`), attempt 1 partial hook only (`Маткапитал остановил`).
- artifact: cover/cover_qa.json
  finding: `gate_status: FAIL`; no `ocr_false_positive_escape` — CORE keys false on both attempts (unlike B10/B12 escape path).
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: false`; editorial checks otherwise PASS (word_count 2003, comment_magnet, interlinks 4).
- artifact: cover/cover-text.json
  finding: hook «Маткапитал остановил сделку до задатка» (6 words) + phone_cta present in brief but not rendered on PNG.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (B13 pre-publish; no post id)

### Named blockers
- COVER_BUDGET_EXHAUSTED
- COVER_CORE_PIXEL_FAIL_NO_ESCAPE
- COVER_WORDSTAT_STRIP_REPEAT
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Owner lock: max 2 attempts → `cover-budget-result.json` → Indexer (no Cover-QA infinite loop).
- Short hook 6 слов + sticky «Хорошо, что проверили» — on-topic matkapital-before-deposit stakes.
- Fail-fast left B13 at budget FAIL per INC-20260829-1252; no PIL mashup / Kie.

### Change
- Attempt 2+ must vary prompt when attempt 1 misses hook/phone/layout/wordstat-strip — fixer applied `TEXT_LAYOUT_RETRY_SUFFIX` in `excalibur_blog_grsai_solo_cover.py` (B13 attempt 2 had reused identical prompt before fix).
- Third live Wordstat strip on cover slot (B10 flakes+escape, B12 escape, B13 core fail) → enforce NO Wordstat strips in cover-scene prefix before first grsai call (extends B12 proposal on `quad-style-the-rieltor.json` split).
- When CORE hook+phone false on both attempts: OCR escape inapplicable — Director proceeds Indexer; do not regen beyond budget.

### Never again
- Expect `apply_ocr_false_positive_escape` when `pixel_hook_title_present` and `pixel_phone_readable` are false on exhausted budget PNG.
- Deep-dive pixel QA after budget exhaust when layout collapsed face-only crop.
- Identical solo prompt on attempt 2 after text-layout miss.

### Proposed apply
- Validate `TEXT_LAYOUT_RETRY_SUFFIX` on next cover run with hook/phone miss on attempt 1.
- After B13+B12 strip evidence: checklist «cover panel prefix = NO Wordstat strips» before quad/solo batch (human review of `memory/cover/quad-style-the-rieltor.json`).

### Durable applied
- `scripts/excalibur_blog_grsai_solo_cover.py` — `TEXT_LAYOUT_RETRY_SUFFIX` + `needs_text_layout_retry()` on attempt 2+ (INC-20260829-1252, commit 350c6b3). Rollback: remove suffix block in solo cover loop.

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-matkapital-potratili-a-detyam-doli-ne-vydelili-v-tyumeni-sdelku-razvernuli-do-de
wp_post_id: none (cover budget FAIL; Indexer path)
