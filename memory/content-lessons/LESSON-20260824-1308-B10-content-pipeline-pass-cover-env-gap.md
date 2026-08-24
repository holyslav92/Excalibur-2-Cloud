## LESSON-20260824-1308-B10-content-pipeline-pass-cover-env-gap
status: proposed
topic_id: B10
category: structure
confidence: low

### Evidence
- artifact: opening-meta-gate.json — PASS
- artifact: quality-bar-9.json — brand_first_person_tyumen, early_cta_tg_max_only, comment_magnet_question, interlink_siblings_2_4, word_count_2000_2600 — all true; единственный FAIL: cover_qa_pass
- artifact: research-agent-report.json — p0_phrase «купить квартиру в тюмени», p0_volume 22660; casus «фиктивная продажа без денег, наследники оспорили»
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; B10 не опубликован → post-publish behavioral data отсутствует

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (no publish → no Metrika cohort for B10)

### Keep
- Scout×Wordstat rework: buyer P0 22660 на casus-тему «мнимая сделка / наследники» — demand anchor не потерян.
- Sol longform B-mode: 2475 слов, 7 inline, 9 H2 без TL;DR opening.

### Change
- Не выводить причинность «контент готов к Дзен» из editorial gates без cover env + publish.
- После tesseract fix — перезапустить cover_qa на существующем cover.png перед publish (не обязательно regen).

### Never again
- Не считать Indexer completion = publish readiness.

### Proposed apply
- Review-only: после env fix B10 — Cover-QA retry → Publish, затем Metrika ingest для behavioral baseline.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-sdelku-zaregistrirovali-deneg-po-faktu-ne-bylo-v-tyumeni-nasledniki-osporili-pok
