# Scout inputs — 2026-09-17 (B27)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-17 (YEKT weekday slot 17:00 — 4-й слот дня)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true

## Slot constraints (HARD FORBIDDEN — same day + 30d)

**Уже сегодня 2026-09-17 (3 поста):**
- запрет аренды в приложении к ДДУ — инвестор отказался от доплаты 240 тыс.
- за 10 дней до ДДУ перенесли в другой корпус — этаж и вид не совпали
- оценка новостройки на 900 тыс. ниже ДДУ — банк урезал кредит (cluster bank_appraisal_below_ddu_price LOCKED)

**Недавно ledger / live (не дублировать):**
- B25: чистовая в ДДУ vs приёмка (acceptance_defects_penalty)
- B26: сдача без разрешения на ввод — банк не дал второй транш
- B19: семейная ипотека + эскроу + маткапитал
- B18: маткапитал + детские доли на **вторичке** (frozen secondary angle — не retitle)
- matkapital_opieka_kids_cancel_3y — вторичка, дети оспорили через 3 года (frozen)

**NO** frozen secondary clusters. **NO** formula spam skeleton «бронь→ДДУ→застройщик» без новой механики.

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 30 active locks (last_sync 2026-09-17)
- Live WP ~20 заголовков прочитаны через `excalibur_blog_today.py` EXCALIBUR_RECENT_WP_POSTS
- `scout_helper.py --check-query` PASS для proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: новострой, маткапитал)
- `story_dup.py --text` PASS

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B27
- **title_draft:** В Тюмени купили новостройку с маткапиталом — через полгода опека не приняла доли детей
- **slug:** v-tyumeni-kupili-novostrojku-s-matkapitalom-cherez-polgoda-opeka-ne-prinyala-doli-detej
- **cluster_id (new):** newbuild_matkapital_child_shares_registration_blocked_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** Семья купила квартиру в новостройке по ДДУ с **семейной ипотекой** и **маткапиталом** в первоначальный взнос на эскроу. После регистрации права и ключей — обязанность в 6 месяцев **выделить доли детям** и согласовать с **опекой**. Соглашение подали с долями 1/4 на каждого — опека вернула: «не соответствует норме площади на ребёнка». **Росреестр** приостановил регистрацию долей; банк предупредил о риске для **льготной семейной ставки**. Финал: переделали соглашение через юриста, регистрация долей заняла ещё 4 месяца, семья едва уложилась в срок — льготную ставку сохранили, но доплатили ~90 тыс. за сопровождение.
- **why_newbuild_not_secondary:** сюжет = ДДУ у застройщика → эскроу → регистрация права на **новое** жильё → пост-регистрационное обязательство по маткапиталу; нет продавца вторички, проверки ЕГРН перед авансом продавцу, наследников или оспаривания старой сделки (отличие от B18 и matkapital_opieka_kids_cancel_3y)
- **story_dup_check:** PASS — distinct from B19 (эскроу не открылся до ДДУ), B18 (доли не видны в выписке на вторичке), bank_appraisal (оценка vs ДДУ), acceptance_defects (чистовая), RVE/tranche B26

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени получила ключи от новостройки, внесла маткапитал через эскроу, оформила семейную ипотеку
- **risk:** без зарегистрированных долей детям — нарушение условий маткапитала и угроза пересмотра льготной ипотеки
- **time:** «через полгода» после регистрации права; опека вернула пакет на 47-й день шестимесячного срока
- **finale:** регистрацию долей приостановили; после исправления соглашения доли внесли в ЕГРН на 11-й неделе второй попытки — штрафов не было, но семья чуть не потеряла семейную ставку
- **comment_magnet_angle:** «Опека завернула доли детям за две недели до дедлайна по маткапиталу: вы бы рискнули семейной ставкой и подали бы „как нарисовал застройщик“, или сначала прогнали бы соглашение через юриста?»

## Klyshin hook

- **klyshin_hook:** none | original: none (свежий Tyumen newbuild matkapital casus без Klyshin — предпочтительно при риске дубля)

## Wordstat MCP-KV (live 2026-09-17)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| маткапитал новостройка тюмень | 55,11176 | 0 (empty API) |
| маткапитал новостройка | 55 | 1 (weak local) |
| маткапитал новостройка | 225 (compare) | 338 |
| покупка новостройки с маткапиталом | 225 | 50 |
| выделение долей маткапитал | 55,11176 | 58 (top: «выделение долей по маткапиталу» 22) |
| **выделение долей детям маткапитал** | **55,11176** | **17** |
| выделение долей детям маткапитал | 225 (compare) | **901** |
| новостройки тюмень | 55,11176 | **4480** (regional spine) |
| семейная ипотека новостройка тюмень | 55,11176 | 24 |

**wordstat_rework log:**
- probe «маткапитал новостройка тюмень» 55,11176 → 0/empty → weak
- probe «маткапитал новостройка» 55 → 1 → weak local
- probe «покупка новостройки с маткапиталом» 225 → 50 → OK compare, нет Tyumen tail
- probe «новостройки тюмень» 55,11176 → 4480 → strong regional anchor
- probe «материнский капитал новостройка» 55,11176 → **15** (contains buyer seeds материнский капитал + новостройка)
- probe «дду материнский капитал» 55,11176 → 7
- **rework:** anchor «новостройки тюмень» 4480 + post-keys obligation → **final P0 «материнский капитал новостройка» 15 (55+11176)** with mechanism spine «выделение долей детям маткапитал» 17 / 901 (RU225)

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_25652/ — 256-ФЗ материнский капитал, обязанность выделить доли
- https://www.consultant.ru/document/cons_doc_LAW_51040/ — 214-ФЗ ДДУ
- https://www.domrf.ru/
- https://t.me/klyshin_A — checked, not used
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

**FORMAT HARD:** include a plain-text block `## Gate log (machine)` where EACH gate field is ONE line starting exactly with `fieldname:` (no markdown bold, no bullets) — required for `excalibur_blog_wordstat_gate.py handoff`. Example lines:
```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: optional | none | original: none | signal: none
wordstat_rework: probe «…» N → … → final P0 «…» N
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «материнский капитал новостройка» 15 | spine «новостройки тюмень» 4480 | mechanism «выделение долей детям маткапитал» 17 / 901
anti_dupe_hard: PASS
```

Lock topic_id B27, title, slug, signal_urls, research angles for Research role.
