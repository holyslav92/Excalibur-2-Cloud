## LESSON-20260905-1107-B23-apartments-flat-ddu-cluster
status: proposed
topic_id: B23
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `newbuild_apartments_instead_flat_ddu_tyumen`; story_dup PASS vs B19/B21/B22/B12; Klyshin none (fresh Tyumen newbuild casus).
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: final P0 «новостройки тюмень» regions 55+11176 freq **3640** (compare RU225 **8705**); exact «апартаменты тюмень» 646 (noisy tail); buyer narrow «купить апартаменты в тюмени» **35** — weak vs newbuild spine, rework to P0 newbuild jargon.
- artifact: research-notes.md
  finding: fresh signal dzen.ru/a/amXODH4m4RWPJY_H (~02.09.2026) + morein.pro/ddu-na-apartamenty; plot = квартира в рекламе/ДДУ vs апартаменты/нежилое в ЕГРН при регистрации права.
- artifact: wp-publish-result.json
  finding: publish PASS post **9749**, live-page PASS, 7 inline uploads, categories=31.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `spine_once_no_recap: true`, `word_count` 2177 (target 1800–2200), `no_composite_disclaimer: true`.
- artifact: stylo-report.json
  finding: `stylo_pass: true`, `sol_rewrite_applied: false` (delta 2.43 < 2.85); elevated `legal_per_1k` noted but within gate.
- artifact: cover/cover_qa.json + .cursor/excalibur-blog-fragments/cover.md
  finding: `ocr_false_positive_escape: true` (11 flaky overrides); `budget_exhausted: false`, grsai_canvas_attempts=1 — canonical escape path, not duplicate of B15 exhaust.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (no CTR/retention for post 9749)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat rework: при слабом exact «апартаменты» (646 noisy / 35 buyer) — P0 через «новостройки тюмень» 3640; on-topic hook через ДДУ+ЕГРН+ипотека.
- Dzen news-casus: event (подписали ДДУ на «квартиру») + risk (ЕГРН = апартаменты → ипотека/прописка) + comment magnet «подписали бы акт при ключах на столе».
- Scout anti-repeat: отклонены parking/cellar (B21 overlap), matkapital (B19), trade-in/day-before-DDU — distinct legal plot locked.
- Cover OCR escape без budget exhaust — штатный путь (cross_run B20/B22).

### Change
- Scout story-cluster ledger: `newbuild_apartments_instead_flat_ddu_tyumen` locked 2026-09-05 (B23).
- После Metrika ingest: cohort tag `cluster:newbuild_apartments_instead_flat_ddu_tyumen` vs sibling DDU clusters (B12 escrow, B22 rate hike).

### Never again
- Брать «апартаменты тюмень» 646 как P0 без rework (отельный хвост).
- Смешивать plot с B21 cellar/parking или B19 matkapital/escroу.
- Fixer regen cover при OCR escape PASS + budget not exhausted.

### Proposed apply
- Scout `used-clusters.json`: cluster_id `newbuild_apartments_instead_flat_ddu_tyumen`.
- Metrika cohort compare после credentials fix.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B23-v-tyumeni-v-ddu-napisali-kvartiru-v-vypiske-okazalis-apartamenty
wp_post_id: 9749
