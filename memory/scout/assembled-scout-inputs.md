# Scout inputs — 2026-09-08 (B24, slot ~15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-08 (YEKT weekday slot ~15:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-08)
- **Live WP 2026-09-08 (~12 titles) — DO NOT reuse plot:**
  - маткапитал в ДДУ за 3 недели до ключей (детские доли)
  - семейная ипотека — созаёмщика убрали за 7 дней до ДДУ
  - рассрочка застройщика — 5 дней просрочки, удержали 180к
  - газ в ДДУ на коттедж — 180 м до магистрали
  - этаж 12 в ДДУ → 2-й на ключах
  - эскроу не хватило 400к до ДДУ
  - участок 12 соток → 8 в кадастре
  - двойная продажа одной квартиры двум семьям
  - доплата 300к за отделку перед ключами
  - перенос сдачи 7 мес + неустойка 340к не выплачена
  - площадь 45 м² → 41 в декларации
  - штраф 190к за отказ подписать акт с браком на приёмке
- **Last 3 published mechanisms (formula spam guard):** matkapital DDU child shares | family mortgage co-borrower removed | developer installment 5-day delay — **must use DIFFERENT newbuild_mechanism**
- **Rejected overlap:** переуступка +280к за сутки / бронь сгорела → closed cluster `booking_expired_price_hike` + `assignment_lost_to_faster_buyer`
- **Rejected overlap:** оценка банка ниже ДДУ → closed `bank_appraisal_below_ddu_price`
- **Rejected overlap:** трейд-ин за день до ДДУ → closed `trade_in_rejected_developer`
- **Rejected overlap:** приёмка брак + штраф 190к → published 2026-09-05 (same-day cluster)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug (pre-validated by conductor)
- `excalibur_blog_topic_focus.py` PASS (on-focus: переуступк, новостройк, дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени на переуступке по новостройке нашли долг 94 тысячи — в день ДДУ сделку остановили
- **slug:** v-tyumeni-na-pereustupke-po-novostrojke-nashli-dolg-94-tysyachi-v-den-ddu-sdelku-ostanovili
- **cluster_id (new):** newbuild_assignment_first_buyer_debt_blocks_ddu_tyumen
- **story_dup_check:** PASS — distinct investor plot: инвестор купил переуступку по ДДУ, за 11 дней до ключей нашёл покупателя на вторую переуступку; в офисе застройщика в день подписания ДДУ с новым покупателем вскрывается **непогашенный долг первого дольщика** (94 тыс. руб. просроченных платежей по графику) → застройщик отказывает в переоформлении, бронь второго покупателя сгорает, инвестор теряет сделку и вынужден гасить долг или искать нового покупателя

## Top-energy mirror + newbuild mechanism

- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** переуступка до ключей / скрытый долг первого дольщика перед застройщиком блокирует переоформление в день ДДУ
- **why_newbuild_not_secondary:** сюжет о праве требования по ДДУ и цепочке переуступок в строящемся ЖК до получения ключей; нет продавца-физлица на вторичке, риск в графике платежей первого дольщика и политике застройщика по уступкам

## Dzen news-casus shape (target PASS)

- **event:** инвестор в Тюмени купил переуступку в новостройке, нашёл покупателя на вторую уступку, все копии ДДУ и согласия застройщика «на месте»
- **risk:** у первого дольщика в цепочке непогашенная задолженность 94 тыс. руб. перед застройщиком — без погашения застройщик не подписывает новый ДДУ
- **time:** в день подписания ДДУ с новым покупателем (за 11 дней до выдачи ключей)
- **finale:** застройщик остановил переоформление; бронь второго покупателя (50 тыс.) не вернули; инвестор остался с объектом и долгом чужого дольщика — сделка сорвалась, ключи не получил в срок
- **comment_magnet_angle:** «Покупатель переуступки обязан закрывать долг первого дольщика — или вы бы сорвали сделку в последний день, даже если квартира уже «ваша» по договору?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen investor-assignment debt casus without Klyshin — preferred; avoids today's 12 live plots and closed assignment-price-hike clusters)

## Wordstat MCP-KV (live 2026-09-08)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| переуступка новостройки | 55 | 14 |
| переуступка новостройки | 11176 | 16 |
| переуступка по дду | 55 | 14 |
| ипотека на переуступку | 55 | 7 |
| риски покупки квартиры по переуступке в новостройке | 55+11176+225 | 10 |
| покупка квартиры в новостройке переуступка | 55 | 5 |
| **новостройки тюмень** | **55** | **3634** |
| новостройки тюмень | 11176 | (included in Tyumen metro) |
| **новостройки тюмень** | **225 (compare)** | **8566** |
| **купить новостройку в тюмени** | **55** | **662** |
| купить новостройку в тюмени | 225 (compare) | 1890 |

**wordstat_rework log:**
- probe «переуступка новостройка тюмень» 55 → empty/error (no stable local tail)
- probe «переуступка новостройки» 55 → 14 / 11176 → 16 (on-topic but weak local volume)
- probe «переуступка по дду» 55 → 14; «ипотека на переуступку» 55 → 7 (weak)
- probe «риски покупки квартиры по переуступке в новостройке» → 10 (combined); story-specific spine confirmed
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, переуступка, купить новостройку) → **final P0 «купить новостройку в тюмени» regions 55,11176,compare225 freq 662 (55) / 8566 (RU225 newbuild spine «новостройки тюмень» 3634/55)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и переуступок; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ / ДДУ / уступка права требования
- https://www.domrf.ru/ — справочник застройщиков / проектные декларации
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, anti_dupe_hard: PASS, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
