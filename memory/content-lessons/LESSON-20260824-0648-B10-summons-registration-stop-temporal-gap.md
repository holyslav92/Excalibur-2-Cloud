## LESSON-20260824-0648-B10-summons-registration-stop-temporal-gap
status: proposed
topic_id: B10
category: structure
confidence: low

### Evidence
- artifact: assembled-title-inputs.md#klyshin_hook + title-brief.json
  finding: hook `summons_registration_stop` — «повестка → стоп регистрации»; casus = чистая ЕГРН на день проверки, но приостановление Росреестра **между авансом и регистрацией** (реестр повесток, 20 дней неявки продавца). Anti-dup vs B01 (строка в ЕГРН **до** аванса) и B09 (обременение **уже в** ЕГРН).
- artifact: quality-bar-9.json — comment_magnet_question PASS, word_count 2562, interlink 4 siblings
- artifact: none (skipped under human-first-v2) — content-evidence-report.json отсутствует
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID absent)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (post-publish, no behavioral cohort)

### Keep
- Klyshin hook `summons_registration_stop` как buyer P0 spine: «купить квартиру в тюмени» 22753 + stickers «реестр повесток» 3675 / «запрет на регистрационные действия» 423.
- Comment magnet (точная формулировка из handoff): «Нужно ли теперь запрашивать выписку из реестра повесток у продавцов-мужчин — или это уже паранойя?»
- Temporal-gap framing: «выписка — фото минуты» vs «Росреестр смотрит в момент подачи» — не чеклист, news-casus.

### Change
- Scout/Title: при rework слабого «повестка регистрация» (3) → поднимать через «реестр повесток» (3675), не drop casus.
- Writer/Sol: явно контрастировать B09 (обременение в выписке) и B10 (чистая выписка + зазор до регистрации).

### Never again
- Не сводить тему к «всем мужчинам справка из реестра повесток» — только договорной риск аванса и временной разрыв проверок.
- Не дублировать B01/B09 angle без temporal-gap кластера.

### Proposed apply
- Зафиксировать в scout handoff template: для `summons_registration_stop` обязательный anti-dup блок vs B01/B09.
- После Metrika ingest — проверить retention/scroll на H2 «выписка — фото минуты» (гипотеза, не причинность).

### Durable applied
- none (первый именованный content run; Writer prompt не трогаем)

### Resolution
status: recorded
article_dir: memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-po-povestke
wp_post_id: 9121
permalink: /blog/vtorichka-i-riski/avans-vnesli-registraciyu-priostanovili-po-povestke/
