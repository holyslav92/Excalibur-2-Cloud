# Assembled scout inputs — B33 slot 17 YEKT 2026-09-20 (weekend owner request)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full `.cursor/excalibur-blog-handoff.md` per SKILL.md only.

**run_date:** 2026-09-20  
**slot:** 17:00 Asia/Yekaterinburg (Sunday weekend)  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild only

## HARD anti-dupe (avoid recent live)

Today 2026-09-20 already published: B30 переуступка 3 года, B31 страховка/одобрение, B32 эскроу чужое юрлицо — **do NOT** repeat «за N дней до ДДU/банк/эскроу» skeleton.  
2026-09-19 KP plots used: gas dates B28, ceiling B live, cadastre fence live — **this plot = BTI area shortfall at house acceptance**, not gas/height/fence.  
Do NOT reuse `keys_delay_penalty_unpaid` cluster (9 months delay / unpaid penalty story).

## Proposed lock (pre-checked 2026-09-20)

- **cluster_id:** `newbuild_kp_bti_area_shortfall_acceptance_tyumen`
- **top_energy_mirror:** `number_claimed_vs_unpaid` / `paper_clean_then_broke`
- **newbuild_mechanism:** семья покупает **дом в коттеджном посёлке под Тюменью** по ДДУ (ИЖС/КП от застройщика); в договоре и буклете **148 м²** общая площадь; на **приёмке** технический план / акт показывает **134 м²** (−14 м²); застройщик: «уточнение проекта», требует **доплату ~420–480 тыс ₽** или не отдаёт ключи; семья **не подписывает акт** и **не платит** до сверки с проектом и приложениями ДДU; часть отделки уже оплачена по графику — **остановились на пороге ключей**
- **why_newbuild_not_secondary:** дом от застройщика по ДДU в КП, не вторичка с ЕГРН-продавцом
- **title draft (H1 direction):** «Под Тюменью на приёмке дома в КП площадь урезали на 14 кв.м — ключи не отдали без доплаты»
- **comment_magnet_angle:** «Если на приёмке дома площадь меньше, чем в ДДU — вы доплачиваете за «уточнение» или отказываетесь от акта?»
- **scout_helper.py --check-query:** PASS 2026-09-20 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam_check:** last3 B30 assignment ban, B31 insurance approval, B32 escrow beneficiary — **KP acceptance area** = new skeleton

## Wordstat MCP-KV (live 2026-09-20)

wordstat_preflight: mcp-kv wordstat_get_user_info OK (implicit via calls)

| phrase | regions 55+11176 | volume |
|--------|------------------|-------:|
| коттеджные поселки тюмень | 55,11176 | **1422** |
| дом в коттеджном поселке тюмень | 55,11176 | 53 |
| приемка квартиры в новостройке тюмень | 55,11176 | 29 |
| приемка новостроек тюмень | 55,11176 | 32 |
| приемка новостройки (RU 225 compare) | 225 | 6703 |

**wordstat_rework:** P0 spine «коттеджные поселки тюмень» 1422 + mechanism «приёмка дома / площадь по ДДU / акт» woven for families; support «приемка квартиры в новостройке тюмень» 29

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: семья на финальной приёмке дома в КП
- risk: площадь в акте меньше ДДU + давление доплатой
- time: день приёмки / порог ключей
- finale: отказ от акта без паники; agency — сверка проекта, экспертиза, переговоры с застройщиком

## signal_urls

- https://72.ru/text/realty/2026/09/15/76640741/
- https://t.me/Tyumen_Rieltor
- https://dzen.ru/holyslav

Output handoff with all required Scout fields including `anti_dupe_hard: PASS`, `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`.
