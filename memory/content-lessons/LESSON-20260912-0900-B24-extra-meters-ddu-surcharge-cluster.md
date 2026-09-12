## LESSON-20260912-0900-B24-extra-meters-ddu-surcharge-cluster
status: proposed
topic_id: B24
category: geo
confidence: low

### Evidence
- artifact: memory/scout/assembled-scout-inputs.md, research-notes.md
  finding: new cluster `newbuild_ddu_extra_meters_surcharge_dispute_tyumen`; story_dup PASS vs live and frozen clusters; fresh Tyumen newbuild casus.
- artifact: scout Wordstat log (assembled-scout-inputs.md)
  finding: final P0 «новостройки тюмень» regions 55+11176 freq **4583** (compare RU225 **8705**); secondary buyer query «купить новостройку в тюмени от застройщика» **453**; exact niche «доплата за квадратные метры в новостройке» **29** (RU225).
- artifact: research-notes.md
  finding: 214-ФЗ ст. 5 (цена и основания перерасчёта), Приказ Росреестра № П/0393 (коэффициенты лоджий 0,5 и балконов 0,3), ЖК РФ ст. 15.
- artifact: wp-publish-result.json
  finding: publish PASS post **10109**, live-page PASS, 7 inline uploads, categories=36,58,54.
- artifact: quality-bar-9.json
  finding: `comment_magnet_question: true`, `spine_once_no_recap: true`, `word_count` 1554 (target 1400–1600), `no_composite_disclaimer: true`, `all_pass: true`.
- artifact: stylo-report.json
  finding: `stylo_pass: true`, `sol_rewrite_applied: true` (delta 2.81 <= 2.85).
- artifact: cover/cover_qa.json
  finding: grsai solo cover attempt 1 PASS, `cover_md5` c1d721ccdb2ff45eac56819f6c0117ee.
- artifact: none (skipped under human-first-v2)
- metrika_signal: none — post-publish baseline

### Named blockers
- EVIDENCE_SKIPPED
- LOW_SAMPLE (post-publish, no behavioral baseline)

### Keep
- Wordstat demand spine: P0 «новостройки тюмень» (4583) как крепкий региональный якорь спроса при нишевом казусе доплаты за метры.
- Dzen news-casus: завершённый казус (выставили 420 тыс., заблокировали ключи, лазерный дальномер показал ошибку лоджии и перегородок, претензия аннулировала счёт).
- Comment magnet: «Застройщик требует 420 тысяч за лишние метры перед ключами — вы бы пошли на независимый обмер или взяли кредит, чтобы не срывать переезд?»
- Grsai solo cover: быстрый чистый проход attempt 1 с фиксацией студийного портрета Святослава и правильной версткой шрифтов.

### Change
- Scout `used-clusters.json`: зафиксировать `newbuild_ddu_extra_meters_surcharge_dispute_tyumen` на 30 дней.

### Never again
- Путать общую площадь жилья (без лоджий по ЖК РФ) и приведённую площадь ДДУ (с понижающими коэффициентами 0,5/0,3).

### Proposed apply
- Scout `used-clusters.json`: cluster_id `newbuild_ddu_extra_meters_surcharge_dispute_tyumen`.

### Resolution
status: recorded
article_dir: memory/blog/articles/B24-v-tyumeni-zastrojschik-potreboval-doplatu-420-tysyach-za-lishnie-metry-klyuchi-ne-otdali
wp_post_id: 10109
