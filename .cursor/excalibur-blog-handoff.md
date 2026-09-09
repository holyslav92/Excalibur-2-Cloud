# Scout handoff — B24

- **run_date:** 2026-09-09  
- **tenant:** The Риэлтор — Святослав Шакин, Тюмень  
- **topic_id:** B24  
- **topic_market_focus:** newbuild_only  
- **cluster_id:** acceptance_defects_penalty  
- **title_draft:** В Тюмени на приёмке новостройки подписали акт без замечаний — банк остановил регистрацию из-за дефектов  
- **slug:** v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-registraciyu  

## Topic lock

**LOCKED:** B24 only.  
Сюжет — исключительно новостройка по ДДУ в Тюмени: приёмка квартиры у застройщика, акт приёма-передачи, обнаруженные после подписи дефекты, приостановка ипотечно-регистрационного процесса. Не использовать и не ретайлить закрытый кластер `newbuild_apartments_instead_flat_ddu_tyumen`; не писать про B23, апартаменты или сравнение «апартаменты vs квартира».

## Demand spine

- **wordstat_preflight:** mcp-kv `wordstat_get_user_info` OK, Yandex Cloud API.
- **wordstat_rework:** probe «приемка квартиры в новостройке» 55+11176 — 122 → probe «акт приемки передачи квартиры» 55+11176 — 37, tail secondary in top requests → локализация под Тюмень и новый объектный механизм → final P0 «приемка квартиры в новостройке тюмень» 55+11176 — 32.
- **wordstat:** mcp_kv live | regions 55, 11176, compare 225 | P0 «приемка квартиры в новостройке тюмень» — **32** | parent spine «приемка квартиры в новостройке» — **122** | RU compare — **6032**.
- **supporting probes:**
  - «приемка квартиры в новостройке» — 122, регионы 55+11176;
  - «приемка квартиры в новостройке» — 6032, RU 225;
  - «акт приемки передачи квартиры» — 37, регионы 55+11176, secondary tail;
  - «дефекты при приемке новостройки» — API empty.

## Newbuild and top-energy lock

- **top_energy_mirror:** `paper_clean_then_broke`.
- **newbuild_mechanism:** Акт приёма-передачи по ДДУ: семья подписала документ «без замечаний» под давлением менеджера застройщика — «потом исправим». Через несколько дней независимая приёмка выявила дефекты отделки, окон и инженерии. На стадии ипотечно-регистрационного оформления банк остановил регистрацию права и выдачу остатка ипотечных средств; застройщик сослался на уже подписанный акт и отказался бесплатно устранять недостатки.
- **why_newbuild_not_secondary:** Это сдача квартиры по ДДУ от застройщика, приёмка построенного объекта, акт приёма-передачи и регистрация права на новостройку с ипотекой. Здесь нет продавца вторички, проверки ЕГРН, сделки купли-продажи вторичного жилья или иных secondary-механик.
- **klyshin_hook:** optional | none | fresh Tyumen newbuild acceptance casus without Klyshin | signal: none.

## Dzen news-casus shape

- **dzen_casus_shape:** PASS.
- **event:** Семья в Тюмени получила ключи от новостройки и на приёмке подписала акт без замечаний.
- **risk:** После подписи обнаружились дефекты отделки, окон и инженерных систем. Подписанный без замечаний акт стал основанием для отказа застройщика от бесплатного исправления, а регистрация права и ипотечный расчёт оказались под угрозой.
- **time:** Через пять дней после подписания акта, при подаче документов на регистрацию права в Росреестр.
- **finale:** Банк остановил регистрацию и выдачу транша. Застройщик отказался устранять недостатки бесплатно, ссылаясь на акт. Семья направила претензию: ключи формально получены, но право не зарегистрировано, а ипотека остаётся в подвешенном состоянии.
- **comment_magnet_angle:** «Менеджер сказал: “Подпишите, потом исправим”. Вы бы подписали акт без замечаний ради ключей в тот же день — или отказались бы принимать квартиру?»

## Anti-repeat and uniqueness

- **anti_repeat_preflight:** live_blog_20 + ledger + used-clusters sync OK | 27 active locks, last sync 2026-09-09 | closed newbuild plots reviewed, including escrow shortfall, wrong floor, double sale, apartments-vs-flat, mortgage rate hike, matkapital before keys, assignment debt, keys without permission, co-borrower removed, installment overdue, cottage gas, land area, extra finishing payment, trade-in rejected, booking expired, appraisal below DDU, keys delay penalty.
- **story_dup_check:** PASS | cluster_id: `acceptance_defects_penalty` | новый отдельный кластер: акт приёмки без замечаний + дефекты + приостановленный банком регистрационно-ипотечный контур.
- **h1_fingerprint_check:** PASS | fingerprint: `приёмка_новостройки__акт_без_замечаний__банк_остановил_регистрацию_из-за_дефектов`.
- **formula_spam_check:** PASS | last3_mechanisms: `keys_without_commissioning_permit | assignment_debt_found | matkapital_before_keys_child_shares` | текущий механизм: `acceptance_act_without_remarks + defects + registration_hold`, не совпадает.
- **anti_dupe_hard:** PASS.

## Research signal URLs

- https://dzen.ru/holyslav
- https://www.consultant.ru/document/cons_doc_LAW_51057/
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

## Gate flat fields (parser)

wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: акт приёма-передачи по ДДУ — подписали «без замечаний», дефекты после приёмки, банк остановил регистрацию
why_newbuild_not_secondary: сдача по ДДУ от застройщика и ипотечная регистрация новостройки, не вторичка
klyshin_hook: none | original: none | signal: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: 27 active locks
dzen_casus_shape: PASS | event: подписали акт без замечаний на приёмке | risk: дефекты + регистрация права | time: через 5 дней | finale: банк остановил регистрацию, претензия застройщику
comment_magnet_angle: «Менеджер сказал „подпишите, потом исправим“ — вы бы подписали акт без замечаний или отказались от ключей?»
wordstat_rework: probe «приемка квартиры в новостройке» 122 → «акт приемки передачи квартиры» 37 → final P0 «приемка квартиры в новостройке тюмень» 32
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «приемка квартиры в новостройке тюмень» 32 | новостройки parent spine 122 Tyumen / RU compare 6032
story_dup_check: PASS | cluster_id: acceptance_defects_penalty
h1_fingerprint_check: PASS | fingerprint: acceptance_act_without_remarks_bank_registration_defects
formula_spam_check: PASS | last3_mechanisms: keys_without_commissioning_permit | assignment_debt_found | matkapital_before_keys_child_shares
anti_dupe_hard: PASS
