## LESSON-20260829-1309-B15-pdkp-double-sale-cluster
status: proposed
topic_id: B15
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs-b15.md
  finding: new cluster `preliminary_contract_seller_sold_elsewhere_tyumen`; story_dup PASS vs rent_to_buy, double_sale_yalutorovsk, deposit_auction; Klyshin none (fresh Tyumen casus preferred).
- artifact: assembled-scout-inputs-b15.md (Wordstat)
  finding: final P0 «предварительный договор купли продажи квартиры» regions 55+11176 freq **62** (compare RU225 6612); broader probe «предварительный договор купли продажи» 265.
- artifact: research-notes.md
  finding: modeled Tyumen casus — no public confirmed case; firewall: не приписывать реальным людям/адресам; ПДКП не в ЕГРН, parallel sale risk, задаток vs аванс, понуждение п.4 ст.445 после регистрации за другими — деньги не квартиру.
- artifact: wp-publish-result.json
  finding: publish PASS post **9310**, live-page PASS, 7 inline uploads, categories=31.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `no_tldr_opening: true`, `early_cta_tg_max_only: true`, word_count **2588**, sibling_interlinks **3**.
- artifact: description-brief.json
  finding: Dzen card distinct from title («У нас же договор» hook), rhythm klyshin_case_hook, verdict PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 9310)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: exact legal phrase weak locally (62) but buyer jargon spine valid; broader «предварительный договор купли продажи» 265 retained in handoff context.
- Dzen news-casus: event (ПДКП+задаток+ипотека) + risk (продавец зарегистрировал другим) + ending landing (остановили ипотечный аванс, agency not panic).
- Research firewall: modeled casus ≠ реальный адрес/сумма; три трека (понуждение / деньги / оспаривание) в практике H2, comment magnet «страховка или бумага».
- Interlink siblings: B02 raspiska, B03 zadatok/torgi, B08 umerшая жена — paper-vs-reality cluster.

### Change
- Scout: для `preliminary_contract_*` cluster держать secondary spine «предварительный договор купли продажи» (265) в Cover-text wordstat stickers, не только exact apartment phrase 62.
- После Metrika ingest: сравнить pdkp cluster vs B02/B03 sibling по scroll depth / TG CTA clicks (когда credentials появятся).

### Never again
- Обещать «суд вернёт квартиру» после регистрации за другим покупателем.
- Подменять modeled family casus реквизитами из чужой сделки или выдуманными суммами задатка.

### Proposed apply
- Scout story-cluster ledger: `preliminary_contract_seller_sold_elsewhere_tyumen` locked 2026-08-29 (B15).
- Metrika cohort tag `cluster:preliminary_contract_seller_sold_elsewhere_tyumen` после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B15-v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim
wp_post_id: 9310
live_url: {{SITE_BASE}}/blog/vtorichka-i-riski/v-tyumeni-podpisali-predvaritelnyj-prodavec-prodal-kvartiru-drugim/
