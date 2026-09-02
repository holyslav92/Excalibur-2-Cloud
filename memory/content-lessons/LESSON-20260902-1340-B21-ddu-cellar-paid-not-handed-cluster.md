## LESSON-20260902-1340-B21-ddu-cellar-paid-not-handed-cluster
status: proposed
topic_id: B21
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-agent-report.json
  finding: new cluster `newbuild_ddu_cellar_paid_not_handed_tyumen`; story_dup PASS vs B12 (`ddu_escrow_handover_delay_tyumen` — перенос сдачи / заморозка эскроу), B20 (смена юрлица), B19 (семейная ипотека + эскроу), today's priemka wet screed / КП utilities; plot = accessory object (кладовка) named in ДДУ with number+area, paid on escrow, not handed at keys / wrong number / absent from acceptance act.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: weak probes «паркинг новостройка тюмень» 2, «кладовка дду новостройка» 0; **rework → final P0 «купить кладовку в новостройке тюмень» regions 55+11176 freq 18** (compare RU225 19); parent «купить кладовку в новостройке» RU225 925; «приемка новостройки тюмень» 35 rejected (overlap acceptance cluster).
- artifact: research-agent-report.json
  finding: fresh NashGorod 20.08.2026 — спрос на кладовые/паркинги в тюменских новостройках −60% г/г; editorial firewall — no public Tyumen case with ЖК/застройщик/банк; 214-ФЗ st.4/7/8 accessory object mechanics; interlink explicitly separates B12/B19/B20 sibling escrow plots.
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `comment_magnet_question: true`, `no_tldr_opening: true`, `spine_once_no_recap: true`, word_count 1812, 4 sibling interlinks (B09/B12/B19/B20).
- artifact: wp-publish-result.json
  finding: publish PASS post **9549**, live-page PASS, 7 inline uploads, featured 9550.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9549 недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при слабом parking/cellar P0 (паркинг 2, «кладовка дду» 0) — buyer jargon «купить кладовку в новостройке тюмень» 18 как demand spine; не брать «приемка новостройки тюмень» 35 — overlap acceptance cluster.
- Plot differentiation: кладовка/нежилое в ДДУ **на ключах** vs B12 перенос сдачи / заморозка эскроу vs B20 смена юрлица vs B19 семейная ипотека — четыре разных newbuild-кластера.
- Dzen news-casus: акт на квартиру под ипотечным давлением + agency ending («право не подписывать акт без оговорок»); comment magnet «подписываете акт, если кладовку не передали?».
- Interlink: B09/B12/B19/B20 siblings — явный plot firewall в research handoff.

### Change
- Scout: cluster `newbuild_ddu_cellar_paid_not_handed_tyumen` lock в used-clusters (content-learner B21).
- После Metrika credentials: cohort `cluster:newbuild_ddu_cellar_paid_not_handed_tyumen` vs B12/B20 escrow siblings по time-on-page.

### Never again
- Смешивать B21 с переносом сдачи / заморозкой эскроу после внесения (B12).
- Смешивать B21 со сменой юрлица / новым ДДУ (B20).
- Смешивать B21 с дефектами приёмки квартиры / мокрой стяжкой (today's acceptance cluster).
- Брать «приемка новостройки тюмень» как P0 при accessory-object plot.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_ddu_cellar_paid_not_handed_tyumen` until 2026-10-02 (B21 ledger).
- Scout story-cluster registry entry (human): required_groups кладовка/нежилое + ДДУ номер/площадь + не передано на ключах + акт без кладовки.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B21 (content-learner 2026-09-02); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo
wp_post_id: 9549
