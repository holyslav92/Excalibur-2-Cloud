# Title inputs — B27 — 2026-09-19

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-rebenku-ispolnilos-7-let-za-5-dnej-do-ddu-semejnuyu-ipoteku-snyali`

## Scout handoff
- cluster_id: family_mortgage_child_age_limit_before_ddu
- klyshin_hook: none (fresh Tyumen newbuild family-mortgage casus without Klyshin)
- top_energy_mirror: clock_ran_out
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала лот в ЖК, получила одобрение семейной ипотеки, назначила подписание ДДУ
  - risk: условие программы — ребёнок младше 7 лет на дату кредитного договора; льгота сгорает
  - time: «за 5 дней до ДДУ», в день рождения ребёнка (исполнилось 7 лет)
  - finale: банк снял семейную ипотеку / пересчитал на рыночную ставку, платёж стал неподъёмным, до эскроу семья не дошла
- comment_magnet_angle: «Ребёнку исполнилось 7 лет в пятницу, ДДУ в среду — кто должен был предупредить семью: банк, застройщик или риелтор?»
- title_draft (rework allowed): В Тюмени ребёнку исполнилось 7 лет за 5 дней до ДДУ — семейную ипотеку сняли
- newbuild_mechanism: семейная ипотека на квартиру в ЖК по ДДУ; бронь, проект ДДУ, эскроу; не вторичка
- story_dup_check: PASS — distinct from B22 (ставка поднята накануне ДДУ), B19 (маткапитал блокирует эскроу), B09 (ЕГРН после одобрения)
- distinct_plot: одобрение семейной ипотеки было, но **ребёнку исполнилось 7 лет до кредитного договора/ДДУ** — банк снял льготное основание (не отзыв одобрения по ЕГРН, не маткапитал, не общее повышение ставки)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «семейная ипотека в тюмени» — 1060 handoff / 734 live (55+11176)
- support: «семейная ипотека тюмень условия» — 459
- support: «семейная ипотека тюмень 2026» — 375
- child: «семейная ипотека ребенку 7 лет» — 26
- child: «ребенок 7 лет можно семейную ипотеку» — 8
- low: «новостройки тюмени семейная ипотека» — 24 (раскрывать через риск календаря, не каталог ЖК)

## Research — subject & conflict
- Subject: семейная ипотека на новостройку в Тюмени, один ребёнок, возрастной порог 7 лет на дату кредитного договора
- Reader problem: семья считает предварительное одобрение фиксацией льготной ставки; откладывает ДДУ; ребёнку исполняется 7 лет за 5 дней до назначенного подписания — банк снимает семейную ставку, платёж не сходится
- Casus: собирательный редакционный кейс (без имён, ЖК, банка, точных сумм платежа)
- Surprising fact: возраст ребёнка определяется на дату **кредитного договора**, не на дату одобрения или брони; бронь и назначенный ДДУ не «фиксируют» право на программу
- Voice angle: разрыв между календарём семьи (день рождения ребёнка) и юридической датой сделки; «ипотека уже одобрена» vs финальная проверка банка
- Finale: семья не подписывает ДДУ, не открывает эскроу; судьба платы за бронь неизвестна
- Distinct from B22 (банк поднял ставку перед ДДУ — другой механизм), B19 (эскроу+маткапитал), B09 (ЕГРН обременение)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09 — другой plot)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)

## Anti-dup published titles
B02–B26 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), перенос сдачи (B12), маткапитал+эскроу (B19), смена юрлица (B20), ставка перед ДДУ (B22), чистовая/приёмка (B25), РВЭ/транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, Klyshin casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 5 дней до ДДУ», «исполнилось 7 лет»)
- One variant only
- Include slug confirmation in angle or separate field if needed
- Subject must be clear: семейная ипотека / новостройка / ребёнок 7 лет

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-rebenku-ispolnilos-7-let-za-5-dnej-do-ddu-semejnuyu-ipoteku-snyali",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
