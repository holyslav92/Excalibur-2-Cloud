## LESSON-20260826-0834-B10-elderly-phone-casus-risk-cluster
status: proposed
topic_id: B10
category: structure
confidence: low

### Evidence
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2580, h2 8, inline_figures 7, sibling_interlinks 3; gates `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: description-brief.json
  finding: Klyshin case hook rhythm, geo Тюмень, `not_equal_title: true` — Дзен-карточка не дублирует H1.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B04 (доверенность), B05 (скидка/риск) — risk-cluster siblings; inbound planned B06, B04, B09.
- artifact: link-verify.json
  finding: 10 links, verdict pass, 0 failed.
- artifact: wp-publish-result.json
  finding: post 9161 published, 7 inline uploads, live-page PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9161

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus shape: пожилой продавец + телефонное управление + родственники **до аванса** — stakes и финал без how-to checklist.
- Cover sticky «Хорошо, что не внесли аванс» зеркалит casus finale и comment-magnet угол.
- Risk-cluster interlink (B02/B04/B05) для vtorichka-i-riski — контекстные sibling, не SEO-хвосты.
- Sol single-shot PASS (15171 tokens, claude-opus-5) на B10 — chunk не требовался (в отличие от B06 524).

### Change
- Scout/handoff: логировать `comment_magnet_angle` для elderly+phone casus — B10 angle «кто реально ведёт к авансу» работает с quality-bar PASS; повторить в bank notes.
- Description: сохранять разрыв title/card (PASS) — телефон у хозяина vs H1 «родственники сорвали».

### Never again
- Drop casus ради чеклиста «маркеры давления» без истории и финала.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).

### Proposed apply
- Scout klyshin bank: tag `elderly_phone_control` + sibling interlink defaults → B02/B04/B05 для Tyumen risk P0.
- После Metrika ingest для 9161 — re-evaluate confidence medium/high если retention/CTA сигналы совпадают с risk-cluster cohort.

### Durable applied
- none (один run, нет Metrika, evidence SKIP)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-v-tyumeni-rodstvenniki-ostanovili-prodazhu-pozhilogo-prodavca-veli-po-telefonu-v
wp_post_id: 9161
