## LESSON-20260901-1338-B20-legal-entity-ddu-escrow-cluster
status: proposed
topic_id: B20
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `newbuild_developer_legal_entity_change_ddu_escrow_tyumen`; story_dup PASS vs B12 (`ddu_escrow_handover_delay_tyumen` — перенос сдачи / эскроу после внесения), B19 (семейная ипотека + маткапитал), daily booking/priemka plots; plot = реорганизация → смена ИНН/ОГРН в ДДУ → банк не открывает эскроу до переаккредитации → срыв до внесения на эскроу.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: weak P0 «застройщик реорганизация» 3, «дду эскроу» 38 (overlap B12/B19); **rework → final P0 «новостройки в тюмени от застройщика» regions 55+11176 freq 651** (compare RU225 1268).
- artifact: research-notes.md
  finding: editorial casus firewall — ребрендинг 72.ru СтройМир→«Север» ≠ смена юрлица; деньги на эскроу не внесены (отличие от B12); interlink явно разводит B19/B12 sibling plots.
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `comment_magnet_question: true`, `no_tldr_opening: true`, `spine_once_no_recap: true`, word_count 2126, 4 sibling interlinks.
- artifact: wp-publish-result.json
  finding: publish PASS post **9490**, live-page PASS, 7 inline uploads, categories dokumenty-i-oformlenie / riski-sdelki / pokupka-kvartiry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9490 недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при слабом legal P0 (реорганизация 3) — buyer jargon «новостройки в тюмени от застройщика» 651 как demand spine; exact «дду эскроу» 38 — secondary, не P0.
- Plot differentiation: смена юрлица **до** эскроу vs B12 заморозка **после** внесения vs B19 семейная ипотека/маткапитал — три разных escrow-кластера, Scout anti-repeat держит отдельно.
- Research firewall: 72.ru ребрендинг только как контекст «вывеска ≠ ООО»; без фамилий/ЖК/банка в casus.
- Dzen news-casus: 72ч дедлайн брони + agency ending («право сказать сначала бумаги»); comment magnet про подпись vs выход из сделки.

### Change
- Scout: добавить `newbuild_developer_legal_entity_change_ddu_escrow_tyumen` в `shared/scout-story-clusters.json` (сейчас sync-used-clusters не ловит newbuild-кластеры по regex) — needs-human.
- После Metrika credentials: cohort `cluster:newbuild_developer_legal_entity_change_ddu_escrow_tyumen` vs B12/B19 escrow siblings по time-on-page.

### Never again
- Смешивать B20 с задержкой сдачи / заморозкой эскроу после внесения (B12).
- Смешивать B20 с блокировкой семейной ипотеки / маткапитала (B19).
- Брать тюменский ребрендинг как доказательство смены юрлица в casus.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_developer_legal_entity_change_ddu_escrow_tyumen` until 2026-10-01 (B20 ledger).
- Scout story-cluster registry entry (human): required_groups юрлицо/реорганизация + новый ДДУ + эскроу не открыт.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B20 (content-learner 2026-09-01); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B20-v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot
wp_post_id: 9490
