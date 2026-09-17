# Scout inputs — 2026-09-17 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-17 (YEKT weekday slot 09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO recent live WP plots: машино-место не в декларации, страховка 186 тыс перед ДДУ, ключи +9 мес без неустойки, отказ созаёмщику семейной ипотеки, бронь этаж/вид vs ДДУ другая секция, переуступка + аванс 350 тыс, КП дом без газа, банк снял ЖК с аккредитации, прайс вырос перед ДДУ, приёмка для родителей, фиксация цены сорвалась, маткапитал ребёнку 7 лет накануне эскроу
- NO frozen cluster in memory/scout/used-clusters.json (30d) — 29 active locks after sync 2026-09-17
- NO B26 skeleton repeat (РВЭ + второй транш траншевой ипотеки)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 29 active locks (last_sync 2026-09-17)
- Ledger: B02–B26 published; live WP ~20 titles reviewed
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: ипотек, новостройк)
- `story_dup.py --text` PASS → cluster `bank_appraisal_below_ddu_price`, fingerprint `amount:ddu_vs_escrow_amount` (distinct mechanism from ddu_amount_vs_escrow_zero — appraisal vs escrow balance)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени банк оценил новостройку на 900 тысяч ниже ДДУ — ипотеку порезали за сутки до подписания
- **slug:** v-tyumeni-bank-otsenil-novostrojku-nizhe-ddu-ipoteku-porezali
- **cluster_id (new):** bank_appraisal_below_ddu_price
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья выбрала квартиру в ЖК по ДДУ; ипотеку одобрили под полную цену договора. За сутки до подписания банк прислал отчёт оценщика: залоговая стоимость на **900 тыс. ₽ ниже** суммы в ДДУ → кредитный лимит урезали → не хватает на взнос/эскроу → сделку остановили до перевода денег
- **why_newbuild_not_secondary:** оценка **строящегося** объекта по ДДУ в цепочке застройщик–банк–эскроу; нет продавца вторички, выписки ЕГРН на квартиру, наследников или осмотра «бабушки»
- **story_dup_check:** PASS — distinct from trade_in_rejected_developer (оценка **старой** квартиры для трейд-ина), B06 avtoocenka (вторичка), mortgage_rate_hike_before_ddu / B22 (ставка, не залог), ddu_amount_vs_escrow_zero (ноль на эскроу, не отчёт оценщика), B26 (РВЭ + транш)

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени забронировала квартиру в новостройке, получила одобрение ипотеки «под ключ» и пришла на подписание ДДУ
- **risk:** банк в последний день снизил сумму кредита из‑за заниженной оценки залога — разрыв с ценой ДДУ ложится на покупателя
- **time:** за **сутки** до подписания ДДУ и открытия эскроу; менеджер ранее обещал «оценка формальность»
- **finale:** семья **не подписала** ДДУ и **не открыла** эскроу; бронь сняли через 48 часов; застройщик поднял цену на 200 тыс.; банк предложил только уменьшенный кредит — доплату из своих семья отказалась вносить
- **comment_magnet_angle:** «Оценку банка можно пересмотреть или сменить банк — а вы бы доплатили разницу из своих, если менеджер молчал про занижение до последнего дня?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild bank-appraisal casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-17)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| оценка квартиры банк ипотека | 55,11176 | 14 |
| оценка квартиры банк ипотека | 225 (compare) | 391 |
| ипотека оценка квартиры новостройка | 55,11176 | 2 (weak) |
| ипотека новостройка тюмень | 55,11176 | 184 |
| **ипотека от застройщика тюмень** | **55,11176** | **519** |
| ипотека от застройщика | 55,11176 | 732 |
| новостройки тюмень | 55,11176 | 4475 (context) |

**wordstat_rework log:**
- probe «оценка квартиры банк ипотека» 55,11176 → 14 (weak local)
- probe «ипотека оценка квартиры новостройка» 55,11176 → 2 (weak)
- **rework:** newbuild buyer jargon ипотека + застройщик + Тюмень → **final P0 «ипотека от застройщика тюмень» regions 55,11176,compare225 freq 519 (55+11176) / 732 (55+11176 parent «ипотека от застройщика»)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, эскроу
- https://www.cbr.ru/ — требования банков к оценке залога
- https://www.domrf.ru/ — реестр застройщиков
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
