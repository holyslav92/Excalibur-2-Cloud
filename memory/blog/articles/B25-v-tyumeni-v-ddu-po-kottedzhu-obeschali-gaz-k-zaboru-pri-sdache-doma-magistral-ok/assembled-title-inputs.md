# Title inputs — B25 — 2026-09-07

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B25. verdict: PASS.

## topic_id
B25

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-po-kottedzhu-obeschali-gaz-k-zaboru-pri-sdache-doma-magistral-ok`

## Scout handoff
- cluster_id: kp_gas_boundary_mismatch_on_keys_tyumen
- klyshin_hook: none (original Tyumen newbuild casus без Klyshin)
- dzen_casus_shape: PASS
  - event: сдача дома в коттеджном посёлке под Тюменью
  - risk: в ДДУ и проектной декларации газ «к границе участка», при сдаче магистраль в 180 метрах от забора; подключение от 600 тыс. руб.
  - time: за две недели до подписания акта приёмки
  - finale: акт не подписали; застройщик предложил доплату 620 тыс. руб. либо рассрочку на коммуникации
- comment_magnet_angle: «Газ в двухстах метрах — это вообще выполнение ДДУ или уже отдельная услуга?»
- title_draft (rework allowed): В Тюмени в ДДУ по коттеджу обещали газ к забору — при сдаче дома магистраль оказалась в 180 метрах
- story_dup_check: PASS
- distinct_plot: не смена юрлица (B20), не апартаменты в ЕГРН (B23), не перенос сдачи/эскроу (B12), не кладовка (B21); стоп на этапе приёмки дома в КП/ИЖС — расхождение обещаний по газу в ДДУ и фактической магистрали

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень купить от застройщика» — 422 (55+11176)
- probe: «купить дом в тюмени от застройщика» — 155
- probe: «коттеджные поселки тюмень купить» — 172
- context: дом/коттедж от застройщика в КП — demand spine под news-casus, не в H1

## Research — subject & conflict (research_start + SERP context)
- Subject: коттедж/дом в коттеджном посёлке от застройщика под Тюменью, ДДУ с обещанием газа к границе участка
- Reader problem: семья купила дом «с газом», в ДДУ написано «к границе участка» — при сдаче узнали, что магистраль в 180 м от забора; подключение стоит от 600 тыс. руб.
- Casus: собирательный редакционный тюменский сюжет (без имён, КП, застройщика)
- Surprising fact: «газ к забору» в ДДУ ≠ газ у забора на ключах; 180 метров = отдельный счёт на сотни тысяч
- Voice angle: застройщик называет это «техническим нюансом», семья отказывается подписывать акт приёмки
- Finale: акт не подписан; застройщик предлагает 620 тыс. руб. доплаты или рассрочку на коммуникации
- Distinct from B20 (юрлицо/эскроу), B23 (апартаменты), B12 (перенос сдачи), B21 (кладовка), B22 (ставка ипотеки)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20)
«В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты» (B23)

## Anti-dup published titles
B02–B15, B19–B23 published. Avoid: расписка, задаток, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН, пожилой, открытая кухня, перенос сдачи (B12), согласие супруги (B15), маткапитал (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки (B22), апартаменты (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (title_draft слишком длинный — сократить)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («при сдаче», «на ключах»)
- Subject clear: коттедж/дом, ДДУ, газ
- One variant only

## Required JSON output
```json
{
  "topic_id": "B25",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-po-kottedzhu-obeschali-gaz-k-zaboru-pri-sdache-doma-magistral-ok",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
