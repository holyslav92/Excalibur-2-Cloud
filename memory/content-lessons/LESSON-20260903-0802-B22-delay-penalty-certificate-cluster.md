## LESSON-20260903-0802-B22-delay-penalty-certificate-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-agent-report.json
  finding: new cluster `newbuild_developer_delay_penalty_certificate_instead_cash_tyumen`; story_dup PASS vs B12 (`ddu_escrow_handover_delay_tyumen` — перенос сдачи / эскроу после внесения), B21 (кладовка), priemka/area plots 2026-09-01/03; plot = просрочка передачи 8 мес → неустойка 214-ФЗ → сертификат/бонус вместо денег в день ключей → ипотека+аренда без компенсации.
- artifact: assembled-scout-inputs.md Wordstat log
  finding: weak «неустойка застройщик дду» 33; **rework → final P0 «неустойка застройщик» regions 55+11176 freq 257** (compare RU225 8500).
- artifact: research-notes.md
  finding: firewall vs B12 (заморозка эскроу после внесения), B21 (кладовка), приёмка/мокрая стяжка; Калининский суд контекст только как тюменская практика, не casus B22.
- artifact: quality-bar-9.json
  finding: `all_pass: true`, word_count **2155**, `comment_magnet_question: true`, `spine_once_no_recap: true`, 4 sibling interlinks, stylo PASS (delta 2.18, no sol_rewrite).
- artifact: wp-publish-result.json
  finding: publish PASS post **9575**, live-page PASS, categories dokumenty-i-oformlenie / riski-sdelki / pokupka-kvartiry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post-publish day 0, no behavioral baseline)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- Wordstat rework: при слабом «неустойка застройщик дду» (33) — buyer jargon «неустойка застройщик» 257 как P0; не уходить в priemka cluster.
- Plot differentiation: сертификат вместо денег **в день ключей** vs B12 перенос сдачи / эскроу vs B21 кладовка vs area-at-acceptance.
- Dzen news-casus: 8 месяцев ипотека+аренда, comment magnet «сертификат vs суд»; ending agency (посчитать до подписи).

### Change
- Scout: lock cluster в `memory/scout/used-clusters.json` (content-learner B22).
- После Metrika credentials: cohort `cluster:newbuild_developer_delay_penalty_certificate_instead_cash_tyumen` vs B12 delay siblings.

### Never again
- Смешивать B22 с B12 (эскроу заморозили после внесения).
- Смешивать B22 с приёмкой/метрами/мокрой стяжкой.
- Брать ребрендинг/мораторий как основной casus без сертификата в день ключей.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_developer_delay_penalty_certificate_instead_cash_tyumen` until 2026-10-03 (B22 ledger).

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B22 (content-learner 2026-09-03); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser
wp_post_id: 9575
