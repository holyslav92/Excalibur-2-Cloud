# Scout inputs — 2026-09-05 (B23)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday slot ~10:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 20 active locks (last_sync 2026-09-04)
- **FROZEN / recent live WP Sep 3–5 (DO NOT reuse plot):**
  - bank appraisal below DDU price — бронь сгорела (2026-09-05)
  - KP land category blocked mortgage (2026-09-04)
  - wrong escrow account / чужой счёт (2026-09-04)
  - acceptance defects + forced act signing (2026-09-04)
  - bank revoked mortgage approval 72h before DDU (2026-09-03)
  - finish type mismatch чистовая vs предчистовая (2026-09-03)
  - keys delayed 8 months + certificate instead of penalty (2026-09-03)
  - DDU area mismatch at keys (2026-09-03)
  - installment increase before handover (2026-09-02)
  - KP without gas/water at keys (2026-09-02)
  - assignment refusal after payment (in_pool)
  - transhevaя mortgage payment spike (in_pool)
  - B22 bank rate hike before DDU (2026-09-04 published)
  - B21 storage room missing; B20 legal entity change; B19 family mortgage escrow
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду, новостройк)
- `excalibur_blog_scout_story_dup.py --text` PASS (30d)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени трейд-ин от застройщика сорвался за день до ДДУ — бронь сгорела
- **slug:** v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela
- **cluster_id (new):** newbuild_trade_in_failed_before_ddu_tyumen
- **story_dup_check:** PASS — distinct from B22 rate hike; distinct from Sep 4 wrong escrow; distinct from assignment refusal (different plot: trade-in of old flat as down payment); plot = семья продала/забронировала старую квартиру по программе трейд-ин застройщика, за день до ДДУ застройщик снизил оценку старой квартиры или отказал в выкупе, первоначальный взнос «исчез», бронь на новостройку сгорела

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала новостройку по программе трейд-ин от застройщика: старую квартиру должны были выкупить как первоначальный взнос, на новую — оформить ДДУ с ипотекой
- **risk:** за 24 часа до подписания ДДУ застройщик (или его партнёр по trade-in) снизил оценку старой квартиры на 400–600 тыс. ₽ или отказал в выкупе из-за «дефектов/сроков» — первоначальный взнос перестал сходиться, банк не открыл сделку
- **time:** за день до подписания ДДУ, после 2–3 недель брони и подготовки документов
- **finale:** ДДУ не подписали, бронь на новостройку сгорела, плата за бронирование не вернули; старая квартира осталась непроданной, семья потеряла и лот в новостройке, и время на рынке
- **comment_magnet_angle:** «Застройщик занизил оценку квартиры в трейд-ин накануне ДДУ — вы бы доплатили разницу из своих или отпустили бы бронь?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild trade-in casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55+11176 | 4683 (context only) |
| ипотека от застройщика тюмень | 55 | 402 (rejected — overlaps B22 mortgage cluster) |
| субсидированная ипотека от застройщика тюмень | 55+225 | 47 / 2340 (rejected — 35% overlap B22 in_pool) |
| переуступка новостройка | 55 | 9 (rejected — assignment in_pool) |
| приемка квартиры в новостройке тюмень | 55 | 20 (rejected — acceptance cluster closed Sep 4) |
| **трейд ин новостройка** | **55+11176** | **479** (national spine; Tyumen localized in title) |
| новостройки трейд ин от застройщика | 225 compare | 121 |
| трейд ин при покупке квартиры в новостройке | 225 compare | 63 |

**wordstat_rework log:**
- probe «переуступка новостройка» 55 → 9 (weak; assignment plot in_pool)
- probe «субсидированная ипотека от застройщика тюмень» 55 → 47 (overlap warning with B22)
- probe «ипотека от застройщика тюмень» 55 → 402 (mortgage cluster saturated)
- probe «трейд ин новостройка» 55+11176 → 479; child «новостройки трейд ин от застройщика» RU225 → 121
- **rework:** localize Tyumen + trade-in buyer jargon on newbuild → **final P0 «трейд ин новостройка» regions 55,11176 freq 479** (compare RU225 479; child «новостройки трейд ин от застройщика» 121)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст trade-in / новостройки; не дубль кластера
- https://www.cbr.ru/ — контекст ипотеки (не герой)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
