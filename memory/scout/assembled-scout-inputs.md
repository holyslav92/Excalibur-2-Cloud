# Scout inputs — 2026-09-11 (B24, slot ~12 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-11 (YEKT weekday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 25 active locks (last_sync 2026-09-11)
- **Live WP ~20 (2026-09-11) — DO NOT reuse plot:**
  - рассрочка застройщика просрочка 4 дня (2026-09-11)
  - запрет аренды до ключей в ДДУ (2026-09-11)
  - дом в посёлке границы участка (2026-09-10)
  - трейд-ин сорвался (2026-09-10)
  - чистовая vs предчистовая (2026-09-10)
  - бронь сгорела цена +450к (2026-09-10)
  - пропал балкон / проектная декларация (2026-09-09)
  - неустойка за просрочку ключей (2026-09-09)
  - ребёнку 7 лет семейная ипотека (2026-09-09)
  - банк остановил транш после приёмки (2026-09-09)
  - ключи без разрешения на ввод (2026-09-08)
  - переуступка долг 94к (2026-09-08)
  - индексация остатка по ДДУ перед сдачей (live 9536, Sep 2)
  - кладовка по ДДУ не выдали (B21)
  - газ у забора в КП (Sep 7)
- **Rejected overlap:** parking «машиноместо по ДДУ на ключах» → 57% overlap with B21 cellar cluster (scout_helper WARNING)
- **Rejected:** price indexation installment (live Sep 2) — same mechanism as closed installment/indexation plots
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, newbuild)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени одобрили субсидированную ипотеку — застройщик снял субсидию за 3 дня до ДДУ
- **slug:** v-tyumeni-odobrili-subsidirovannuyu-ipoteku-zastrojschik-snyal-subsidiyu-za-3-dn
- **cluster_id (new):** subsidized_mortgage_revoked_before_ddu_tyumen
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** субсидированная ипотека от застройщика на квартиру в ЖК — банк одобрил льготную ставку, за 3 дня до подписания ДДУ застройщик отозвал субсидию / пересчитал цену без скидки, платёж вырос, сделку остановили до эскроу
- **why_newbuild_not_secondary:** сюжет только про покупку квартиры в новостройке по ДДУ с ипотечной программой застройщика; нет продавца вторички, ЕГРН-вторички, бабушки, банкротства
- **story_dup_check:** PASS — distinct from B22 (банк поднял рыночную ставку), from family mortgage child-age, from escrow/matkapital B19; mechanism = отзыв субсидии застройщика, не банковский rate hike

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке под «красивую» субсидированную ставку от застройщика, банк выдал одобрение, бронь держали
- **risk:** за 3 дня до ДДУ застройщик снял субсидию / изменил коммерческие условия — цена в договоре и платёж по ипотеке выросли на сотни тысяч, одобрение перестало покрывать сделку
- **time:** за 3 дня до подписания ДДУ, после 2–3 недель одобрения ипотеки
- **finale:** банк отказал пересчитывать кредит на новую сумму без повторной заявки; семья не подписала ДДУ, бронь сгорела, субсидия «как в рекламе» не восстановили
- **comment_magnet_angle:** «Одобрение ипотеки на руках, а застройщик снял субсидию за три дня до ДДУ — вы бы всё равно подписали договор „чтобы не потерять квартиру“, или остановили бы сделку?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus without Klyshin — preferred; avoids today's installment/rent clusters)

## Wordstat MCP-KV (live 2026-09-11)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| машиноместо в дду | 55,11176,225 | 63 (rejected — B21 overlap) |
| паркинг новостройка тюмень | 55,11176,225 | 14 (weak) |
| субсидированная ипотека новостройка | 55,11176,225 | 385 (RU-wide; top child noisy) |
| индексация цены дду | 55,11176,225 | 2 (plot taken live Sep 2) |
| **ипотека от застройщика тюмень** | **55,11176** | **514** |
| субсидированная ипотека от застройщика тюмень | 55,11176 | 27 (narrow P0 child) |
| ипотека тюмень новостройки от застройщика | 55,11176 | 98 (context) |

**wordstat_rework log:**
- probe «машиноместо в дду» → 63 → rejected (B21 cellar/parking overlap 57%)
- probe «паркинг новостройка тюмень» → 14 → weak, rejected
- probe «индексация цены дду» → 2 → plot closed on live (рассрочка остаток +400к)
- probe «субсидированная ипотека новостройка» → 385 RU → rework localize Tyumen + застройщик
- **final P0 «ипотека от застройщика тюмень» regions 55,11176,compare225 freq 514 (Tyumen+область)**

## signal_urls (research)

- https://www.cbr.ru/ — ключевая ставка / контекст субсидий (не герой)
- https://дом.рф/ or https://www.domrf.ru/ — ипотечные программы застройщиков
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ, цена в ДДУ
- {{SITE_BASE}}/blog/pokupka-kvartiry/ — sibling newbuild casus
- {{SITE_BASE}}/blog/ipoteka/v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi/ — B22 contrast (банк поднял ставку, не застройщик снял субсидию)
- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

## Research angles (for Research role)

1. Как оформляется субсидированная ипотека от застройщика в Тюмени 2026: кто платит разницу ставки, срок действия субсидии, привязка к ДДУ
2. Может ли застройщик односторонне отозвать субсидию после одобрения банка — типовые формулировки в договоре бронирования и ДДУ
3. Срок действия одобрения ипотеки vs срок брони — что сгорает первым
4. Разница механизмов: субсидия застройщика vs скидка в цене vs траншевая ипотека (B22 — банк поднял ставку)
5. Практика Тюмени: МПЛ, лимиты ПСК, когда банк отказывает пересчитать одобрение на новую цену ДДУ

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
