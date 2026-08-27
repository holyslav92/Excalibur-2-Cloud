## LESSON-20260827-0801-B11-double-sale-casus-text-pass
status: proposed
topic_id: B11
category: other
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: все текстовые gates PASS — word_count 2197, h2 7, inline_figures 7, sibling_interlinks 4; `comment_magnet_question`, `early_cta_tg_max_only`, `no_tldr_opening`, `interlink_siblings_2_4` PASS. Единственный FAIL — `cover_qa_pass`.
- artifact: opening-meta-gate.json
  finding: prose lead + structural opening gate PASS (Sol owns opening).
- artifact: description-brief.json (implied via derouter stamp)
  finding: description gate PASS; Дзен-карточка после Sol.
- artifact: cover/cover-text.json
  finding: double-sale casus hook «Чистая выписка не спасла аванс»; meme_picks roll_safe + grumpy_cat; 7 inline label sets on-topic (ЕГРН, аванс, ВС № 8-КГ21-16-К4).
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post не опубликован, нет CTR/retention

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (unpublished — нет live behavioral data)
- PUBLISH_BLOCKED_COVER_ONLY

### Keep
- News-casus shape: двойная продажа + аванс до регистрации + Ялуторовск/Тюмень stakes — без how-to checklist lead.
- Risk-cluster interlink pattern (siblings на vtorichka-i-riski) — 4 outbound links PASS quality-bar.
- Sol 3-part merge (writer→sol) на длинном casus без 524 timeout — text path stable.

### Change
- Scout/handoff: tag `double_sale_avans` + `comment_magnet_angle` «кому вернуть аванс если квартиру продали дважды» — зеркалит финал и cover sticky.
- При text PASS + cover FAIL: Indexer всё равно обновляет llms.txt (fail-fast canon) — B11 подтверждает.

### Never again
- Считать run «failed» целиком когда только cover блокирует publish — текстовый контур отдельный success signal.
- Выводить engagement potential из quality-bar text PASS без Metrika и без publish.

### Proposed apply
- Scout klyshin bank: tag `double_sale_avans` + sibling defaults (B01 EGRN, B02 расписка, B04 доверенность) для Tyumen risk P0.
- После cover fix + publish B11 — re-run content-learner с Metrika ingest для cohort compare с B10 elderly_phone.

### Durable applied
- none (один unpublished run, evidence SKIP, Metrika blocked)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-kvartiru-prodali-dvazhdy-vtoroj-pokupatel-v-tyumeni-poteryal-avans
wp_post_id: none (publish stopped)
