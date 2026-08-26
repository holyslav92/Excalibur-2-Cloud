## LESSON-20260826-1116-B11-bankruptcy-seller-casus-risk-cluster
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2465, h2 8, inline_figures 7, sibling_interlinks 4; `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: description-brief.json
  finding: Klyshin case hook rhythm, geo Тюмень, `not_equal_title: true` — Дзен-карточка про ключи/ЕГРН vs H1 про банкротство и суд.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B05 (скидка/риск), B09 (ипотека/ЕГРН), B10 (пожилой/телефон) — risk-cluster siblings; inbound planned B06, B04, B09.
- artifact: link-verify.json
  finding: 11 links, verdict pass, 0 failed.
- artifact: wp-publish-result.json
  finding: post 9171 published, 7 inline uploads, live-page PASS.
- artifact: article.html (comment magnet)
  finding: острый вопрос «Выписка была чистая, аванс внесли — значит банкротство продавца вас не касается?» — inversion casus (объект чистый vs человек в банкротстве).
- artifact: cover/cover-text.json
  finding: sticky «Проверяйте продавца» зеркалит thesis «реестр молчит про банкротство личности»; inline labels cite ЕФРСБ, ФССП, КАД, ст. 213.9/213.32, дело А22-1776/2013.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9171

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus shape: чистая выписка + год жизни + финуправляющий + отмена регистрации — stakes и финал без how-to checklist в лиде.
- Cover hook inversion «Чистая выписка квартиру не спасла» — on-topic stakes, не SEO-хвост.
- Практика после истории (ЕФРСБ/ФССП/КАД) — не bullet-dump в первом экране.
- Risk-cluster interlink (B02/B05/B09/B10) для vtorichka-i-riski — контекстные sibling.

### Change
- Scout/handoff: tag `seller_bankruptcy_person_not_object` + log `comment_magnet_angle` «чистая выписка ≠ защита от банкротства продавца» для Klyshin bank notes.
- Description vs H1 split (PASS) — сохранять: карточка про ключи/ЕГРН, H1 про суд и конкурсную массу.

### Never again
- Drop casus ради чеклиста «проверьте ЕГРН» без истории финуправляющего и отмены регистрации.
- Выводить engagement из quality-bar PASS без Metrika cohort.
- Писать «выписка = безопасность» без counter-case банкротства личности.

### Proposed apply
- Scout klyshin bank: tag `seller_bankruptcy_person_not_object` + sibling defaults → B02/B05/B09/B10 для Tyumen risk P0.
- После Metrika ingest для 9171 — re-evaluate confidence medium/high если retention/CTA совпадают с bankruptcy-risk cohort.

### Durable applied
- none (один bankruptcy run, нет Metrika, evidence SKIP)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-kupili-kvartiru-v-tyumeni-prodavec-ushel-v-bankrotstvo-finupravlyayuschij-ospori
wp_post_id: 9171
live_url: {{SITE_BASE}}/blog/vtorichka-i-riski/kupili-kvartiru-v-tyumeni-prodavec-ushel-v-bankrotstvo-finupravlyayuschij-ospori/
