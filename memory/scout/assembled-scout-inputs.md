# Scout inputs — 2026-09-18 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**FORBIDDEN:** B26 / RVE / второй транш / разрешение на ввод — УЖЕ ОПУБЛИКОВАНО 2026-09-13. НЕ ПИШИ B26. ТОЛЬКО B27 ниже.

**run_date:** 2026-09-18 (YEKT Friday slot ~10:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (site blog tenant)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — live WP last ~20)

Closed / avoid same cluster:
- matkapital + детские доли в новостройке (LIVE 2026-09-17)
- приложение к ДДУ запретило аренду
- перенос в другой корпус перед ДДУ
- оценка банка ниже ДДУ (bank_appraisal_below_ddu_price)
- машино-место не в декларации
- страховка перед эскроу (186k)
- ключи с опозданием 9 мес (keys_delay_penalty_unpaid)
- отказ созаёмщику семейной ипотеки
- бронь этаж/вид vs ДДУ (booking_expired_price_hike)
- переуступка сорвалась (assignment)
- КП дом без газа
- банк снял ЖК с аккредитации
- B26 RVE + второй транш; B25 отделка; B23 апартаменты; B19 эскроу не открыли; B22 ставка накануне ДДУ

**Rejected during scout:**
- developer cash mimo escrow — fingerprint dup ddu_amount_vs_escrow_zero / insurance before escrow
- elevator at acceptance — acceptance_defects_penalty cluster locked
- turnkey kitchen missing — overlap B25/B21

## Anti-repeat preflight (DONE)

- `used-clusters.json` last_sync 2026-09-18 (user confirmed sync done)
- Live WP 20 titles fetched via wordpress_get_posts
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `story_dup.py --text` PASS
- `excalibur_blog_topic_focus.py` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B27
- **title_draft:** В Тюмени одобрение ипотеки сгорело на 87-й день — семья не успела на ДДУ
- **slug:** v-tyumeni-odobrenie-ipoteki-sgorelo-na-87-den-semya-ne-uspela-ddu
- **cluster_id (new):** mortgage_approval_expired_waiting_ddu_tyumen
- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** Банк одобрил ипотеку на новостройку по ДДУ; застройщик поставил семью в очередь на подписание — **87 дней** без выхода на эскроу; **срок действия одобрения (типично 90 дней)** истёк → банк аннулировал решение / предложил переодобрение под новые условия → до эскроу не дошли, бронь/лот под угрозой
- **why_newbuild_not_secondary:** цепочка «одобрение → очередь застройщика → проект ДДУ → эскроу»; нет продавца вторички, ЕГРН-вторички, наследников, бабушки или маткапитала-вторички
- **story_dup_check:** PASS — distinct from B19 (эскроу не открыли после одобрения), B22 (ставка выросла накануне ДДУ), LIVE co-borrower denied, LIVE accreditation removed, LIVE child turned 7, B26 RVE+tranche

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени получила одобрение ипотеки на квартиру в новостройке и внесла бронь; застройщик обещал «подписание на следующей неделе»
- **risk:** одобрение банка ограничено по сроку; без подписанного ДДУ и открытого эскроу деньги не уходят, но **решение банка «сгорает»**
- **time:** 87-й день после одобрения; за 3 дня до дедлайна менеджер прислал проект ДДУ
- **finale:** банк закрыл старое одобрение; новое — меньшая сумма и выше ставка; семья отказалась от подписания в этот день, сняла бронь до аванса — лот ушёл в продажу, деньги на эскроу не переводили
- **comment_magnet_angle:** «Очередь на ДДУ затянулась почти на три месяца — одобрение сгорело на 87-й день. Кто виноват: застройщик, брокер или семья должна была торопить банк с продлением?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-18)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| одобрение ипотеки срок действия | 55,11176 | 1 (weak — plot-specific) |
| срок действия одобрения ипотеки | 225 compare | 44 |
| ипотека тюмень новостройки от застройщика | 55,11176 | **100** |
| ипотека тюмень новостройки от застройщика | 225 compare | **146** |
| квартиры в тюмени новостройка ипотека | 55,11176 | 103 (alt) |
| новостройки тюмень | 55,11176 | 4480 (context) |

**wordstat_rework log:**
- probe «одобрение ипотеки срок действия» 55,11176 → 1 (weak; casus-specific)
- probe «срок действия одобрения ипотеки» 225 → 44 (compare only)
- **rework:** buyer spine newbuild + ипотека + Тюмень → **final P0 «ипотека тюмень новостройки от застройщика» regions 55,11176,compare225 freq 100 (55+11176) / 146 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ
- https://www.domrf.ru/
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
