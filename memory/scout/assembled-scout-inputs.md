# Scout inputs — 2026-08-30 (B18)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-30 (YEKT Sunday weekend Grok slot 17:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 18 active locks
- **FROZEN today (30 Aug 2026 — DO NOT reuse):**
  - B15 seller_mortgage_closure vs EGRN lien — «Продавец закрыл ипотеку, но залог сорвал сделку в Тюмени»
  - B16 communal_share_preemptive_right_neighbor — «В Тюмени сосед остановил покупку доли перед авансом»
  - B17 registered_persons_before_advance — «Перед авансом в Тюмени нашли прописанных — сделку остановили»
- User-frozen plots: ЕГРН/банкротство, опека/маткапитал 3y, 4 months search, yellow opinion, повестка, бабушка/доверенность, ПНД 3млн, супружеская доля/наследники/нотариус, суд 2 года, rent_to_buy B13, кладовка подарок, ПДКП, умершая жена, расписка, задаток торги, приставы 2 дня, строка ЕГРН ипотека, скидка 2млн
- Closed clusters (30d): see `memory/scout/used-clusters.json` (18 locks through ~2026-09-29)
- Live WP feed ~20 (2026-08-30): B17 registered, B16 communal, B15 seller mortgage, double sale preliminary contract, кладовка gift, аккредитив, приставы 2d, guardianship court, rent_to_buy 3y, newbuild delay, Yalutorovsk double sale, B11 open kitchen, etc.
- `published-titles-only.md` + `shared/published-articles.md` — B02–B14 ledger (+ B15–B17 live today)

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B18
- **title_draft:** В Тюмени купили квартиру с маткапиталом — детских долей в собственности не оказалось
- **slug:** v-tyumeni-kupili-kvartiru-s-matkapitalom-detskih-doley-ne-okazalos
- **cluster_id (new):** matkapital_missing_child_shares
- **story_dup_check:** PASS — distinct from matkapital_opieka_kids_cancel_3y (опека молчала 3 года / дети оспорили) and seller_bankruptcy; plot = маткапитал использован, но детские доли не выделены / не видны в ЕГРН, сделку остановили до аванса

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала вторичку, продавец подтвердил использование маткапитала при покупке, покупатели запросили документы о выделении долей детям
- **risk:** в ЕГРН и пакете документов нет зарегистрированных детских долей — без согласия опеки и выделения долей сделку нельзя провести легально; риск оспаривания и отмены регистрации
- **time:** за несколько дней до аванса, после одобрения ипотеки и согласования цены
- **finale:** сделку развернули до передачи денег; покупатели ушли искать другой объект; продавец должен выделить доли и пройти опеку (месяцы), покупатели не стали ждать
- **comment_magnet_angle:** «Если продавец говорит „доли выделены“, но в ЕГРН их нет — вы верите на слово или ждёте свежую выписку до аванса?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen matkapital child-shares casus without Klyshin — preferred; avoid today's B15/B16/B17 and frozen matkapital_opieka 3y plot)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-08-30)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| маткапитал детские доли | 55+11176 | 6 (API totalCount only) |
| маткапитал при покупке квартиры | 55+11176 | 22 |
| материнский капитал квартира (cluster) | 55+11176 | 1108 total; top «квартира за материнский капитал» 127 |
| доля ребенка в квартире по материнскому капиталу | 55+11176 | 77 |
| **продажа квартиры с материнским капиталом** | **55+11176** | **43** |
| продажа квартиры с материнским капиталом | 225 (compare) | 4752 |
| предварительный договор купли продажи квартиры | 55+11176 | 58 (rejected — live WP double-sale overlap) |

**wordstat_rework log:**
- probe «маткапитал детские доли» 55+11176 → 6 (narrow spine)
- probe «маткапитал при покупке квартиры» 55+11176 → 22
- probe «материнский капитал квартира» 55+11176 → cluster «доля ребенка в квартире по материнскому капиталу» 77; «продажа квартиры с материнским капиталом» 43
- **rework:** buyer jargon «проверка квартиры с маткапиталом при покупке» → **final P0 «продажа квартиры с материнским капиталом» regions 55,11176 freq 43** (compare RU225 4752); on-plot spine for buyer checking seller's matkapital history

## signal_urls (research)

- {{SITE_BASE}}/blog/ — live sibling posts (avoid duplicate clusters)
- https://dzen.ru/holyslav — канал holyslav: маткапитал / детские доли (контекст, не дубль matkapital_opieka 3y)
- https://t.me/klyshin_A — checked, not used this slot
- https://t.me/holyslav92
- https://base.garant.ru/ — выделение долей детям при использовании маткапитала (нормы)
- https://www.consultant.ru/document/cons_doc_LAW_114247/ — Жилищный кодекс / обязанность выделить доли

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B18, title, slug, signal_urls, research angles for Research role.
