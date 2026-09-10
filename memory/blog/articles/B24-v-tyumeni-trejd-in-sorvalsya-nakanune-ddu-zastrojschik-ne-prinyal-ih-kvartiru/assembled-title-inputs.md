# Title inputs — B24 — 2026-09-10

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-trejd-in-sorvalsya-nakanune-ddu-zastrojschik-ne-prinyal-ih-kvartiru`

## Scout handoff
- cluster_id: trade_in_rejected_developer
- klyshin_hook: none (fresh Tyumen newbuild trade-in casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, внесла бронь, получила ипотечное одобрение и рассчитывала закрыть первоначальный взнос через trade-in от застройщика
  - risk: за 24–36 часов до ДДУ оценщик снизил стоимость старой квартиры на 1,2 млн ₽; суммы зачёта не хватило для первоначального взноса и одобренного лимита; застройщик не принял объект на ранее озвученных условиях
  - time: пятница перед встречей в офисе застройщика в понедельник (подписание ДДУ)
  - finale: trade-in не состоялся, семья не подписала ДДУ, бронь сняли, планировку забронировал другой покупатель; деньги на эскроу не ушли, но скидка и выбранная квартира потеряны
- comment_magnet_angle: «Застройщик обещал trade-in устно и в рекламе, а в ДДУ этой строки нет: вы бы всё равно подписали договор бронирования, если условия trade-in не прописаны отдельным приложением?»
- title_draft (rework allowed): В Тюмени трейд-ин сорвался накануне ДДУ — застройщик не принял их квартиру
- story_dup_check: PASS — distinct from B22 (bank raised mortgage rate before DDU), B19 (escrow/matkapital), B06 (auto-appraisal on secondary as standalone deal), burned booking by price
- distinct_plot: trade-in оценка/отказ застройщика **перед ДДУ** — не банк меняет ставку, не эскроу/маткапитал, не автооценка вторички как отдельная сделка

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4670 (55+11176; RU225: 8607)
- support: «купить новостройку в тюмени» — 899
- support: «ипотека новостройка тюмень» — 201
- narrow: «трейд ин новостройка» — 5
- child: «дду новостройка» — 20

## Research — subject & conflict
- Subject: новостройка в Тюмени, trade-in старой квартиры в зачёт ДДУ, заниженная оценка за 24–36 часов до подписания, срыв первоначального взноса и ипотеки, потеря брони и планировки
- Reader problem: семья считает устное обещание менеджера и фиксацию цены новостройки при брони гарантией выкупа старой квартиры по ожидаемой сумме; за день до ДДУ оценка меняется
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм брони)
- Surprising fact: цена новостройки может быть зафиксирована на брони, но выкупная цена старой квартиры — нет; у ТИС оценку делает партнёр, выкупную стоимость утверждает покупатель
- Voice angle: разрыв между маркетинговым «в зачёт» и моментом, когда после финальной оценки нечем закрыть разницу; потеря до эскроу — без выбранной планировки, акции и времени
- Finale: ДДУ не подписали → бронь сняли → планировку забрал другой покупатель
- Distinct from B22 (ставка банка перед ДДУ), B19 (маткапитал/эскроу), B06 (автооценка на вторичке)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«Автооценка занизила цену — и квартира подорожала за сутки» (B06 — вторичка, другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка (B06), наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал+эскроу (B19), смена юрлица (B20), кладовка (B21), ставка банка перед ДДУ (B22), апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («накануне ДДУ», «за 24 часа»)
- One variant only
- Use «трейд-ин» or «trade-in» naturally; subject = trade-in / застройщик / оценка старой квартиры перед ДДУ
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
  "slug": "v-tyumeni-trejd-in-sorvalsya-nakanune-ddu-zastrojschik-ne-prinyal-ih-kvartiru",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
