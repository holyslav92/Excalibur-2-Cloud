# Title inputs — B24 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Return ONE title-brief JSON for topic B24. **LOCKED H1** from Scout — use verbatim for both `h1` and `title`. verdict: PASS.

## LOCKED H1 (verbatim — do not shorten or rephrase)
В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela`

## Scout handoff
- cluster_id: newbuild_assignment_seller_raised_price_booking_lost_tyumen
- klyshin_hook: none (fresh Tyumen newbuild assignment casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в строящемся ЖК по переуступке; цена у первого дольщика ниже застройщика; согласовали сумму, проверили исходный ДДУ, внесли аванс по уступке, получили бронь у застройщика
  - risk: за сутки до подписания договора переуступки продавец потребовал доплату около 280 тысяч рублей; объяснения менялись (рост цены у застройщика, индексация, ошибка в расчёте); без доплаты отказался продолжать и давать согласие
  - time: до регистрации переуступки оставалось 24 часа; до этого прошла неделя согласований и бронирования
  - finale: покупатель не доплатил; переуступка сорвалась; бронь у застройщика сгорела; квартира ушла другому; аванс удержан полностью или возвращён частично — по условиям соглашения
- comment_magnet_angle: «Продавец по переуступке поднял цену накануне ДДУ: вы бы доплатили 280 тысяч, чтобы не потерять бронь, или отпустили квартиру, даже если аванс может сгореть?»
- title_draft (preferred shape): В Тюмени переуступку подняли на 280 тысяч за сутки до ДДУ — бронь сгорела
- story_dup_check: PASS — distinct from B22 (bank rate before DDU), B23 (bank appraisal below DDU price), trade-in cluster, generic price-after-booking without assignment seller
- distinct_plot: **продавец права требования по переуступке** меняет согласованную доплату перед регистрации уступки; не банк, не оценка, не трейд-ин

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 639 (55+11176; Scout live)
- context anchor: «новостройки тюмень» — 3640 (region 55)
- niche: «переуступка новостройка» — 13
- legal spine: «договор уступки права требования» — 85
- child: «покупка новостройки по переуступке» — 2

## Research — subject & conflict
- Subject: покупка новостройки в Тюмени по переуступке права требования по ДДУ; аванс по уступке; бронь у застройщика; цедент требует +280 000 ₽ за сутки до регистрации
- Reader problem: семья вложила время и деньги; перед регистрацией цедент меняет сумму; короткий срок брони; решать — доплачивать или рисковать авансом
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, застройщика)
- Surprising fact: при переуступке покупают право требования по ДДУ, не «квартиру со скидкой»; рост витринной цены у застройщика не переписывает автоматически цену уступки
- Voice angle: разрыв между закреплённой ценой уступки в документах и тикающей бронью у застройщика
- Finale: отказ доплатить → срыв переуступки → бронь сгорела → лот другому → спор об авансе
- Distinct from B22 (банк поднял ставку перед ДДУ — бронь сгорела); B23 (оценка ниже цены ДДУ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: банк, не продавец уступки)
«Автооценка занизила цену — и квартира подорожала за сутки» (B06 — другой plot)

## Anti-dup published titles
B02–B22 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), банк поднял ставку перед ДДУ (B22).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, как устроена, гайд

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («за сутки до ДДУ», «накануне ДДУ»)
- Include digit 280 thousand as punch when possible
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-pereustupku-podnyali-za-sutki-do-ddu-bron-sgorela",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
