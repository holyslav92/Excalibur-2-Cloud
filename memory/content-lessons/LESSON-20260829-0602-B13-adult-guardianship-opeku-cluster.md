## LESSON-20260829-0602-B13-adult-guardianship-opeku-cluster
status: proposed
topic_id: B13
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md
  finding: cluster `adult_guardianship_incapacitated_blocks_sale`; story_dup PASS vs `matkapital_opieka_kids` (детская доля) и `elderly_seller_led_by_phone` (телефон); P0 «признание недееспособным» 55+11176 freq 157; comment_magnet «родня тянет опеку — внесёте аванс или ждёте суда?»
- artifact: quality-bar-9.json
  finding: text gates all PASS — word_count 2547, h2 8, inline_figures 7, sibling_interlinks 4, `comment_magnet_question`, `no_tldr_opening`, `early_cta_tg_max_only`.
- artifact: description-brief.json
  finding: Klyshin rhythm, geo Тюмень, `not_equal_title: true` — «Пенсионер выглядел безупречно… до аванса оставались сутки».
- artifact: opening-meta-gate.json
  finding: PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; post не live, нет behavioral baseline

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (unpublished)
- PUBLISH_BLOCKED_COVER_QA_FAIL (cover, не editorial)

### Keep
- News-casus shape: взрослая опека/недееспособность **до аванса** — distinct от matkapital+дети и elderly+phone clusters.
- Comment magnet на agency («ждёте справки из суда»), не how-to checklist finale.
- Description card ≠ H1 — stakes «сутки до аванса» в карточке, H1 — «родственники пошли в суд».
- Fresh Tyumen casus без Klyshin (scout preference) — research angles ст. 171/177 ГК, ст. 37 опека.

### Change
- Scout bank: tag `adult_guardianship_incapacitated` + lock cluster после publish (сейчас publish blocked — sync `used-clusters` отложен).
- Interlink defaults: siblings risk-cluster (B10 elderly phone, B05 PND/discount, court-contest posts) — проверить при publish.

### Never again
- Смешивать взрослую опеку с matkapital/детскими долями в scout dup check.
- Выводить engagement potential из quality-bar PASS без Metrika (unpublished).

### Proposed apply
- Scout `next-cluster-guidance.md`: после B13 publish — lock `adult_guardianship_incapacitated_blocks_sale` 30d.
- Metrika re-evaluate medium confidence после publish + credentials fix.

### Durable applied
- none (один run, unpublished, evidence SKIP, Metrika absent)

### Resolution
status: recorded
article_dir: memory/blog/articles/B13-v-tyumeni-rodstvenniki-oformili-opeku-nad-prodavcom-za-den-do-avansa-sdelku-osta
wp_post_id: none (publish blocked)
