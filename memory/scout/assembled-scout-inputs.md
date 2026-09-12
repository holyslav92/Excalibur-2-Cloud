# Scout inputs — 2026-09-09 (B24, slot 12:00 UTC / 17:00 YEKT)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-09 (weekday slot 17:00 YEKT / 12:00 UTC)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень ({{PUBLIC_SITE_URL}})
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 23 active locks (last_sync 2026-09-09)
- **Live WP ~20 (2026-09-09) — DO NOT reuse plot:**
  - неустойка за просрочку ключей / приёмка (2026-09-09)
  - ребёнку 7 лет — семейная ипотека пересчитали (2026-09-09)
  - акт приёмки без замечаний — банк остановил транш (2026-09-09)
  - ключи без разрешения на ввод (2026-09-08)
  - переуступка долг 94 тыс (2026-09-08)
  - маткапитал за 3 недели до ключей (2026-09-08)
  - созаёмщика исключили перед ДДУ (2026-09-07)
  - рассрочка застройщика — ДДУ расторгли (2026-09-07)
  - газ у коттеджа обещали у забора (2026-09-07)
  - этаж в ДДУ vs на ключах 12 vs 2 (2026-09-07)
  - эскроу не хватило 400 тыс (2026-09-06)
  - участок 12 соток vs 8 в кадастре (2026-09-06)
  - ДДУ 45 м² vs декларация 41 (2026-09-05) — area plot TAKEN
  - доплата 300 тыс за отделку перед ключами / предчистовая (2026-09-06) — finish plot TAKEN
  - B23 апартаменты вместо квартиры в ЕГРН
  - B22 ставка ипотеки перед ДДУ / бронь сгорела
  - B21 кладовка оплачена — не выдали
  - B20 смена юрлица застройщика
- **Rejected candidates (scout_helper FAIL or overlap):**
  - «на ключах не оказалось балкон» → 35% overlap B21 cellar cluster
  - страховка жизни перед ДДУ → 41% overlap escrow-400k cluster
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_scout_story_dup.py --text` PASS
- `excalibur_blog_topic_focus.py` PASS

## Proposed topic (PASS all gates)

- **topic_id:** B24
- **title_draft:** В Тюмени изменили проектную декларацию — в новой планировке пропал балкон из ДДУ
- **slug:** v-tyumeni-izmenili-proektnuyu-deklaratsiyu-propala-balkon-iz-ddu
- **article_dir:** memory/blog/articles/B24-v-tyumeni-izmenili-proektnuyu-deklaratsiyu-propala-balkon-iz-ddu
- **cluster_id (new):** newbuild_project_declaration_balcony_removed_tyumen
- **top_energy_mirror:** paper_clean_then_broke
- **newbuild_mechanism:** изменение проектной декларации / проектной документации застройщика — в приложении к ДДУ и на планировке был застеклённый балкон/лоджия, после внесения изменений в проект на приёмке балкон отсутствует; застройщик ссылается на уведомление об изменении проекта
- **why_newbuild_not_secondary:** сюжет только про ДДУ, застройщика, проектную декларацию и приёмку квартиры в новостройке; не про вторичку, не про ЕГРН-продавца
- **story_dup_check:** PASS — distinct from B23 apartments, B21 cellar, area 45/41, floor 12/2, gas, escrow-400k

## Dzen news-casus shape (target PASS)

- **event:** семья в Тюмени выбрала квартиру в новостройке с застеклённым балконом по планировке в ДДУ и рекламе, внесла аванс/эскроу, дождалась ключей
- **risk:** застройщик опубликовал изменение проектной декларации; на фактической планировке балкон/лоджия исчезли — меньше площадь, другой вид из окна, нельзя застеклить «как в шоуруме», банк может пересмотреть залоговую стоимость
- **time:** на приёмке квартиры, за 2–3 недели до подписания акта передачи (после уведомления об изменении проекта)
- **finale:** семья отказалась подписывать акт без скидки/восстановления балкона; застройщик предложил символическую компенсацию; банк приостановил последний транш ипотеки; спор ушёл в претензию/досудебку — ключи не получили
- **comment_magnet_angle:** «В приложении к ДДУ нарисован балкон, а застройщик говорит „проект изменился по закону“: вы бы подписали акт без лоджии ради ключей или требовали скидку или расторжение ДДУ?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild project-change casus without Klyshin — preferred)

## Wordstat MCP-KV (live 2026-09-09)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| балкон новостройка | 55,11176 | 25 |
| новостройки с балконами | 55,11176 | 13 (child) |
| проектная декларация застройщика | 55,11176 | 20 |
| приемка квартиры в новостройке тюмень | 55,11176 | 30 |
| **новостройки тюмень** | **55,11176** | **4642** |
| **новостройки тюмень** | **225 (compare)** | **8616** |

**wordstat_rework log:**
- probe «балкон новостройка» 55+11176 → 25; child «новостройки с балконами» → 13 (story hook, moderate)
- probe «проектная декларация застройщика» 55+11176 → 20 (mechanism-specific, moderate)
- probe «площадь в дду» 55+11176 → 10 (weak; area plot taken by live 45/41 m² post)
- probe «чистовая отделка новостройка» 55+11176 → 34 (finish plot taken by live 300k доплата)
- **rework:** localize Tyumen + newbuild buyer jargon (новостройки, ДДУ, проектная декларация) → **final P0 «новостройки тюмень» regions 55,11176,compare225 freq 4642 (55+11176) / 8616 (RU225)**

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек; не дубль кластера
- https://www.domrf.ru/ — проектные декларации застройщиков (dom.rf)
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — 214-ФЗ, изменение проектной декларации
- https://t.me/klyshin_A — checked, not used this slot
- {{PUBLIC_SITE_URL}}/blog/
- https://t.me/Tyumen_Rieltor

## Output required

Write complete Scout handoff markdown per SKILL.md with ALL fields including YAML frontmatter:
topic_id, title, slug, article_dir, cluster_id, top_energy_mirror, newbuild_mechanism, why_newbuild_not_secondary, wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id, h1_fingerprint_check PASS + fingerprint, formula_spam_check PASS + last3_mechanisms, anti_dupe_hard PASS, signal_urls, status: PASS.

Lock topic_id B24, title, slug, article_dir, signal_urls for Research role.
