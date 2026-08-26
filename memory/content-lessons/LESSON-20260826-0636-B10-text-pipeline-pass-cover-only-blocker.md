## LESSON-20260826-0636-B10-text-pipeline-pass-cover-only-blocker
status: proposed
topic_id: B10
category: structure
confidence: medium

### Evidence
- artifact: quality-bar-9.json#checks
  finding: 15/16 checks PASS — brand_first_person_tyumen, phone_in_body, CTAs (early/mid/end), interlink_siblings_2_4, word_count_2000_2600, h2_count_7_plus, inline_figures_7, comment_magnet_question, no_tldr_opening; sole FAIL `cover_qa_pass`.
- artifact: opening-meta-gate.json
  finding: PASS — прозаический лид, comment magnet, dzen casus shape.
- artifact: description-brief.json (present post-Sol)
  finding: Description stage PASS per run handoff.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — credentials missing; нельзя оценить post-publish engagement для B10 (не опубликован)

### Named blockers
- PUBLISH_STOP_COVER
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (unpublished — нет behavioral data)

### Keep
- Разделение Writer (смысл) / Sol (слог) — текст готов к publish без prose rewrite.
- quality-bar-9 как единый pre-publish checklist: cover_qa корректно блокирует при visual FAIL.

### Change
- Content-learner handoff: при text PASS + cover FAIL — lessons в cover category, не трогать article.html / Writer.
- Директор: не откатывать Sol/Writer; маршрут → Cover fixer / owner review / optional Indexer с budget stamp.

### Never again
- Переписывать article.html из-за cover pixel fails.
- Считать text pipeline «неготовым» только потому что quality-bar-9 all_pass=false — проверять какой check упал.

### Proposed apply
- Runbook director: `cover_qa FAIL` → INC cover fixer, не Writer/Sol return.
- После publish B10 (когда cover resolved) — повторить Metrika ingest для cohort.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-kupili-kvartiru-v-tyumeni-cherez-god-finupravlyayuschij-osporil-sdelku
