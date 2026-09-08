# Scout inputs — 2026-09-08 (B24, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-08 (YEKT weekday slot ~12:00 / 17:00 MSK)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-08)
- **Live WP ~20 (2026-09-08) — DO NOT reuse plot:**
  - переуступка долг 94к — сделку остановили
  - маткапитал за 3 недели до ключей — детские доли
  - созаёмщика убрали за 7 дней до ДДУ
  - рассрочка застройщика — 5 дней просрочки, удержали 180к
  - газ у коттеджа в ДДУ — 180 м до магистрали
  - этаж 12→2 по ДДУ
  - эскроу не хватило 400к до ДДУ
  - 12→8 соток в кадастре
  - двойная продажа одной квартиры
  - доплата за отделку 300к перед ключами
  - перенос сдачи 7 мес + неустойка 340к
  - площадь 45→41 по декларации
  - на приёмке брак — застройщик потребовал 190к (2026-09-05)
  - апартаменты вместо квартиры в ЕГРН (B23)
- **Rejected overlap:** приёмка/дефекты/акт приёмки — live 2026-09-05 «на приёмке нашли брак — 190 тысяч»
- **Rejected overlap:** перенос ключей/неустойка — live 2026-09-05 «задержал ключи на 7 месяцев»
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: застройщик, дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени застройщик выдал ключи по ДДУ без разрешения на ввод — банк остановил остаток ипотеки
- **slug:** v-tyumeni-zastrojschik-vydal-klyuchi-po-ddu-bez-razresheniya-na-vvod-bank-ostanovil-ostatok-ipoteki
- **article_dir:** memory/blog/articles/B24-v-tyumeni-zastrojschik-vydal-klyuchi-po-ddu-bez-razresheniya-na-vvod-bank-ostano
- **cluster_id (new):** newbuild_keys_without_commissioning_mortgage_hold_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** ключи и акт приёма-передачи по ДДУ выдали до публикации разрешения на ввод в эксплуатацию; банк приостановил перевод остатка ипотеки на эскроу
- **why_newbuild_not_secondary:** сюжет про сдачу объекта застройщиком по ДДУ, разрешение на ввод и ипотечный транш после сдачи новостройки — не покупка вторички и не ЕГРН-риски продавца
- **story_dup_check:** PASS — distinct plot: ключи уже на руках, но в реестре/на сайте застройщика нет РНВ → банк не выдаёт остаток кредита, застройщик давит «акт подписан — всё нормально»

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени получила от застройщика ключи по ДДУ, подписала акт приёма-передачи, начала ремонт
- **risk:** разрешения на ввод в эксплуатацию в открытых реестрах ещё нет — банк отказывается переводить остаток ипотеки на эскроу; без транша семья платит из своих + ипотечный график «висит»
- **time:** через 5–10 дней после подписания акта, когда в банк подали на выдачу остатка кредита
- **finale:** банк заморозил выдачу до появления РНВ; застройщик ссылается на подписанный акт; семья остановила приёмку окончательно и подала претензию — спор до суда / досудебки
- **comment_magnet_angle:** «Ключи на руках, а ипотека не дошла: вы бы подписали акт, если в реестре ещё нет разрешения на ввод, или ждали бы РНВ, даже если застройщик торопит?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild commissioning casus without Klyshin — preferred; avoids today's 12 live plots)

## Wordstat MCP-KV (live 2026-09-08)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| ввод жк в эксплуатацию | 55,11176 | 21 |
| разрешение на ввод в эксплуатацию жк | 55,11176 | 9 |
| приемка квартиры в новостройке тюмень | 55,11176 | 32 (rejected — live acceptance defects 2026-09-05) |
| приемка квартиры в новостройке | 55,11176 | 122 |
| приемка квартиры в новостройке | 225 compare | 6032 |
| **купить квартиру в тюмени новостройка ипотека** | **55,11176** | **85** |
| купить квартиру в тюмени новостройка ипотека | 225 compare | 123 |
| квартира в тюмени купить новостройки | 55,11176 | 644 (context) |

**wordstat_rework log:**
- probe «ввод жк в эксплуатацию» 55,11176 → 21 (on-mechanism but weak alone)
- probe «разрешение на ввод в эксплуатацию жк» → 9 (weak)
- probe «приемка квартиры в новостройке тюмень» → 32 (rejected — overlaps live acceptance-defects cluster)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройка, ДДУ, ипотека, застройщик) → **final P0 «купить квартиру в тюмени новостройка ипотека» regions 55,11176,compare225 freq 85 (Tyumen) / 123 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ, ввод в эксплуатацию
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, article_dir, signal_urls, research angles for Research role.
