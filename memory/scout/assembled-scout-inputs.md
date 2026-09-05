# Scout inputs — 2026-09-05 (B24 weekend slot 12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **FROZEN today 2026-09-05 morning (DO NOT reuse plot):**
  - `newbuild_bank_appraisal_below_ddu_price_tyumen` — B23 «Ипотеку в Тюмени одобрили: оценка ниже на 400 тысяч — бронь сгорела»
  - `newbuild_trade_in_failed_before_ddu_tyumen` — «В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела»
- **Recent newbuild live WP Sep 3–5 (distinct cluster required):**
  - bank appraisal below DDU (B23)
  - trade-in failed before DDU
  - KP land category blocked mortgage (cottage)
  - wrong escrow account / advance to stranger account
  - bank rate raised before DDU (B22)
  - acceptance defects act keys denied
  - bank revoked approval 72h before DDU
  - finish type mismatch чистовая vs предчистовая
  - keys delayed 8 months + certificate
  - DDU area mismatch at keys
  - storage room missing (B21)
  - installment increase before handover
  - legal entity change + escrow (B20)
  - family mortgage escrow matkapital (B19)
- **Closed clusters (30d):** all in used-clusters.json
- `scout_story_dup.py --text` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду, переуступк)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела
- **slug:** v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela
- **cluster_id (new):** newbuild_assignment_seller_raised_price_booking_lost_tyumen
- **story_dup_check:** PASS — distinct from B22 rate change (bank not seller); distinct from B23 appraisal; distinct from trade-in; distinct from price-after-booking generic posts; plot = покупатель новостройки по переуступке согласовал цену и внёс аванс продавцу переуступки, за 24 часа до регистрации переуступки и подписания ДДУ продавец поднял доплату на ~280 тыс. ₽, покупатель отказался, потерял бронь у застройщика и аванс по договору переуступки частично/полностью

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени нашла квартиру в строящемся ЖК по переуступке — цена ниже, чем у застройщика; согласовали с первым дольщиком сумму, внесли аванс по договору переуступки, забронировали лот у застройщика до даты подписания
- **risk:** за сутки до подписания переуступки и ДДУ продавец переуступки потребовал доплату ~280 тыс. ₽ («рост цены застройщика», «индексация», «ошибка в расчёте») — без этого не выйдет на сделку и не даст согласие застройщика
- **time:** 24 часа до регистрации переуступки, после недель согласований и проверки ДДУ первоначального дольщика
- **finale:** покупатель отказался платить доплату; продавец переуступки сорвал сделку; бронь у застройщика сгорела; аванс по переуступке удержан или возвращён частично; семья вернулась к поиску, квартира ушла
- **comment_magnet_angle:** «Продавец переуступки поднял цену накануне ДДУ — вы бы доплатили 280 тысяч или отпустили бронь, даже если аванс сгорит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild assignment casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55 | 3640 (context anchor) |
| купить новостройку в тюмени | 55 | 639 |
| переуступка новостройка | 55+11176 | 13 |
| переуступка квартиры в новостройке риски | 55 | 2 |
| покупка новостройки по переуступке | 55+11176 | 2 |
| семейная ипотека новостройка | 55+11176 | 112 (rejected — B19 cluster) |
| ипотека на новостройку процентная ставка | 55+11176 | 21 (rejected — B22 cluster) |

**wordstat_rework log:**
- probe «переуступка новостройка» 55+11176 → 13; child «покупка новостройки по переуступке» → 2; «риски покупки квартиры по переуступке в новостройке» → 2
- weak niche volume → rework: anchor P0 to high-demand «купить новостройку в тюмени» 55 → **639** + localize assignment buyer jargon in H1/casus (переуступка, ДДУ, бронь)
- **final P0 «купить новостройку в тюмени» regions 55,11176 freq 639** (compare: новостройки тюмень 3640 context)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст переуступок/новостроек
- https://www.consultant.ru/document/cons_doc_LAW_5142/ — ГК РФ уступка права требования (ст. 382–390)
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
