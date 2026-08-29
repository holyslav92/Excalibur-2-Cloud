# Scout inputs — 2026-08-29 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks
- **FROZEN today (29 Aug 2026 live plots — DO NOT reuse):**
  - FSSP arrest 2 days before registration — daily «приставы арестовали квартиру» (overlap BLOCKER)
  - rent_to_buy_owner_sold_while_contract — «три года платили — собственник продал другим»
  - guardianship day before advance — «родственники оформили опеку за день до аванса»
  - Yalutorovsk double sale — «квартиру продали двоим»
- Closed clusters (30d): illegal_renovation (B11), marital_share, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction, B12 ddu_escrow_handover_delay, etc.
- `published-titles-only.md` + `shared/published-articles.md` — B02–B12 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B13
- **title_draft:** Аккредитив открыли — продавцу деньги не дошли, сделку в Тюмени сорвали
- **slug:** akkreditiv-otkryli-prodavcu-dengi-ne-doshli-sdelku-v-tyumeni-sorvali
- **cluster_id (new):** letter_of_credit_seller_no_money_tyumen
- **story_dup_check:** PASS — distinct from B12 escrow/DDU delay (застройщик/эскроу), seller_bankruptcy (банкротство), egrn_line (строка обременения в выписке); plot = безотзывный аккредитив открыт, банк не раскрыл продавцу из-за расхождения условий/документов, регистрация сорвана

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени согласовала вторичку, банк открыл безотзывный аккредитив, стороны пришли на регистрацию в МФЦ
- **risk:** банк не исполнил аккредитив — расхождение в договоре/реквизитах или условие «после регистрации» не выполнено; продавец не получил деньги, покупатель не может зарегистрировать право
- **time:** в день подачи на регистрацию / через сутки после открытия аккредитива
- **finale:** сделку развернули; аккредитив закрыли без выплаты продавцу; покупатели потеряли 2–3 недели и комиссию банка; объект ушёл другим (или продавец вернулся к переговорам после исправления документов)
- **comment_magnet_angle:** «Если банк уже открыл аккредитив — вы считаете, что деньги „на месте“, или ждёте раскрытия после регистрации?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen akkreditiv casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| аккредитив при покупке квартиры | 55+11176 | 44 |
| аккредитив при покупке квартиры | 225 (compare) | 3799 |
| аккредитив в банке при покупке квартиры | 55+11176 | 11 |
| купить квартиру в тюмени | 55+11176 | 22699 (context only) |
| машино место квартира | 55+11176 | 1 (rejected — weak) |
| кладовка квартира егрн | 55+11176 | API empty (rejected — EGRN cluster overlap risk) |

**wordstat_rework log:**
- probe «аккредитив при покупке квартиры» 55+11176 → 44 (on-plot)
- probe «аккредитив квартира тюмень» → API empty (skip)
- rework buyer jargon: «безотзывный аккредитив сделка» → keep P0 «аккредитив при покупке квартиры» 44 (compare RU225 3799) — buyer demand spine for H2/practice, not in H1

**final P0:** «аккредитив при покупке квартиры» regions 55,11176 freq 44 (compare RU225 3799)

## signal_urls (research)

- https://www.sberbank.ru/ru/person/credits/home/buy/accreddit — условия аккредитива Сбер (контекст)
- https://base.garant.ru/ — ГК РФ ст. 867–877 аккредитив (официальный контекст)
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
