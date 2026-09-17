# Title inputs — B27 — 2026-09-17

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-za-10-dnej-do-ddu-perenesli-v-drugoj-korpus-etazh-i-vid-ne-sovpali-sde`

## Scout handoff
- cluster_id: developer_corps_transfer_before_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild corpus-transfer casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени полгода выбирала новостройку; бронь 200 тыс. ₽; одобрение семейной ипотеки под конкретный корпус и лот (корпус А, 14-й этаж, вид на парк)
  - risk: за 10 дней до подписания ДДУ застройщик «заморозил» корпус А и предлагает только корпус Б — 6-й этаж, вид на стройплощадку, площадь −1,2 м², другой адрес в проекте ДДУ; при подписании теряют первоначальный лот и фиксированную цену
  - time: за 10 дней до назначенного подписания ДДУ; за 2 дня до открытия эскроу
  - finale: семья отказалась подписывать ДДУ с новым корпусом; застройщик — возврат брони «в течение 45 дней» без неустойки; банк снял резерв по ипотеке; до эскроу не дошли; альтернативный лот в ЖК уже разобрали
- comment_magnet_angle: «Бронь была на 14-й этаж с видом, в ДДУ дали 6-й на стройку: это законная „замена корпуса“ или подмена объекта, за которую надо было уходить сразу?»
- title_draft (rework allowed): В Тюмени за 10 дней до ДДУ перенесли в другой корпус — этаж и вид не совпали, сделку остановили
- story_dup_check: PASS — distinct from booking_expired_price_hike (48h section mismatch, same corps), ddu_apartment_vs_apartments_mismatch, floor-at-keys casus, bank appraisal, parking declaration, insurance pre-DDU, mortgage rate hike (B22)
- distinct_plot: **другой корпус** + этаж + вид + площадь **до** подписания ДДУ (не секция в том же корпусе, не этаж на ключах, не банк/ипотека/страховка)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 928 (55+11176; RU225 compare via scout)
- support: «новостройки тюмень» — 4480
- support: «квартиры в тюмени новостройки» — 1137
- support: «новостройки в тюмени от застройщика» — 674
- weak: «бронь новостройка тюмень» — 0 (no data; keep casus, rework phrasing)

## Research — subject & conflict
- Subject: новостройка в Тюмени, платная бронь на конкретный корпус/этаж/вид, семейная ипотека под лот; застройщик «пересаживает» в другой корпус за 10 дней до ДДУ
- Reader problem: семья полгода выбирала лот; банк готовит эскроу; срок одобрения ипотеки тикает; альтернативный лот уже разобрали
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, застройщика)
- Surprising fact: до регистрации ДДУ «замена корпуса» — не допсоглашение, а предложение заключить договор на другой объект; отказ подписать — законная остановка сделки; деньги за квартиру на эскроу ещё не лежат
- Voice angle: «заморозили корпус — сели в другой»: пока ДДУ не подписан, нельзя легально пересадить с 14-го с видом на парк на 6-й с видом на кран без согласия
- Finale: отказ от ДДУ → спор о возврате брони → снятие резерва ипотеки → до эскроу не дошли
- Distinct from B22 (ставка ипотеки перед ДДУ), B25 (чистовая на приёмке), B23 (апартаменты в ДДУ), LIVE 48h section casus (тот же корпус)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B26 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22), апартаменты (B23), чистовая на приёмке (B25), РВЭ без разрешения (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026
**NO colon (:) in H1** — use em dash (—) if needed, never «отказалась от ДДУ: квартиру…»

## Constraints
- Max ~50–70 chars (working title draft is too long — sharpen)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, **must include temporal marker** «за 10 дней до ДДУ»
- Must mention **другой корпус** (distinct plot); этаж/вид optional if over length
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-za-10-dnej-do-ddu-perenesli-v-drugoj-korpus-etazh-i-vid-ne-sovpali-sde",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
