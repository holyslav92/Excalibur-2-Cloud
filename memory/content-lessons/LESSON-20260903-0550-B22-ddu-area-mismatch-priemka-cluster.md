## LESSON-20260903-0550-B22-ddu-area-mismatch-priemka-cluster
status: proposed
topic_id: B22
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md
  finding: new cluster `newbuild_ddu_area_mismatch_overpay_tyumen`; story_dup PASS vs B21 (кладовка/другое помещение), B12 (срок сдачи/эскроу), B20 (смена юрлица), wet screed priemka (дефекты стяжки); plot = площадь в ДДУ > обмеры БТИ/акта приёмки → переплата за метры → застройщик отказывает в перерасчёте.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: weak on-plot P0 «площадь квартиры дду» 11, «площадь квартиры новостройка» 7; secondary «приемка квартиры в новостройке тюмень» 35; **rework → final P0 «купить новостройку в тюмени» regions 55+11176 freq 857** (compare RU225 1884).
- artifact: quality-bar-9.json
  finding: `all_pass: true`, `comment_magnet_question: true`, `no_tldr_opening: true`, `spine_once_no_recap: true`, word_count 2115, 6 H2, 7 inline figures, 3 sibling interlinks.
- artifact: wp-publish-result.json
  finding: publish PASS post **9562**, live-page PASS, 7 inline uploads (9564–9570), featured 9563, categories dokumenty-i-oformlenie / riski-sdelki / pokupka-kvartiry.
- artifact: description-brief.json
  finding: Dzen card PASS — not_equal_title, klyshin_case_hook rhythm; comment magnet angle «сверяете метры до акта».
- artifact: stylo-report.json
  finding: stylo_pass true (delta 1.95 < 2.85), sol_rewrite_applied false; lead 46 words (z=+1.81 vs gold) — within gate, no Sol retry.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (post-publish day 0, no behavioral baseline)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish day 0)

### Keep
- Wordstat rework: при слабом area P0 (площадь дду 11) — buyer jargon «купить новостройку в тюмени» 857 как demand spine; «приемка квартиры в новостройке тюмень» 35 — secondary local, не P0.
- Plot differentiation: площадь ДДУ vs обмеры приёмки vs B21 кладовка, B12 срок сдачи, B20 юрлицо, wet screed defects — отдельные priemka/DDU кластеры.
- Engagement bomb: news-casus приёмка + agency ending (акт с замечанием, не «бегите»); comment magnet про сверку метров до подписи.
- Fresh Tyumen newbuild casus без Klyshin (scout klyshin_hook: none).

### Change
- Scout: cluster `newbuild_ddu_area_mismatch_overpay_tyumen` lock в used-clusters (content-learner B22).
- После Metrika credentials: cohort `cluster:newbuild_ddu_area_mismatch_overpay_tyumen` vs B21 cellar / wet screed priemka siblings.

### Never again
- Смешивать B22 с кладовкой по ДДУ (B21) или сменой юрлица/эскроу (B20).
- Drop hook при weak Wordstat «площадь квартиры дду» без rework на newbuild buyer jargon.
- Priemka wet screed defects как тот же plot что area mismatch.

### Proposed apply
- `memory/scout/used-clusters.json`: lock `newbuild_ddu_area_mismatch_overpay_tyumen` until 2026-10-03 (B22 ledger).
- Scout story-cluster registry entry (human): required_groups площадь/ДДУ + обмеры приёмки + отказ перерасчёта.

### Durable applied
- memory/scout/used-clusters.json — добавлен cluster row B22 (content-learner 2026-09-03); rollback: удалить row при erroneous lock

### Resolution
status: recorded
article_dir: memory/blog/articles/B22-v-tyumeni-ploschad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry
wp_post_id: 9562
