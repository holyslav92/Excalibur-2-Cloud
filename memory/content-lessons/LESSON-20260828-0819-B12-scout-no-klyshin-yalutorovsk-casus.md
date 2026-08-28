## LESSON-20260828-0819-B12-scout-no-klyshin-yalutorovsk-casus
status: proposed
topic_id: B12
category: geo
confidence: medium

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md
  finding: Scout locked B12 without Klyshin — fresh Tyumen-region casus (Ялуторовск, URA.RU 22.06.2026); `klyshin_hook: none` preferred when no fresh @klyshin_A plot match.
- artifact: research-agent-report.json#overlap_check
  finding: `cluster_id: double_sale_two_buyers_rieltor_poa` PASS vs 30d locks; distinct from B04 `doverennost_svo_seller` (double sale two buyers via realtor POA, not SVO seller).
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `no_tldr_opening: true`, word_count 2587 — news-casus shape held without Klyshin anchor.
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post 9240 ingest недоступен)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (behavioral baseline отсутствует)

### Keep
- Scout triple gate: Wordstat rework + dzen_casus_shape + story_dup_check перед lock.
- Hot regional casus (Ялуторовск / Тюменская область) без Klyshin, когда cluster свежий и signal_urls (URA.RU) верифицированы.
- Comment magnet «Кто прав — первый заплатил или тот, кто заплатил больше?» — острый вопрос для Дзена, не how-to checklist.

### Change
- Scout handoff: при `klyshin_hook: none` явно фиксировать `cluster_id` и отличие от ближайшего locked cluster (B04 doverennost) — уже сделано для B12; повторять в handoff template.
- Research: primary casus URA.RU июнь 2026 — в run notes отметить возраст сигнала; при publish август держать «свежесть» через региональный контекст (Ставрополь приговор 12.08.2026) без выдумки дат.

### Never again
- Принудительный Klyshin hook, когда нет свежего поста на тот же plot и есть verified regional casus.
- Путать cluster `double_sale_two_buyers_rieltor_poa` с `doverennost_svo_seller` — разные finale и comment magnet.

### Proposed apply
- Scout skill runbook: «no Klyshin» path = PASS при verified signal_urls + story_dup PASS + Wordstat rework log (не binary skip слабого hook).
- После Metrika ingest post 9240 — проверить, даёт ли Ялуторовск/geo в title uplift vs Tyumen-only posts (low-confidence until credentials fixed).

### Durable applied
- none (первый именованный learner run для no-Klyshin regional casus)

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-v-yalutorovske-kvartiru-prodali-dvum-pokupatelyam-pervuyu-pytayutsya-vyselit
wp_post_id: 9240
