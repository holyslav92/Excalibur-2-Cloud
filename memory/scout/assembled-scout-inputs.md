# Scout inputs — 2026-08-29 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday weekend slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- **FROZEN today (29 Aug 2026 live plots — DO NOT reuse):**
  - rent_to_buy_owner_sold_while_contract — «В Тюмени три года платили за квартиру — собственник продал её другим»
  - guardianship/incapacity day before advance — «Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд»
- Closed clusters (30d): illegal_renovation (B11), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction, B12 ddu_escrow_handover_delay, live double_sale Ялуторовск, etc.
- Live WP ~20 (from excalibur_blog_today RECENT_WP_POSTS): today's rent_to_buy + guardianship; B12 escrow delay; Yalutorovsk double sale; B11 open kitchen; notarius; court 2y; matkapital; bankruptcy; elderly phone; pnd discount; etc.
- `published-titles-only.md` + `shared/published-articles.md` — B02–B12 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B13
- **title_draft:** В Тюмени приставы наложили арест за два дня до регистрации — аванс ещё не вносили
- **slug:** v-tyumeni-pristavy-nalozhili-arest-za-dva-dnya-do-registracii
- **cluster_id (new):** fssp_arrest_day_before_registration_tyumen
- **story_dup_check:** PASS — distinct from seller_bankruptcy (банкротство/финуправляющий), egrn_line_blocks_advance (строка обременения в выписке), military_summons, receipt/no money; plot = внезапный запрет ФССП на регистрационные действия за 48 часов до сделки после «чистой» проверки продавца

## Dzen news-casus shape (target PASS)

- **event:** пара в Тюмени выбрала вторичку, проверила продавца в ФССП и банкротство, согласовала ипотеку и дату регистрации в МФЦ
- **risk:** судебный пристав внёс запрет на регистрационные действия по долгу продавца — Росреестр приостановил сделку; деньги ещё на аккредитиве/не внесены
- **time:** за два дня до подачи на регистрацию (после одобрения ипотеки)
- **finale:** сделку развернули до аванса; покупатели ушли к другому объекту; продавец должен гасить долг и снимать запрет (2–6 недель) — покупатели не ждали
- **comment_magnet_angle:** «Если сегодня в ФССП чисто — вы всё равно вносите аванс до регистрации или ждёте финальной проверки в день сделки?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen FSSP casus without Klyshin — preferred; avoid today's rent_to_buy and guardianship plots)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| пристав арест квартира | 55+11176 | 38 |
| долг капремонт | 55+11176 | 47 (rejected — weaker casus spine) |
| переуступка дду | 55+11176 | 25 (rejected — too close to B12 escrow/DDU cluster) |
| купить кладовку в тюмени | 55+11176 | 108 (rejected — EGRN dup with egrn_line if «выписка» in hook) |
| **фссп проверить задолженность** | **55+11176** | **232** |
| фссп по тюменской области проверить задолженность | 55+11176 | 54 |
| фссп проверить задолженность | 225 (compare) | 18776 |
| купить квартиру в тюмени | 55+11176 | 22699 (context only) |

**wordstat_rework log:**
- probe «пристав арест квартира» 55+11176 → 38 (on-plot but narrow)
- probe «запрет фссп квартира» → API empty (skip)
- probe «долг капремонт» 55+11176 → 47 (weak P0)
- **rework:** buyer jargon «проверить продавца у приставов» → **final P0 «фссп проверить задолженность» regions 55,11176 freq 232** (compare RU225 18776); local variant «фссп по тюменской области проверить задолженность» 54

## signal_urls (research)

- https://dzen.ru/a/ailPOoO-Zyx4iqEu — канал holyslav: ФССП и приостановка сделки (контекст, не дубль кластера)
- https://publishernews.ru/PressRelease/PressReleaseShow.asp?id=738661 — Росреестр: приостановка из-за долгов/запрета
- https://t.me/klyshin_A — checked, not used this slot
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
