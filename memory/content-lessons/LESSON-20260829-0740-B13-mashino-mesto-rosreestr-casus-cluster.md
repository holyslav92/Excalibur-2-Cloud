## LESSON-20260829-0740-B13-mashino-mesto-rosreestr-casus-cluster
status: proposed
topic_id: B13
category: geo
confidence: low

### Evidence
- artifact: memory/scout/.cursor/excalibur-blog-handoff.md
  finding: distinct 30d cluster — обещанное машино-место/паркинг «в подарок», права не в ЕГРН / чужой собственник; `story_dup_check: PASS`; P0 Wordstat «купить машиноместо в тюмени» freq 53 (rework from weak «машиноместо егрн» 3).
- artifact: quality-bar-9.json
  finding: prose pipeline PASS — word_count 2513, comment_magnet, interlinks 4, ending agency («аванс не внесли»); only cover_qa blocked publish.
- artifact: cover/cover-text.json
  finding: hook/sticky on-topic («исчезло из реестра», «Проверили до аванса»); meme_picks disappointed_black_guy + grumpy_cat aligned with casus tone.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post unpublished — no behavioral cohort

### Named blockers
- PUBLISH_BLOCKED_COVER_QA
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (unpublished)

### Keep
- Scout triple gate: Wordstat rework слабого «машиноместо егрн» → buyer P0 «купить машиноместо в тюмени» без смены news-casus shape.
- Comment magnet: «внесли бы аванс, если машино-место обещают в подарок, но отдельной выписки ЕГРН нет?»
- Отдельная выписка ЕГРН на машино-место vs квартира — практика в H2, финал = agency not panic.

### Change
- После publish unblock: отметить cluster `mashino_mesto_podarok_egrn` в `memory/scout/used-clusters.json` (Fixer/Publish handoff).
- Cover scene: parking-ramp full-body → close-up face+phone для OCR (см. sibling lesson B13 cover).

### Never again
- Смешивать «номер на схеме» с зарегистрированным правом без отдельной выписки — core casus heat сохранять.
- Sugar ending «всё нашли место» — канон ending landing agency.

### Proposed apply
- Scout `next-cluster-guidance.md` — mashino-mesto cluster now live-validated in draft (review-only until publish).

### Durable applied
- none (unpublished; low confidence without Metrika)

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-v-tyumeni-obeschali-mashino-mesto-k-kvartire-v-rosreestre-prav-na-nego-ne-nashli
