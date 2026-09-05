# Scout inputs — 2026-09-05 (B23)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **Live WP 2026-09-05 (~12 titles) — DO NOT reuse plot:**
  - инвестор: аренда запрещена до ключей в ДДУ
  - переуступка +280к за сутки до ДДУ
  - трейд-ин сорвался за день до ДДУ
  - оценка банка ниже цены ДДУ на 400к
  - категория земли сорвала ипотеку на дом в посёлке
  - аванс на чужой счёт
  - банк поднял ставку ипотеки перед ДДУ (B22)
  - застройщик потребовал акт с дефектами — иначе без ключей
  - банк снял одобрение ипотеки за 72 часа до ДДУ
  - чистовая vs предчистовая в ДДУ
  - ключи задержали 8 месяцев — неустойка сертификатом
  - на приёмке не хватило метров — отказ в пересчёте
- **Rejected overlap:** parking/cellar angle «оплатили машиноместо по ДДУ» → 47% overlap with B21 cellar cluster
- **Rejected overlap:** matkapital/PFR return → overlap with live «банк снял одобрение 72ч»
- **Rejected overlap:** developer installment cancelled → overlap with trade-in/day-before-DDU cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир, дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени в ДДУ написали квартиру — в выписке оказались апартаменты
- **slug:** v-tyumeni-v-ddu-napisali-kvartiru-v-vypiske-okazalis-apartamenty
- **cluster_id (new):** newbuild_apartments_instead_flat_ddu_tyumen
- **story_dup_check:** PASS — distinct legal plot: в ДДУ и рекламе объект назван «квартира»/жилое помещение, семья внесла аванс и подписала ипотеку под жильё; при регистрации права в Росреестре в выписке ЕГРН статус — **апартаменты** (нежилое/коммерческое назначение) → выше коммуналка, нет прописки, ипотечная программа под угрозой, застройщик ссылается на формулировку в приложении к ДДУ

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала «квартиру» в новостройке, подписала ДДУ и ипотеку, деньги ушли на эскроу
- **risk:** при подаче на регистрацию права в ЕГРН объект зарегистрирован как **апартаменты**, а не жилое помещение — нет постоянной регистрации, коммунальные тарифы как у коммерции, семейная/льготная ипотека может не пройти, налог и перепродажа по другим правилам
- **time:** на этапе регистрации права после сдачи дома / перед получением ключей (через 2–3 недели после подачи документов)
- **finale:** банк приостановил выдачу остатка ипотеки; застройщик отказался менять назначение; семья остановила приёмку и подала претензию — ключи не получили, спор ушёл в досудебку (или суд с требованием признать объект жилым / расторгнуть ДДУ)
- **comment_magnet_angle:** «В ДДУ везде написано „квартира“, а в выписке — апартаменты: вы бы всё равно подписали акт приёмки или шли бы в суд, даже если ключи уже «на столе»?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild apartments-vs-flat casus without Klyshin — preferred; avoids today's 12 live plots and B21 cellar/parking overlap)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| апартаменты тюмень | 55 | 646 (noisy tail — отели/прочее) |
| купить апартаменты в тюмени | 55 | 35 (buyer, narrow) |
| маткапитал новостройка | 55 | 1 (rejected — B19 escrow cluster) |
| рассрочка застройщик новостройка | 55 | 2 (rejected — overlap trade-in/day-before-DDU) |
| машиноместо новостройка | 55 | 2 (rejected — 47% overlap B21 cellar) |
| **новостройки тюмень** | **55** | **3640** |
| новостройки тюмень | 11176 | (included in Tyumen metro demand) |
| **новостройки тюмень** | **225 (compare)** | **8705** |
| купить новостройку в тюмени | 55 | 639 (context) |

**wordstat_rework log:**
- probe «апартаменты тюмень» 55 → 646; top child «купить апартаменты в тюмени» → 35 (on-topic but weak vs newbuild spine; tail polluted)
- probe «маткапитал новостройка» 55 → 1 (weak; matkapital/escrow plot taken by B19)
- probe «машиноместо новостройка» 55 → 2 (weak; cellar/parking plot overlap B21)
- probe «рассрочка застройщик новостройка» 55 → 2 (weak; day-before-DDU timing cluster on live)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, выписка ЕГРН) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 3640 (55) / 8705 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и ипотеки; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ / жилое vs нежилое (контекст апартаментов)
- https://www.domrf.ru/ — справочник застройщиков / ДДУ (контекст регистрации)
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
