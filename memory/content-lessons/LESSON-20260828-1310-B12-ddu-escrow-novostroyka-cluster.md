## LESSON-20260828-1310-B12-ddu-escrow-novostroyka-cluster
status: proposed
topic_id: B12
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `ddu_escrow_handover_delay_tyumen`; story_dup PASS vs B02/B09/B11; Klyshin optional (none used).
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: final P0 «новостройки тюмень» regions 55+11176 freq **4717** (compare RU225 8980); exact DDU phrase «купить квартиру по дду» weak locally (23).
- artifact: research-notes.md
  finding: fresh regional signal 27.08.2026 — арендный дом Защитников Отечества 36 (не семейный ДДУ кейс); family casus modeled, not attributed to real ЖК.
- artifact: wp-publish-result.json
  finding: publish PASS post **9250**, live-page PASS, 7 inline uploads, categories=31.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `no_tldr_opening: true`, `early_cta_tg_max_only: true`.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 9250)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: когда exact legal phrase слаб локально (ДДУ 23), P0 через buyer jargon «новостройки тюмень» 4717 — demand spine сохранён.
- Dzen news-casus: event (перенос ключей) + risk (эскроу заморожен, ипотека идёт) + comment magnet «ждёте или требуете возврат».
- Research firewall: региональный сигнал (арендный дом) ≠ семейный кейс — не смешивать в фактах.

### Change
- Scout: для novostroyka cluster держать secondary spine «купить новостройку в тюмени» (830) в handoff для Cover-text/inline labels.
- После Metrika ingest: сравнить ddu_escrow cluster vs B02 novostroyka sibling по time-on-page / scroll (когда credentials появятся).

### Never again
- Подменять modeled family casus реквизитами из чужого ЖК (Защитников 36).
- Брать exact «купить квартиру по дду» как P0 при 23 в Tyumen без rework.

### Proposed apply
- Scout story-cluster ledger: `ddu_escrow_handover_delay_tyumen` locked 2026-08-28 (B12).
- Metrika cohort tag `cluster:ddu_escrow_handover_delay_tyumen` после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B12-klyuchi-ot-novostrojki-v-tyumeni-perenesli-na-god-dengi-na-eskrou-zamorozili
wp_post_id: 9250
