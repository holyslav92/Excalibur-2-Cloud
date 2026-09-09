# Scout inputs — 2026-09-09 (B24 ONLY — NOT B23)

**FORBIDDEN:** Do NOT write B23, apartments-vs-flat, or cluster `newbuild_apartments_instead_flat_ddu_tyumen`. That topic is CLOSED and published.

**MANDATORY topic lock for this run:**
- topic_id: **B24**
- cluster_id: **acceptance_defects_penalty**
- title: **В Тюмени на приёмке новостройки подписали акт без замечаний — банк остановил регистрацию из-за дефектов**

**CRITICAL EXECUTION CONTEXT:** You are inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). **Write ONLY the Scout handoff markdown** for B24 acceptance_defects_penalty — no tool calls, no refusals.

**run_date:** 2026-09-09 (YEKT weekday slot ~09:00)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_id:** B24
**topic_market_focus:** newbuild_only

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 27 active locks (last_sync 2026-09-09)
- Live WP last ~12 (2026-09-05–2026-09-08) — closed newbuild plots include: escrow shortfall, wrong floor, double sale, apartamenty vs kvartira, mortgage rate hike, matkapital before keys, assignment debt, keys without permission, co-borrower removed, installment overdue, cottage gas, land area, extra finishing payment, trade-in rejected, booking expired, appraisal below DDU, keys delay penalty
- **Formula spam last 3 mechanisms:** keys_without_commissioning_permit | assignment_debt_found | matkapital_before_keys_child_shares — proposed angle is **acceptance/act defects**, distinct
- `scout_helper.py --check-query` PASS
- `excalibur_blog_topic_focus.py` PASS (marker: новострой)

## Proposed topic (PASS all gates)

- **title_draft:** В Тюмени на приёмке новостройки подписали акт без замечаний — банк остановил регистрацию из-за дефектов
- **slug:** v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-registraciyu
- **cluster_id:** acceptance_defects_penalty
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** акт приёмки-передачи по ДДУ — семья подписала «без замечаний» под давлением менеджера («потом исправим»), через несколько дней независимая приёмка нашла дефекты; банк приостановил регистрацию права и выдачу остатка ипотеки, застройщик отказался устранять по уже подписанному акту
- **why_newbuild_not_secondary:** сюжет только про сдачу объекта по ДДУ от застройщика, акт приёмки-передачи и ипотечную регистрацию новостройки — не осмотр вторички и не ЕГРН-продавец

## Dzen news-casus shape (PASS)

- **event:** семья получила ключи от новостройки в Тюмени, на приёмке подписала акт без замечаний
- **risk:** скрытые дефекты (отделка, окна, инженерия) + подписанный акт лишает претензий; банк не регистрирует право при открытых недоделках
- **time:** через 5 дней после подписания акта, на этапе подачи документов в Росреестр
- **finale:** банк остановил регистрацию и выдачу транша; застройщик отказал в бесплатном устранении — семья подала претензию, ключи формально получены, но право не зарегистрировано, ипотека «в подвешенном состоянии»
- **comment_magnet_angle:** «Менеджер сказал „подпишите, потом исправим“ — вы бы подписали акт без замечаний или отказались от ключей в тот же день?»

## Klyshin hook

- **klyshin_hook:** none (fresh Tyumen newbuild acceptance casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-09)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|------|
| приемка квартиры в новостройке | 55+11176 | 122 |
| приемка квартиры в новостройке | 225 compare | 6032 |
| приемка квартиры в новостройке тюмень | 55+11176 | 32 |
| акт приемки передачи квартиры | 55+11176 | 37 (tail secondary) |
| дефекты при приемке новостройки | 55+11176 | API empty |

**wordstat_rework:**
- probe «приемка квартиры в новостройке» 55+11176 → 122
- probe «акт приемки передачи квартиры» 55+11176 → 37 (secondary tail in top requests)
- rework: localize Tyumen → **final P0 «приемка квартиры в новостройке тюмень» 55+11176 freq 32** (parent spine 122 / RU 6032)

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ, приёмка долевого строительства
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Output required

Write complete Scout handoff markdown per SKILL.md with ALL fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard PASS.
Lock topic_id B24, title, slug, signal_urls.
