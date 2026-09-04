## LESSON-20260904-0821-B22-newbuild-mortgage-rate-before-ddu-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-agent-report.json
  finding: new cluster `newbuild_mortgage_rate_changed_before_ddu_tyumen`; story_dup PASS vs Sep 3 «банк снял одобрение» (revocation, not rate change); vs B19 family mortgage escrow; vs B20 legal-entity escrow; plot = одобрение ипотеки на новостройку было, за 24–48 ч до ДДУ банк изменил процентную ставку / условия программы, платёж вырос (+15–20 тыс. ₽), семья остановила сделку, бронь сгорела.
- artifact: research-agent-report.json#wordstat
  finding: weak P0 «ипотека на новостройку процентная ставка» regions 55+11176 freq **21** (compare RU225 960); support «ставка ипотеки новостройка» 54, «ипотека в тюмени на новостройки» 41; rework from broader probes rejected (долгострой 86 — B12 overlap; эскроу 2 — B19/B20).
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `comment_magnet_question: true`, `no_tldr_opening: true`, `spine_once_no_recap: true`, word_count 2136, interlink_siblings_2_4, categories ipoteka / pokupka-kvartiry.
- artifact: wp-publish-result.json
  finding: publish PASS post **9627**, featured + 7 inline uploads.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9627 ingest skipped; day-0, no behavioral baseline)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0)

### Keep
- Wordstat rework: при слабом rate-specific P0 (21) — держать buyer jargon «ипотека на новостройку процентная ставка» как spine; не drop на escrow/долгострой кластеры.
- Plot differentiation: **изменение ставки** накануне ДДУ vs **отзыв одобрения** (Sep 3) vs семейная ипотека/эскроу (B19) vs смена юрлица (B20).
- Klyshin none — fresh Tyumen newbuild mortgage-rate casus без Klyshin preferred.
- Dzen news-casus: 24–48 ч до ДДУ + agency ending; comment magnet «подписали бы на новых условиях или развернулись».

### Change
- Scout: cluster lock в `memory/scout/used-clusters.json` (content-learner B22).
- После Metrika credentials: cohort `cluster:newbuild_mortgage_rate_changed_before_ddu_tyumen` vs Sep 3 approval-revocation sibling.

### Never again
- Смешивать B22 с отзывом одобрения ипотеки (revocation plot).
- Смешивать B22 с семейной ипотекой / маткапиталом / эскроу-блоком (B19/B20).
- Drop hook при P0=21 без newbuild mortgage-rate rework.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_mortgage_rate_changed_before_ddu_tyumen` until 2026-10-04 (B22 ledger).

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B22 (content-learner 2026-09-04); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi
wp_post_id: 9627
