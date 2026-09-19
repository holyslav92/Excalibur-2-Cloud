# Scout inputs — 2026-09-19 (B28)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-19 (YEKT Saturday slot 12:00 — weekend automation)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN)

- NO B27 land lease in declaration (published 2026-09-19 10:02)
- NO family mortgage child turned 7 / семейная ипотека сняли (published 2026-09-19 11:00)
- NO cottage KP kadastr fence 1.8m (2026-09-18 live)
- NO BTI area 4.2 sqm less than DDU (2026-09-18 live)
- NO assignment 28 days lost to another buyer (2026-09-18 live)
- NO mortgage approval expired day 87 (2026-09-18 live)
- NO matkapital child shares day 47 (2026-09-17 live)
- NO DDU appendix rental ban investor (2026-09-17 live)
- NO different building/corpus 10 days before DDU (2026-09-17 live)
- NO bank appraisal 900k lower (cluster bank_appraisal_below_ddu_price locked)
- NO parking spot missing in declaration (2026-09-16 live)
- NO insurance 186k before DDU (2026-09-16 live)
- NO keys 9 months late penalty unpaid (cluster keys_delay_penalty_unpaid locked)
- NO co-borrower refused family mortgage (2026-09-16 live)
- NO B26 RVE delay blocks tranche (published 2026-09-13)
- NO acceptance_defects_penalty cluster (act refusal / elevator defects — locked)
- NO KP gas/utilities handover without signing act phrasing (triggers acceptance cluster)
- NO frozen cluster in memory/scout/used-clusters.json (30d)
- NO secondary market plots

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-19)
- Live WP recent (~10): семейная ипотека 7 лет, B27 земля аренда декларация, коттедж кадастр 1.8м, БТИ −4.2 кв.м, переуступка 28д, ипотека 87-й день, маткапитал детские доли 47д, приложение запрет аренды, другой корпус 10д, оценка −900к
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B28
- **title_draft:** В Тюмени в доме КП потолки ниже ДДУ на 25 сантиметров — замер на сдаче показал 2,45 вместо 2,7 метра, перерасчёт отказали
- **slug:** v-tyumeni-v-kp-potolki-nizhe-ddu-25-sm-zamer-na-sdache
- **cluster_id (new):** newbuild_ceiling_height_below_ddu_kp_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** ДДУ на дом в коттеджном посёлке под Тюменью: в приложении и планировке зафиксирована высота потолков **2,7 м**. На сдаче лазерный замер в гостиной и двух спальнях — **2,45 м** (минус 25 см). Застройщик назвал «конструктивный допуск», предложил скидку 80 тысяч вместо перерасчёта цены. Семья с детьми отказалась подписывать акт приёма-передачи, ключи не взяли, финальный транш на эскроу не переводили
- **why_newbuild_not_secondary:** Сюжет только в цепочке долевого строительства дома от застройщика в КП: ДДУ, приложение с теххарактеристиками, сдача нового дома. Нет продавца вторички, ЕГРН-квартиры, наследников, бабушки, опеки или соседской доли
- **story_dup_check:** PASS — distinct from BTI площадь −4.2 кв.м (2026-09-18), коттедж кадастр забор 1.8м (2026-09-18), B25 чистовая отделка, acceptance_defects лифт/родители, B27 декларация земля аренда

## Dzen news-casus shape (target PASS)

- **event:** семья с двумя детьми и инвестор купили дом в коттеджном посёлке под Тюменью; в офисе продаж показали макет с «высокими потолками 2,7»
- **risk:** фактическая высота ниже ДДУ → меньше объём жилья, комфорт, риск отказа банка при переоценке; застройщик давит подписать акт «как есть»
- **time:** день сдачи дома, замер перед подписанием акта приёма-передачи
- **finale:** замер 2,45 м вместо 2,7 м; застройщик предложил скидку 80 тысяч «подпишите сейчас»; семья отказалась, акт не подписали, ключи не получили; через 9 дней застройщик вернул задаток 250 тысяч, на регистрацию не вышли
- **comment_magnet_angle:** «Если потолки на 25 см ниже, чем в ДДУ, — вы подпишете акт за обещанную скидку или остановитесь до ключей?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen KP ceiling-height casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-19)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55,11176 | 4430 |
| новостройки тюмень | 225 (compare) | 8321 |
| дома в тюмени от застройщика | 55,11176 | 253 |
| купить дом в тюмени от застройщика | 55,11176 | 130 |
| купить дом в тюмени от застройщика | 225 (compare) | 256 |
| коттеджные поселки тюмень | 55,11176 | 1455 |
| высота потолков дду | 55,11176 | 0 (no data / too weak) |
| приемка дома от застройщика | 55,11176 | 2 (weak mechanism tail) |

**wordstat_rework log:**
- probe «высота потолков дду» 55,11176 → 0 (too weak for P0 alone)
- probe «приемка дома от застройщика» 55,11176 → 2 (weak + acceptance cluster risk in H1)
- probe «дома в тюмени от застройщика» 55,11176 → 253 (KP buyer spine, moderate)
- probe «коттеджные поселки тюмень» 55,11176 → 1455 (strong KP segment)
- **rework:** anchor buyer spine «новостройки тюмень» + KP/house mechanism in H1; secondary KP phrase «коттеджные поселки тюмень» in body/research
- **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4430 (55+11176) / RU compare 8321 (225)**

## Gates (conductor verified)

- h1_fingerprint_check: PASS | fingerprint: height:ceiling_below_ddu_kp (distinct from amount:ddu_vs_escrow_amount, booking_expired, keys_delay)
- formula_spam_check: PASS | last3_mechanisms: B25 chistovaya_acceptance / B26 rve_no_permission_tranche / B27 land_lease_declaration
- anti_dupe_hard: PASS

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — реестр застройщиков / проектные декларации
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ, ДДУ, характеристики объекта
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B28, title, slug, signal_urls, research angles for Research role.
