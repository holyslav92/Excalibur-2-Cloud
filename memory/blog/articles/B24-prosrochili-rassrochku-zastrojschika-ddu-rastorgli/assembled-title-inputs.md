# Title inputs — B24 — 2026-09-07

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-prosrochili-rassrochku-zastrojschika-ddu-rastorgli-uderzhali-vznos`

## Scout handoff
- cluster_id: installment_penalty_developer
- klyshin_hook: none (fresh Tyumen newbuild installment casus without Klyshin)
- top_energy_mirror: clock_ran_out — пять дней просрочки превратились в угрозу потери ДДУ, квартиры и первого взноса
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в ЖК, оформила рассрочку от застройщика, внесла первый взнос и продолжала платить по графику
  - risk: очередной платёж задержался на пять дней; застройщик трактует просрочку как нарушение ДДУ, начисляет пени и инициирует расторжение с удержанием внесённой суммы
  - time: на пятый день после установленной даты платежа, примерно за три недели до плановой сдачи корпуса
  - finale: уведомление о расторжении; взнос 180 тыс. руб. удержали; квартиру снова выставили на продажу; претензия направлена, спор на досудебной стадии — ключи не переданы, деньги не возвращены
- comment_magnet_angle: «Просрочка на пять дней — законный повод расторгнуть ДДУ и оставить взнос у застройщика, или вы бы требовали вернуть всё через суд, даже если в договоре есть “копеечная” неустойка?»
- title_draft (rework allowed): В Тюмени просрочили рассрочку застройщика на пять дней — ДДУ расторгли и удержали взнос
- story_dup_check: PASS — distinct from delay of handover/penalty, early payoff discount loss, escrow/matkapital, mortgage rate change before DDU
- distinct_plot: просрочка графика рассрочки по ДДУ → одностороннее расторжение застройщиком → удержание первого взноса (не задержка сдачи, не досрочное погашение, не смена юрлица)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4670 (55+11176; RU225: 8658)
- support: «купить новостройку в тюмени» — 870
- narrow: «рассрочка застройщик новостройка» — 11
- narrow: «рассрочка новостройка тюмень» — 12
- narrow: «ДДУ расторжение новостройка» — 0 / empty

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с рассрочкой от застройщика, просрочка очередного платежа на 5 дней, одностороннее расторжение, удержание 180 000 руб. взноса
- Reader problem: покупатель не понимает, может ли застройщик из-за короткой просрочки забрать квартиру и удержать первый взнос
- Casus: редакционный сюжет для Тюмени (без ЖК, застройщика, банка, персональных данных)
- Surprising fact: при законном одностороннем отказе 214-ФЗ запрещает зачесть неустойку в сумму возврата — пеня не вычитается автоматически из внесённых денег
- Voice angle: разрыв между короткой задержкой платежа и риском потерять квартиру за три недели до сдачи; отделить эмоциональное уведомление от юридических порогов (систематичность / 2 месяца по ч. 5 ст. 5)
- Finale: расторжение инициировано, взнос удержан, квартира снова в продаже, досудебный спор открыт
- Legal note for angle (not in H1): единичная 5-дневная просрочка сама по себе не соответствует основаниям ч. 5 ст. 5 214-ФЗ

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22), апартаменты вместо квартиры (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на пять дней», «за три недели до сдачи»)
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
  "slug": "v-tyumeni-prosrochili-rassrochku-zastrojschika-ddu-rastorgli-uderzhali-vznos",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
