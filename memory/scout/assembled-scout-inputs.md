# Scout inputs — 2026-10-02 slot 09:00 YEKT (B34)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-10-02 (YEKT weekday slot 09:00)
**slot_rubric:** novostroyki
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** newbuild_only (owner lock)
**dzen_rf_pack:** true

## Trend Radar (slot 09:00 novostroyki)

- **viral_mechanism (energy only):** договор vs реальность (mirror top Dzen energy; plot NOT rental — newbuild ДДУ/бронь only)
- **top_energy_mirror:** paper_clean_then_broke
- Source: `memory/blog/trend-radar/trend-radar.json` generated 2026-10-02T05:22 UTC, slot_local 09:00

## Slot constraints (HARD FORBIDDEN — live Oct 2026 + user blocklist)

- NO школа в рекламе ЖК vs декларация (2026-10-01 live)
- NO эскроу + объявление «сдам» / сдача в аренду в новостройке (2026-10-01 live)
- NO бронь «двор без машин» → проезд (2026-09-30 live)
- NO приёмка промёрзшая стена (2026-09-30 live)
- NO семейная ипотека пересчёт на вторичке 1 октября (2026-10-01 live)
- NO площадь в ДДУ урезали перед эскроу (2026-09-29 live)
- NO свидетельство второго ребёнка / семейная ипотека стоп перед эскроу (2026-09-29 live)
- NO frozen clusters in `memory/scout/used-clusters.json` (14 active locks after sync 2026-10-02)
- NO secondary-market casus (аванс, ЕГРН-вторичка, бабушка, банкрот продавца, дарственная…)
- NO formula skeleton clone of last-3 ledger: insurance spike before DDU (B31), чужое юрлицо на эскроу (B32), долг за свет на вторичке (B33)
- Prefer title **without** «за N дней до эскроу» countdown (overused on live WP)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 14 active lock(s), last_sync 2026-10-02
- Live WP recent (EXCALIBUR_RECENT_WP_POSTS 2026-10-02): семейная ипотека вторичка 1 окт; эскроу+«сдам»; школа в рекламе; банкрот вторичка; запрет пристава; двор/бронь; промёрзшая стена; аренда ЕГРН; дарственная; площадь ДДУ; свидетельство ребёнка; долг за свет
- Ledger last published: B33, B32, B31 (mechanisms: utility debt secondary, escrow wrong entity, insurance before DDU)

## Proposed topic (conductor pre-check — run scout_helper after handoff)

- **topic_id:** B34
- **title_draft:** В Тюмени в презентации ЖК обещали взнос 35 рублей — в приложении к ДДУ вышло 89, ипотеку урезали
- **slug:** v-tyumeni-v-prezentacii-zhk-vznos-35-a-v-ddu-89-semya-ostanovila-sdelku
- **article_dir:** memory/blog/articles/B34-v-tyumeni-v-prezentacii-zhk-vznos-35-a-v-ddu-89-semya-ostanovila-sdelku
- **cluster_id (new):** newbuild_management_fee_ddu_appendix_vs_sales_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья с ипотекой на квартиру в строящемся ЖК в Тюмени. В офисе продаж и PDF-презентации зафиксировали «плата за содержание с ключей — от 35 ₽/м²». На предподписании ДДУ в приложении №3 — тариф **89 ₽/м²** с ежегодной индексацией и отдельной строкой на капремонт. Банк пересчитал полный платёж (ипотека + содержание) и **урезал одобренную сумму на ~620 тысяч**. Семья отказалась подписывать ДДУ, эскроу не открывали, бронь 150 тысяч вернули полностью после претензии
- **why_newbuild_not_secondary:** Риск только в цепочке первички: бронь застройщика, приложение к ДДУ о содержании общего имущества до передачи УК, ипотечное одобрение под полную нагрузку платежа. Нет продавца вторички, ДКП, чистой выписки ЕГРН на «чужую» квартиру
- **story_dup rationale:** Отличается от B27 (аренда земли в декларации), B25 (чистовая на приёмке), booking_expired_price_hike (секция/этаж), B31/B32 (страховка/реквизиты эскроу), школа в рекламе (инфраструктура), площадь в ДДУ (метраж)

## Dzen news-casus shape (target PASS)

- **event:** супруги с ребёнком выбрали трёшку в строящемся ЖК; менеджер прислал презентацию со сметой «35 ₽/м² содержание»; на встрече у юриста застройщика открыли проект ДДУ
- **risk:** завышенный взнос на содержание + индексация ломает бюджет и долговую нагрузку для банка; без подписания ДДУ нет эскроу и нет фиксации цены квартиры
- **time:** на предподписании ДДУ, за несколько дней до планового открытия эскроу-счёта (без countdown-hook в H1)
- **finale:** банк снизил лимит ипотеки; семья написала отказ от ДДУ, застройщик вернул бронь 150 тыс., к другому корпусу не переходили
- **comment_magnet_angle:** «Если в презентации 35 ₽, а в ДДУ 89 ₽ за квадрат — вы подписали бы «чтобы не потерять бронь» или развернулись бы сразу?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen newbuild casus без Klyshin)

## Wordstat MCP-KV (live 2026-10-02)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4360 |
| новостройки тюмень | 225 (compare) | 8336 |
| плата за содержание жилья | 55,11176 | 6 |
| управляющая компания новостройка | 55,11176 | 2 |
| договор долевого участия тюмень | 55,11176 | 3 |
| дду новостройка тюмень | 55,11176 | API empty |
| эскроу счет новостройка | 55,11176 | API empty |
| приемка квартиры в новостройке тюмень | 55,11176 | 14 |

**wordstat_rework log:**
- probe «плата за содержание жилья» 55,11176 → 6 (слабо для P0)
- probe «управляющая компания новостройка» → 2 (слабо)
- probe «договор долевого участия тюмень» → 3 (слабо)
- probe «приемка квартиры в новостройке тюмень» → 14 (слабо + риск overlap с acceptance cluster)
- probe «дду новостройка тюмень» / «эскроу счет новостройка» → пустой ответ API
- **rework:** buyer spine «новостройки тюмень» + механика взноса в приложении к ДДУ в H1/теле
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4360 (55+11176) / 8336 (225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — проектные декларации, образцы ДДУ
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, содержание общего имущества
- https://t.me/klyshin_A — checked, not used
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields including:
`slot_rubric: novostroyki`, `viral_mechanism`, wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B34, title, slug, article_dir, signal_urls, research angles for Research role.
