# Scout inputs — 2026-09-16 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-16 (YEKT weekday slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — recent WP ~20)

Do NOT recycle plots from last ~14 days:
- бронь/этаж vs ДДУ секция (booking_expired_price_hike)
- переуступка не согласована / аванс завис (assignment)
- газ в КП на ключах (KP utilities)
- банк снял ЖК с аккредитации
- фиксация цены / прайс ЖК вырос
- двойная бронь на одну квартиру
- площадь −2 кв.м на приёмке
- маткапитал + 7 лет ребёнку накануне эскроу
- трёшка→двушка перед эскроу
- приёмка новостройки для родителей / лифт
- банковская оценка ниже ДДУ (LIVE-V-TYUMENI-BANK-OCENIL-NO)
- эскроу ноль vs сумма ДДУ, ставка накануне ДДУ, trade-in, рассрочка штраф, РВЭ без разрешения (B26)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 28 active locks (last_sync 2026-09-16)
- Live WP recent titles ingested via `excalibur_blog_today.py` EXCALIBUR_RECENT_WP_POSTS (12 posts 2026-09-13..15)
- `shared/published-articles.md` + `shared/published-titles.md` read
- `scout_helper.py --check-query` PASS
- `excalibur_blog_topic_focus.py` PASS
- `story_dup.py --text` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B27
- **title_draft:** В Тюмени банк отказал созаёмщику по семейной ипотеке — за 4 дня до эскроу сделку остановили
- **slug:** v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou
- **article_dir:** memory/blog/articles/B27-v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou
- **cluster_id (new):** newbuild_coborrower_rejected_family_mortgage
- **top_energy_mirror:** stopped_before_money
- **newbuild_mechanism:** Семья взяла **семейную ипотеку** на квартиру в новостройке по ДДУ; муж — заёмщик, жена — **созаёмщик** с доходом. За 4 дня до открытия **эскроу** банк отклонил созаёмщика (скоринг/кредитная история/несоответствие документов о доходе) → одобрение семейной ипотеки **аннулировали**, бронь на квартиру в ЖК под угрозой, деньги на эскроу не ушли
- **why_newbuild_not_secondary:** цепочка ДДУ + семейная ипотека + эскроу + бронь у застройщика; нет продавца вторички, ЕГРН, наследников, бабушки или маткапитала на вторичке
- **story_dup_check:** PASS — отличается от escrow_not_opened_after_mortgage (B19: эскроу не открылся), mortgage_rate_hike_before_ddu (ставка), matkapital 7 лет (возраст ребёнка), bank accreditation, bank appraisal

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала двушку в новостройке, одобрили семейную ипотеку на двоих, застройщик держал бронь до эскроу
- **risk:** без двух заёмщиков банк не даёт лимит семейной ипотеки → не хватает на квартиру; отказ созаёмщика = срыв всей сделки
- **time:** за 4 дня до даты открытия эскроу-счёта; срок брони — ещё 6 дней
- **finale:** семья остановила подписание ДДУ, сняли бронь без штрафа по письму застройщика; искали замену созаёмщика (родителя) — банк отказал; квартиру ушла в продажу другому покупателю через 11 дней
- **comment_magnet_angle:** «Семейную ипотеку одобрили на двоих, а за четыре дня до эскроу банк “зарубил” созаёмщика: вы бы успели подобрать другого или сразу снимали бы бронь?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-16)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| созаемщик ипотека | 55,11176 | 515 |
| семейная ипотека есть ли созаемщики | 55,11176 | 15 (tail) |
| новостройки тюмени семейная ипотека | 55,11176 | 24 |
| купить новостройку в тюмени | 55,11176 | 902 |
| новостройки тюмень | 55,11176 | 4475 |
| **семейная ипотека тюмень** | **55,11176** | **1240** |
| семейная ипотека тюмень | 225 (compare RU) | 1745 |

**wordstat_rework log:**
- probe «созаемщик ипотека» 55,11176 → 515 (механика сюжета, слабее как P0 spine)
- probe «новостройки тюмени семейная ипотека» → 24 (слабый)
- probe «купить новостройку в тюмени» → 902 (сильный buyer, но менее точный к casus)
- **rework:** локализация семейная ипотека + Тюмень → **final P0 «семейная ипотека тюмень» regions 55,11176,compare225 freq 1240 (55+11176) / 1745 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — семейная ипотека, аккредитованные ЖК
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, эскроу
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used

## Director next

```bash
python3 scripts/excalibur_blog_research_start.py --topic-id B27 --title "В Тюмени банк отказал созаёмщику по семейной ипотеке — за 4 дня до эскроу сделку остановили"
```
