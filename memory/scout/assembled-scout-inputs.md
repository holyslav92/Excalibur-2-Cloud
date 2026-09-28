# Scout inputs — 2026-09-28 (B33)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-28 (YEKT weekday slot **17:00**)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — same day 2026-09-28 and recent live)

- NO escrow co-borrower (live 2026-09-28: банк потребовал созаёмщика за 3 дня до эскроу)
- NO second bathroom vanished from DDU appendix (live 2026-09-28)
- NO EИСЖС construction suspension before escrow (live 2026-09-28)
- NO studio → commercial in DDU (2026-09-27)
- NO townhouse → apartment in block (2026-09-27)
- NO installment vs price +340k (2026-09-27)
- NO UK fee 180k before keys (2026-09-27)
- NO elevator tech inspection before keys (2026-09-26)
- NO rent ban in DDU appendix (2026-09-26)
- NO parking benefit cancelled before keys (2026-09-26)
- NO KP lot lost 1 hour before DDU (2026-09-26)
- NO glazed balcony → cold balcony (2026-09-26)
- NO sqm 54→49 in DDU (2026-09-26 live)
- NO B25 chistovaya on acceptance / bare walls on keys (cluster acceptance_defects overlap risk)
- NO family mortgage revoked for child registration (scout_helper overlap with B29 reserved)
- NO frozen secondary clusters in used-clusters.json (30d)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 17 active locks (last_sync 2026-09-28)
- Live WP ~20 titles fetched 2026-09-28 (tymenrieltor.ru blog)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B33
- **title_draft:** В Тюмени за 4 дня до ДДУ застройщик привязал чистовую к подрядчику — без допсоглашения эскроу не открыли
- **slug:** za-4-dnya-do-ddu-zastrojschik-privyazal-chistovuyu-k-podryadchiku-bez-dop-soglasheniya-eskrou
- **article_dir:** memory/blog/articles/B33-za-4-dnya-do-ddu-zastrojschik-privyazal-chistovuyu-k-podryadchiku-bez-dop-soglasheniya-eskrou
- **cluster_id (new):** newbuild_mandatory_partner_finishing_before_escrow_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** Семья с двумя детьми берёт квартиру в новостройке Тюмени с обещанной чистовой в брони. За 4 дня до подписания ДДУ менеджер выдаёт **отдельный договор** на отделку только у «партнёрского» подрядчика (~520–580 тыс. ₽), не в цене ДДУ. Банк при ипотеке требует, чтобы обязательства по отделке не конфликтовали с залогом и эскроу: без подписанного допсоглашения или отказа от «партнёра» **счёт эскроу не открывают**, сделку останавливают до перевода денег
- **why_newbuild_not_secondary:** Цепочка только новостройки: бронь застройщика, проект ДДУ, навязанный подрядчик отделки, банк и эскроу. Нет продавца вторички, ЕГРН-рисков, наследников, опеки, бабушки или соседской доли
- **story_dup_check:** PASS — отличается от B25 (дефекты чистовой на приёмке), от сегодняшних созаёмщика/санузла/ЕИСЖС, от B31 страховки, от B32 чужого юрлица в реквизитах эскроу

## Dzen news-casus shape (target PASS)

- **event:** семья выбрала трёшку в новостройке Тюмени «с чистовой по прайсу»; в брони отметили пакет отделки и срок сдачи корпуса
- **risk:** отдельный договор с подрядчиком вне ДДУ = скрытый платёж сотни тысяч; банк может отказать в ипотеке/эскроу, если обязательства не прозрачны; отказ от «партнёра» грозит потерей брони
- **time:** за 4 дня до назначенного подписания ДДУ и открытия эскроу; вечером перед визитом в банк прислали проект допсоглашения
- **finale:** банк поставил сделку на паузу — эскроу не открыли; семья отказалась подписывать договор с подрядчиком; застройщик предложил «вернуть бронь 80%»; ДДУ не подписали, на эскроу денег нет
- **comment_magnet_angle:** «Если чистовую можно купить только у “партнёра” за полмиллиона сверх ДДУ — вы подпишете допсоглашение или снимете бронь, даже если квартира “горит”?»

## Klyshin hook

- **klyshin_hook:** none | original: none (свежий Tyumen newbuild finishing casus без Klyshin)

## Wordstat MCP-KV (live 2026-09-28)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4350 |
| новостройки тюмень | 225 (compare) | 8246 |
| купить новостройку в тюмени | 55,11176 | 891 |
| отделка новостройка тюмень | 55,11176 | 23 |
| новостройки тюмени от застройщика с отделкой | 55,11176 | 11 |
| ремонт новостроек тюмень | 55,11176 | 270 |
| планировка квартиры новостройка | 55,11176 | 29 |
| эскроу счет новостройка | 55,11176 | 1 |

**wordstat_rework log:**
- probe «отделка новостройка тюмень» 55,11176 → 23 (слабо для P0 alone)
- probe «новостройки тюмени от застройщика с отделкой» 55,11176 → 11 (слабо)
- probe «эскроу счет новостройка» 55,11176 → 1 (слабо)
- **rework:** demand spine «новостройки тюмень» + механика навязанной чистовой/подрядчика в H1 и теле casus
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4350 (55+11176) / 8246 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — реестр застройщиков, типовые условия ДДУ
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ (договор долевого участия, цена, приложения)
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md (Russian prose where appropriate) with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B33, title, slug, article_dir, signal_urls, research angles for Research role. Include slot 17:00 YEKT.
