# Assembled scout inputs — slot 09:00 YEKT 2026-09-30

**CONDUCTOR NOTE:** Gates already run in CI (scout_helper PASS, story_dup PASS, Wordstat live).  
**YOUR TASK:** Output **only** the Scout handoff markdown body (all SKILL fields). **Do not** emit `DEROUTER SCOUT BLOCKER` or refuse — filesystem/tools are on the conductor side.

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full handoff per SKILL.md field list.

**run_date:** 2026-09-30  
**slot:** 09:00 Asia/Yekaterinburg  
**topic_id:** B34  
**slot_rubric:** novostroyki  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень

## Trend Radar (2026-09-30, slot novostroyki)

Mirror **energy** (not rental plot): top angle «договор vs реальность» + «часы/срок съели аванс» / almost lost перед ключами — **plot ONLY newbuild приёмка + ДДУ + срок ключей**.

## HARD avoid (owner + recent WP)

Do NOT retread: эскроу+площадь, семейная ипотека+свидетельство, бронь+санузел, созаёмщик, ДДУ+чистовая+подрядчик, дарственная, аренда+ЕГРН, долг за свет; closed clusters in `memory/scout/used-clusters.json`.

## Proposed lock (pre-checked 2026-09-30)

- **cluster_id:** `newbuild_acceptance_frost_damaged_wall_keys_delayed_tyumen`
- **top_energy_mirror:** `almost_lost_before_keys` + trend `часы/срок съели аванс` (40 дней без ключей vs съём + ипотека)
- **newbuild_mechanism:** семья с детьми на финальной **приёмке** новостройки в Тюмени (ДДУ, ипотека, эскроу уже открыт); на осмотре — **промёрзшая/мокрая стена** (существенный недостаток); акт **не подписали**; застройщик назвал срок устранения ~40 дней; ключи и регистрация отложены; риск двойной аренды + платёж по ипотеке
- **why_newbuild_not_secondary:** приёмка у застройщика по ДДУ в строящемся/сданном ЖК, не сделка с продавцом на вторичке
- **title draft (H1):** «На приёмке новостройки в Тюмени нашли промёрзшую стену — ключи отложили на 40 дней»
- **comment_magnet_angle:** «Подписали бы акт с замечанием без независимой экспертизы ради ключей — или ждали бы 40 дней?»
- **scout_helper.py --check-query:** PASS 2026-09-30 (anti_dupe_hard PASS, topic focus PASS)
- **story_dup_check:** PASS — distinct from `acceptance_defects_penalty` (лифт/родители/10 минут)

## Wordstat MCP-KV (live 2026-09-30)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

| phrase | regions | volume |
|--------|---------|-------:|
| новостройки тюмень | 55 | 3547 |
| приемка квартиры в новостройке | 55+11176 | 122 |
| приемка квартиры в новостройке тюмень | 55+11176 | **28** |
| приемка квартиры в новостройке тюмень | 225 (RU compare) | 59 |

**wordstat_rework:** probe «новостройки тюмень» 3547 (broad) → spine «приемка квартиры в новостройке» 122 → localize **final P0** «приемка квартиры в новостройке тюмень» **28** (55+11176) / RU compare **59**

**klyshin_hook:** none

## dzen_casus_shape: PASS

- event: финальная приёмка квартиры в новостройке Тюмени
- risk: промёрзшая стена / существенный недостаток
- time: день приёмки + ~40 дней до повторной выдачи ключей
- finale: не подписали акт; agency — что фиксировать до акта и когда требовать неустойку по ДДУ

## formula_spam (last 3 published WP newbuild-related)

Recent: эскроу+площадь, семейная ипотека+свидетельство, ДДУ+подрядчик — skeleton **приёмка + существенный дефект стены + отложенные ключи** = new mechanism.

## signal_urls

- https://dzen.ru/holyslav
- https://t.me/Tyumen_Rieltor

Output handoff with all required Scout fields including `slot_rubric: novostroyki`, `viral_mechanism`, `anti_dupe_hard: PASS`.
