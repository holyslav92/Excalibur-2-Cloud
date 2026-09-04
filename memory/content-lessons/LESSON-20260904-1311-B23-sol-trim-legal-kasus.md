## LESSON-20260904-1311-B23-sol-trim-legal-kasus
status: proposed
topic_id: B23
category: structure
confidence: medium

### Evidence
- artifact: assembled-sol-inputs.md
  finding: Writer ~2569 words; Sol brief mandates ~1800–2200, spine-once (категория/ВРИ, звонок банка, выписка ЕГРН — один раз each).
- artifact: derouter-opus-stamp-sol-trim.json
  finding: dedicated Sol TRIM pass `sol_trim_chunk` 3 parts; `word_count_before: 2303` → `word_count_after: 2195`.
- artifact: assembled-sol-trim-inputs.md
  finding: aggressive trim targets 1900–2100; remove Малиновка duplicate, inline_3 duplicate figure; preserve 6 H2, 7 inline, 4 interlinks, comment magnet.
- artifact: quality-bar-9.json
  finding: final `word_count: 2141`, `word_count_1800_2200: true`, `spine_once_no_recap: true`, 6 H2, 7 inline.
- artifact: stylo-report.json
  finding: spine_overlap 0.05 (pass delta 1.94); legal-term density elevated but within stylo pass — trim addressed length not voice rewrite.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER
- cross_run: LESSON-20260828-1310-B12-sol-tighten-writer-over-2600, LESSON-20260901-1338-B20-sol-trim-spine-once — B23 third legal-heavy KP trim (writer 2569 → final 2141)

### Named blockers
- WRITER_OVERLENGTH_LEGAL_CASUS
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Two-pass Sol: full rewrite then TRIM chunk — не третий Sol voice pass.
- Trim brief with explicit «СОХРАНИТЬ» list (H2, figures, CTAs, interlinks, comment magnet, table).
- KP land-category facts: категория/ВРИ explained once in plain language.

### Change
- Director runbook: 6-H2 legal KP casus — plan Sol TRIM when writer >2400 (B23 writer 2569 needed ~350w cut).
- Writer brief: target 2000–2150 on 6-H2 KP topics to reduce TRIM token spend.

### Never again
- Publish 6-H2 legal casus >2200 without Sol TRIM when spine-once at risk.
- Delete interlink differentiation during trim (B12/B19/B20 anchors preserved).

### Proposed apply
- `assembled-sol-trim-inputs.md` pattern validated on B12/B20/B23; human review for Sol skill template (not auto-apply).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya
wp_post_id: 9653
