# Scout inputs — 2026-09-14 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-14 (YEKT weekday slot ~12:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO acceptance finishing / чистовая vs голые стены (B25 / acceptance_defects_penalty)
- NO РВЭ / второй транш без ввода (B26 / newbuild_rve_delay_blocks_mortgage_tranche_tyumen)
- NO DDU area 54 vs 52 m² (LIVE today 2026-09-14 morning)
- NO KP 12 vs 9,7 sotok, parking double-sold, assignment 7 days, transh +480k, early payment discount, bank appraisal -680k, family mortgage Oct 1, house defect 850k, DDU 4,2 mln escrow zero (all live WP last 48h)
- NO keys_delay_penalty_unpaid — H1 fingerprint duplicate LIVE-V-TYUMENI-ZASTROJSCHIK-P (420k extra meters)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-14)
- Live WP last ~20 (2026-09-14): 54 m² vs 2 кв.м меньше; KP 12/9,7; РВЭ+транш 520к; чистовая B25; парковка P-42; переуступка 7 дней; транш +480к; скидка досрочный платёж; оценка -680к; семейная ипотека до 1 окт; дом брак 850к; эскроу ноль 4,2 млн; доплата 420к за метры; и др.
- **Rejected:** keys_delay_penalty_unpaid — fingerprint dup
- **Rejected:** elevator_not_ready_acceptance — story dup acceptance_defects_penalty
- **Rejected:** ddu_floor_mismatch — overlap with predchistovaya cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: квартир, застройщик)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени застройщик продал одну квартиру двум дольщикам — второму оставили только бронь
- **slug:** v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-dolschikam
- **cluster_id (new):** double_sale_same_unit_newbuild
- **top_energy_mirror:** someone_else_took_object
- **newbuild_mechanism:** менеджер офиса продаж ЖК оформил **две брони/ДДУ на один и тот же номер квартиры** (одна планировка, один лот в шоуруме) → первая семья успела открыть эскроу → вторая за 4 дня до подписания узнала, что лот «закрыт» → застройщик вернул второй семье только сумму брони (180 тыс.) без компенсации разницы цены на аналог (+390 тыс. на ту же планировку в соседней секции)
- **why_newbuild_not_secondary:** сюжет в офисе застройщика, бронь/ДДУ/эскроу по 214-ФЗ, нет продавца-физлица, ЕГРН-вторички, наследников или осмотра у бабушки; конфликт между двумя дольщиками одного ЖК
- **story_dup_check:** PASS — distinct from assignment_lost_to_faster_buyer (переуступка, другой покупатель на ту же планировку, не двойной лот), booking_expired_price_hike (субсидия/цена), trade_in, bank appraisal

## Dzen news-casus shape (target PASS)

- **event:** две семьи в Тюмени выбрали одну и ту же квартиру в новостройке; обе внесли бронь в офисе застройщика в разные дни одной недели
- **risk:** двойная продажа одного лота — зарегистрировать право может только один дольщик; вторая семья теряет объект и вынуждена брать аналог дороже
- **time:** за 4 дня до открытия эскроу у второй семьи менеджер сообщил, что «квартира уже в работе у другого дольщика»; первая семья подписала ДДУ 11 дней раньше
- **finale:** второй покупатель получил возврат брони 180 тыс.; застройщик предложил «похожую» планировку в другой секции +390 тыс. к цене; вторая семья отказалась от доплаты, подала претензию; первая семья продолжила сделку — спор о компенсации у второй не закрыт
- **comment_magnet_angle:** «Один номер квартиры — два договора брони: вы бы доплатили 390 тысяч за „такую же“ планировку в соседней секции или требовали бы от застройщика ту же цену?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen double-sale newbuild casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-14)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4502 |
| купить новостройку в тюмени | 55,11176 | 909 |
| купить новостройку в тюмени | 225 (compare) | 1918 |
| неустойка застройщика | 55,11176 | 139 (rejected plot — fingerprint dup) |
| приемка квартиры в новостройке тюмень | 55,11176 | 36 (rejected — acceptance cluster) |
| семейная ипотека новостройка тюмень | 55,11176 | 24 (live WP Oct 1 angle taken) |

**wordstat_rework log:**
- probe «новостройки тюмень» 55,11176 → 4502 (strong spine, generic)
- probe «купить новостройку в тюмени» 55,11176 → 909 (buyer-intent P0)
- compare RU225 «купить новостройку в тюмени» → 1918
- **final P0:** «купить новостройку в тюмени» regions 55,11176,compare225 freq **909** (Tyumen+область) / **1918** (RU225)

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, договор участия в долевом строительстве
- https://www.domrf.ru/ — реестр застройщиков
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
