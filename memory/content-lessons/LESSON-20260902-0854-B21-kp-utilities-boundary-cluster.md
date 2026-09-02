## LESSON-20260902-0854-B21-kp-utilities-boundary-cluster
status: proposed
topic_id: B21
category: geo
confidence: medium

### Evidence
- artifact: memory/scout/excalibur-blog-handoff.md
  finding: new cluster `newbuild_kp_land_boundary_utilities_denied_tyumen`; P0 Wordstat «коттеджные поселки тюмень купить дом» 59 (55+11176); `story_dup_check: PASS`; differentiated from B12 handover delay, B19 family mortgage, B20 legal entity change, wet screed acceptance.
- artifact: research-notes.md + assembled-research-inputs.md
  finding: plot firewall — дом в КП (не квартира ЖК), газ/вода у забора не подведены, мотивированный отказ + граница участка vs генплан; не путать с квартирной приёмкой.
- artifact: article.html + quality-bar-9.json
  finding: 6-H2 structure with seller-formula table («газ в посёлке» vs «точка на участке»), 4 sibling interlinks (B12/B19/B20/B09), comment magnet on act vs utilities; `word_count` 1994.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Newbuild-only via дом от застройщика в КП — не вторичка; Scout quad gate + dedicated cluster id в `used-clusters.json`.
- Comment magnet на подпись акта vs ожидание коммуникаций — engagement bomb для Дзен на загородном newbuild сюжете.
- Table H2 «формулировка продавца → что значит → чем проверяется» — utility без checklist-finale.

### Change
- Scout: при слабом Wordstat на KP-хвостах — rework с «коттеджный посёлок»/«купить дом» jargon (B21: 10→1831→59), не drop и не вторичка.
- Research/Writer: явный plot firewall в brief (не B12 перенос сдачи, не B20 смена юрлица, не wet screed квартира).

### Never again
- Retitle frozen secondary clusters под KP hook.
- Смешивать «газ в посёлке» и «ввод на участок» без таблицы формул в utility H2.

### Proposed apply
- `shared/scout-story-clusters.json` — cluster `newbuild_kp_land_boundary_utilities_denied_tyumen` live; Scout anti-repeat 30d lock validated.
- Human review: KP utilities как recurring Tyumen newbuild sub-cluster (дома от застройщика).

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B21-v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli
wp_post_id: 9523
