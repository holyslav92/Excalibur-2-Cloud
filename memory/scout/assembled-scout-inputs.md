# Scout inputs — B34 slot 17:00 YEKT 2026-10-03

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed Trend Radar, Wordstat MCP-KV, anti-dupe shell gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-03  
**slot:** 17:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka (вторичка Тюмень)  
**tenant:** The Риэлтор — Святослав Шакин, tymenrieltor.ru  
**topic_market_focus:** rubric_per_slot  
**dzen_rf_pack:** true

## Trend Radar (slot vtorichka, 2026-10-03)

`memory/blog/trend-radar/trend-radar.json`:
- **viral_mechanism:** almost lost перед ключами/деньгами (Life «спрос на вторичку с 1 октября», 38k views — energy only, NOT calendar glue in H1)
- **energy mirror:** «бумага чистая» → всплывает скрытый правовой риск за день до денег на столе
- **secondary angle:** пенсионеры переоформляют жильё на родственников (юр.хаб) — mirror «дарение/переоформление» без копирования сюжета

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK
- `scout_helper.py --check-query` + `--check-story` → ANTI-DUPE HARD PASS (2026-10-03)
- `excalibur_blog_topic_focus.py` → PASS (allow_hit=аванс)
- Avoid: B33 utility electricity debt; today WP secondary — перепланировка, аренда на Авито; frozen clusters in used-clusters.json

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** За 4 дня до аванса в Тюмени всплыла дарственная полгода назад — банк остановил сделку
- **slug:** za-4-dnya-do-avansa-v-tyumeni-vsplyla-darstvennaya-polgoda-nazad-bank-ostanovil-sdelku
- **article_dir:** memory/blog/articles/B34-za-4-dnya-do-avansa-v-tyumeni-vsplyla-darstvennaya-polgoda-nazad-bank-ostanovil-sdelku
- **cluster_id (new):** secondary_recent_gift_deed_before_advance_tyumen
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — выписка ЕГРН чистая, пока банк не увидел свежую дарственную
- **vtorichka_mechanism:** Пара покупает трёшку на вторичке в Тюмени, ипотека одобрена, аванс через 4 дня. Продавец — единственный собственник по выписке. Риэлтор запрашивает цепочку оснований: **7 месяцев назад** квартира перешла по **дарственной** от матери. Банк (ипотечный мониторинг) фиксирует короткий срок владения + риск оспаривания дарения/претензии наследников → **снимает одобрение за 4 дня до аванса**. Покупатели **не вносят аванс**, пересобирают пакет с другим объектом
- **why_vtorichka_not_newbuild:** вторичка, ДКП, дарственная, аванс, банк на вторичке — без ДДУ/эскроу/застройщика
- **story_dup_check:** PASS — distinct from electricity debt B33, перепланировка, аренда-объявление, банкрот, ЕГРН-строка
- **h1_fingerprint_check:** PASS — «4 дня + аванс + дарственная полгода» unique
- **formula_spam_check:** PASS — last3 mix newbuild/secondary different mechanisms

## Dzen news-casus shape: PASS

- **event:** семья согласовала цену, осмотр прошёл, ипотека «зелёная»
- **risk:** дарственная <3 лет → банк боится оспаривания; аванс 400k на подходе
- **time:** за 4 дня до внесения аванса на безопасный счёт
- **finale:** аванс не внесли; продавец предлагал «подождём год» — покупатели ушли к объекту с длинной историей владения; agency: смотреть основание права **до** аванса
- **comment_magnet_angle:** «Если перед авансом всплывает свежая дарственная, а продавец клянётся «мама не оспорит» — вы бы всё равно внесли аванс?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-10-03)

| probe | regions | freq |
|-------|---------|-----:|
| купить квартиру в тюмени вторичка | 55,11176 | 3375 |
| дарственная на квартиру | 55,11176 | 755 |
| дарение недвижимости | 55,11176 | 219 |

**wordstat_rework:** spine P0 **«купить квартиру в тюмени вторичка»** 3375 + дарственная mechanism in H1  
**final P0:** «купить квартиру в тюмени вторичка» regions 55,11176 freq **3375**

## Handoff flags

- `needs_scout: false`
- `anti_dupe_hard: PASS`
- `dzen_casus_shape: PASS`
- `wp_category_slugs`: vtorichka-i-riski, proverka-pered-pokupkoj

Output full handoff per SKILL with all required fields.
