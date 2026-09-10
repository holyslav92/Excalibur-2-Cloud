# Title inputs — B24 — 2026-09-10

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu`

## Scout handoff
- cluster_id: finish_package_mismatch_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild finish-package casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила новостройку, где ДДУ и приложение закрепляли чистовую отделку (обои, ламинат, готовый санузел, сантехника, двери)
  - risk: на первой приёмке — предчистовая/whitebox: штукатурка без обоев, стяжка без финиша, санузел без комплекта; застройщик предлагает акт «без замечаний» или доплату за доведение до чистовой
  - time: первая приёмка, первые 48 часов после уведомления о готовности
  - finale: отказ от акта «без замечаний», фиксация несоответствия с приложением к ДДУ, претензия / спор о приведении отделки к договорному пакету
- comment_magnet_angle: «В акте написали „без замечаний“, а отделка не та, что в ДДУ — вы бы всё равно подписали ключи или шли в претензию, даже если застройщик грозит неустойкой за затягивание?»
- title_draft (rework allowed): В Тюмени в ДДУ обещали чистовую — на ключах отдали предчистовую
- story_dup_check: PASS — cluster `finish_package_mismatch_ddu_tyumen`, distinct from B21 (kladovka), B12 (delay), B23 (apartments in EGRN), booking/DDU mismatch plots
- distinct_plot: расхождение **пакета отделки** (чистовая в ДДУ/приложении vs предчистовая/whitebox на ключах); не дефекты качества при совпадающем стандарте

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «отделка квартир в новостройках» — **173** (Tyumen 55+11176)
- support: «отделка новостройка» — **260** (55+11176)
- support: «новостройки Тюмень» — **4642** (55+11176)
- support: «чистовая отделка новостройка» — **34**; «тюмень новостройки с чистовой отделкой» — **8**
- support: «вайт бокс отделка квартиры в новостройке» — **10** (55+11176)

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ с чистовой отделкой по приложению (обои, ламинат, сантехника, двери), фактическая сдача предчистовой/whitebox на приёмке
- Reader problem: семья приходит на первую приёмку и видит не обещанную чистовую, а whitebox; представитель предлагает акт без замечаний или доплату; покупатель боится потерять ключи или позицию
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка)
- Surprising fact: whitebox и «с ремонтом» на рынке Тюмени — разные продукты; подмена пакета — не спор о вкусе обоев, а несоответствие приложению к ДДУ
- Voice angle: на приёмке смотреть не на шоурум и не на «потом доделаем», а на приложение к своему ДДУ
- Finale: отказ от акта «без замечаний» → фиксация расхождения → претензия
- Distinct from B21 (kladovka), B12 (перенос сдачи), B23 (квартира vs апартаменты в ЕГРН), B22 (ставка перед ДДУ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты» (B23 — другой plot)
«V tyumeni oplatili kladovku po ddu na klyuchah pomescheniya ne bylo» (B21 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка ипотеки перед ДДУ (B22), квартира vs апартаменты (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на ключах», «на приёмке», «в ДДУ»)
- **H1 на русском:** «предчистовую» или «предчистовая» — **не** whitebox/англицизм в заголовке (slug = predchistovuyu)
- Prefer scout title_draft energy: «В Тюmenи в ДДУ обещали чистовую — на ключах отдали предчистовую»
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
  "slug": "v-tyumeni-v-ddu-obeschali-chistovuyu-na-klyuchah-otdali-predchistovuyu",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
