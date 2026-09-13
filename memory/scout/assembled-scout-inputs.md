# Scout inputs — 2026-09-13 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-13 (YEKT Sunday slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO acceptance_defects / chistovaya / finishing mismatch (B25 cluster: acceptance_defects_penalty)
- NO RVE / tranche / mortgage tranche block (B26 cluster: newbuild_rve_delay_blocks_mortgage_tranche_tyumen)
- NO parking/mashino-mesto double-sold (B24 cluster: newbuild_parking_spot_double_sold_tyumen)
- NO DDU apartment vs apartments (B23)
- NO assignment / переуступка stolen (LIVE 2026-09-12: soglasovali-pereustupku; scout_helper overlap 37%)
- NO family mortgage age/recalc (LIVE 2026-09-12: odobrili-semejnuyu-ipoteku)
- NO cottage construction defects only (LIVE 2026-09-12: dom-ne-prinyali-brak-850k — другой механизм: брак дома, не площадь участка)
- NO booking_expired_price_hike (used-clusters + LIVE)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-13)
- Live WP recent (~12): B26 RVE+tranche, B25 chistovaya, B24 parking, B23 apartamenty, transhevaya +480k, installment penalty, escrow zero, subsidized mortgage removed, trade-in, bank appraisal -680k, family mortgage recalc, cottage defects 850k, assignment lost 7 days, KP extra meters 420k
- **Rejected:** assignment_lost_to_faster_buyer — scout_helper WARNING 37% overlap LIVE-V-TYUMENI-SOGLASOVALI-PE
- **Rejected:** family_mortgage_child_age_deadline — overlap LIVE-V-TYUMENI-ODOBRILI-SEMEJ
- **Rejected:** keys_delay_penalty_unpaid — H1 fingerprint dup LIVE-V-TYUMENI-ZASTROJSCHIK-P
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: тюмен, КП)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени в договоре КП обещали 12 соток — на ключах оказалось 9,7
- **slug:** v-tyumeni-v-dogovore-kp-obeschali-12-sotok-na-klyuchah-okazalos-9-7
- **cluster_id (new):** newbuild_kp_plot_area_mismatch_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** покупка **дома в коттеджном посёлке (КП/ИЖС от застройщика)** — в договоре и схеме планировочной организации участка зафиксированы **12,0 соток**, при межевании и выдаче ключей факт **9,7 соток** → переплата ~**850 тыс.** за «воздух», регистрация земельного участка тормозится, застройщик ссылается на «актуальную топосъёмку» и отказывается пересчитывать цену
- **why_newbuild_not_secondary:** сюжет целиком в цепочке договор с застройщиком КП → эскроу/рассрочка → сдача дома + **земельный участок** → межевание → регистрация; нет продавца вторички, ЕГРН-квартиры, наследников, бабушки или соседской доли
- **story_dup_check:** PASS — distinct from B25 (чистовая в квартире ЖК), B26 (РВЭ+транш), B24 (паркинг), B23 (апартаменты), LIVE cottage defects 850k (строительный брак дома, не площадь участка), LIVE extra meters 420k (лишние м² в доме, не сотки земли)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила дом в коттеджном посёлке у застройщика; в договоре и презентации — участок 12 соток, дом под ключ
- **risk:** фактическая площадь участка после межевания 9,7 соток → переплата за 2,3 сотки (~850 тыс. по цене сотки в КП), невозможность оформить границы «как в договоре», риск соседнего захвата / спора с КП
- **time:** расхождение всплыло на приёмке за **3 дня** до подписания акта; межевой план пришёл с отметкой «уточнённая площадь» через **11 дней** после уведомления о готовности дома
- **finale:** семья отказалась подписывать акт; застройщик предложил «доплатить за соседний кусок» или принять 9,7 соток без скидки; деньги на эскроу заморожены, ключи не выдали, спор ушёл в претензию и запрос на независимое межевание
- **comment_magnet_angle:** «В договоре КП 12 соток, на межевании 9,7: вы бы подписали акт „с оговоркой“ ради ключей или заморозили бы сделку, даже если аренда съедает бюджет?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP plot-area casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-13)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройки | 55,11176 | 18 (rejected — LIVE assignment overlap) |
| семейная ипотека новостройка | 55,11176 | 93 (rejected — LIVE family recalc overlap) |
| неустойка застройщика | 55,11176 | 138 (rejected — fingerprint dup keys_delay live) |
| коттеджный поселок тюмень участок | 55,11176 | 34 (weak local tail) |
| участок в коттеджном поселке | 55,11176 | 52 (support) |
| **коттеджные поселки тюмень** | **55,11176** | **1566** |
| **коттеджные поселки тюмень** | **225 (compare)** | **2525** |
| новостройки тюмень | 55 | 3640 (context spine) |

**wordstat_rework log:**
- probe «переуступка новостройки» 55,11176 → 18 (plot blocked by LIVE overlap)
- probe «коттеджный поселок тюмень участок» → 34 (weak)
- probe «участок в коттеджном поселке» → 52 (support)
- **rework:** buyer jargon КП + коттеджный посёлок + Тюмень + участок → **final P0 «коттеджные поселки тюмень» regions 55,11176,compare225 freq 1566 (55+11176) / 2525 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, земельные участки в КП
- https://www.consultant.ru/document/cons_doc_LAW_122948/ — Земельный кодекс, межевание
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
