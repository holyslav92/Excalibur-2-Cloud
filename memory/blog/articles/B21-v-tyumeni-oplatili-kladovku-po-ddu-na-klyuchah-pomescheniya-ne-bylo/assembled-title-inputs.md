# Title inputs — B21 — 2026-09-02

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B21. verdict: PASS.

## topic_id
B21

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo`

## Scout handoff
- cluster_id: newbuild_ddu_cellar_paid_not_handed_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в новостройке; в ДДУ отдельной строкой указана кладовка с номером и площадью, сумма включена в цену и оплачена на эскроу
  - risk: в день выдачи ключей кладовку не передали — «ещё не построили», номер изменился или это «опция»; в акте приёма-передачи кладовки нет
  - time: день выдачи ключей через 14 месяцев после подписания ДДУ
  - finale: акт на квартиру подписали под давлением срока ипотеки; кладовку обещали «дописать потом»; через 2 месяца предложили меньшую кладовку или доплату 180 тыс. ₽; спор в претензии; ключи от квартиры уже получены
- comment_magnet_angle: «Кладовку прописали в ДДУ с номером — вы подписываете акт приёмки квартиры, если кладовку не передали?»
- title_draft (rework allowed): В Тюмени оплатили кладовку по ДДУ — на ключах помещения не было
- story_dup_check: PASS
- distinct_plot: не перенос сдачи/заморозка эскроу (B12), не смена юрлица (B20), не маткапитал/семейная ипотека (B19), не дефекты приёмки квартиры; стоп на оплаченной кладовке по ДДУ, непереданной на ключах

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить кладовку в новостройке тюмень» — 18 (55+11176)
- compare RU225: «купить кладовку в новостройке тюмень» — 19
- support: «кладовка новостройка» — 25
- parent: «купить кладовку в новостройке» — 925 (RU225)
- context: «приемка квартиры в новостройке тюмень» — 35 (acceptance cluster — не дублировать угол)
- probe: «кладовка дду новостройка» — 0 (Tyumen; WORDSTAT PARTIAL)

## Research — subject & conflict
- Subject: новостройка в Тюмени, кладовка как нежилое помещение в зарегистрированном ДДУ (номер, площадь, цена), оплата через эскроу, непередача на день ключей
- Reader problem: покупатель оплатил кладовку по ДДУ, но на выдаче ключей помещение не передали; неясно, можно ли подписывать акт на квартиру и не потеряет ли права на кладовку
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка)
- Surprising fact: спрос на кладовые в тюменских новостройках упал >60% г/г, но у уже оплатившего покупателя проблема обратная — добиться согласованной кладовки после акта на квартиру сложнее
- Voice angle: семья уже «внутри» квартиры с ипотекой — спор идёт за метры в подвале, которые в ДДУ выглядели как закрытая сделка
- Finale: подписали акт на квартиру под ипотечным давлением → устное «допишем потом» → через 2 месяца меньшая кладовка или доплата → претензия
- Distinct from B12 (перенос сдачи, эскроу заморозили), B20 (смена юрлица, новый ДДУ), B19 (маткапитал блокирует эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B15, B19, B20 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на ключах», «через 14 месяцев»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B21",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
