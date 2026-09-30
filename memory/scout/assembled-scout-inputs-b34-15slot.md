# Scout inputs — B34 slot 15:00 YEKT 2026-09-30

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-30  
**slot:** 15:00 Asia/Yekaterinburg  
**slot_rubric:** vtorichka (вторичка Тюмень)  
**tenant:** The Риэлтор — Святослав Шакин, tymenrieltor.ru  
**topic_market_focus:** rubric_per_slot  
**dzen_rf_pack:** true (shared/dzen-content-rules.md + rf-blocked-entities.json read)

## Trend Radar (slot vtorichka)

`memory/blog/trend-radar/trend-radar.json` (2026-09-30, slot 15:00):
- **viral_mechanism:** almost lost перед ключами/деньгами (Life: спрос на вторичку с 1 октября; Окулов PRO: «легально кидают» на загородном доме)
- **energy mirror:** выписка и осмотр «чистые» → внезапный стоп перед авансом, когда деньги уже на столе

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → OK (15 active locks)
- **Avoid today/recent:** дарственная (2026-09-29), аренда 3 года в ЕГРН (2026-09-29), B33 долг за свет 186k, newbuild слоты 09/12 сегодня
- Frozen/active clusters: egrn_line_blocks_advance (B09), bank_appraisal_below_ddu_price (newbuild), seller_bankruptcy, matkapital/opieka, communal share, forged consent, etc.
- `EXCALIBUR_BLOG_SLOT=15:00 scout_helper.py --check-query` PASS 2026-09-30
- `story_dup.py --text` PASS 2026-09-30

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** В Тюмени за 4 дня до аванса пристав запретил регистрацию вторички — продавец умолчал
- **slug:** za-4-dnya-do-avansa-pristav-zapretil-registraciyu-vtorichka-tyumen-prodavec-umolchal
- **article_dir:** memory/blog/articles/B34-za-4-dnya-do-avansa-pristav-zapretil-registraciyu-vtorichka-tyumen-prodavec-umolchal
- **cluster_id (new):** secondary_fssp_registration_ban_before_advance_tyumen
- **slot_rubric:** vtorichka
- **viral_mechanism:** almost lost перед авансом — «всё согласовано», пока вечером не открыли сведения ФССП / запрет Росреестра
- **vtorichka_mechanism:** Пара с одобренной ипотекой на вторичку в Тюмени. Продавец-физлицо, ДКП на нотариусе назначен через 4 дня, аванс 400 тыс. готовят к внесению на безопасный счёт. Свежая выписка без ипотечного обременения, согласие супруги есть. Риэлтор по расширенному пакету запросил **сведения о наличии исполнительных производств** и **статус регистрационных действий** — всплыл **запрет на регистрацию** (пристав, долг продавца ~620 тыс.). Росреестр не зарегистрирует переход права, пока запрет не снят. Семья **не внесла аванс**, сделку остановили; продавец обещал «снять за два дня» — покупатели отказались ждать без гарантий
- **why_vtorichka_not_newbuild:** вторичка, ДКП, аванс, пристав/ФССП, регистрация перехода права — без ДДУ, эскроу, застройщика, брони
- **story_dup_check:** PASS — не egrn_line (не строка обременения ипотеки B09), не банкротство продавца (другой механизм), не ЖКУ/186k B33, не дарственная/аренда ЕГРН
- **h1_fingerprint_check:** PASS — «4 дня + аванс + пристав + запрет регистрации»
- **formula_spam_check:** PASS — last3 published B32 escrow requisites, B33 utility debt, B31 insurance DDU; механизм ФССП/запрет регистрации новый

## Dzen news-casus shape: PASS

- **event:** семья выбрала вторичку, торг согласован, банк одобрил ипотеку, нотариус назначен
- **risk:** аванс + ипотека «в воздухе», регистрация заблокирована запретом пристава
- **time:** за 4 дня до планового внесения аванса
- **finale:** аванс не внесли; продавец давил сроками — отказались; пошли с полной проверкой ФССП/запретов **до** аванса на следующем объекте
- **comment_magnet_angle:** «Если перед авансом всплывает запрет пристава, а продавец клянётся «снимут за два дня» — вы бы внесли аванс или развернулись?»

## Klyshin hook

- **klyshin_hook:** none (original Tyumen secondary casus)

## Wordstat MCP-KV (live 2026-09-30)

| probe | regions | freq |
|-------|---------|-----:|
| wordstat_get_user_info | — | OK |
| купить квартиру в тюмени вторичка | 55,11176 | 3305 |
| купить квартиру в тюмени вторичка (compare RU) | 225 | 6219 |
| разрешение опеки на продажу квартиры | 55,11176 | 80 |
| согласие супруга на продажу квартиры | 55,11176 | 56 |
| как проверить продавца на банкротство при покупке квартиры | 55,11176 | 13 |
| банкротство продавца квартиры | 55,11176 | 24 (aggregate probe) |

**wordstat_rework:** probe «запрет на регистрацию квартиры пристав» — API empty/malformed; probe «арест квартиры при покупке» — empty → spine P0 **«купить квартиру в тюмени вторичка»** 3305 (55+11176) + ФССП/запрет регистрации в H1/casus  
**final P0:** «купить квартиру в тюмени вторичка» regions 55,11176 freq **3305** (compare RU 225: **6219**)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend energy: https://dzen.ru/a/aqcTwkjUgT5jdBjX (спрос на вторичку); https://dzen.ru/a/Zw9N_lUREDllN79D (almost lost)

Output full handoff per SKILL with: `slot_rubric: vtorichka`, `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `needs_scout: false`, `wp_category_slugs` suggestion (vtorichka-i-riski, proverka-pered-pokupkoj).
