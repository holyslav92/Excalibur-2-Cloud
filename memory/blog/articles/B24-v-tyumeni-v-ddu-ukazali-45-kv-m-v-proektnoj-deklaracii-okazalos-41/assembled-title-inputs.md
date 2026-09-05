# Title inputs — B24 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-ukazali-45-kv-m-v-proektnoj-deklaracii-okazalos-41`

## Scout handoff
- cluster_id: newbuild_ddu_area_vs_project_declaration_mismatch_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus without Klyshin — preferred)
- dzen_casus_shape: PASS
  - event: семья подписала ДДУ на новостройку в Тюмени, банк готовил ипотеку
  - risk: в ДДУ указано 45 кв.м, в проектной декларации застройщика (dom.rf / ЕИСЖС) для того же лота — 41 кв.м
  - time: за три дня до регистрации / до перевода денег на эскроу
  - finale: регистрацию остановили, деньги на эскроу не перевели, бронь под угрозой
- comment_magnet_angle: «Смотреть проектную декларацию до ДДУ — паранойя или норма?»
- title_draft (rework allowed): В Тюмени в ДДУ указали 45 кв.м — в проектной декларации оказалось 41
- story_dup_check: PASS — distinct legal plot: расхождение площади в ДДУ vs проектная декларация; не B23 (квартира vs апартаменты в ЕГРН), не B22 (ставка перед ДДУ), не B21 (кладовка), не B20 (смена юрлица), не B19 (маткапитал/эскроу)
- distinct_plot: менеджер ОП показывает планировку 45 м², в декларации на dom.rf для лота 41 м² (балкон/лоджия по-разному или ошибка в экспликации); банк сверяет предмет залога с декларацией перед эскроу

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4660 (55+11176; compare RU225)
- support: «проектная декларация застройщика» — 48
- support: «приемка квартиры в новостройке тюмень» — 33

## Research facts (research-input.md; research-notes pending)
- Subject: новостройка в Тюмени, ДДУ, проектная декларация на наш.дом.рф / dom.rf, ипотека, эскроу
- Reader problem: семья нашла квартиру в новостройке, одобрила ипотеку, готовится к ДДУ — и видит, что площадь в договоре не бьётся с проектной декларацией застройщика
- Casus: собирательный тюменский сюжет (без имён ЖК/банка)
- Surprising fact: расхождение 4 кв.м (45 vs 41) ≈ 8,9% — существенно для цены и ипотеки; банк может отказать в открытии эскроу при несоответствии предмета ДДУ
- Legal: ст. 4 и 7 214-ФЗ — проектная декларация обязательна; ДДУ должен соответствовать проектной документации; до перевода на эскроу — точка контроля
- Finale: регистрацию остановили, эскроу не открыли, бронь под угрозой
- Distinct from B23 (апартаменты в ЕГРН), B22 (ставка ипотеки перед ДДУ), B21 (кладовка), B20 (смена юрлица), B19 (маткапитал)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты» (B23 — другой plot: статус, не площадь)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), квартира vs апартаменты в ЕГРН (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за три дня до регистрации», «перед эскроу»)
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
  "slug": "v-tyumeni-v-ddu-ukazali-45-kv-m-v-proektnoj-deklaracii-okazalos-41",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
