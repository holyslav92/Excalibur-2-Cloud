## LESSON-20260901-0813-B19-matkapital-escrow-cluster
status: proposed
topic_id: B19
category: geo
confidence: low

### Evidence
- artifact: research-agent-report.json, scout/assembled-scout-inputs.md
  finding: new cluster `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen`; story_dup PASS; Klyshin optional (none used).
- artifact: research-agent-report.json#wordstat
  finding: P0 «купить новостройку в тюмени в ипотеку» Tyumen 55+11176 **93** (RU225 140); rework from weak «маткапитал новостройка» (3) via «семейная ипотека новостройка» (126).
- artifact: title-brief.json
  finding: comment_magnet — маткапитал на прошлую квартиру vs бронь новостройки в семейную ипотеку; dzen_casus_shape PASS.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `no_tldr_opening: true`, `word_count: 2125`, `sibling_interlinks: 4`.
- artifact: wp-publish-result.json
  finding: publish PASS post **9452**, categories ipoteka + matkapital-i-sdelki, 7 inline uploads.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: exact «маткапитал новостройка» (3) → family mortgage + newbuild Tyumen P0 (93) — demand spine без вторички.
- Dzen news-casus: false finale (одобрение ≠ сделка) + matkapital/детские доли blocker + agency landing (справка/доли до брони).
- Research firewall: modeled family casus; SFR/dom.rf rules verified; не смешивать с unrelated ЖК сигналами.

### Change
- Scout ledger: lock `newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` 2026-09-01 (B19).
- После Metrika ingest: cohort tag vs B12 `ddu_escrow_handover_delay_tyumen` sibling — time-on-page / scroll на ipoteka+matkapital рубриках.

### Never again
- Drop hook при слабом «маткапитал новостройка» (3) без rework на семейную ипотеку + newbuild Tyumen.
- Вторичка как сюжет при `topic_market_focus: newbuild_only`.

### Proposed apply
- `memory/scout/used-clusters.json` — cluster locked for B19.
- Metrika cohort `cluster:newbuild_family_mortgage_matkapital_escrow_blocked_tyumen` после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B19-semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli
wp_post_id: 9452
