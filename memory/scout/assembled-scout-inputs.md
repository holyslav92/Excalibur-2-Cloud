# Scout inputs — 2026-09-07 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-07 (YEKT Monday slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 29 active locks (2026-09-07)
- **Live WP / EXCALIBUR_RECENT_WP_POSTS 2026-09-05–06 — DO NOT reuse plot:**
  - эскроу не хватило 400к до суммы ДДУ
  - ДДУ 12 соток → кадастр 8 (КП/участок)
  - застройщик продал 1 квартиру 2 семьям
  - доплата 300к за отделку перед ключами
  - перенос сдачи 7 мес + неустойка 340к не выплачена
  - ДДУ 45 м² → декларация 41
  - приёмка брак → штраф 190к
  - апартаменты вместо квартиры (B23)
  - рассрочка — потеря скидки при досрочном закрытии
  - запрет аренды до ключей (инвестор)
  - переуступка +280к за сутки
  - трейд-ин сорвался за день до ДДУ
- **Rejected overlap:** машино-место/кладовка по ДДУ → overlap B21 cellar cluster
- **Rejected overlap:** площадь меньше в декларации → live 45→41 м² cluster
- **Rejected overlap:** неустойка за просрочку ключей → live 7 мес / 340к cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир, дду)
- `excalibur_blog_scout_story_dup.py` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени в ДДУ был 12-й этаж — на ключах отдали квартиру на 2-м
- **slug:** v-tyumeni-v-ddu-byl-12-etazh-na-klyuchah-otdali-kvartiru-na-2-m
- **cluster_id (new):** ddu_floor_changed_at_keys_tyumen
- **story_dup_check:** PASS — distinct plot: в ДДУ и брони зафиксирован 12-й этаж (вид, тишина, цена выше нижних этажей); на выдаче ключей застройщик ведёт в квартиру на 2-м этаже со ссылкой на «перераспределение секции» / «техническую корректировку проекта»; покупатель отказывается подписывать акт, банк не выдаёт остаток ипотеки без акта, спор о расторжении ДДУ или замене объекта

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру на 12-м этаже в новостройке, внесла бронь и подписала ДДУ с указанием этажа в приложении
- **risk:** на ключах объект физически на 2-м этаже — другой вид, шум, безопасность, рыночная цена ниже; застройщик ссылается на изменение проектной документации; без акта приёмки ипотека и регистрация права стопорятся
- **time:** в день выдачи ключей / на приёмке (через 2–3 года после ДДУ, в день, когда семья приехала с мебелью)
- **finale:** акт не подписали; застройщик предложил «компенсацию скидкой на паркинг» — отказ; претензия и приостановка платежей по ипотеке; ключи не получили, дело ушло в досудебку (или суд о замене объекта / расторжении ДДУ)
- **comment_magnet_angle:** «В ДДУ чётко написан 12-й этаж, а ключи от 2-го: вы бы подписали акт ради мебели и ипотеки или ушли бы в суд, даже если застройщик даст скидку на паркинг?»

## Top energy + newbuild mapping

- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** этаж/секция в ДДУ и приложении vs фактическая квартира на выдаче ключей; изменение проектной документации застройщиком
- **why_newbuild_not_secondary:** сюжет целиком в цепочке ДДУ → сдача → акт приёмки → ипотека/эскроу; нет продавца вторички, ЕГРН-наследников или осмотра у бабушки

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild floor-mismatch casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-07)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| этаж новостройка дду | 55+11176 | API empty (no tail) |
| приемка новостроек тюмень | 55+11176 | 36 |
| приемка квартиры в новостройке тюмень | 55+11176 | 33 |
| купить новостройку в тюмени | 55+11176 | 865 |
| **новостройки тюмень** | **55+11176** | **4663** |
| **новостройки тюмень** | **225 (compare)** | **8691** |

**wordstat_rework log:**
- probe «этаж новостройка дду» 55+11176 → empty (слишком узко; не drop casus)
- probe «приемка новостроек тюмень» 55+11176 → 36 (on-topic keys stage, weak spine)
- probe «купить новостройку в тюмени» 55+11176 → 865 (buyer intent, ok)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, ключи, приёмка) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4663 (55+11176) / 8691 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст канала, не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ / изменение проектной документации
- https://www.consultant.ru/document/cons_doc_LAW_122475/ — 214-ФЗ ДДУ, права дольщика при изменении объекта
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
