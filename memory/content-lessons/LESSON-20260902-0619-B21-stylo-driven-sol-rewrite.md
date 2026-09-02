## LESSON-20260902-0619-B21-stylo-driven-sol-rewrite
status: proposed
topic_id: B21
category: voice
confidence: medium

### Evidence
- artifact: stylo-report.json
  finding: initial Sol FAIL stylo delta **2.921** (threshold 2.85); после одного stylo-driven Sol rewrite PASS delta **2.1805**; `sol_rewrite_applied: true`.
- artifact: memory/stylo/history.jsonl
  finding: run1 `lead_word_count: 60`, `spine_overlap: 0.083`, `stylo_pass: false`; run2 после rewrite `lead_word_count: 26`, `spine_overlap: 0.049`, `stylo_pass: true`; `legal_per_1k` остаётся высоким (68–71) но в пределах PASS.
- artifact: stylo-notes.md
  finding: правки только ритм/голос — короче абзацы, меньше spine overlap лид↔финал, больше тире/«ёлочек»; факты и newbuild-фокус не трогать.
- artifact: quality-bar-9.json
  finding: final `word_count: 2117` (1800–2200 band), `spine_once_no_recap: true`, `dzen_reading_minutes_est: 11`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260901-1338-B20-sol-trim-spine-once — B20 post-Sol TRIM для length; B21 stylo-driven Sol для voice без отдельного TRIM pass

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- ≤1 stylo-driven Sol pass на legal-heavy newbuild casus: сжать лид (60→26 слов), снизить spine_overlap, не трогать H2/факты/interlinks.
- Stylo notes как numeric brief (z-scores) — не переписывать Writer draft.

### Change
- Writer/Sol brief для assignment/legal casus: target lead 4–6 предложений (~25–35 слов) на первом Sol, чтобы снизить вероятность stylo FAIL на длинном лиде.
- Director: если stylo FAIL на legal casus — stylo-notes Sol **до** Description/Cover (не после cover budget).

### Never again
- Второй stylo-driven Sol pass (канон ≤1).
- Stylo rewrite, меняющий plot firewall (B12/B19/B20 differentiation) или факты из research.

### Proposed apply
- Stylo history pattern B21 documented; human review для Writer brief lead word-count guard (не auto-apply to writer-master-prompt).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-/
wp_post_id: 9510
