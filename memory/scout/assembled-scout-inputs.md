# Scout inputs — 2026-09-10 (B24, slot ~15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-10 (Thursday, YEKT slot ~15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 23 active locks (last_sync 2026-09-10)
- **Live WP 2026-09-07..10 — DO NOT reuse plot:**
  - 2026-09-10: чистовая vs предчистовая в ДДУ (отделка на ключах)
  - 2026-09-10: бронь сгорела +450к (booking_expired_price_hike)
  - 2026-09-09: пропал балкон из планировки / банк заморозил транш
  - 2026-09-09: неустойка за год просрочки ключей
  - 2026-09-09: семейная ипотека пересчитали — ребёнку 7 лет
  - 2026-09-09: банк остановил транш после приёмки без замечаний
  - 2026-09-08: ключи без разрешения на ввод / банк заморозил ипотеку
  - 2026-09-08: переуступка — долг 94к
  - 2026-09-08: маткапитал / детские доли за 3 недели до ключей
  - 2026-09-07: созаёмщика исключили за 7 дней до ДДУ
  - 2026-09-07: рассрочка застройщика — 5 дней просрочки, ДДУ расторгли
  - 2026-09-07: коттедж — газ обещали у забора, 180 м
- **Rejected overlap:** bank appraisal with amount «420 тысяч» → H1 FINGERPRINT DUPLICATE with installment cluster
- **Rejected overlap:** bank revoked mortgage 72h → booking_expired_price_hike cluster lock (today's bron post)
- **Rejected overlap:** parking/cellar «машино-место по ДДУ» → overlap B21 cellar cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_scout_story_dup.py --text` PASS
- `excalibur_blog_topic_focus.py` PASS (on-focus: новострой, дду, застройщ)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени трейд-ин сорвался накануне ДДУ — застройщик не принял их квартиру
- **slug:** v-tyumeni-trejd-in-sorvalsya-nakanune-ddu-zastrojschik-ne-prinyal-kvartiru
- **cluster_id (new):** trade_in_rejected_developer
- **story_dup_check:** PASS — distinct legal plot: семья в Тюмени шла в новостройку по схеме trade-in — застройщик обещал выкупить их старую квартиру и зачесть сумму в цену ДДУ; за день до подписания ДДУ оценщик застройщика занизил старую квартиру на 1,2 млн, trade-in «не сошёлся», банк не открыл эскроу на полную сумму, бронь на новую планировку сняли — объект ушёл в бронь другому покупателю

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке под trade-in, внесла бронь, получила одобрение ипотеки, готовилась к ДДУ
- **risk:** застройщик в одностороннем порядке снизил оценку старой квартиры / отказал в выкупе по ранее озвученной цене — разрыв между «зачтённой» суммой и реальной ценой ДДУ; без trade-in не хватает первоначального взноса и одобленного лимита
- **time:** за 24–36 часов до подписания ДДУ и открытия эскроу (пятница перед понедельником в офисе застройщика)
- **finale:** trade-in сорвался, бронь на новостройку сняли, планировку забронировал другой покупатель; семья остановила подписание ДДУ — деньги на эскроу не ушли, но бронь и скидка по акции потеряны
- **comment_magnet_angle:** «Застройщик обещал trade-in устно и в рекламе, а в ДДУ этой строки нет: вы бы всё равно подписали договор бронирования, если trade-in не прописан отдельным приложением?»

## Top-energy + newbuild mapping

- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** trade-in от застройщика — выкуп старой квартиры в зачёт цены ДДУ; срыв накануне подписания из-за заниженной оценки / отказа застройщика
- **why_newbuild_not_secondary:** сюжет целиком в цепочке покупки новостройки (бронь ЖК, ДДУ, эскроу, ипотека на объект от застройщика); старая квартира — только залог схемы trade-in, не самостоятельная вторичная сделка

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild trade-in casus without Klyshin — preferred; avoids today's bron/finish clusters and Sept live plots)

## Wordstat MCP-KV (live 2026-09-10)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| трейд ин новостройка | 55+11176 | 5 |
| trade in | 55+11176 | 213 (noisy — авто/прочее) |
| дду новостройка | 55+11176 | 20 |
| эскроу новостройка | 55+11176 | 2 |
| ипотека новостройка тюмень | 55+11176 | 201 |
| **новостройки тюмень** | **55+11176** | **4670** |
| **новостройки тюмень** | **225 (compare)** | **8607** |
| **купить новостройку в тюмени** | **55+11176** | **899** |
| купить новостройку в тюмени | 225 (compare) | 1902 |

**wordstat_rework log:**
- probe «трейд ин новостройка» 55+11176 → 5 (weak narrow; on-topic trade-in buyer)
- probe «trade in» 55+11176 → 213 (noisy tail — не P0)
- probe «дду новостройка» 55+11176 → 20 (weak)
- probe «эскроу новостройка» 55+11176 → 2 (weak; escrow clusters B19/B20/live taken)
- **rework:** localize Tyumen + newbuild buyer spine (новостройки, купить новостройку, ДДУ) → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 899 (55+11176) / 1902 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль trade-in кластера
- https://www.domrf.ru/ — справочник застройщиков / ДДУ
- https://www.consultant.ru/document/cons_doc_LAW_214754/ — 214-ФЗ, эскроу (контекст)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard: PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
