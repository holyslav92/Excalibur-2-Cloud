# Scout inputs — B34 slot 12:00 YEKT 2026-10-01

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-01
**slot:** 12:00 YEKT
**slot_rubric:** novostroyki (новостройки)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Trend Radar (2026-10-01, slot novostroyki)

Top viral **energy** (do NOT copy rent/secondary plots): «Потерять квартиру из-за сдачи в аренду» (231k views, mechanism «договор vs реальность»). Map to **newbuild ONLY**: семейная ипотека + ДДУ/эскроу + запрет/риск сдачи до регистрации, банк снимает одобрение до денег на эскроу.

## Slot constraints (HARD FORBIDDEN today / 30d)

- NO Oct 1 09:00 live: школа в рекламе ЖК vs декларация 2030, ДДУ не подписали (declaration/ad mismatch — other mechanism)
- NO escrow_not_opened_after_mortgage cluster (subcontractor finish, Oct 28 lock)
- NO ddu_apartment_vs_apartments, booking_expired_price_hike, bank_appraisal, keys_delay, acceptance_defects, ddu_amount_vs_escrow_zero, assignment ban B30, insurance B31, wrong escrow entity B32, birth cert B29, area cut escrow, cosigner escrow, frozen wall acceptance, courtyard bron change
- NO secondary: банкрот продавца, долг за свет B33, пристав, дарственная, аренда в ЕГРН вторички
- NO frozen secondary retitle (бабушка, ЕГРН, опека…)
- Full locks: memory/scout/used-clusters.json (synced 2026-10-01)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 15 active locks
- Live WP recent (~12): школа в рекламе ЖК 2026-10-01; банкротство продавца; пристав; двор без машин; промёрзшая стена; аренда 3 года ЕГРН; дарственная; площадь ДДУ; свидетельство ребёнка; долг за свет; чистовая подрядчик; созаёмщик
- `scout_helper.py --check-query` PASS
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B34
- **title_draft:** За 4 дня до эскроу в Тюмени нашли объявление на сдачу квартиры в новостройке — семейную ипотеку сняли
- **slug:** v-tyumeni-za-4-dnya-do-eskrou-obyavlenie-na-sdachu-snyalo-semejnuyu-ipoteku
- **article_dir:** memory/blog/articles/B34-v-tyumeni-za-4-dnya-do-eskrou-obyavlenie-na-sdachu-snyalo-semejnuyu-ipoteku
- **cluster_id (new):** newbuild_rental_listing_family_mortgage_revoked_tyumen
- **top_energy_mirror:** almost_lost_home (вирусный угол «потерять жильё из-за аренды») + stopped_before_money (остановили до эскроу)
- **newbuild_mechanism:** Семья с двумя детьми берёт квартиру в ЖК в Тюмени по семейной ипотеке. Пока ждут ключи, родственник «на всякий случай» выложил объявление на сдачу будущей квартиры (фото с брони/визитки застройщика). За 4 дня до открытия эскроу банк при мониторинге целевого кредита увидел объявление, запросил пояснения по целевому использованию и **снял одобрение семейной ипотеки** — до подписания ДДУ и перевода на эскроу не дошли
- **why_newbuild_not_secondary:** Цепочка только новостройки: бронь/ДДУ, семейная ипотека на первичку, эскроу, запрет сдачи до регистрации в договоре банка/застройщика. Нет продавца вторички, ЕГРН сделки, аванса на вторичку, наследников или коммунальных долгов
- **story_dup_check:** PASS — не пересекается с B19 (эскроу+маткапитал), B31 (страховка), B29 (нулевой взнос), Oct 1 школа/декларация, B30 (уступка)

## Dzen news-casus shape (PASS)

- **event:** семья оформила бронь в новостройке Тюмени, получила одобрение семейной ипотеки, назначили дату открытия эскроу
- **risk:** без ипотеки не тянут ДДУ; бронь сгорает; объявление на сдачу до регистрации = нарушение целевого кредита
- **time:** за 4 дня до эскроу, вечером после звонка кредитного инспектора
- **finale:** банк отозвал одобрение, эскроу не открыли, ДДУ перенесли и не подписали; семья сняла объявление, пересобрала пакет через другой банк через 3 недели (другая ставка — отдельная боль, не sugar ending)
- **comment_magnet_angle:** «Если родственник выложил сдачу „на будущее“, а банк снял семейную ипотеку за 4 дня до эскроу — кого вините: семью, банк или того, кто нажал „опубликовать“?»

## Klyshin hook

- **klyshin_hook:** none (свежий Tyumen casus без Klyshin)

## Wordstat MCP-KV (live 2026-10-01)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions 55+11176 | freq |
|-------|------------------|------|
| сдача квартиры новостройка до регистрации | 55,11176 | API empty (~0–1) |
| семейная ипотека новостройка тюмень | 55,11176 | 43 |
| сдать квартиру в новостройке | 55,11176 | 1230 (в выдаче доминант «сданные новостройки купить», не наш сюжет) |
| семейная ипотека тюмень | 55,11176 | **2062** |
| купить новостройку в тюмени | 55,11176 | 1907 |
| новостройки тюмень | 55,11176 | 8295 |

**Compare RU (225):** новостройки тюмень — запрос локальный; для compare контекст «новостройки» RU-scale (типично десятки тысяч+ по смежным; spine локальный).

**wordstat_rework:**
- probe «сдача квартиры новостройка до регистрации» → пусто/1 (слабо для P0)
- probe «семейная ипотека новостройка тюмень» → 43 (слабо)
- **rework:** якорь buyer P0 «семейная ипотека тюмень» + механика сдачи/эскроу в H1 и теле
- **final P0 «семейная ипотека тюмень» regions 55,11176,compare225 freq 2062**

## Required handoff fields (output all)

wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape, comment_magnet_angle, wordstat_rework, wordstat line, story_dup_check, h1_fingerprint_check, formula_spam_check, anti_dupe_hard, slot_rubric=novostroyki, quad gate PASS (Trend Radar × Wordstat × news-casus × slot rubric × anti-dupe)
