# Scout inputs — 2026-09-12 (B24)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**FORBIDDEN:** topic B23 / apartments-vs-flat / cluster `newbuild_apartments_instead_flat_ddu_tyumen` — **already published 2026-09-05**. You MUST output **B24 only** (escrow zero vs DDU amount). Any B23 text = FAIL.

**run_date:** 2026-09-12 (owner-requested Saturday slot)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 24 active locks (last_sync 2026-09-12)
- Live WP ~20 (2026-09-12) — DO NOT reuse plot:
  - застройщик потребовал 420 тыс за лишние метры — ключи не выдал
  - переуступку согласовали — квартиру забрали за 24ч до аванса
  - застройщик снял субсидию за 3 дня до ДДУ
  - рассрочка просрочена на 4 дня — квартира ушла
  - в ДДУ запретили аренду до ключей
  - дом в КП — границы участка не совпали с ДДУ
  - трейд-ин сорвался (занизили оценку)
  - в ДДУ обещали чистовую — отдали предчистовую
  - бронь сгорела — цена +450 тыс
  - пропал балкон из планировки
  - застройщик год не платил неустойку
  - ребёнку 7 лет — семейную ипотеку пересчитали
  - приёмка без замечаний — банк остановил транш
  - ключи без разрешения на ввод — банк заморозил ипотеку
  - переуступка — долг 94 тыс
  - маткапитал — детские доли
  - созаёмщика убрали перед ДДУ
  - ДДУ расторгли за просрочку рассрочки
  - коттедж — газ в ДДУ vs факт
  - этаж в ДДУ 12-й — на ключах 2-й
- **Rejected title:** «650 тысяч брони на эскроу ноль» → H1 fingerprint DUPLICATE amount:booking_expired (live бронь +450k)
- `scout_helper.py --check-query` PASS
- `scout_story_dup.py --text` PASS cluster ddu_amount_vs_escrow_zero
- `excalibur_blog_topic_focus.py` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B24
- **title_draft:** В ДДУ в Тюмени указали 4,2 млн — за неделю до подписания на эскроу был ноль
- **slug:** v-tyumeni-v-ddu-42-mln-na-eskrou-nol
- **cluster_id (new):** ddu_amount_vs_escrow_zero
- **top_energy_mirror:** number_in_claim_vs_zero_paid
- **newbuild_mechanism:** сумма в ДДУ (взнос/эскроу) ≠ фактический остаток на эскроу-счёте перед подписанием; семья перевела деньги застройщику «как бронь», банк перед ДДУ видит пустой эскроу → ипотека/регистрация стоп
- **why_newbuild_not_secondary:** сюжет только про ДДУ, эскроу и застройщика новостройки; вторичка/ЕГРН-продавец не участвуют

## Dzen news-casus shape (PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке, согласовала ипотеку, готовилась к подписанию ДДУ
- **risk:** в тексте ДДУ указана сумма 4,2 млн к размещению на эскроу, а на счёте за неделю до подписания — 0 ₽; деньги лежали у застройщика как «бронь/взнос», не на эскроу
- **time:** за 7 дней / в день подписания ДДУ
- **finale:** банк не открыл сделку / заморозил ипотеку; застройщик потребовал перевести ещё раз; семья остановила подписание — бронь и планировка под угрозой (допустим частичный возврат только «удержания»)
- **comment_magnet_angle:** «Если менеджер говорит „мы сами положим на эскроу“ — вы всё равно идёте на подписание или сначала смотрите выписку по счёту?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild escrow-vs-DDU casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-12)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| эскроу счет новостройка тюмень | 55 | 1 (weak) |
| счет эскроу дду | 55+11176 | 27 (on-plot, weak) |
| эскроу счет | 55+11176 | 863 |
| договор долевого участия | 55+11176 | 382 |
| договор долевого участия | 225 compare | 16756 |
| **новостройки тюмень** | **55+11176** | **4583** |
| новостройки тюмень | 225 compare | 8447 |

**wordstat_rework:** probe «эскроу счет новостройка тюмень» 1 → «счет эскроу дду» 27 → «эскроу счет» 863 → localize Tyumen newbuild → **final P0 «новостройки тюмень» 4583 (55+11176) / 8447 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_48699/ — 214-ФЗ / эскроу
- https://www.domrf.ru/
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used

## Output required

Write complete Scout handoff markdown per SKILL.md with ALL fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 mcp_kv regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls.
