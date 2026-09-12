# Scout inputs — 2026-09-08 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-08 (YEKT weekday slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 28 active locks (last_sync 2026-09-08)
- **Live WP Sep 5–7 (~12 titles) — DO NOT reuse plot:**
  - созаёмщика убрали за 7 дней до ДДУ
  - рассрочка застройщика — 5 дней просрочки, ДДУ расторгли
  - газ у коттеджа в ДДУ vs факт 180 м
  - этаж в ДДУ 12-й — на ключах 2-й
  - на эскроу не хватило 400 тыс до ДДУ
  - участок 12 соток в ДДУ — кадастр 8
  - двойная продажа одной квартиры
  - доплата 300 тыс за отделку перед ключами
  - задержка ключей 7 мес — неустойка не выплачена
  - площадь 45 м² в ДДУ — декларация 41
  - штраф 190 тыс за отказ подписать акт с браком
  - апартаменты вместо квартиры в выписке (B23)
- **Distinct from B18** `matkapital_missing_child_shares` (secondary ЕГРН plot) — this slot is **newbuild DDU + matkapital + child shares wording before keys**
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новострой, дду, маткапитал)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени маткапитал внесли в ДДУ на новостройку — за три недели до ключей сделку остановили
- **slug:** v-tyumeni-matkapital-v-ddu-na-novostrojku-pered-klyuchami-sdelku-ostanovili
- **cluster_id (new):** newbuild_matkapital_child_shares_ddu_blocked
- **story_dup_check:** PASS — distinct legal plot: семья направила маткапитал в первоначальный взнос по семейной ипотеке на новостройку, подписала ДДУ; в договоре и приложениях **нет корректной формулировки об обязательстве выделить доли детям**; за три недели до выдачи ключей ПФР/банк остановили сделку — без исправления ДДУ или соглашения о долях регистрация права невозможна

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени купила квартиру в новостройке с маткапиталом и семейной ипотекой, деньги на эскроу, дом сдан
- **risk:** маткапитал использован, но в ДДУ не прописано обязательство выделить доли детям в срок — ПФР отказывает в согласовании, банк блокирует регистрацию права
- **time:** за три недели до подписания акта приёмки и получения ключей
- **finale:** сделку остановили; застройщик отказался бесплатно переподписывать ДДУ; семья внесла допсоглашение через юриста — ключи перенесли на месяц, без исправления риск расторжения и возврата маткапитала
- **comment_magnet_angle:** «Доли детям — прямо в ДДУ или отдельным соглашением до подписания: где бы вы поставили красную линию, если ключи уже «на подходе»?»

## Top-energy mirror

- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** маткапитал + семейная ипотека на ДДУ новостройки — обязательство выделить доли детям не зафиксировано в договоре; ПФР/банк блокируют регистрацию за 3 недели до ключей
- **why_newbuild_not_secondary:** сюжет в цепочке ДДУ/застройщик/эскроу/ипотека на новостройку; не покупка вторички и не проверка детских долей в ЕГРН продавца (B18)

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild matkapital casus without Klyshin — preferred; avoids Sep 5–7 live plots)

## Wordstat MCP-KV (live 2026-09-08)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| маткапитал новостройка | 55,11176,225 | 349 |
| новостройки с маткапиталом | 55,11176,225 | **175** |
| маткапитал ипотека новостройка | 55,11176,225 | 102 |
| выделение долей детям маткапитал | 225 (compare) | 872 |
| приемка квартиры новостройка тюмень | 55 | 65 (rejected — acceptance fine cluster Sep 5) |
| рассрочка от застройщика тюмень | 55 | 110 (rejected — installment cancel Sep 7) |

**wordstat_rework log:**
- probe «маткапитал новостройка» 55,11176,225 → 349; top «новостройки с маткапиталом» → 175
- probe «маткапитал ипотека новостройка» → 102 (supporting)
- probe «выделение долей детям маткапитал» RU225 → 872 (mechanism demand spine)
- rejected weak/overlap probes: приёмка (Sep 5), рассрочка (Sep 7)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, маткапитал, ДДУ, доли детям) → **final P0 «новостройки с маткапиталом» regions 55,11176,compare225 freq 175**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и семейной ипотеки
- https://www.consultant.ru/document/cons_doc_LAW_25659/ — 256-ФЗ материнский капитал / выделение долей
- https://www.domrf.ru/ — справочник застройщиков / ДДУ
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
