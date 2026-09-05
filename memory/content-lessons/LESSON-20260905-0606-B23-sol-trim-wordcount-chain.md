## LESSON-20260905-0606-B23-sol-trim-wordcount-chain
status: proposed
topic_id: B23
category: structure
confidence: medium

### Evidence
- artifact: derouter-opus-stamp-writer-trim.json
  finding: writer_trim_chunk 2852 → 2592 words (−260).
- artifact: derouter-opus-stamp-sol-trim.json
  finding: sol_trim_chunk 2296 → 2237 words (−59); sol-fix-notes: end_cta_full_channels, dual_cta_soft, target 1800–2200 без смены H2/7 inline/interlinks.
- artifact: quality-bar-9.json
  finding: final `word_count: 2183`, `word_count_1800_2200: true`, `spine_once_no_recap: true`, `comment_magnet_question: true`, 6 H2, 7 inline, 3 sibling interlinks.
- artifact: stylo-report.json
  finding: `stylo_pass: true`, delta 2.8166 < 2.85; no Sol rewrite for voice.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-sol-tighten-writer-over-2600, LESSON-20260901-1338-B20-sol-trim-spine-once — третий run с writer+sol trim chain до quality-bar PASS

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Sol TRIM после Sol для 6-H2 newbuild casus: CTA/end channels + word_count без structural regression.
- Stylo PASS на первом проходе — не запускать stylo-driven Sol при delta < threshold.
- Brief «не трогать» 6 H2, 7 figures, interlinks, comment magnet — trim только повторы.

### Change
- Director runbook: при writer draft >2600 на trade-in/legal casus — планировать writer_trim + sol_trim до quality-bar (не ждать FAIL).
- Writer target 2000–2150 на 6-H2 (снижает двойной trim token spend: B23 потерял ~320 слов суммарно).

### Never again
- Публиковать без end_cta_full_channels (site home link в excalibur-cta-end).
- Удалять dual_cta_soft («консультация» + «до аванса») при trim.

### Proposed apply
- `assembled-sol-trim-inputs.md` + sol-fix-notes pattern validated on B23; human review для Sol skill template (не auto-apply в writer-master-prompt).

### Durable applied
- none — третий cross-run; needs-human для director runbook template

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela
wp_post_id: 9697
