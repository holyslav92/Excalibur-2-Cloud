# Scout inputs — 2026-08-27 run (YEKT slot 2)

## Run context
- date: 2026-08-27 (четверг)
- tenant: The Риэлтор / Святослав Шакин / Тюмень
- topic_id candidate: B11
- dzen_rf_pack: true — соблюдать shared/dzen-content-rules.md + rf-blocked-entities.json

## wordstat_preflight
- MCP-KV wordstat_get_user_info: OK (Yandex Cloud API, folder b1g6bq34gkivjj20be06)

## Klyshin live signal (2026-08-27)
- https://t.me/klyshin_A — свежие посты:
  - «Клиенты все чаще готовы купить плохую квартиру» (усталость на рынке)
  - «Теперь при покупке квартиры придется проверять еще и повестки?»
  - «Не знаете, что посмотреть на выходных? Посмотрите, как люди законно теряют квартиры» — видео 5 схем пост-покупки
  - «Нотариус не спасает от мошенников» — исследование 40% сделок
- hook_id: five_court_schemes (angle: двойная продажа / два договора на одну квартиру)
- original hook: «5 схем — квартиру забирают судом после покупки» → локализованный casus: двойная продажа

## External signals (≥2 URLs)
1. https://t.me/klyshin_A — пост про 5 схем / потерю квартиры после покупки
2. https://dzen.ru/holyslav — канал «Советы от риелтора» (engagement champion: casus с финалом)
3. Live WP anti-dup window checked via excalibur_blog_today.py

## Wordstat live (MCP-KV, regions 55+11176, compare 225)

### Probes tried
| probe | Tyumen 55+11176 | RU 225 | note |
|-------|-----------------|--------|------|
| двойная продажа квартиры | API empty | 281 («двойные продажи квартир») | legal casus cluster |
| брачный договор квартира | 89 | — | alternate, not chosen |
| купить квартиру в тюмени | 22722 | 39950 | final P0 buyer spine |
| вторичка в тюмени | 6037 | — | secondary cluster |
| проверка квартиры перед покупкой | 3 | — | weak → rework |

### wordstat_rework log
- probe «двойная продажа квартиры» Tyumen empty → national 281 confirms buyer legal risk cluster
- rework «купить квартиру в тюмени» 22722 (RU225 39950) — demand spine под Tyumen casus
- rework «вторичка в тюмени» 6037 — secondary buyer intent

### final P0
- phrase: «купить квартиру в тюмени»
- volume: 22722 (regions 55+11176)
- compare_ru: 39950

## Dzen news-casus shape (PASS)
- event: продавец подписал два договора на одну квартиру в Тюмени
- risk: двойная продажа / аванс второму покупателю при живом первом договоре
- time: «за две недели до регистрации» / «через месяц после аванса»
- hero: покупатель №2, выписка «чистая», аванс внесён
- finale: суд вернул деньги первому / второй покупатель потерял аванс / регистрацию отменили
- comment_magnet_angle: «А вы бы внесли аванс, если выписка чистая, а риелтор продавца клянётся, что других покупателей нет?»

## Story-duplicate check (scout_helper PASS)
- query: «Квартиру продали дважды — второй покупатель потерял аванс в Тюмени»
- result: NO CANNIBALIZATION RISK + TOPIC FOCUS PASS

## Title draft (news headline, Klyshin rhythm)
**Квартиру продали дважды — второй покупатель в Тюмени потерял аванс**

## Forbidden overlaps (already published / live WP — DO NOT reuse)
- B02 расписка, B03 торги/дарение, B04 доверенность СВО, B05 скидка/бабушка, B06 автооценка, B07 наследство сын, B08 умершая жена, B09 ипотека ЕГРН, B10 телефонные мошенники/пожилой
- LIVE: tired buyer 4 months, summons registration stop, notary +70k, bankruptcy seller, matkapital children, clean extract half year

## Task for Derouter scout role
Write `.cursor/excalibur-blog-handoff.md` with:
- topic_id: B11
- slug suggestion
- title draft (as above or stronger news headline ≤70 chars)
- klyshin_hook line
- dzen_casus_shape: PASS with all 5 elements
- comment_magnet_angle
- wordstat_rework + wordstat lines (live frequencies only)
- signal_urls
- brief angle for Research (facts = Tyumen / Shakin, not Moscow copy)
