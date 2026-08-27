## LESSON-20260827-0609-B11-publish-live-interlink-notes
status: proposed
topic_id: B11
category: cta
confidence: low

### Evidence
- artifact: wp-publish-result.json + memory/blog/wp-publish-log.md
  finding: post_id 9191 published 2026-08-27; wp_category_slugs vtorichka-i-riski + riski-sdelki (31,58); featured 9192; inline 9193–9199 (7/7); schema_meta ok; live-page PASS; llms deploy PASS.
- artifact: interlink-plan.json + link-verify.json
  finding: outbound 4 siblings — B02 (расписка), B05 (скидка/риск), B07 (наследство, plot guard), B09 (ипотека/ЕГРН); verdict pass, 0 failed links.
- artifact: wp-publish-log.md
  finding: **no inbound targets with post_id in ledger** — auto inbound «Читайте также» skipped (same pattern B06/B10).
- artifact: live-page-report.json
  finding: gate PASS on permalink /blog/vtorichka-i-riski/v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri/
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет post-publish CTR/retention для 9191

### Named blockers
- INBOUND_INTERLINK_LEDGER_GAP (sibling post_id null in ledger)
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE

### Keep
- Dual rubric vtorichka-i-riski + riski-sdelki для tired-buyer/inheritance risk casus.
- Outbound risk-cluster interlink 2–4 (фактически 4) — контекстные sibling, не SEO-хвосты.
- SFTP publish path + 7 inline uploads + yoast_social_image — parity B10 pattern.

### Change
- Ledger hygiene: backfill `post_id` для B02/B05/B07/B09 в `shared/published-articles.md` — unlock inbound auto-interlink на следующих publish.
- После Metrika ingest 9191 — baseline для inheritance-risk cohort vs B07/B10.

### Never again
- Publish без wp_category_slugs при wp_categories_required=true.
- Вывод engagement из publish PASS без Metrika (причина не подтверждена).

### Proposed apply
- Fixer/backfill task: populate post_id in published-articles ledger for siblings → enable inbound on B12+.
- Publish log template: note inbound skip reason explicitly (уже в wp-publish-log B11).

### Durable applied
- none (env/ledger gap, не content rewrite)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri
wp_post_id: 9191
permalink: /blog/vtorichka-i-riski/v-tyumeni-chetyre-mesyaca-iskali-vtorichku-ustavshij-pokupatel-soglasilsya-na-ri/
