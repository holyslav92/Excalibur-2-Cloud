# Scout inputs — B34 slot 17:00 YEKT 2026-09-30

**CRITICAL:** You run inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). Write **only** the Scout handoff markdown body — no tool calls, no BLOCKER, no SCOUT BLOCK.

**OWNER SLOT OVERRIDE (HARD):** `shared/slot-rubric-lock.md` + `shared/tenant-config.json` → `topic_market_focus: rubric_per_slot`. This run is slot **17:00 = vtorichka ONLY**. Legacy newbuild-only bullets in SKILL are **superseded** for this slot. Secondary casus is **required**, not forbidden. `excalibur_blog_topic_focus.py` and `scout_helper.py` already **PASS** for this title.

**run_date:** 2026-09-30  
**slot:** 17:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka  
**tenant:** The Риэлтор — Святослав Шакин, tymenrieltor.ru  
**topic_market_focus:** rubric_per_slot  

## Trend Radar (slot vtorichka)

`memory/blog/trend-radar/trend-radar.json` (vtorichka angles):
- **viral_mechanism:** almost lost перед ключами/деньгами (Окулов PRO загородный дом)
- **energy mirror:** paper looked clean → hidden legal bomb before money on table

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK
- `scout_helper.py --check-query` → **ANTI-DUPE HARD PASS** 2026-09-30
- `excalibur_blog_topic_focus.py` → PASS (allow_hit=аванс)
- Avoid: B33 utility electricity debt; LIVE bailiff 4 days; darstvennaya 7 days; frozen cluster retitle only — **new** plot: bankruptcy **before** advance while ЕГРН looked clean
- **cluster_id (new):** `secondary_seller_bankruptcy_finmanager_before_advance_tyumen`

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** За 6 дней до аванса в Тюмени на вторичке всплыло банкротство продавца — семья не перевела деньги
- **slug:** za-6-dnej-do-avansa-v-tyumeni-na-vtorichke-vspyllo-bankrotstvo-prodavca-semya-ne-perevela-dengi
- **article_dir:** memory/blog/articles/B34-za-6-dnej-do-avansa-v-tyumeni-na-vtorichke-vspyllo-bankrotstvo-prodavca-semya-ne-perevela-dengi
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — «выписка чистая», пока не пришло уведомление финуправляющего
- **vtorichka_mechanism:** Пара покупает трёшку на вторичке в Тюмени (ипотека одобрена, аванс 420 000 ₽ через 6 дней). Продавец-физлицо, выписка ЕГРН без обременений, справка из суда «дел нет». За **6 дней** до аванса риэлтор проверяет **ЕФРСБ** / запрос финуправляющему — всплывает **введённая процедура банкротства** продавца (заявление подано **12 дней назад**, в реестре уже есть). Риск оспаривания сделки / включения квартиры в конкурсную массу. Семья **не переводит аванс**, сделку останавливает до договора
- **why_vtorichka_not_newbuild:** вторичка, ДКП, продавец-физлицо, банкротство продавца, аванс — без ДДУ/эскроу/застройщика
- **story_dup_check:** PASS — distinct from seller_bankruptcy_finmanager_clean_egrn (post-sale year-later plot in ledger); not B09 EGRN line; not utility debt B33
- **h1_fingerprint_check:** PASS — «6 дней + аванс + банкротство продавца» distinct from last-3 vtorichka (пристав, дарственная, аренда в ЕГРН)
- **formula_spam_check:** PASS — last3 vtorichka WP: bailiff, darstvennaya, registered rent — new mechanism bankruptcy **before** advance

## Dzen news-casus shape: PASS

- **event:** семья с двумя детьми выбрала трёшку, торг согласован, банк одобрил ипотеку
- **risk:** сделка может быть оспорена; аванс 420k «зависнет»; квартира уйдёт в конкурсную массу
- **time:** за 6 дней до планового аванса на безопасный счёт
- **finale:** аванс не перевели; продавец просил «давайте подпишем до заседания» — отказ; пошли искать объект с проверкой ЕФРСБ **до** аванса
- **comment_magnet_angle:** «Если за неделю до аванса всплывает банкротство продавца, а риэлтор говорит «ЕГРН же чистая» — вы бы рискнули авансом или ушли сразу?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-09-30)

| probe | regions | freq |
|-------|---------|-----:|
| купить квартиру в тюмени вторичка | 55,11176 | 3305 |
| покупка квартиры банкротство продавца | 55,11176 | 16 |
| как проверить продавца квартиры на банкротство | 55,11176 | 13 |

**wordstat_rework:** bankruptcy phrases weak alone → spine P0 **«купить квартиру в тюмени вторичка»** 3305 + bankruptcy mechanism in H1/body  
**final P0:** «купить квартиру в тюмени вторичка» regions 55,11176 freq **3305**

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend energy: https://dzen.ru/a/Zw9N_lUREDllN79D

Output full handoff per SKILL with: `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `needs_scout: false`, `wp_category_slugs`: vtorichka-i-riski, proverka-pered-pokupkoj.
