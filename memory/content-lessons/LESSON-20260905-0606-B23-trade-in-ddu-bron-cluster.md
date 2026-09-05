## LESSON-20260905-0606-B23-trade-in-ddu-bron-cluster
status: proposed
topic_id: B23
category: geo
confidence: medium

### Evidence
- artifact: research-agent-report.json#overlap_check
  finding: `cluster_id: newbuild_trade_in_failed_before_ddu_tyumen`, `story_dup_check: PASS` — distinct from B22 rate hike, Sep 4 wrong escrow, assignment refusal; plot = trade-in old flat as down payment, оценка снижена/выкуп сорван за 24ч до ДДУ, бронь сгорела.
- artifact: research-agent-report.json#wordstat
  finding: P0 «трейд ин новостройка» RU225 479; Tyumen 11176 alone 6 — localized via Tyumen developers/media (Брусника Дни обмена 4–5.09, ttis.ru, 72.ru test 12 programs).
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, word_count 2183, `ending landing` preserved — comment magnet «доплатили разницу или отпустили бронь?».
- artifact: description-brief.json
  finding: Dzen card distinct from title; rhythm klyshin_case_hook; verdict PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9697 ingest skipped)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (no behavioral baseline for new cluster)

### Keep
- Scout quad gate: newbuild-only trade-in casus без Klyshin (fresh Tyumen hook preferred).
- Research: official developer terms (ttis.ru, enco.ru) + local media discount ranges; не выдумывать фиксированную оценку в ДДУ.
- Interlink to sibling «день до ДДУ» plots (B22 rate hike, B20 legal entity) без spine-once collision.

### Change
- Scout ledger: зарегистрировать `newbuild_trade_in_failed_before_ddu_tyumen` в `memory/scout/used-clusters.json` после publish (30d anti-repeat).
- Wordstat weak Tyumen (6) + strong RU spine (479) — rework localize в title/handoff, не drop hook.

### Never again
- Вторичка как сюжет при `topic_market_focus: newbuild_only`.
- Повтор cluster «trade-in сорвался до ДДУ» в 30д с новым title-only retitle.

### Proposed apply
- Human review: добавить cluster в `shared/scout-story-clusters.json` examples если отсутствует.
- Director: trade-in + бронь + ДДУ = high-engagement newbuild risk lane (семьи + инвесторы).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela
wp_post_id: 9697
