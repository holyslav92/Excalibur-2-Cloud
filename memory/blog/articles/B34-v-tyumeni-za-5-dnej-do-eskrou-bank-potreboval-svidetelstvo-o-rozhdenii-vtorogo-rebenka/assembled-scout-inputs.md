# Scout inputs — 2026-09-29 (B34)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-29
**slot:** 09:00 YEKT — rubric `novostroyki`
**tenant:** The Риэлтор — Святослав Шакин, Тюмень
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true (dzen-content-rules + rf-blocked-entities read by conductor)

## Trend Radar (2026-09-29, novostroyki)

Mirror **energy** only (not rental plots):
- Top mechanism: `договор vs реальность` (СИЛА ПРАВА, 231k views)
- Secondary energy: `часы/срок съели аванс` (deadline before money)

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 18 active locks (2026-09-29)
- Ledger + live WP ~12: recent newbuild — co-borrower escrow, second sanuzel, EISZHS halt, studio→commercial, townhouse→apartment, installment -340k, UK 180k, lift inspection, rental ban DDU, parking lgot cancelled; B33 secondary electricity debt (not our plot)
- **FORBIDDEN today:** parking separate DDU / gift parking (live `za-4-dnya-do-eskrou-mashinomesto-vynesli-v-otdelnyj-ddu`), taunhaus→apartment broni mismatch, matkapital escrow B19, co-borrower escrow live 2026-09-28

## Proposed topic (pre-gated PASS)

- **topic_id:** B34
- **title_draft:** В Тюмени за 5 дней до эскроу банк потребовал свидетельство о рождении второго ребёнка — семейная ипотека под угрозой
- **slug:** v-tyumeni-za-5-dnej-do-eskrou-bank-potreboval-svidetelstvo-o-rozhdenii-vtorogo-rebenka
- **article_dir:** memory/blog/articles/B34-v-tyumeni-za-5-dnej-do-eskrou-bank-potreboval-svidetelstvo-o-rozhdenii-vtorogo-rebenka
- **cluster_id (new):** family_mortgage_second_child_birth_cert_before_escrow_tyumen
- **top_energy_mirror:** stopped_before_money (clock + bank gate before escrow)
- **newbuild_mechanism:** Семья с одним ребёнком оформляет **семейную ипотеку** на квартиру в строящемся ЖК Тюмени (ДДУ + эскроу). В брони и одобрении банка указана льготная программа «семейная ипотека». За **5 дней до открытия эскроу** риск-менеджер запрашивает **свидетельство о рождении второго ребёнка** (или актуальную выписку ЗАГС): в анкете/скоринге числится второй ребёнок, документ не приложили или ребёнок ещё не зарегистрирован. Банк ставит одобрение на паузу; застройщик напоминает, что бронь истекает через 72 часа. Семья **не открывает эскроу**, пересматривает программу (дожидаться регистрации / менять банк / терять бронь)
- **why_newbuild_not_secondary:** Сюжет в цепочке **новостройка**: бронь застройщика, проект ДДУ, счёт эскроу, ипотека на объект долевого строительства. Нет продавца вторички, ЕГРН-сделки, наследников, опеки на вторичке
- **scout_helper.py --check-query:** PASS 2026-09-29 (anti_dupe_hard PASS, topic focus PASS; fingerprint escrow_blocked — distinct from co-borrower escrow live and B19 matkapital)
- **story_dup.py --text:** PASS — cluster_id new
- **formula_spam_check:** last3 live newbuild skew escrow/DDU mismatch clauses; this skeleton = **family mortgage eligibility document** before escrow (new mechanism for last-3)

## Dzen news-casus shape (PASS)

- **event:** семья выбрала двушку в тюменском ЖК под семейную ипотеку, одобрение получили, дату эскроу назначили
- **risk:** без подтверждения права на семейную программу банк переведёт на рыночную ставку или снимет одобрение; бронь и цена лота под таймером
- **time:** 5 дней до открытия эскроу-счёта; параллельно срок брони 72 часа
- **finale:** свидетельство не успели / ребёнок не зарегистрирован — банк не открыл эскроу; семья не внесла деньги, бронь сгорела частично или перенесли сделку на другой банк с потерей скидки; agency landing: сверять условия семейной ипотеки и пакет документов **до** брони, не за 5 дней до эскроу
- **comment_magnet_angle:** «Если банк за 5 дней до эскроу требует свидетельство о втором ребёнке, а документа ещё нет — вы бы торопили регистрацию или отказывались от лота?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen family-mortgage casus without Klyshin)

## Wordstat MCP-KV (live 2026-09-29)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq |
|-------|---------|-----:|
| семейная ипотека тюмень | 55,11176 | 1309 |
| семейная ипотека тюмень условия | 55,11176 | 504 |
| семейная ипотека тюмень 2026 | 55,11176 | 422 |
| новостройки тюмень | 55,11176 | 8246 |
| купить новостройку в тюмени | 55,11176 | 1913 |
| семейная ипотека новостройка | 225 compare | 9481 |
| квартира в новостройке семейная ипотека | 225 compare | 2074 |

**wordstat_rework:**
- probe «семейная ипотека новостройка тюмень» → API empty {}
- probe «дду новостройка тюмень» → API empty {}
- **rework:** anchor Tyumen buyer spine «семейная ипотека тюмень» + newbuild escrow deadline in H1
- **final P0:** «семейная ипотека тюмень» **1309** (regions 55,11176); compare RU «семейная ипотека новостройка» **9481** (225)

## signal_urls (research)

- https://dzen.ru/holyslav
- https://www.domrf.ru/ — семейная ипотека / застройщики
- https://www.cbr.ru/ — ипотечные программы (контекст)
- Consultant 102-ФЗ / банковские правила семейной ипотеки (условия второго ребёнка) — для Research
- {{SITE_BASE}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check, formula_spam_check, anti_dupe_hard: PASS.

Lock topic_id B34, title, slug, article_dir, slot_rubric novostroyki, viral_mechanism from Trend Radar, research angles for Research role.
