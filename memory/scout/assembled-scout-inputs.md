# Scout inputs — 2026-09-06 (B24, slot 15:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-06 (YEKT Sunday slot 15:00 — owner weekend request)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → active locks synced 2026-09-06
- **Live WP 2026-09-06 (~12 titles) — DO NOT reuse plot:**
  - застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили
  - застройщик запросил 300 тыс перед ключами — нет в ДДУ (отделка)
  - застройщик задержал ключи 7 мес — неустойку не выплатил
  - ДДУ 45 м² vs декларация 41 м²
  - приёмка: брак → штраф 190 тыс
  - апартаменты вместо квартиры (B23)
  - рассрочка — потеряли скидку при досрочном закрытии
  - инвестор: аренда запрещена до ключей
  - переуступка +280к за сутки
  - трейд-ин сорвался за день до ДДУ
  - оценка банка ниже цены ДДУ на 400к
  - категория земли сорвала ипотеку на дом в посёлке (другой механизм — не площадь)
- **Rejected overlap:** «площадь квартиры в ДДУ vs факт» → overlap with live DDU 45 vs 41 m² cluster
- **Rejected overlap:** «газ не подключили к дому» → weak Wordstat; timing overlap delay-keys cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени в ДДУ обещали участок 12 соток — в кадастре оказалось 8
- **slug:** v-tyumeni-v-ddu-obeshchali-uchastok-12-sotok-v-kadastre-okazalos-8
- **cluster_id (new):** newbuild_kp_plot_size_mismatch_ddu_cadastre_tyumen
- **story_dup_check:** PASS — distinct plot: семья берёт **дом в коттеджном посёлке** от застройщика по ДДУ; в договоре и на визуализации **12 соток**, кадастровый план и выписка ЕГРН перед ипотекой показывают **8 соток** (границы «съела» сервисная зона/дорога) → банк остановил выдачу, застройщик отказывается пересчитывать цену

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала дом в КП от застройщика, внесла бронь и пошла в ипотеку под участок 12 соток
- **risk:** кадастровый паспорт и межевание показали **8 соток** вместо 12 — цена в ДДУ не сходится с фактом, банк не открывает эскроу на полную сумму
- **time:** за 5 дней до подписания ДДУ, после заказа выписки ЕГРН и кадастрового плана
- **finale:** банк приостановил сделку; застройщик предложил «доплатить за оставшиеся 4 сотки отдельным договором»; семья остановила подписание и вернула бронь частично — спор на досудебке
- **comment_magnet_angle:** «Если в ДДУ 12 соток, а на межевании 8 — вы бы подписали ДДУ с оговоркой „как есть“ или разорвали бы бронь, даже если дом уже почти готов?»

## top_energy_mirror + newbuild

- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** дом/участок в КП от застройщика — площадь в ДДУ vs кадастр
- **why_newbuild_not_secondary:** сюжет только про покупку **нового дома от застройщика** в коттеджном посёлке (ДДУ, эскроу, ипотека на ИЖС/КП), не про вторичный участок или продавца-физлицо

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP plot-size casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-06)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| **новостройки тюмень** | **55** | **4663** |
| новостройки тюмень | 11176 | (Tyumen oblast included) |
| **новостройки тюмень** | **225 (compare)** | **8691** |
| дом в коттеджном поселке тюмень | 55 | 42 |
| купить дом в коттеджном поселке тюмень | 55 | 20 |
| купить новостройку в тюмени | 55 | 865 (context) |

**wordstat_rework log:**
- probe «дом в коттеджном поселке тюмень» 55 → 42 (on-topic houses, weak spine)
- probe «участок новостройка тюмень» 55 → MCP empty (weak)
- **rework:** anchor P0 on newbuild demand spine + localize KP jargon in H1 → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4663 (55) / 8691 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек/ипотеки
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ, земельные участки
- https://www.domrf.ru/ — застройщики / ДДУ на дома
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
