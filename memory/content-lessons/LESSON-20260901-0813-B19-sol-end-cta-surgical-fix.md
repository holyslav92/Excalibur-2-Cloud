## LESSON-20260901-0813-B19-sol-end-cta-surgical-fix
status: proposed
topic_id: B19
category: cta
confidence: low

### Evidence
- artifact: quality-bar-9.json (first pass implied by INC-20260901-0812)
  finding: Sol first pass missing `end_cta_full_channels` + `dual_cta_soft`; surgical HTML fix → final PASS (word_count 2125, dual_cta_soft true, end_cta_full_channels true).
- artifact: article.meta.json / wp-publish-result.json
  finding: publish PASS post 9452; categories ipoteka + matkapital-i-sdelki.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- SOL_END_CTA_DRIFT
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- Early TG+MAX only in lead; mid nudge; full end channel ul after story landing — canonical quality-bar-9.
- Surgical Sol fix (not Writer rewrite) when only CTA block missing; trim duplicate recap to stay ≤2200 words.

### Change
- Sol pass checklist: verify `excalibur-cta-end` full channel ul (Дзен/VK/site/gajdy/rieltor-tyumen) + consult+deal phrases **before** quality-bar stamp — one-off drift, no prompt change.

### Never again
- Publish with quality-bar FAIL on end_cta/dual_cta.
- Full Sol regen when only end CTA ul missing.

### Proposed apply
- Director pre-publish: run `quality-bar-9` after Sol; if end_cta fail → surgical HTML patch in article.html only.
- No automatic change to Sol skill or writer-master-prompt (protected).

### Durable applied
- none — article HTML fix only (INC-20260901-0812 fixed, no repo code change)

### Resolution
status: recorded
article_dir: memory/blog/articles/B19-semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli
wp_post_id: 9452
