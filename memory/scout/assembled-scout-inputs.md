# Scout inputs — 2026-08-29 (B13)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-29 (YEKT Saturday, slot ~10:01)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 16 active locks (2026-08-29)
- Closed clusters (30d): illegal_renovation_rosreestr_blocks_registration (B11), marital_share_heirs_notary_checked, court_took_apartment_relatives_contested, matkapital_opieka_kids_cancel_3y, elderly_seller_led_by_phone, seller_bankruptcy_finmanager_clean_egrn, pnd_3mln_discount, military_summons_stopped_registration, four_months_search_yellow_opinion_lawyers_refused, grandma_owner_missing_viewing_old_poa, egrn_line_blocks_advance, deceased_spouse_share_surprise, inheritance_son_first_marriage_no_refusal, discount_two_million_hidden_risk, doverennost_svo_seller, deposit_before_auction
- Live WP ~20 titles (2026-08-29, from excalibur_blog_today): rent-to-own «три года платили по найму» (2026-08-29), B12 escrow novostroyka, double sale Ялуторовск, B11 open kitchen, notarius supruzheskaya, court 2y relatives, 4 months search, matkapital+opieka kids, bankruptcy finmanager, elderly phone, pnd discount, clean EGRN 3 months, etc.
- **AVOID this slot:** rent-to-own (live today), double_sale_two_buyers (live 2026-08-28), ddu_escrow (B12), parking_storage EGRN angle (FAILED dup vs egrn_line_blocks_advance on «выписка ЕГРН + аванс» wording)
- `published-titles-only.md` + `shared/published-articles.md` — B02–B12 ledger

## Proposed topic (PASS scout_helper --check-query + story_dup PASS)

- **topic_id:** B13
- **title_draft:** В Тюмени родственники оформили опеку над продавцом — за день до аванса сделку остановили
- **slug:** v-tyumeni-opeku-nad-vzroslym-sobstvennikom-oformili-pered-sdelkoj
- **cluster_id (new):** adult_guardianship_incapacitated_blocks_sale
- **story_dup_check:** PASS — distinct from matkapital_opieka_kids (детские доли/маткапитал, не взрослый недееспособный); NOT elderly_phone (телефон/родственники сорвали); NOT rent-to-own / double_sale / escrow live posts; finale = опека над взрослым + оспаривание/остановка до аванса, NOT строка ЕГРН

## Dzen news-casus shape (target PASS)

- **event:** покупатель в Тюмени согласовал вторичку, прошёл осмотр и банк; продавец-пенсионер подписывал договор — внезапно всплыло заявление родственников о признании его недееспособным и назначении опекуна
- **risk:** сделка с гражданином, признанным или признаваемым недееспособным, ничтожна/оспорима (ст. 171, 177 ГК РФ); без разрешения органов опеки отчуждение квартиры невозможно (ст. 37 ГК РФ) — покупатель рискует потерять аванс и квартиру при последующем суде
- **time:** за один рабочий день до внесения аванса (договор уже на подписи, деньги на счёте)
- **finale:** риэлтор остановил внесение аванса; родственники подали в суд — регистрацию не провели; покупатель не потерял деньги (альтернатива для Research: ВС РФ обзор 12/2026 по оспариванию сделок с жилыми помещениями)
- **comment_magnet_angle:** «Если продавец выглядит адекватно, а родня уже тянет опеку — вы всё равно внесёте аванс или ждёте справки из суда?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen adult-guardianship casus without Klyshin — preferred; avoid closed plots and live rent-to-own / double-sale posts)
- **signal_urls:** https://vsrf.ru/documents/all/36132/ | https://iviba.ru/tematicheskij-obzor-verhovnogo-suda-rossijskoj-federacii-n-12-2026/ | https://www.consultant.ru/document/cons_doc_LAW_5142/20fe084332f905f42fb9823c3c45bd0bc416726a/ | https://moshousing.ru/kvartiry-nedeesposobnyh-prava-riski-i-zashchita-pokupatelya/ | https://dzen.ru/holyslav | {{SITE_BASE}}/blog/ | https://t.me/holyslav92

## Wordstat MCP-KV (live 2026-08-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| недееспособный продажа квартиры | 55+11176 | 6 |
| признание недееспособным | 55+11176 | **157** |
| признание недееспособным | 225 (compare) | 14093 |
| разрешение опеки на продажу квартиры | 55+11176 | 77 |
| разрешение опеки на продажу квартиры | 225 (compare) | 3841 |
| опека продажа квартиры | 55+11176 | 186 (top phrase 77) |
| машино-место егрн | 55+11176 | 1 (rejected — dup egrn_line) |

**wordstat_rework log:**
- probe «недееспособный продажа квартиры» 55+11176 → 6 (weak exact)
- probe «разрешение опеки на продажу квартиры» 55+11176 → 77 (sale angle but overlaps kids-opieka SERP)
- probe «машино-место егрн» / parking angle → story_dup FAIL vs egrn_line_blocks_advance
- **rework:** adult incapacity buyer jargon + Tyumen casus → **final P0 «признание недееспособным» regions 55,11176 freq 157** (compare RU225 14093); secondary spine «разрешение опеки на продажу квартиры» 77

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B13, title, slug, signal_urls, research angles for Research role.
