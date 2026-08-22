# Scout inputs — 2026-08-22 (B08)

## Director preflight
- wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, folder b1g6bq34gkivjj20be06)
- regions: Тюмень=55, Тюменская область=11176, compare RU=225
- published ledger: B02–B07 (see shared/published-articles.md)
- live WP recent: EGRN daily «строка после которой аванс нельзя» (2026-08-22) — longform B08 = **ипотека + отмена регистрации**, другой финал и plot
- scout_helper --check-query: PASS (no story duplicate)

## Klyshin hook (selected)
- hook_id: `pre_advance_check`
- original: «Сначала проверка. Потом аванс.» — предавансовая проверка ЕГРН до аванса
- angle: новость-казус — в выписке ЕГРН пропущена строка обременения; ипотека одобрена, регистрацию отменили
- signal: https://t.me/klyshin_A (пост 2026-08: отчёт 2900 ₽, список документов до аванса)
- secondary signals: https://dzen.ru/holyslav | site blog | https://t.me/holyslav92

## Dzen news-casus shape (PASS)
- event: «сделка с ипотекой дошла до Росреестра — регистрацию отменили»
- risk: «скрытая строка в выписке ЕГРН / обременение»
- time: «через полгода после одобрения ипотеки» / «на этапе регистрации»
- victim: «покупатель проверил документы и банк одобрил — казалось безопасно»
- finale: «Росреестр отменил регистрацию, сделку приостановили»

## Wordstat live (MCP-KV, regions 55+11176)
| probe | total shows |
|-------|-------------|
| «проверка квартиры перед покупкой» | 9 |
| «выписка егрн квартира» | 246 |
| «егрн» | 7543 |
| «выписка из егрн» (similar) | 2648 |
| «мошенники при покупке квартиры» | 1 (rejected — weak) |

### Rework log
1. probe «проверка квартиры перед покупкой» → 9 (слабо)
2. rework «выписка егрн квартира» → 246
3. rework «егрн» → 7543 (buyer spine)
4. final P0 «купить квартиру в тюмени» → **22880** (RU225 **40230**)

## Title draft (news headline, Klyshin rhythm)
**Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка**

## topic_id
B08

## Slug hint
ipoteku-odobrili-a-registraciyu-otmenili-v-vypiske-visela-odna-stroka

## Runtime note (HARD)
Ты вызываешься **из** `excalibur_blog_derouter_opus_chat.py` — shell уже выполнен дирижёром.
Твой ответ **станет** содержимым `.cursor/excalibur-blog-handoff.md` (скрипт пишет файл).
**Не отказывайся** и не проси запустить скрипт. Выведи **только** markdown handoff ниже.

## Task for Derouter scout role
Output handoff markdown with all required fields:
- topic_id B08
- title draft
- external_signal summary
- signal_urls (≥2)
- klyshin_hook line
- dzen_casus_shape: PASS with event/risk/time/finale
- wordstat_rework line with probes and final P0
- wordstat line with regions and frequencies
- short angle for Research (Тюмень, Святослав Шакин facts)
