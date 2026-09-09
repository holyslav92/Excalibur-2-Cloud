# Scout inputs — 2026-09-09 (B24, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-09 (YEKT weekday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{SITE_BASE}})
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 26 active locks (last_sync 2026-09-09)
- **Live WP last ~20 (2026-09-05..09) — DO NOT reuse plot:**
  - приёмка без замечаний → банк остановил транш (2026-09-09)
  - ключи без разрешения на ввод — банк заморозил ипотеку (2026-09-08)
  - долг 94 тыс на переуступке (2026-09-08)
  - маткапитал за 3 недели до ключей / детские доли (2026-09-08)
  - созаёмщика исключили за 7 дней до ДДУ (2026-09-07)
  - рассрочка: 5 дней просрочки — удержали 180 тыс (2026-09-07)
  - газ у коттеджа 180 м (2026-09-07)
  - этаж 12→2 на ключах (2026-09-07)
  - эскроу не хватило 400к (2026-09-06)
  - участок 12→8 соток (2026-09-06)
  - двойная продажа квартиры двум семьям (2026-09-06)
  - доплата 300к за отделку перед ключами (2026-09-06)
  - неустойка 340к не выплатили (2026-09-05)
  - площадь 45→41 м² (2026-09-05)
  - штраф 190к за отказ подписать акт с браком (2026-09-05)
  - апартаменты вместо квартиры B23 (2026-09-05)
  - оценка банка ниже на 400к (2026-09-05 live)
  - банк поднял ставку B22
  - кладовка B21, эскроу B19, смена юрлица B20
- **Ledger last 3 mechanisms:** B21 кладовка/ДДУ; B22 ставка ипотеки; B23 квартира vs апартаменты — новый mechanism обязателен
- `scout_helper.py --check-query` PASS
- `excalibur_blog_topic_focus.py` PASS
- `scout_story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени ребёнку исполнилось 7 лет накануне ДДУ — семейную ипотеку пересчитали
- **short_title (research_start):** Ребёнку 7 лет накануне ДДУ — семейную ипотеку пересчитали
- **slug:** v-tyumeni-rebenku-ispolnilos-7-let-nakanune-ddu-semejnuyu-ipoteku-pereschitali
- **cluster_id (new):** newbuild_family_mortgage_child_age_clock_tyumen
- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** семейная ипотека на новостройку привязана к возрасту ребёнка (льгота действует, пока ребёнку нет 7 лет); за 5–7 дней до подписания ДДУ ребёнку исполнилось 7 лет → банк пересчитал ставку/лимит → ежемесячный платёж и одобренная сумма не сходятся с бронью в ЖК
- **why_newbuild_not_secondary:** сделка через ДДУ с застройщиком, бронь на квартиру в новостройке, эскроу и ипотечный транш — не покупка вторички; риск в тайминге программы до подписания договор долевого участия

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени получила предварительное одобрение семейной ипотеки на квартиру в новостройке, внесла бронь и готовилась к подписанию ДДУ
- **risk:** накануне подписания (за 5–7 дней) младшему ребёнку исполнилось 7 лет — банк снял льготную ставку/урезал лимит кредита; разница в ежемесячном платеже и недостающий первоначальный взнос
- **time:** «за шесть дней до ДДУ» / «накануне подписания»
- **finale:** банк отказал выдавать кредит на прежних условиях; бронь сгорела, застройщик не продлил цену — семья остановилась до перевода на эскроу (или внесла доплату из резерва и успела переподать документы — финал с потерей брони/переплатой)
- **comment_magnet_angle:** «Ребёнку исполнилось 7 лет за неделю до ДДУ: вы бы торопили подпись или снимали бронь и искали другой банк?»

## Klyshin hook

- **klyshin_hook:** none | fresh Tyumen newbuild casus without Klyshin (preferred; avoids family-mortgage+escrow B19 cluster and Sept live plots)

## Wordstat MCP-KV (live 2026-09-09)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| семейная ипотека тюмень | 55+11176 | 1210 |
| семейная ипотека в тюмени | 55+11176 | 752 (top child) |
| новостройки тюмени семейная ипотека | 55+11176 | 27 |
| семейная ипотека в тюмени | 225 (compare) | 1099 |
| купить новостройку в тюмени | 55+11176 | 885 (context) |
| страхование ипотеки | 55+11176 | 1142 (rejected — no casus post, but weaker story fit vs child-age clock) |

**wordstat_rework log:**
- probe «новостройки тюмени семейная ипотека» 55+11176 → 27 (on-topic newbuild but weak spine)
- probe «семейная ипотека тюмень» 55+11176 → 1210; top «семейная ипотека в тюмени» → 752
- compare RU225 «семейная ипотека в тюмени» → 1099
- **rework:** localize Tyumen + family buyer jargon (семейная ипотека, ДДУ, новостройка, возраст ребёнка) → **final P0 «семейная ипотека в тюмени» regions 55,11176,compare225 freq 752 (55+11176) / 1099 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://www.consultant.ru/document/cons_doc_LAW_483391/ — 102-ФЗ / семейная ипотека (контекст возраста)
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard: PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
