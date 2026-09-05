# Scout inputs — 2026-09-05 (B23)

**CRITICAL EXECUTION CONTEXT:** You are already running inside `excalibur_blog_derouter_opus_chat.py` (utility tier gpt-5.6-terra). The conductor completed all shell/MCP/Wordstat gates. **Your job is ONLY to write the Scout handoff markdown body** — no tool calls, no BLOCKER messages, no refusals. Output the complete handoff text now.

**run_date:** 2026-09-05 (YEKT Saturday slot ~10:17 MSK)
**tenant:** The Риэлтор — Святослав Шакин, Тюмень (tymenrieltor.ru)
**topic_market_focus:** newbuild_only
**dzen_rf_pack:** true — Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN heroes DENY

## Anti-repeat preflight (DONE)

- `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 21 active locks (last_sync 2026-09-05)
- **Recent newbuild live WP Sep 1–5 (distinct cluster required):**
  - trade-in от застройщика сорвался за день до ДДУ — бронь сгорела
  - ипотека одобрена, оценка банка ниже цены ДДУ на 400к — бронь сгорела
  - категория земли сорвала ипотеку на дом в КП
  - аванс перевели на чужой эскроу-счёт
  - банк поднял ставку перед ДДУ (B22)
  - застройщик потребовал подписать акт с дефектами
  - банк снял одобрение за 72ч до ДДУ
  - показали чистовую — в ДДУ предчистовая
  - ключи задержали 8 мес — неустойку сертификатом
  - площадь в ДДУ не сошлась с ключами
  - кладовка по ДДУ не оказалась (B21)
  - смена юрлица застройщика (B20)
  - семейная ипотека — эскроу не открыли (B19)
  - оплатили переуступку — застройщик не оформил ДДУ
  - цена выросла после брони на 380 тыс.
  - дом в КП без газа и воды на ключах
  - мокрая стяжка на приёмке
- **Closed clusters (30d):** see memory/scout/used-clusters.json; B22 newbuild_mortgage_rate_changed_before_ddu_tyumen published 2026-09-04
- `scout_helper.py --check-query` PASS for proposed title+cluster+slug
- `excalibur_blog_topic_focus.py` PASS (on-focus: дду)

## Proposed topic (PASS topic_focus + scout_helper + story_dup PASS)

- **topic_id:** B23
- **title_draft:** В Тюмени инвестор купил новостройку под сдачу — в ДДУ запретили аренду до ключей
- **slug:** v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuchey
- **cluster_id (new):** newbuild_investor_ddu_rental_ban_before_keys_tyumen
- **story_dup_check:** PASS — distinct from Sep 2 assignment refusal (paid uступка, developer won't re-register); distinct from Sep 1 price hike after booking; distinct from all mortgage/bank/escrow/defects/delay clusters; plot = инвестор бронирует лот под арендный доход, на этапе ДДУ в договоре пункт о запрете сдачи/субаренды до регистрации права собственности и/или без согласия застройщика; инвестор отказывается подписывать, бронь сгорает или вынужден подписать без планируемого дохода

## Dzen news-casus shape (target PASS)

- **event:** инвестор в Тюмени выбрал студию/однушку в строящемся ЖК под сдачу в аренду, внёс бронь, банк одобрил ипотеку с расчётом окупаемости от аренды после сдачи дома
- **risk:** в проекте ДДУ обнаружен пункт: запрет на сдачу в аренду до получения ключей и регистрации собственности (или сдача только через управляющую компанию застройщика с комиссией); расчёт доходности рушится, выход через переуступку до ключей либо запрещён, либо с штрафом
- **time:** накануне подписания ДДУ, через 2–3 недели после брони и одобрения ипотеки
- **finale:** инвестор отказался подписывать ДДУ на таких условиях; бронь сгорела, застройщик удержал плату за бронирование; квартира ушла в продажу, инвестор искал другой лот с другим застройщиком
- **comment_magnet_angle:** «Запрет на аренду в ДДУ до ключей — это законно или застройщик просто держит инвестора на крючке?»

## Klyshin hook

- **klyshin_hook:** none | original: none (fresh Tyumen newbuild investor casus without Klyshin — preferred; open angle from next-cluster-guidance: инвестор сдача vs переуступка до ключей)

## Wordstat MCP-KV (live 2026-09-05)

**Preflight:** wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| новостройки тюмень | 55+11176 | 4660 (context) |
| новостройки тюмень | 225 (compare) | 8705 |
| купить новостройку в тюмени | 55+11176 | 856 |
| купить новостройку в тюмени | 225 (compare) | 1867 |
| ипотека тюмень новостройки от застройщика | 55+11176 | 100 |
| новостройки семейная ипотека тюмень | 55+11176 | 30 (family angle — B19 cluster) |
| дом в тюмени в коттеджном поселке | 55+11176 | 64 (KP angle — Sep 4 land category cluster) |
| приемка квартиры в новостройке тюмень | 55+11176 | 33 (acceptance cluster closed) |
| переуступка новостройка тюмень | 55+11176 | API empty |
| долгострой тюмень новостройки | 55+11176 | API empty |

**wordstat_rework log:**
- probe «новостройки тюмень» 55+11176 → 4660 (strong but generic; kept as context)
- probe «новостройки семейная ипотека тюмень» 55+11176 → 30 (weak; B19 escrow/matkapital cluster)
- probe «дом в тюмени в коттеджном поселке» 55+11176 → 64 (KP plot taken Sep 2–4)
- probe «ипотека тюмень новостройки от застройщика» 55+11176 → 100 (mortgage-heavy; overlaps B22/B19 bank clusters)
- probe «купить новостройку в тюмени» 55+11176 → 856; compare RU225 → 1867
- **rework:** localize Tyumen + investor buyer intent on newbuild purchase → **final P0 «купить новостройку в тюмени» regions 55,11176 freq 856** (compare RU225 1867)

## signal_urls (research)

- https://dzen.ru/holyslav — контекст новостроек и инвестиционных кейсов; не дубль кластера
- https://t.me/klyshin_A — checked, not used this slot
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/
- Контекст: 214-ФЗ о долевом строительстве, типовые пункты ДДУ об использовании объекта (без героизации Meta/запрещённых площадок)

## Output required

Write complete Scout handoff markdown per SKILL.md with all fields:
wordstat_preflight, klyshin_hook, anti_repeat_preflight, dzen_casus_shape PASS (event/risk/time/finale), comment_magnet_angle, wordstat_rework, wordstat P0 with mcp_kv + regions 55,11176,compare225, story_dup_check PASS + cluster_id.

Lock topic_id B23, title, slug, signal_urls, research angles for Research role.
