# Scout inputs — 2026-09-12 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-12 (YEKT Saturday automation slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 25 active locks (last_sync 2026-09-12)
- **Live WP last ~20 titles (2026-09-12) — DO NOT reuse plot:**
  1. В ДДУ в Тюмени указали 4,2 млн — на эскроу был ноль (ddu_amount_vs_escrow_zero)
  2. В Тюмени застройщик потребовал 420 тысяч за лишние метры — ключи не выдал (developer_extra_sqm_payment)
  3. В Тюмени согласовали переуступку — квартиру забрали за 24 часа до аванса (pereustupka_stolen)
  4. В Тюмени застройщик снял субсидию за 3 дня до ДДУ — бронь сгорела (subsidy_removed)
  5. В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла (installment_penalty_developer)
  6. В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов (rent_forbidden_before_keys)
  7. В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки (plot_boundary_mismatch)
  8. В Тюмени занизили оценку на 1,2 млн — трейд-ин сорвался перед ДДУ (trade_in)
  9. В Тюмени в ДДУ обещали 4 позиции чистовой — отдали предчистовую (finish_level_mismatch)
  10. В Тюмени бронь новостройки сгорела — цена выросла на 450 тысяч (booking_expired_price_hike)
  11. В Тюмени пропал балкон на ключах — через 2 дня банк заморозил транш (balcony_plan_change)
  12. В Тюмени застройщик год не платил неустойку — семья остановила приёмку (penalty_1y_delay)
  13. Перед ДДУ ребёнку исполнилось 7 лет — семейную ипотеку пересчитали (child age trigger — NOT same as Oct 1 rule)
  14. В Тюмени банк остановил транш после приёмки без замечаний (acceptance_defects)
  15. В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку
  16. В Тюмени на переуступке нашли долг 94 тысячи — сделку остановили
  17. За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей
  18. В Тюмени за 7 дней до ДДУ созаёмщика убрали — ипотеки не хватило
  19. В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч
  20. В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м
- **Rejected overlap:** apartments-vs-flat (B23 / LIVE 9749 Sep 5); bank appraisal below DDU (LIVE 9684 Sep 5); developer double-sale same unit (LIVE 9823 Sep 6); escrow shortfall 400k (LIVE 9849 Sep 6)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, новострой)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени одобрили семейную ипотеку на новостройку — за 19 дней до 1 октября банк пересчитал лимит
- **slug:** v-tyumeni-semejnuyu-ipoteku-odobrili-za-19-dnej-do-oktyabrya-bank-pereschital-limit
- **cluster_id (new):** family_mortgage_october_2026_deadline_tyumen
- **story_dup_check:** PASS — distinct legal plot: семья получила предварительное одобрение семейной ипотеки на квартиру в новостройке по «старым» условиям; за 19 дней до 1 октября 2026 банк пересчитал лимит/ставку/доступную сумму из‑за ожидаемых изменений программы с 1 октября → платёж и первый взнос не сходятся с ценой в ДДУ, бронь под угрозой; NOT developer subsidy removal, NOT child-turned-7 trigger, NOT escrow zero

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в ЖК, получила одобрение семейной ипотеки на новостройку, внесла платную бронь и готовилась к ДДУ
- **risk:** банк за 19 дней до 1 октября 2026 пересчитал одобрение — снизил лимит или поднял ставку из‑за грядущих изменений семейной ипотеки; разрыв с ценой ДДУ и первым взносом
- **time:** «за 19 дней до 1 октября», накануне подписания ДДУ / открытия эскроу
- **finale:** подписание ДДУ остановили до перевода денег; бронь сгорела или застройщик поднял цену; семья не внесла аванс на эскроу вовремя — сделку заморозили, обратились к риелтору до денег
- **comment_magnet_angle:** «Одобрение уже было на руках — вы бы подписали ДДУ в последние дни сентября или подождали ясности после 1 октября, даже если бронь горит?»

## Top-energy + newbuild (required)

- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** семейная ипотека на новостройку (ДДУ/эскроу/бронь в ЖК) + календарный дедлайн изменений программы с 1 октября 2026 — банк пересчитал лимит перед подписанием
- **why_newbuild_not_secondary:** сделка с застройщиком по ДДУ, эскроу-счёт, бронь в ЖК; stakes — первый взнос и ипотечный лимит под цену договора долевого участия, не покупка квартиры у физлица на вторичке

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus; timely October 2026 rule deadline without Klyshin — avoids 12 closed live clusters)

## Wordstat MCP-KV (live 2026-09-12)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| семейная ипотека октябрь 2026 | 55+11176 | 323 (top child: «семейная ипотека с октября 2026» 273) |
| семейная ипотека с 1 октября 2026 | 55+11176 | 231 |
| семейная ипотека в тюмени | 55+11176 | 740 |
| семейная ипотека тюмень 2026 | 55+11176 | 380 |
| новостройки тюмень | 55+11176 | 4560 (context spine) |
| семейная ипотека в тюмени | 225 (compare) | 1083 |

**wordstat_rework log:**
- probe «семейная ипотека октябрь 2026» 55+11176 → 323; child «семейная ипотека с 1 октября 2026» → 231 (on-topic, timely)
- probe «новостройки семейная ипотека тюмень» → 23 (weak narrow)
- probe «дду тюмень» → 15 (weak)
- **rework:** localize Tyumen buyer + newbuild + семейная ипотека + октябрь 2026 deadline → **final P0 «семейная ипотека в тюмени» regions 55,11176,compare225 freq 740 (55+11176) / 1083 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст семейной ипотеки и новостроек (старые чеклисты Aug 2026 — не копировать shape)
- https://www.domrf.ru/ — семейная ипотека / справочник программ
- https://www.cbr.ru/ — контекст ипотечных лимитов (если нужен фон)
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
