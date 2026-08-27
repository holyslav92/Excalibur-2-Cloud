## LESSON-20260827-1328-B11-notary-cooperative-share-casus
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: memory/scout/klyshin-topic-bank.json#notary_not_shield_70k
  finding: Scout B11 = fresh Klyshin 27.08 (кооператив/пай/супружеская доля); hook «нотариус всё проверил — не броня»; Wordstat rework 25→3→181→22722; final P0 «купить квартиру в тюмени» 22722; отклонены summons, matkapital+opeka, tired_buyer, live notarius+sud (другой plot).
- artifact: research-notes.md
  finding: overlap guard vs B07/B08 — отличается кооператив + пай + 18-летнее нотариальное оформление + невыделенная супружеская доля + неясные наследники; финал — аванс на паузе.
- artifact: description-brief.json
  finding: Klyshin case rhythm, geo Тюмень, `not_equal_title: true` — Дзен-карточка про кооператив/наследство, не дублирует H1 про супружескую долю.
- artifact: quality-bar-9.json
  finding: all_pass — word_count 2596, h2 8, inline_figures 7, sibling_interlinks 4; `no_tldr_opening`, `comment_magnet_question`, `early_cta_tg_max_only`, `interlink_siblings_2_4` PASS.
- artifact: interlink-plan.json
  finding: outbound B02 (расписка), B07 (наследство сын), B08 (умершая жена), B09 (ипотека/ЕГРН) — inheritance/risk cluster; inbound planned B06, B04, B09.
- artifact: link-verify.json
  finding: 11 links, verdict pass, 0 failed.
- artifact: wp-publish-result.json
  finding: post 9214 published, 7 inline uploads, live-page PASS.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER; нет CTR/retention для post 9214

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, нет behavioral ingest)

### Keep
- News-casus shape: кооператив + пай в браке + нотариус 18 лет назад + наследники **до аванса** — stakes без how-to checklist.
- Klyshin hook `notary_not_shield_70k` локализован в cooperative-share plot (не дублирует B06 «нотариус +70k» загород).
- Cover sticky «Проверка не закончена» + comment-magnet угол «кто реально закрыл цепочку».
- Inheritance-cluster interlink (B02/B07/B08/B09) для vtorichka-i-riski — контекстные sibling, не SEO-хвосты.
- Sol 4-chunk merge PASS (derouter-opus-stamp-sol-part1..4) на longform 2596 слов — chunk path работает после B10.

### Change
- Scout bank: tag `cooperative_share_inheritance` + log `comment_magnet_angle` для notary-shield casus — B11 angle «справка о пае ≠ закрытая цепочка».
- Wordstat niche spine «квартира наследство продажа» 181 — держать в stickers/H2, не в hook title (P0 buyer «купить квартиру в тюмени»).

### Never again
- Drop cooperative-share casus ради generic «проверка перед покупкой» чеклиста.
- Reuse B06 загородный +70k plot под тем же hook_id без anti-dup guard.
- Выводить engagement из quality-bar PASS без Metrika cohort (причина не подтверждена).

### Proposed apply
- Scout klyshin bank: tag `cooperative_share_inheritance` + sibling interlink defaults → B02/B07/B08/B09 для Tyumen inheritance P0.
- После Metrika ingest для 9214 — re-evaluate confidence medium/high если retention/CTA сигналы совпадают с inheritance-cluster cohort.

### Durable applied
- none (один run по casus-cluster, нет Metrika; scout tag — proposed only)

### Resolution
status: recorded
article_dir: memory/blog/articles/B11-notarius-18-let-nazad-vse-proveril-v-tyumeni-pered-avansom-vsplyla-supruzheskaya
wp_post_id: 9214
