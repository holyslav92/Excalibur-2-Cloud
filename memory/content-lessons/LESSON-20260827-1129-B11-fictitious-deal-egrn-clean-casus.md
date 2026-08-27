## LESSON-20260827-1129-B11-fictitious-deal-egrn-clean-casus
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2591, h2 8, inline_figures 7, sibling_interlinks 4; gates `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: title-brief.json
  finding: angle — суд отменил право через два года из‑за фиктивной прошлой сделки между родственниками при «чистой» ЕГРН; `comment_magnet_angle` — резать аванс vs верить выписке.
- artifact: description-brief.json
  finding: Klyshin case hook rhythm, geo Тюмень, `not_equal_title: true` — карточка про цепочку родственников без оплаты, не дублирует H1.
- artifact: research-agent-report.json
  finding: fresh_signal PASS — Klyshin схема №3 «квартира без денег» (16.08.2026) + PRIME/РИА 27.08.2026 (Русяев, ст. 170 ГК); Wordstat P0 «купить квартиру в тюмени» 17699.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B07 (наследство), B09 (ЕГРН/ипотека), B10 (родственники/телефон) — risk-cluster siblings; inbound applied B06, B04, B09 (post_id 8984, 8823, 9063).
- artifact: cover/cover-text.json
  finding: hook «Чистая выписка — квартиру забрал суд» (6 слов + em dash), sticky «Выписка не видит оплату» — зеркалит casus finale и comment-magnet.
- artifact: cover/cover-budget-result.json + cover/cover_qa.json
  finding: 2/2 grsai attempts exhausted (hook OCR flakes, wordstat strips); Cover-QA PASS via `ocr_false_positive_escape` (B08/B09/B10 pattern, 4-й live proof).
- artifact: wp-publish-result.json
  finding: post 9201 published, 7 inline uploads, live-page PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9201

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, нет behavioral ingest)
- COVER_BUDGET_EXHAUSTED (unblocked OCR escape — не pipeline blocker)

### Keep
- News-casus shape: покупатель с «чистой» выпиской → финал «суд забрал через два года» из‑за фиктивной родственной сделки без денег — stakes без how-to checklist.
- Comment magnet «режете аванс или верите ЕГРН» — прямой Дзен-угол из title-brief, quality-bar PASS.
- Risk-cluster interlink (B02/B07/B09/B10) для vtorichka-i-riski + dokumenty-i-oformlenie — контекстные sibling, не SEO-хвосты.
- Cover sticky «Выписка не видит оплату» + hook с em dash — on-topic stakes; OCR escape после budget exhaust (см. LESSON-20260826-0834-B10-cover-budget-ocr-escape).

### Change
- Scout/handoff: tag `fictitious_relative_chain` в klyshin bank — B11 = схема №3 five_court_schemes; sibling defaults → B02/B07/B09/B10.
- Description: сохранять разрыв title/card (PASS) — H1 «суд забрал» vs card «договор между родственниками — деньги не передавались».
- Sol: 3-part chunk (~54k tokens total) — мониторить latency; не возвращать к single-shot если quality-bar PASS.

### Never again
- Писать «выписка чистая = безопасно» без casus-финала про цепочку родственников и отсутствие оплаты.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).
- Deep-dive Cover-QA pixels после budget exhaust при visual OK PNG.

### Proposed apply
- Scout klyshin bank: tag `fictitious_relative_chain` + `comment_magnet_angle` template «ЕГРН чистая vs аванс» для Tyumen buyer P0.
- После Metrika ingest для 9201 — re-evaluate confidence medium/high если retention/CTA сигналы совпадают с risk-cluster cohort (B02/B07/B09/B10).

### Durable applied
- none (один run, evidence SKIP, Metrika BLOCKER; cover OCR escape уже в cover-canon)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-rodstvenniki-osporili-prodazhu-v-proshloj-sdelke-deneg-ne-bylo
wp_post_id: 9201
