# Title inputs — B21 — 2026-09-02

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B21. verdict: PASS.

## topic_id
B21

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli`

## Scout handoff
- cluster_id: newbuild_kp_land_boundary_utilities_denied_tyumen
- klyshin_hook: none (fresh Tyumen newbuild KP casus; signal https://t.me/klyshin_A checked, not used)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала дом в коттеджном посёлке от застройщика, подписала ДДУ, внесла деньги на эскроу, оформила ипотеку; на презентации — план с газом и водой у границы участка
  - risk: в день выдачи ключей коммуникации не подведены к границе участка / кадастровый контур не совпадает; застройщик настаивает на акте «как есть»; банк не разблокирует остаток ипотеки
  - time: день выдачи ключей, ~3 месяца после внесения на эскроу, после обещанного срока сдачи
  - finale (editorial): акт не подписали → суд → расторжение ДДУ → возврат с эскроу ~4 месяца → аналогичный дом подорожал → выбор между другим КП и квартирой в ЖК
- comment_magnet_angle: «Дом в коттеджном посёлке без газа и воды у забора — вы всё равно подпишете акт приёмки или будете ждать, пока застройщик подведёт коммуникации?»
- title_draft (rework allowed): В Тюмени в КП обещали газ и воду — на ключах коммуникации не подвели
- story_dup_check: PASS
- distinct_plot: не перенос сдачи/заморозка эскроу (B12), не маткапитал/семейная ипотека (B19), не смена юрлица (B20), не квартирная приёмка; стоп = дом в КП, газ/вода у забора не подведены к ключам, отказ от акта

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «коттеджные поселки тюмень купить дом» — 59 (55+11176), compare RU225 — 125
- support: «расторжение дду» — 123 (legal context, not main hook)
- support: «коттеджный поселок тюмень» — 1831 (too broad for H1)
- buyer spine: «новостройки тюмень купить от застройщика» — 528 (context only)

## Research — subject & conflict
- Subject: дом от застройщика в коттеджном посёлке под Тюменью по ДДУ; обещанные газ и вода у границы участка; приёмка ключей
- Reader problem: семья купила дом в КП, ориентируясь на обещание газа и воды, а в день ключей видит, что подключаться не к чему; подписывать акт страшно, отказ кажется риском для ипотеки и эскроу
- Casus: собирательный редакционный тюменский сюжет (без имён, КП, банка, сумм)
- Surprising fact: для ИЖС в МЖК раскрытие эскроу связано с вводом всех домов по проектной декларации, а не прямо с подписью конкретного покупателя на акте
- Voice angle: не «дом без коммуникаций — всегда ловушка», а разбор точки, где рекламное «сети в посёлке» должно стать проверяемым обязательством по конкретному дому и участку
- Key tension: «газ есть в посёлке» ≠ «газ подведён к границе вашего участка»; рекламный генплан ≠ кадастровый контур
- Finale: отказ от акта → суд → расторжение → возврат эскроу; аналог подорожал
- Distinct from B12 (перенос сдачи ЖК), B19 (маткапитал/эскроу), B20 (смена юрлица), B09 (ЕГРН после одобрения)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B15, B19, B20 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица/новый ДДУ (B20).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (HARD max 70)
- News headline energy, Klyshin rhythm, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на ключах», «в день выдачи»)
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
  "slug": "v-tyumeni-v-kp-obeschali-gaz-i-vodu-na-klyuchah-kommunikacii-ne-podveli",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
