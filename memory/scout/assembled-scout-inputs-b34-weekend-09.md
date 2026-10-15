# Scout inputs — B34 weekend slot 09:00 YEKT 2026-10-11

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-11 (weekend authorized run, slot 09:00 Asia/Yekaterinburg)
**slot_rubric:** novostroyki (HARD)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Trend Radar (slot novostroyki, energy ONLY)

`memory/blog/trend-radar/trend-radar.json` (2026-10-11T04:25:16Z, slot 09:00):
- **viral_mechanism:** договор vs реальность (top angle ~231k views — rent plot NOT copied; energy mirrored into newbuild)
- **secondary energy (do not plot):** часы/срок съели аванс — NOT used as primary mechanism today

## Slot rubric

`novostroyki` — ДДУ, эскроу, застройщик, бронь, приложения к ДДУ. NO secondary avans/EGRN/darstvennaya plots.

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 11 active locks (2026-10-11)
- Live WP ~20 fetched: exclude recent newbuild/live plots (семейная ипотека ребёнок 7 лет, 0 доли в ДДУ у мамы, кладовая 190k, взнос 35/89, отделка 290k, БТИ +4 м², объявление «сдам» до эскроу, дом без эскроу 600, и др.)
- `scout_helper.py --check-query` + `topic_focus` + `story_dup` — conductor ran PASS before Derouter

## Proposed topic (PASS)

- **topic_id:** B34
- **title_draft:** В Тюмени за 3 дня до ДДУ тариф управляющей компании в приложении вырос с 52 до 186 рублей — эскроу не открыли
- **slug:** v-tyumeni-za-3-dnya-do-ddu-tarif-uk-v-prilozhenii-vyros-s-52-do-186-eskrou-ne-otkryli
- **article_dir:** memory/blog/articles/B34-v-tyumeni-za-3-dnya-do-ddu-tarif-uk-v-prilozhenii-vyros-s-52-do-186-eskrou-ne-otkryli
- **cluster_id (new):** newbuild_hoa_tariff_ddu_appendix_vs_sales_broni_tyumen
- **slot_rubric:** novostroyki
- **viral_mechanism:** договор vs реальность (Trend Radar novostroyki slot)
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья с ребёнком и инвестор-родственник берут студию в новостройке Тюмени «под сдачу после ключей». В брони и PDF-презентации менеджер зафиксировал «содержание ~52 ₽/м², без обязательных пакетов». Ипотеку одобрили. За 3 дня до подписания ДДУ открыли приложение №2: тариф управляющей компании **186 ₽/м²**, плюс обязательный пакет «умный дом» **320 000 ₽** до выдачи ключей. Пересчёт денежного потока (ипотека + коммуналка) перестал сходиться — семья **не открыла эскроу**, застройщик удержал часть брони (~80 000 ₽ из 150 000 ₽), ДДУ не подписали
- **why_newbuild_not_secondary:** Сюжет только в цепочке покупки у застройщика: бронь, ДДУ, приложение к договору, тариф УК/эксплуатация, эскроу, ипотека на новостройку. Нет продавца вторички, аванса на ДКП, ЕГРН-вторички, опеки, наследников
- **story_dup_check:** PASS — не пересекается с B27 земля-аренда, B28 газ-КП, B29 нулевой взнос, B30 запрет переуступки, B31 страховка+платёж, B32 чужое юрлицо эскроу, live «взнос 35/89», «кладовая 190k», «сдам до эскроу»

## Dzen news-casus shape: PASS

- **event:** семья выбрала студию в строящемся ЖК в Тюмени под сдачу; менеджер в брони написал «содержание 52 ₽/м²»
- **risk:** тариф УК и обязательные пакеты в приложении к ДДУ съедают «арендную математику»; без эскроу срывается ипотека
- **time:** за 3 дня до назначенного подписания ДДУ и открытия эскроу-счёта
- **finale:** в приложении — 186 ₽/м² и пакет 320 тыс.; застройщик предложил «подпишите, потом пересмотрим тариф»; семья отказалась; эскроу не открыли; бронь вернули частично
- **comment_magnet_angle:** «Если в брони УК 52 ₽, а в приложении к ДДУ — 186 ₽, вы бы подписали ДДУ, чтобы не потерять бронь, или ушли бы сразу?»

## Klyshin hook

- **klyshin_hook:** none

## Wordstat MCP-KV (live 2026-10-11)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

**Note:** `wordstat_get_top_requests` returned intermittent `400 Invalid query` / connection errors on all probes this run. Frequencies below are **live MCP-KV** via `wordstat_get_dynamics` `PERIOD_MONTHLY` (canonical buyer spine; not invented).

| probe | tool | regions | period | freq (monthly shows) |
|-------|------|---------|--------|---------------------:|
| коммунальные платежи новостройка | dynamics | 55,11176 | 2025-09 | 1 |
| сдать новостройку в аренду | dynamics | 55,11176 | 2025-09 | N/A |
| купить новостройку в тюмени | dynamics | 55,11176 | 2025-10 | 1301 |
| новостройки тюмень | dynamics | 55,11176 | 2025-10 | **5670** |
| новостройки (compare) | dynamics | 225 | 2025-10 | 1263808 |

**wordstat_rework log:**
- probe «коммунальные платежи новостройка» 55,11176 → 1 (too weak for P0)
- probe «сдать новостройку в аренду» 55,11176 → N/A (too weak)
- **rework:** anchor buyer spine «новостройки тюмень» + УК/приложение к ДДУ mechanism in H1/body (investor cash-flow casus)
- **final P0:** «новостройки тюмень» regions 55,11176,compare225 freq **5670** (2025-10 monthly); compare «новостройки» RU 225 **1263808**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — проектные декларации / застройщики
- https://t.me/Tyumen_Rieltor
- Trend energy (mechanics only): https://dzen.ru/a/YA7B343-ezstBMCs
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields including:
`slot_rubric`, `viral_mechanism`, `wordstat_preflight`, `top_energy_mirror`, `newbuild_mechanism`, `why_newbuild_not_secondary`, `klyshin_hook`, `anti_repeat_preflight`, `dzen_casus_shape: PASS`, `comment_magnet_angle`, `wordstat_rework`, `wordstat` (mcp_kv live + regions 55,11176,compare225 + P0 freq), `story_dup_check`, `h1_fingerprint_check`, `formula_spam_check`, `anti_dupe_hard: PASS`.

Lock topic_id B34, title, slug, article_dir.
