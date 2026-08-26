## LESSON-20260826-1306-B11-matkapital-egrn-false-comfort-cluster
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2504, h2 8, inline_figures 7, sibling_interlinks 4; `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: research-agent-report.json
  finding: angle «детские доли в квартире» vol 35 (Tyumen 55+11176); rework from «маткапитал при покупке квартиры» (19); overlap_check отделяет plot «опека молчала → дети оспорили через 3 года» от live cluster «доли не видели в выписке».
- artifact: description-brief.json
  finding: Klyshin case hook — «чистый ЕГРН успокоил» vs финал «через три года дети забрали»; `not_equal_title: true`, geo Тюмень.
- artifact: cover/cover-text.json
  finding: hook 6 слов «Маткапитал: сделку отменили через три года»; sticky «Чистая выписка не спасла» зеркалит comment_magnet «верите словам „уже всё оформили“?».
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B07 (наследство/сын), B08 (брак/неофициальный), B09 (ипотека/ЕГРН) — matkapital+title-risk cluster; inbound planned B06, B04, B09.
- artifact: wp-publish-result.json
  finding: post 9181 published; categories 31,48 (`vtorichka-i-riski`, `matkapital-i-sdelki`); 7 inline uploads; live-page PASS.
- artifact: link-verify.json
  finding: 11 links, verdict pass, 0 failed.
- artifact: derouter-opus-stamp-sol-part1.json (+ part2/3)
  finding: Sol single-shot claude-opus-5, ~17.7k tokens part1 alone — без 524 chunk fallback.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post 9181 behavioral baseline недоступен

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus: маткапитал + молчание опеки + отмена через годы — stakes «чистая выписка» vs реальный риск, не how-to checklist.
- Comment magnet «останавливаете сделку или верите „уже всё оформили“?» — buyer decision fork, не термин-дамп.
- Dual WP rubric `matkapital-i-sdelki` + `vtorichka-i-riski` для P0 matkapital angle.
- Cross-rubric interlink B09 (ипотека/ЕГРН строка) + B07 (наследство) — контекст sibling, не SEO-хвост.
- Research guard: механизм без выдуманного номера дела (research-notes.md handoff constraint).

### Change
- Scout bank: tag `matkapital_child_shares` + `egrn_false_comfort` — B11 angle «опека молчала / три года» отделён от «доли не видели» cluster; логировать в handoff.
- Description sticky/hook trio: ЕГРН clean → delayed cancel — повторять rhythm для matkapital P0 при vol <100 после rework.

### Never again
- Подменять casus маткапитала чеклистом «6 месяцев на доли» без истории и финала суда.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).
- Drop matkapital hook при angle vol 35 без Tyumen buyer rework (B11 прошёл rework → P0 spine 6068).

### Proposed apply
- Scout klyshin bank: `matkapital_child_shares` sibling defaults → B02/B07/B08/B09; dual category `matkapital-i-sdelki`.
- После Metrika ingest для post 9181 — re-evaluate confidence medium/high если retention совпадает с matkapital cohort.

### Durable applied
- none (один run, evidence SKIP, Metrika absent)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-matkapital-byl-opeka-molchala-cherez-tri-goda-deti-osporili-sdelku-v-tyumeni
wp_post_id: 9181
