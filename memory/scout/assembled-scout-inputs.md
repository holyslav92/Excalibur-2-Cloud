# Scout inputs — 2026-08-31 (B15)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-31 (YEKT Monday slot 09:00 / UTC 05:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- **DO NOT reuse (30d closed clusters):** marital_share_heirs, court_took_apartment, four_months_search, matkapital_opieka, seller_bankruptcy, elderly_phone, pnd_discount, military_summons, grandma_poa, inheritance_son, egrn_line, deceased_spouse, discount_2m, doverennost_svo, deposit_auction, illegal_renovation (B11), matkapital_missing_child_shares (B18), registered_persons (B17), communal_share_neighbor (B16), B14 mortgage lien
- **Live WP plots already published (do not duplicate):** приставы арест (2026-08-29), предварительный договор продали другим, кладовка в подарок, аккредитив, rent_to_buy три года, опека над продавцом, маткапитал детские доли, прописанные, коммуналка сосед, и др. (see EXCALIBUR_RECENT_WP_POSTS from today.py)
- `published-titles-only.md` + `shared/published-articles.md` — B02–B14 ledger

## Proposed topic (PASS story_dup + scout_helper)

- **topic_id:** B15
- **title_draft:** В Тюмени поддельное согласие супруги остановило сделку перед авансом
- **slug:** v-tyumeni-poddelnoe-soglasie-suprugi-ostanovilo-sdelku-pered-avansom
- **cluster_id (new):** forged_spouse_consent_blocks_advance
- **story_dup_check:** PASS — distinct from marital_share_heirs_notary_checked (нотариус/доля), deceased_spouse_share_surprise (умерший супруг), registered_persons (прописанные), doverennost_svo; plot = фальшивое нотариальное согласие супруга вскрылось на сделке/перед авансом

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала вторичку в браке одного собственника; продавец показал нотариальное согласие супруги на продажу
- **risk:** подпись/бланк согласия не совпал с реестром нотариуса или супруга заявила, что не подписывала — сделка юридически невозможна без действительного согласия
- **time:** в день сделки / за день до внесения аванса, после одобрения ипотеки и «чистой» выписки ЕГРН
- **finale:** банк/риэлтор остановили передачу денег; покупатели не внесли аванс; продавец ушёл «за новым согласием» — сделка сорвалась
- **comment_magnet_angle:** «Если согласие супруга лежит в конверте — вы всё равно вносите аванс или ждёте проверки у нотариуса в день сделки?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen casus without Klyshin — preferred)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-08-31)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| согласие супруга на продажу квартиры | 55+11176 | **54** |
| согласие супруга на продажу квартиры | 225 (compare) | **4816** |
| нужно согласие супруга на продажу квартиры | 55+11176 | 23 |
| согласие бывшего супруга на продажу квартиры | 55+11176 | 7 |
| нотариус согласие супруга на продажу квартиры | 55+11176 | (via RU 742 context) |
| мнимая сделка | 55+11176 | 55 (rejected — overlaps court_took_apartment cluster) |
| оспорили продажу квартиры | 55+11176 | 9 (weak P0) |

**wordstat_rework log:**
- probe «мнимая сделка» 55+11176 → 55 — **rejected** (story_dup BLOCKER vs court_took_apartment)
- probe «оспорили продажу квартиры» → 9 — weak
- probe «согласие супруга на продажу квартиры» 55+11176 → **54** (compare RU225 **4816**) — **final P0**
- local buyer jargon: нотариальное согласие, проверка подлинности, брак + один собственник

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_5142/ — ГК РФ брачный договор / распоряжение общим имуществом (контекст)
- https://dzen.ru/holyslav — канал tenant
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B15, title, slug, signal_urls, research angles for Research role.
