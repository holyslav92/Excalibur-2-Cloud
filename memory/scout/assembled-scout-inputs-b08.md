# Scout assembled inputs — B08 run 2026-08-22

**INSTRUCTION FOR DEROUTER:** Ты Scout Excalibur BLOG. Твой ответ — **только** готовый текст файла handoff (markdown/plain), без пояснений, без BLOCKER, без shell. Cursor уже вызвал этот скрипт за тебя. Запиши handoff по формату из SKILL.

## Run context
- topic_id: B08 (next after B07)
- brand: The Риэлтор / Святослав Шакин / Тюмень
- date: 2026-08-22
- dzen_rf_pack: true
- story shape: news-casus (shared/dzen-news-casus.md)

## Rejected hook (live WP overlap)
- notary_not_shield_70k → SCOUT HELPER FAIL: overlap with LIVE-NOTARIUS-VSE-PROVERIL (WP already published notary +70k story)

## Selected Klyshin hook
- hook_id: zags_dead_wife_marital_share
- original: «Продавец сказал: "В браке не был". А потом нашлась умершая жена и наследники»
- angle: справка ЗАГС не на ту дату; умершая супруга; супружеская доля не выделена; цепочка наследников; банк отказал
- signal: https://t.me/klyshin_A (пост август 2026: брат и сестра, ДКП 1998, справка ЗАГС с 2004, муж был в браке, супруга умерла, дети от двух браков, наследство принято но доля в квартире не оформили, «покупайте так» — отказ; банк тоже отказал)
- localize: кейс переносим в Тюмень (вторичка), факты — Святослав Шакин / Тюмень

## Anti-dup check
- scout_helper: PASS (no cannibalization)
- story_dup: PASS (not inheritance_son_first_marriage cluster — другой plot: умершая жена + неоформленная супружеская доля + справка ЗАГС на неверный период)
- blocked clusters avoided: inheritance_son_first_marriage, matkapital, doverennost_svo, deposit_before_auction, discount_two_million

## Published siblings (do not duplicate plot)
- B07 nasledstvo-kvartiry-syn-ot-pervogo-braka-ne-otkazalsya
- Live WP: ipoteku-odobrili (ипотека+ЕГРН), v-vypiske-egrn-est-stroka, tri-mesyaca-iskali-kvartiru, notarius +70k

## Wordstat (MCP-KV live, regions 55+11176, compare 225)
- wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-22)
- probes:
  - «брачная доля квартиры» → 3
  - «согласие супруга на продажу квартиры» → 49
  - «наследство квартира продажа» → 157
  - «купить квартиру в тюмени» → 22880 (RU225: 40230)
- rework: слабый юридический жаргон → buyer spine «наследство квартира продажа» 157 + финальный P0 «купить квартиру в тюмени» 22880

## Title draft (news headline, Klyshin rhythm)
Сказали «в браке не был» — а в Тюмени перед авансом всплыла умершая жена и неоформленная доля

## Slug suggestion
skazali-v-brake-ne-byl-umershaya-zhena-neoformlennaya-dolya

## dzen_casus_shape
- PASS
- event: продавцы показали справку ЗАГС «не состоял в браке», проверка перед авансом в Тюмени
- risk: супружеская доля умершей жены не выделена; наследники приняли наследство, долю в квартире не оформили
- time: «перед авансом» / «на этапе проверки документов»
- finale: банк отказал в ипотеке; покупатель отказался от сделки (не «покупайте так»)

## signal_urls (≥2 today)
- https://t.me/klyshin_A
- https://dzen.ru/holyslav (свежий пост «Ипотеку одобрили, но обременение в ЕГРН…» — контекст проверки до аванса)
- https://t.me/holyslav92

## Output format required
Write `.cursor/excalibur-blog-handoff.md` with:
- topic_id B08
- title draft
- slug
- external_signal summary
- signal_urls list
- wordstat_preflight line
- klyshin_hook line (id | original | angle | signal URL)
- dzen_casus_shape line with event/risk/time/finale
- wordstat_rework line with all probe frequencies
- wordstat line with mcp_kv live, regions 55,11176,compare225, final P0 phrase+volume
- brief angle for Research/Writer (Tyumen casus, not checklist)
