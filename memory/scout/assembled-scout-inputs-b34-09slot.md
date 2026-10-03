# Scout inputs — B34 slot 09:00 YEKT 2026-10-03

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-03  
**slot:** 09:00 Asia/Yekaterinburg  
**slot_rubric:** novostroyki (новостройки Тюмень ONLY)  
**tenant:** The Риэлтор — Святослав Шакин  
**topic_market_focus:** newbuild_focus_lock  
**dzen_rf_pack:** true (dzen-content-rules + rf-blocked-entities read)

## Trend Radar (slot novostroyki)

`memory/blog/trend-radar/trend-radar.json` (2026-10-03 09:00):
- **viral_mechanism:** договор vs реальность (СИЛА ПРАВА 231k views — «потерять квартиру из-за сдачи в аренду» energy)
- **energy mirror for newbuild:** paper_clean_then_broke — в ДДУ/брони одна площадь, на приёмке по БТИ другая цифра и доплата до ключей
- **NOT copying:** аренда как главный сюжет (Oct 1 live: объявление на сдачу до эскроу — другой cluster); mirror **stakes/договор≠факт**, plot = приёмка новостройки

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 13 active locks OK
- Closed newbuild clusters to avoid: booking_expired, acceptance_defects_penalty, cellar_paid B21/Oct2 190k, escrow rent listing Oct1, school declaration, deposit 35/89 mismatch, bank appraisal, keys delay penalty, etc.
- `scout_helper.py --check-query` PASS 2026-10-03
- `excalibur_blog_topic_focus.py` PASS (allow_hit=тюмен)
- `story_dup.py` — distinct cluster `newbuild_bti_area_surcharge_before_keys_tyumen`

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** В Тюмени на приёмке БТИ добавила 4 кв.м — застройщик потребовал доплату 380 тысяч, семья отложила ключи
- **slug:** v-tyumeni-na-priemke-bti-dobavila-4-kvm-doplatu-380-tysyach-semya-otlozhila-klyuchi
- **article_dir:** memory/blog/articles/B34-v-tyumeni-na-priemke-bti-dobavila-4-kvm-doplatu-380-tysyach-semya-otlozhila-klyuchi
- **cluster_id (new):** newbuild_bti_area_surcharge_before_keys_tyumen
- **slot_rubric:** novostroyki
- **newbuild_mechanism:** Семья с двумя детьми покупает трёшку в новостройке Тюмени по ДДУ (ипотека одобрена, эскроу открыт). В договоре и брони — 78,2 кв.м. На приёмке замер БТИ показывает **82,0 кв.м** (+3,8 округлённо «4 кв.м» в заголовке). Застройщик выставляет доплату **380 000 ₽** по цене кв.м из ДДУ и не отдаёт ключи без оплаты/подписания акта с новой площадью. Банк предупреждает: без акта приёмки ипотечный график «висит», неустойка за просрочку ключей тикает с другой стороны. Семья **не подписала акт в тот день**, зафиксировала расхождения, отложила ключи и пошла сверять проектную документацию и порядок доплаты (composite Tyumen casus)
- **why_newbuild_not_secondary:** объект в строящемся/сданном ЖК по ДДУ, приёмка у застройщика, БТИ и акт ввода — не вторичный ДКП/ЕГРН продавца
- **story_dup_check:** PASS — not acceptance_defects_penalty (промёрзшая стена), not cellar paid option, not chistovaya B25, not BTI retitle of secondary
- **h1_fingerprint_check:** PASS — «приёмка + БТИ +4 кв.м + доплата 380» distinct
- **formula_spam_check:** PASS — last3 live newbuild mechanisms: paid cellar option 190k; presentation deposit 35 vs DDU 89; school year declaration vs ad — this is BTI area surcharge at keys

## Dzen news-casus shape: PASS

- **event:** семья приехала на приёмку с ипотекой и детьми, ожидала ключи
- **risk:** доплата 380k + двойной дедлайн (банк/неустойка застройщика)
- **time:** день приёмки, до подписания акта
- **finale:** акт не подписали в день приёмки; зафиксировали расхождение площади; договорились о повторной сверке с проектом — ключи отложили, не ушли в «тихую» доплату
- **comment_magnet_angle:** «Если на приёмке площадь выросла на 4 кв.м и просят доплату 380 тысяч — вы подписываете акт в тот же день или стопаете до сверки с ДДУ?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-10-03)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| probe | regions 55,11176 | freq |
|-------|------------------|-----:|
| бти новостройка | 55,11176 | 1 |
| дду новостройка | 55,11176 | 17 |
| приемка квартиры в новостройке тюмень | 55,11176 | 10 |
| купить новостройку в тюмени | 55,11176 | 908 |
| новостройки тюмень | 55,11176 | 4394 |
| compare купить новостройку в тюмени RU 225 | 225 | 1900 |

**wordstat_rework:** BTI-specific probes weak (1–17) → spine P0 **«новостройки тюмень»** 4394 (buyer demand Тюмень+область) + BTI/приёмка mechanism in H1  
**final P0:** «новостройки тюмень» regions 55,11176 freq **4394** (compare «купить новостройку в тюмени» 908 local / 1900 RU)

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- Trend energy (mechanics only): https://dzen.ru/a/YA7B343-ezstBMCs

Output full handoff per SKILL with all required single-line fields block, `anti_dupe_hard: PASS`, `dzen_casus_shape: PASS`, `slot_rubric: novostroyki`, suggest `wp_category_slugs`: proverka-pered-pokupkoj, novostroyki (or topic_defaults).
