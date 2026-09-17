# Title inputs — B27 — 2026-09-17

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-prilozhenii-k-ddu-nashli-zapret-sdavat-kvartiru-investor-ostanovil-e`

## Scout handoff
- cluster_id: newbuild_ddu_rental_ban_investor_tyumen
- klyshin_hook: none (fresh Tyumen newbuild rental-ban casus without Klyshin)
- top_energy_mirror: stopped_before_money
- newbuild_mechanism: инвестор в Тюмени берёт студию в строящемся ЖК под аренду; бронь + предодобрение ипотеки; за 2 дня до визита в банк юрист на стр. 14 приложения №3 к проекту ДДУ находит запрет сдавать до регистрации дома и после — только с согласия УК; аренда была в финмодели; ДДУ не подписан, эскроу не открывали, деньги не переводились; бронь сгорела; альтернативный лот без ограничения на 240 тыс. ₽ дороже — отказ
- dzen_casus_shape: PASS
  - event: инвестор в Тюмени, студия в новостройке под сдачу; менеджер обещал «свободное использование»
  - risk: приложение к ДДУ запрещает аренду до ключей/регистрации и ограничивает после; без аренды сделка не сходится
  - time: 2 дня до визита в банк для открытия эскроу
  - finale: ДДУ не подписан; бронь потеряна; эскроу не открывали; отказ от доплаты 240 тыс. за другой лот
- comment_magnet_angle: «Менеджер сказал: сдавать можно. В приложении — запрет. Доплатите 240 тысяч за другой лот или уйдёте к другому застройщику, даже потеряв бронь?»
- title_draft (rework allowed): В Тюмени в приложении к ДДУ нашли запрет сдавать квартиру — инвестор остановил эскроу
- **SEMANTIC HARD:** hero did NOT open or fund escrow — use «до эскроу», «не подписал ДДУ», «остановил сделку», NOT «остановил эскроу» as if account existed
- story_dup_check: PASS — distinct plot: rental ban in DDU appendix blocks investor model; not B12/B19/B20/B22/B23/B25/B26
- distinct_plot: запрет аренды в приложении к ДДУ → отказ до подписи; не B22 (ставка), не B23 (апартаменты), не B25 (чистовая), не B26 (РВЭ/транш)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 928 (55+11176)
- support: «студия в тюмени купить в новостройках» — 106; «новостройки тюмень купить в ипотеку» — 92
- RU225: «договор долевого участия эскроу» — 439; «можно ли сдать квартиру в новостройке» — 43
- rework: spine через ДДУ/приложение/аренда/новостройка/эскроу до регистрации

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ + приложения, инвестор под аренду, бронь, ипотека, эскроу до регистрации
- Reader problem: устное «можно сдавать» vs запрет в приложении №3; обнаружение за 2 дня до банка
- Casus: редакционный тюменский сценарий 2026 (без имён, ЖК, банка)
- Voice angle: сделка выглядит собранной (бронь + ипотека), доходная модель рушится одной оговоркой в приложении
- Surprising fact: 214-ФЗ не требует «право сдавать» в ДДУ; деньги на эскроу — после регистрации; отказ до подписи дешевле, чем после
- Finale: не подписал ДДУ; бронь сгорела; отказ от лота +240 тыс.
- Distinct from B22 (ставка), B19 (эскроу/маткапитал), B20 (юрлицо), B25 (отделка), B26 (РВЭ/транш)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — other plot)

## Anti-dup published titles
B02–B15, B19–B26 published. Avoid: перенос сдачи (B12), маткапитал/эскроу (B19), юрлицо (B20), ставка (B22), апартаменты (B23), чистовая (B25), РВЭ/транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (scout draft ~78 — tighten while keeping stakes + newbuild marker)
- **HARD:** include «новостройк» or «застройщик» or «ДДУ» or «эскроу» in h1 (topic_focus gate)
- **HARD:** do NOT imply escrow was opened/funded — prefer «до эскроу», «не подписал ДДУ»
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker when it helps («2 дня до банка», «в приложении к ДДУ», «240 тысяч»)
- One variant only
- Clear subject: приложение к ДДУ / запрет аренды / инвестор / новостройка

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-prilozhenii-k-ddu-nashli-zapret-sdavat-kvartiru-investor-ostanovil-e",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
