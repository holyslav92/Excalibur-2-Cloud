## LESSON-20260902-0854-B21-stylo-sol-rhythm-legal-kp
status: proposed
topic_id: B21
category: voice
confidence: medium

### Evidence
- artifact: memory/stylo/history.jsonl
  finding: stylo pass 1 FAIL (`delta: 3.48`, threshold 2.85, `stylo_pass: false`); pass 2 PASS (`delta: 2.57`, `sol_rewrite: true`).
- artifact: stylo-report.json + drafts/stylo-sol-input.md
  finding: first Sol drift — `lead_word_count` 64 vs gold 29.5 (z=+3.78), `sent_len_mean` 19.6, `legal_per_1k` 54.2, `spine_overlap` 0.082; stylo-driven Sol brief: shorten lead to ~40–50 words (4–6 sentences), shorter sentences (~12–14), merge short `<p>`, cut «к»/«и», plain-language legal terms; final `lead_word_count` 18, `word_count` 1994, quality-bar PASS.
- artifact: quality-bar-9.json
  finding: `spine_once_no_recap: true`, `word_count_1800_2200: true`, 6 H2, 7 inline, comment magnet preserved after one Sol rewrite.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-sol-tighten-writer-over-2600 (volume trim); LESSON-20260901-1338-B20-sol-trim-spine-once (post-Sol TRIM) — B21 first **stylo FAIL → stylo-driven Sol rhythm** on legal KP casus without word-count cap breach

### Named blockers
- STYLO_DELTA_FAIL_FIRST_SOL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Stylo gate before Description: один stylo-driven Sol pass при delta>2.85 — не полный рерайт, факты/H2/inline/CTA/interlinks frozen.
- Brief в `drafts/stylo-sol-input.md` с numeric z-scores и explicit lead cap (~40–50 слов) — Sol сжал лид без потери 4–6 предложений engagement lock.

### Change
- Director: на legal-heavy KP/ДДУ casus планировать stylo check сразу после первого Sol (не ждать quality-bar); типичный drift — длинный лид + юртермины + рваный sent_len.
- Writer/Sol assembled brief: target lead ~35–45 слов на 4–6 предложений для 6-H2 legal casus (снижает stylo rewrite token spend).

### Never again
- Второй stylo-driven Sol pass (канон ≤1).
- Автоматически менять Writer master-prompt — proposals только в content-lessons.

### Proposed apply
- Human review: добавить «stylo rhythm check» в Director runbook после Sol на legal KP topics; template `drafts/stylo-sol-input.md` validated on B21.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli
wp_post_id: 9523
