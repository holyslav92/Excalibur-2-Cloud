## LESSON-20260828-0630-B11-illegal-renovation-risk-cluster
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md
  finding: new cluster `illegal_renovation_rosreestr_blocks_registration`; story_dup_check PASS (отделён от court_took_apartment, egrn_line, discount_2m); finale = приостановка/отказ Росреестра, не «суд забрал» и не родственники.
- artifact: research-notes.md
  finding: overlap note — отличается от B09 (обременение/ипотека); buyer spine перепланировка + ЕГРН/техпаспорт; моделируемый Tyumen casus без Klyshin.
- artifact: title-brief.json
  finding: H1 «В Тюмени открытая кухня остановила регистрацию квартиры»; `comment_magnet_angle`: «Скидку за открытую кухню вы бы взяли — или это всегда красный флаг?»; verdict PASS.
- artifact: description-brief.json
  finding: Klyshin case hook rhythm, geo Тюмень, `not_equal_title: true` — скидка за кухню vs H1 про регистрацию.
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2553, h2 9, inline_figures 7, sibling_interlinks 4; `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B05 (скидка/риск), B06 (автооценка), B09 (регистрация/ЕГРН) — risk-cluster siblings; inbound planned B06, B04, B09.
- artifact: link-verify.json
  finding: 11 links, verdict pass, 0 failed.
- artifact: wp-publish-result.json
  finding: post 9230 published, categories vtorichka-i-riski + dokumenty-i-oformlenie, live-page PASS.
- artifact: derouter-opus-stamp-sol-part1.json (+ part2/3)
  finding: Sol single-shot 3-part PASS on claude-opus-5 (~17k tokens part1); no Derouter 524 chunk fallback.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9230

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- Scout new cluster без Klyshin — fresh Tyumen casus; Wordstat P0 «покупка квартиры с неузаконенной перепланировкой» RU225 **192** (из scout handoff, не invent).
- News-casus shape: открытая кухня + скидка + аванс → Росреестр приостановил до собственности; comment magnet про «скидку за кухню» как красный флаг.
- Risk-cluster interlink (B02/B05/B06/B09) + overlap guard vs B09 egrn_line — документировано в research-notes.
- Cover sticky «Сначала сверка, потом аванс» зеркалит практический финал casus.

### Change
- Scout bank: после publish зафиксировать cluster `illegal_renovation_rosreestr_blocks_registration` в `used-clusters.json` (sync script) — handoff открыл cluster, ledger sync на момент learner ещё без B11 entry.
- Description/title split: сохранять разрыв H1 (регистрация) vs card (скидка за кухню) — PASS на B11.

### Never again
- Смешивать illegal_renovation finale с court_took_apartment или egrn_line mortgage plot в одном cluster.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).

### Proposed apply
- Scout story-clusters: add `illegal_renovation_rosreestr_blocks_registration` lock 30d после B11 publish (fixer/sync).
- Klyshin bank tag `open_kitchen_discount_trap` + sibling defaults B05/B06/B09 для перепланировка P0.
- После Metrika ingest для 9230 — re-evaluate confidence medium/high если retention/CTA совпадают с discount-risk cohort (B05/B06).

### Durable applied
- none (один run, нет Metrika, evidence SKIP)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-v-tyumeni-kupili-kvartiru-s-otkrytoj-kuhnej-rosreestr-otkazal-v-registracii
wp_post_id: 9230
