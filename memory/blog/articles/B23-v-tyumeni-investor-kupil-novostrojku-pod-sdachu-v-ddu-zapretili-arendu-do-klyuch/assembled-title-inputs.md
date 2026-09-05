# Title inputs — B23 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B23. verdict: PASS.

## topic_id
B23

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch`

## Scout handoff
- cluster_id: newbuild_investor_ddu_rental_ban_before_keys_tyumen
- klyshin_hook: none (fresh Tyumen newbuild investor rental-ban casus without Klyshin)
- dzen_casus_shape: PASS
  - event: инвестор в Тюмени выбрал студию или однушку в строящемся ЖК под сдачу; внёс бронь; банк одобрил ипотеку с расчётом окупаемости после сдачи дома
  - risk: в проекте ДДУ — запрет аренды до получения ключей и регистрации собственности либо сдача только через УК застройщика с комиссией; доходность и выход через переуступку рушатся
  - time: накануне подписания ДДУ, через 2–3 недели после брони и одобрения ипотеки
  - finale: инвестор отказался подписывать ДДУ; бронь сгорела; плату за бронирование удержали; квартира вернулась в продажу; покупатель ищет другой объект у другого застройщика
- comment_magnet_angle: «Запрет на аренду в ДДУ до ключей — это законно или застройщик просто держит инвестора на крючке?»
- title_draft (rework allowed): В Тюмени инвестор купил новостройку под сдачу — в ДДУ запретили аренду до ключей
- story_dup_check: PASS — distinct from B22 (bank rate before DDU), B19 (matkapital/escrow), B12 (handover delay), B20 (legal entity change), mortgage clusters
- distinct_plot: инвестор под **будущую аренду**; ограничение в **ДДУ на сдачу до ключей** / УК / переуступку — не банк, не эскроу, не приёмка, не ипотечная ставка

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4660 (55+11176; RU225: 8705)
- child: «купить новостройку в тюмени» — 856
- support: «переуступка новостройка» — 2469 (RU225)
- support: «сдавать квартиру в аренду в новостройке» — 55 (RU225)

## Research — subject & conflict
- Subject: инвестор, новостройка в Тюмени, ДДУ, запрет аренды до ключей, бронь, ипотечное одобрение, доходность под сдачу
- Reader problem: считает доходность по будущей аренде; узнаёт об ограничениях только перед ДДУ — запрет сдачи до передачи, согласование арендатора, обязательная УК, комиссия, ограничение переуступки
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, застройщика, точных сумм брони)
- Surprising fact: запрет аренды до ключей может быть нейтральным следствием статуса объекта; опаснее условия после передачи и стоимость выхода через переуступку
- Voice angle: инвестор считает не цену метра, а момент, когда квартира реально принесёт доход; один пункт в ДДУ меняет всю модель
- Finale: отказ от ДДУ → потеря брони → поиск другого лота с проектом ДДУ до оплаты брони
- Distinct from B22 (ставка ипотеки перед ДДУ), B19 (маткапитал/эскроу), B12 (перенос ключей), B20 (смена юрлица)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: банк, не аренда)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B22 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc with finale hint, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («перед ДДУ», «до ключей», «накануне подписания»)
- newbuild only — investor rental scenario
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B23",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-investor-kupil-novostrojku-pod-sdachu-v-ddu-zapretili-arendu-do-klyuch",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
