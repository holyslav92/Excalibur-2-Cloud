## LESSON-20260901-1338-B20-sol-trim-spine-once
status: proposed
topic_id: B20
category: structure
confidence: medium

### Evidence
- artifact: assembled-sol-trim-inputs.md
  finding: dedicated Sol TRIM pass после Sol; brief: сжать ~80–150 слов, убрать spine-once повторы (ст.58 ГК, эскроу/аккредитация в соседних H2); вход ~2259–2307 слов → цель 2000–2150.
- artifact: quality-bar-9.json
  finding: final `word_count: 2126`, `word_count_1800_2200: true`, `spine_once_no_recap: true`, 6 H2, 7 inline, comment magnet preserved.
- artifact: article.html
  finding: explicit B12/B19 interlink differentiation («деньги на эскроу не внесены» vs frozen escrow / family mortgage) — spine-once guard в финале.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-sol-tighten-writer-over-2600 — B12 full Sol trim ~346w; B20 lighter post-Sol TRIM ~130w

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Sol TRIM как отдельный проход для legal-heavy newbuild casus: не переписывать с нуля, сохранить H2/inline/CTA/comment magnet/interlinks дословно.
- Brief с явным списком «не трогать» (6 H2, 7 figure, 4 interlink href) — trim без structural regression.

### Change
- Director: при writer+sol >2200 на 6-H2 legal casus — планировать Sol TRIM pass в runbook (не ждать quality-bar FAIL).
- Writer brief: target 2000–2150 на 6-H2 + table novostroyka topics (снижает Sol TRIM token spend).

### Never again
- Удалять sibling interlink differentiation при trim (B12/B19 anchors — часть plot firewall).
- Публиковать без Sol TRIM если word_count >2200 и spine_once gate at risk.

### Proposed apply
- `assembled-sol-trim-inputs.md` pattern validated on B20; human review для template в Sol skill (не auto-apply).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B20-v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot
wp_post_id: 9490
