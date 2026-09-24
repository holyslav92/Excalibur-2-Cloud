# Assembled scout inputs — B33 slot 17 YEKT 2026-09-24

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-24  
**slot:** 17:00 Asia/Yekaterinburg  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild_only  
**dzen_rf_pack:** true

## HARD anti-dupe (recent live — DO NOT reuse mechanism)

User/conductor blocklist 2026-09-24:
- matkapital SFR escrow 7d before DDU
- kindergarten render vs declaration 5d before DDU
- child 7 years on DDU day family mortgage
- KP forest vs neighbor fence
- furniture partner pack 4d before DDU
- co-borrower refused escrow 3d
- show-room ceilings vs explication
- house rotation windows vs magistral
- declaration delivery shift bank cut mortgage
- cellar separate DDU
- down payment 15→25% 5d before DDU
- terrace on visualization only

Also avoid all clusters in `memory/scout/used-clusters.json` (30d).

## Proposed lock (pre-checked 2026-09-24)

- **cluster_id:** `newbuild_last_floor_bank_mortgage_decline_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** Семья с детьми выбирает квартиру на **последнем этаже** новостройки в Тюмени (вид, тишина, нет соседей сверху). В брони и у менеджера зафиксировано: «ипотека на любой этаж, одобрение есть». За **4 дня до подписания ДДУ** ипотечный менеджер банка присылает отказ/аннулирование одобрения: внутренняя политика банка **не кредитует последние этажи** (или только с увеличенным взносом). Застройщик предлагает «пересядьте на этаж ниже за тот же чек» — вид и планировка другие. Семья **останавливает сделку до эскроу**; бронь частично удержана (composite casus, без имён ЖК/банка в handoff как репортаж).
- **why_newbuild_not_secondary:** Сюжет только в цепочке покупки квартиры в строящемся доме: бронь, одобрение ипотеки под ДДУ, эскроу, политика банка по этажности объекта. Нет продавца вторички, ЕГРН, наследников, опеки, соседской доли.
- **title draft (H1 direction):** «За 4 дня до ДДУ в Тюмени банк снял ипотеку на последний этаж — в брони менеджер писал „любой этаж“»
- **slug:** `za-4-dnya-do-ddu-bank-snyal-ipoteku-na-poslednij-etazh-menedzher-obeschal-lyuboj`
- **article_dir:** `memory/blog/articles/B33-za-4-dnya-do-ddu-bank-snyal-ipoteku-na-poslednij-etazh-menedzher-obeschal-lyuboj`
- **comment_magnet_angle:** «Если банк режет последний этаж за несколько дней до ДДУ, вы бы согласились на этаж ниже, чтобы не потерять бронь, или разорвали бы бронь сразу?»
- **scout_helper.py --check-query:** PASS 2026-09-24 (anti_dupe_hard PASS, topic focus PASS)
- **story_dup.py --text:** PASS 2026-09-24
- **formula_spam_check:** last3 live = matkapital/SFR escrow; kindergarten render vs PD; child 7y family mortgage — **different** mechanism (bank floor policy vs promo/docs/age)

## Wordstat MCP-KV (live 2026-09-24)

wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| phrase | regions | volume |
|--------|---------|-------:|
| новостройки тюмень | 55,11176 | 4294 |
| новостройки тюмень | 225 (compare) | 8168 |
| купить новостройку в тюмени | 55,11176 | 897 |
| квартиры в тюмени новостройки | 55,11176 | 1040 |
| ипотека в тюмени на новостройки | 55,11176 | 26 |
| ипотека последний этаж | 55,11176 | empty/<5 |
| дду новостройка тюмень | 55,11176 | empty |

**wordstat_rework:** probe «ипотека последний этаж» 55,11176 → empty (too weak alone) → probe «ипотека в тюмени на новостройки» 26 (weak) → anchor buyer spine **«новостройки тюмень»** 4294 (55+11176) with mechanism last-floor bank policy in H1/body.

**final P0:** «новостройки тюмень» regions 55,11176,compare225 freq **4294** (55+11176) / RU compare **8168** (225)

**klyshin_hook:** none (fresh Tyumen casus without Klyshin)

## dzen_casus_shape: PASS

- event: семья выбрала последний этаж в новостройке Тюмени, ипотека предварительно одобрена
- risk: банк аннулирует одобрение из‑за политики по последним этажам; смена этажа = другая квартира и платёж
- time: за 4 дня до назначенного подписания ДДУ
- finale: отказ от ДДУ до эскроу; частичная потеря брони; семья ищет другой объект с письменным подтверждением этажности в банке

## signal_urls

- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A (optional signal only — hook not used)

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`, `wordstat:` line with mcp_kv live.
