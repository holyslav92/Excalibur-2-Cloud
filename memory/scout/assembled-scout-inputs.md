# Scout inputs — 2026-08-31 (B19)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-08-31 (YEKT Monday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_focus:** real_estate
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 19 active locks
- **FROZEN today on live WP (31 Aug 2026 — DO NOT reuse plots):**
  - double_sale_same_apartment — «В Тюмени квартиру продали дважды — второй аванс остановили»
  - fake_spouse_consent B15 — «В Тюмени не подтвердили согласие супруги — аванс остановили»
  - matkapital_missing_child_shares B18 — «Квартиру с маткапиталом не купили: детских долей не было в ЕГРН»
  - registered_persons B17 — «Перед авансом в Тюмени нашли прописанных — сделку остановили»
  - communal_share B16 — «В Тюмени сосед остановил покупку доли перед авансом»
  - preliminary_contract_sold_others — «В Тюмени подписали предварительный договор — квартиру продали другим»
  - storage_room_not_in_egrn — «В Тюмени кладовка „в подарок“ остановила сделку — в ЕГРН её не было»
  - escrow_accreditiv_wrong — «Аккредитив открыли, сделку зарегистрировали — продавец без денег»
  - fssp_arrest — «В Тюмени приставы арестовали квартиру за два дня до регистрации»
  - rent_to_buy_owner_sold — «В Тюмени три года платили за квартиру — собственник продал её другим»
  - adult_guardianship — «Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд»
- Closed clusters (30d): see `memory/scout/used-clusters.json` (19 entries through deposit_before_auction)
- Live WP ~20 fetched via wordpress_get_posts 2026-08-31
- `published-titles-only.md` + `shared/published-articles.md` — ledger through B15 (2026-08-31)
- `scout_helper.py --check-query` + `story_dup` → PASS for proposed topic

## Proposed topic (PASS scout_helper + story_dup)

- **topic_id:** B19
- **title_draft:** В Тюмени долг по капремонту остановил сделку — справка УК за три дня до аванса
- **slug:** v-tyumeni-dolg-po-kapremontu-ostanovil-sdelku-spravka-uk
- **cluster_id (new):** kapremont_debt_new_owner_blocks_sale
- **story_dup_check:** PASS — distinct from egrn_line_blocks_advance (строка в выписке ЕГРН), seller_bankruptcy, registered_persons, communal_share, illegal_renovation; plot = скрытый долг фонду капремонта/УК, не виден в стандартной выписке ЕГРН, всплыл по справке управляющей компании за 72 часа до аванса

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала вторичку в панельном доме, получила одобрение ипотеки, согласовала дату сделки; продавец показал «чистую» выписку ЕГРН и квитанции без просрочек
- **risk:** справка из УК/регионального фонда капремонта показала накопленный долг продавца (сотни тысяч рублей) — по закону обязанность может перейти к новому собственнику или стать предметом взыскания после регистрации
- **time:** за три дня до внесения аванса, после юридической проверки и банковского одобрения
- **finale:** сделку остановили до аванса; покупатели отказались ждать, пока продавец гасит долг и получает справку об отсутствии задолженности; деньги не ушли
- **comment_magnet_angle:** «Справку из УК о долгах по капремонту вы запрашиваете всегда — или считаете, что „чистой“ выписки ЕГРН достаточно?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen kapremont casus without Klyshin — preferred; avoid today's double_sale, spouse consent, and all live-WP plots listed above)
- **signal_urls:** see list below

## Wordstat MCP-KV (live 2026-08-31)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка дду | 55+11176 | 25 (rejected — too close to B12 novostroyka/escrow cluster) |
| переуступка квартиры | 55+11176 | 55 (rejected — weak Tyumen spine vs kapremont) |
| купить квартиру по переуступке | 55+11176 | 2 (rejected after rework) |
| новостройки тюмень | 55+11176 | 4695 (context only — B12 closed) |
| спор о границе квартиры | 55+11176 | API empty |
| машино-место егрн | 55+11176 | 4 (rejected — live WP has кладовка cluster today) |
| **долг по капремонту** | **55+11176** | **29** |
| долг по капремонту новый собственник | 55+11176 | 6 |
| долги по капремонту переходят на нового собственника | 55+11176 | 4 |
| справка об отсутствии долгов по капремонту | 55+11176 | 3 |
| долг по капремонту | 225 (compare) | API partial — related «капитальный ремонт это» 166 in Tyumen tree |

**wordstat_rework log:**
- probe «переуступка дду» 55+11176 → 25 (on-plot novostroyka but overlaps B12 escrow/DDU — skip)
- probe «переуступка квартиры» 55+11176 → 55 (assignment angle weak local volume)
- probe «спор о границе квартиры» → API empty
- probe «машино-место егрн» 55+11176 → 4 (dup risk with storage_room live plot)
- **rework:** buyer-жаргон «долг капремонт новый собственник» + проверка УК перед авансом → plot-demand «долг по капремонту» 29 (niche) + **final P0 demand spine «купить квартиру в тюмени вторичка» 4146** (buyer seed for gate; plot stays kapremont casus)

## signal_urls (research)

- https://www.consultant.ru/law/podborki/perehodyat_li_dolgi_po_kapremontu_na_novogo_sobstvennika/ — ЖК РФ ст. 158: долг переходит к новому собственнику
- https://rapsinews.ru/legislation_news/20260331/311728759.html — законопроект 1192673-8 (контекст августа 2026: правило пока не изменено)
- https://oblgazeta.ru/infrastructure-and-construction/overhaul/2024/08/61562/ — как проверить долг по капремонту перед сделкой
- https://dzen.ru/holyslav — канал holyslav (buyer casus energy, не дубль кластера)
- https://t.me/holyslav92
- https://t.me/klyshin_A — checked, not used this slot

## Output required

Write complete Scout handoff markdown per SKILL.md.

**HARD — include these exact flat `key: value` lines (not only bullets) for wordstat_gate.py:**

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: optional | none | original: none | signal: https://t.me/klyshin_A (checked, not used)
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: <ids>
dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
comment_magnet_angle: «…?»
wordstat_rework: probe «переуступка дду» 25 → … → plot «долг по капремонту» 29 → final P0 «купить квартиру в тюмени вторичка» 4146
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени вторичка» 4146 | plot-demand «долг по капремонту» 29
story_dup_check: PASS | cluster_id: kapremont_debt_new_owner_blocks_sale
```

Then full handoff sections (Topic lock, Research brief, signal_urls, etc.).

Lock topic_id B19, title, slug, signal_urls, research angles for Research role.
