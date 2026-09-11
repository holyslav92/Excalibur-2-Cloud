# Scout inputs — 2026-09-11 (B24, slot ~12:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-11 (YEKT weekday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 24 active locks (last_sync 2026-09-11)
- **Live WP ~12 titles — DO NOT reuse plot:**
  - 2026-09-11: аренда запрещена за 7 дней до ДДУ — инвестор потерял 2 жильцов (ddu_rent_investor)
  - 2026-09-10: ДДУ на дом — границы участка не совпали (КП/ИЖС)
  - 2026-09-10: трейд-ин занизили оценку — сорвался перед ДДУ
  - 2026-09-10: чистовая vs предчистовая в ДДУ
  - 2026-09-10: бронь сгорела — цена +450к
  - 2026-09-09: пропал балкон из ДДУ / проектная декларация
  - 2026-09-09: неустойка за просрочку ключей
  - 2026-09-09: ребёнку 7 лет — семейная ипотека пересчитали
  - 2026-09-09: банк остановил транш после приёмки
  - 2026-09-08: ключи без разрешения на ввод
  - 2026-09-08: долг на переуступке 94к
  - 2026-09-08: маткапитал в ДДУ за 3 недели до ключей
- **Rejected overlap:** parking/mashinomesto in DDU → fingerprint storage_missing, too close to B21 cellar cluster
- **Rejected overlap:** subsidized rate expired → B22 bank rate before DDU + live mortgage clusters
- **Rejected overlap:** ЖКУ до ключей → weak Wordstat (empty response)
- **Rejected overlap:** area shrink in DDU → weak Wordstat (10 total)
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: застройщ, тюмен)
- `excalibur_blog_scout_story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B24
- **title_draft:** В Тюмени просрочили рассрочку от застройщика на 4 дня — вернули только 180 тысяч из 400
- **slug:** v-tyumeni-prosrochili-rassrochku-ot-zastrojschika-vernuli-180-iz-400
- **cluster_id (new):** installment_penalty_developer
- **story_dup_check:** PASS — distinct legal plot: семья взяла квартиру в новостройке по **рассрочке от застройщика** (не ипотека), внесла первый платёж 400 тыс.; из‑за задержки перевода на 4 дня застройщик применил штраф/расторжение по договору рассрочки и вернул только 180 тыс.; квартиру выставили другому покупателю

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке и подписала договор рассрочки с застройщиком вместо ипотеки
- **risk:** в договоре рассрочки — жёсткий срок платежа и штраф/расторжение при просрочке даже на несколько дней; деньги не на эскроу, а на счёт застройщика
- **time:** «на 4 дня» — просрочка одного ежемесячного платежа после первого взноса
- **finale:** застройщик расторг договор, вернул 180 тыс. из 400, квартиру продал другому; семья потеряла 220 тыс. и объект
- **comment_magnet_angle:** «Рассрочка от застройщика без ипотеки — это свобода или ловушка: вы бы рискнули одним пропуском платежа ради скидки?»

## Top-energy mirror (owner lock)

- **top_energy_mirror:** clock_ran_out
- **newbuild_mechanism:** рассрочка от застройщика + штраф/расторжение за просрочку платежа (не банковская ипотека)
- **why_newbuild_not_secondary:** сюжет только про покупку квартиры в новостройке по договору с застройщиком; вторичка, ЕГРН и продавец-физлицо не участвуют

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen installment casus without Klyshin — avoids today's rent-in-DDU slot and B21 parking/cellar overlap)

## Wordstat MCP-KV (live 2026-09-11)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| рассрочка от застройщика | 55,11176 | 231 |
| рассрочка от застройщика тюмень | 55,11176 | 137 |
| квартира в рассрочку от застройщика тюмень | 55,11176 | 64 |
| машиноместо тюмень | 55,11176 | 227 (rejected — storage_missing overlap B21) |
| субсидированная ипотека от застройщика тюмень | 55,11176 | 27 (rejected — B22 rate cluster) |
| новостройки тюмень | 55,11176 | 4583 (context spine) |
| рассрочка от застройщика тюмень | 225 (compare) | 217 |

**wordstat_rework log:**
- probe «рассрочка от застройщика» 55,11176 → 231
- probe «рассрочка от застройщика тюмень» 55,11176 → 137 (Tyumen-local buyer intent)
- probe «квартира в рассрочку от застройщика тюмень» 55,11176 → 64 (supporting)
- probe «машиноместо тюмень» 227 — rejected plot overlap B21
- **final P0 «рассрочка от застройщика тюмень» regions 55,11176,compare225 freq 137 (55+11176) / 217 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ / ДДУ контекст (рассрочка vs эскроу)
- https://www.domrf.ru/ — справочник застройщиков
- https://t.me/klyshin_A — checked, not used this slot
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS, formula_spam_check PASS, anti_dupe_hard PASS.

Lock topic_id B24, title, slug, signal_urls, research angles for Research role.
