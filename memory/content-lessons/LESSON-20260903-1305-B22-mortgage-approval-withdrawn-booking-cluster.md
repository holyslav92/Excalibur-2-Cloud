## LESSON-20260903-1305-B22-mortgage-approval-withdrawn-booking-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: research-agent-report.json, research-notes.md
  finding: new cluster `newbuild_mortgage_approval_withdrawn_booking_lost_tyumen`; story_dup PASS vs live `egrn_line_blocks_advance` (B09 — обременение в ЕГРН после одобрения), B12 (эскроу заморожен после внесения), B19 (семейная ипотека / эскроу не открыт), B20 (смена юрлица до эскроу); plot = предварительное одобрение → бронь → банк снимает решение за 72ч до ДДУ → бронь сгорела, лот ушёл другому.
- artifact: research-agent-report.json#wordstat
  finding: weak «бронь новостройки» 3 → rework «ипотека в тюмени на новостройки» 41 → **final P0 «купить квартиру в тюмени новостройка ипотека» 86**; spine phrases «одобрение ипотеки» 224, «сколько действует одобрение ипотеки» 24.
- artifact: research-notes.md#case_verification
  finding: NOT_A_CONFIRMED_SINGLE_FAMILY_REPORT — типовой локальный casus; fresh signals РИА 30.08 (МФО/рассрочка ~30% отказов брокеры), Коммерсант 57% ипотек на новостройки Тюмень июль 2026, 72.ru 27.08 trade-in бронь слетает (контекст, не доказательство casus).
- artifact: quality-bar-9.json
  finding: `all_pass: true`, word_count 2070, `comment_magnet_question: true`, `spine_once_no_recap: true`, 3 sibling interlinks (B12/B19/B20).
- artifact: title-brief.json
  finding: comment magnet «успели бы найти другой банк или отказались бы от этой квартиры?»; H1 stakes 72ч + ДДУ + бронь.
- artifact: wp-publish-result.json
  finding: publish PASS post **9601**, live-page PASS, 7 inline uploads, categories ipoteka / riski-sdelki / pokupka-kvartiry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (нет ingest; behavioral baseline для post 9601 недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0, no behavioral baseline)

### Keep
- Wordstat rework: при слабом «бронь новостройки» (3) — buyer spine «купить квартиру в тюмени новостройка ипотека» 86 + secondary «одобрение ипотеки» 224; не дропать hook из‑за weak бронь-term.
- Plot differentiation: отзыв одобрения **до** ДДУ/эскроу vs B12 заморозка после внесения vs B19/B20 escrow-блокеры vs B09 ЕГРН-строка на вторичке — пять разных ипотечных кластеров.
- Research firewall: РИА МФО/рассрочка и 72.ru trade-in — контекст риска сроков, не «подтверждённый случай»; без фамилий/ЖК/банка.
- Dzen news-casus: 72ч дедлайн + agency ending (сверить статус одобрения и срок брони до внесения); comment magnet про второй банк vs отказ от лота.
- Interlink triangle B12/B19/B20 — явно разводит escrow/ипотечные sibling plots.

### Change
- Scout: добавить `newbuild_mortgage_approval_withdrawn_booking_lost_tyumen` в `shared/scout-story-clusters.json` (sync-used-clusters regex может не ловить newbuild mortgage cluster) — needs-human.
- После Metrika credentials: cohort `cluster:newbuild_mortgage_approval_withdrawn_booking_lost_tyumen` vs B09/B12/B19/B20 mortgage siblings по time-on-page.

### Never again
- Смешивать B22 с блокировкой регистрации по ЕГРН на вторичке (B09 live `egrn_line_blocks_advance`).
- Смешивать B22 с заморозкой эскроу после внесения (B12) или семейной ипотекой/сменой юрлица (B19/B20).
- Подавать предварительное одобрение как гарантию выдачи в день ДДУ без оговорки повторной проверки банка.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_mortgage_approval_withdrawn_booking_lost_tyumen` until 2026-10-03 (B22 ledger).
- Scout story-cluster registry entry (human): required_groups предварительное одобрение + бронь новостройки + отзыв решения + потеря лота.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B22 (content-learner 2026-09-03); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela-za-tri-dnya-d
wp_post_id: 9601
