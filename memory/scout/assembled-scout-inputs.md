# Scout inputs — 2026-09-06 (B24, Sunday 12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-06 (YEKT Sunday slot 12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → active locks synced 2026-09-06
- **Live WP 2026-09-05–06 (~15 titles) — DO NOT reuse plot:**
  - доплата 300к за «улучшенную отделку» перед ключами (2026-09-06)
  - ключи задержали 7 мес — неустойку 340к не выплатили
  - ДДУ 45 м² vs декларация 41 м²
  - приёмка с браком — штраф 190к от застройщика
  - апартаменты вместо квартиры в ЕГРН (B23)
  - рассрочка — потеряли скидку при досрочном закрытии
  - инвестор: аренда запрещена до ключей
  - переуступка +280к за сутки до ДДУ
  - трейд-ин сорвался за день до ДДУ
  - оценка банка ниже цены ДДУ на 400к
  - категория земли сорвала ипотеку на дом в посёлке
  - банк поднял ставку ипотеки перед ДДУ (B22)
  - кладовка в ДДУ — на ключах не оказалось (B21)
- **Rejected:** паркинг/машиноместо → overlap B21 cellar cluster
- **Rejected:** семейная ипотека квота банка → 37% overlap переуступка/day-before-DDU
- **Alternative PASS (not chosen):** КП газ только проект — distinct but weaker engagement vs double-sale
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир, дду, застройщик)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени застройщик продал одну квартиру двум семьям — второй ДДУ остановили
- **slug:** v-tyumeni-odnu-kvartiru-prodali-dvum-semyam-vtoroj-ddu-ostanovili
- **cluster_id (new):** newbuild_double_sale_same_unit_tyumen
- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** двойная продажа одного объекта в новостройке — две семьи подписали ДДУ/бронь на одну и ту же квартиру в одном ЖК; первая семья внесла аванс на эскроу, вторая пришла на подписание через 3 дня — в реестре договоров застройщика объект уже «занят»
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ/застройщик/эскроу новостройки; нет продавца-физлица, ЕГРН-вторички, наследников или банкротства продавца
- **story_dup_check:** PASS — уникальный plot: не переуступка, не бронь-сгорела-цена, не апартаменты, не отделка/доплата

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в строящемся ЖК, внесла бронь и подписала ДДУ; через несколько дней менеджер застройщика звонит второй семье с тем же номером квартиры
- **risk:** двойная продажа одного лота — у второй семьи уже одобрена ипотека и переведён аванс; у первой — зарегистрирован ДДУ; застройщик ссылается на «ошибку CRM» / смену планировки
- **time:** за 48–72 часа до подписания второго ДДУ / перед внесением остатка на эскроу
- **finale:** банк второй семьи остановил сделку; первая семья подала в Росреестр; застройщик предложил «аналогичную» квартиру на этаж выше с доплатой — вторая семья отказалась, вернула бронь частично, спор в досудебке
- **comment_magnet_angle:** «Если менеджер предлагает „точно такую же, но на этаж выше“ после двойной продажи — вы берёте или требуете именно свой номер в ДДУ?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild double-sale casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| **новостройки тюмень** | **55** | **4663** |
| новостройки тюмень | 11176 | (Tyumen metro) |
| **новостройки тюмень** | **225 (compare)** | **8705** |
| купить новостройку в тюмени | 55 | 865 |
| дду новостройка | 55 | (buyer context) |
| бронь новостройка тюмень | 55 | (weak, rework anchor) |

**wordstat_rework log:**
- probe «двойная продажа квартира» → low/niche; anchor to newbuild buyer spine
- **rework:** localize Tyumen + newbuild jargon (новостройки, ДДУ, бронь, эскроу, застройщик) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4663 (55) / 8705 (RU225)**

## signal_urls (research)

- https://www.consultant.ru/document/cons_doc_LAW_122757/ — 214-ФЗ, ДДУ, права дольщика
- https://www.domrf.ru/ — реестр застройщиков / проектная декларация
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, anti_dupe_hard: PASS, formula_spam_check PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
