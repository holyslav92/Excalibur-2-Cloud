## LESSON-20260904-0821-B22-cover-ocr-escape-identity-skin-blob
status: proposed
topic_id: B22
category: structure
confidence: medium

### Evidence
- artifact: cover/cover_qa.json
  finding: `ocr_false_positive_escape: true` (B08/B09/B15 live pattern); `identity_skin_blob_flake: true`; 5 flaky checks overridden (`pixel_designed_thumbnail`, `pixel_hook_title_not_truncated`, `pixel_identity_matches_studio`, `pixel_no_collage_inset`, `pixel_no_wordstat_query_strips`); visual core OK — face + Cyrillic hook + phone; `cover_budget_exhausted` absent; gate_status PASS.
- artifact: cover/cover_qa.json#pixel_evidence
  finding: hook «Банк поднял ставку — платёж вырос» (6 слов); mean_lum=194; host close-up face_h_frac=0.49; 1 wordstat paper-gold region; meme disaster_girl + keyboard_cat.
- artifact: quality-bar-9.json
  finding: `cover_qa_pass: true`, `cover_phone_on_cover: true`, `all_pass: true`.
- artifact: memory/pipeline-fix-queue.md#INC-20260904-0816-cover-qa-ocr-escape-first-pass-b22
  finding: first pixel QA FAIL on OCR/identity flakes; re-run with `apply_ocr_false_positive_escape` → PASS; no code change (canon already canonical).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-cover-ocr-escape-no-budget-exhaust — B20 5-й proof; B22 6-й live OCR escape без budget exhaust

### Named blockers
- OCR_FALSE_POSITIVE_FLAKES
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- `apply_ocr_false_positive_escape` при визуально OK PNG (host face + Cyrillic hook + phone) — штатный путь, не regen loop.
- Short hook 6 слов + sticky «Одобрение не гарантия» — on-topic mortgage-rate stakes.
- Cover fail-fast: max 2 grsai attempts; OCR escape → Indexer/Publish.

### Change
- none durable — canon validated; B22 adds explicit `identity_skin_blob_flake` flag to escape evidence (уже в pixel_qa path).

### Never again
- Fixer regen при escape PASS и budget not exhausted.
- PIL mashup / Kie при OCR flakes.

### Proposed apply
- Director runbook: B22 — шестой live OCR escape (B08/B09/B10/B15/B20/B22); `memory/cover/cover-canon.json` pattern stable; first-pass flake → re-QA with escape, not regen.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi
wp_post_id: 9627
