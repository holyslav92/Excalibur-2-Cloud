# Title inputs — B19 — 2026-09-01

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B19. verdict: PASS.

## topic_id
B19

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli`

## Scout handoff
- cluster_id: newbuild_family_mortgage_matkapital_escrow_blocked_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке под семейную ипотеку; банк одобрил кредит и согласовал маткапитал в первоначальный взнос
  - risk: при открытии эскроу выяснилось незакрытое обязательство по прошлому маткапиталу — нет подтверждения выделения детских долей; банк приостановил открытие эскроу
  - time: за 48 часов до дедлайна брони, уже после одобрения семейной ипотеки
  - finale: бронь сняли, квартира вернулась в продажу, плата за бронь потеряна, 2–4 недели на новый объект и документы по маткапиталу
- comment_magnet_angle: «Маткапитал уже использовали на прошлую квартиру — вы всё равно бронируете новостройку в семейную ипотеку или сначала закрываете обязательства и справку в ПФР?»
- title_draft (rework allowed): Семейную ипотеку на новостройку в Тюмени одобрили — эскроу не открыли из‑за маткапитала
- story_dup_check: PASS
- distinct_plot: не перенос сдачи/заморозка эскроу после оплаты (B12), не приёмка/стяжка, не вторичка; стоп на этапе ДДУ/эскроу из‑за прошлого маткапитала

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени в ипотеку» — 93 (55+11176), RU225: 140
- support: «семейная ипотека новостройка» — 126
- support: «новостройки тюмени семейная ипотека» — 40 (RU225: 55)
- low: «маткапитал новостройка» — 3 (раскрывать как риск внутри семейной ипотеки, не в H1)

## Research — subject & conflict
- Subject: семейная ипотека на новостройку в Тюмени, маткапитал в первоначальный взнос, эскроу не открыли
- Reader problem: после фразы «ипотеку одобрили» семья считает сделку почти закрытой — но банк останавливает эскроу из‑за незакрытых детских долей по прошлому маткапиталу, пока истекает бронь
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, сумм)
- Surprising fact: банк при новой сделке проверяет историю прошлого маткапитала и ЕГРН по старой квартире — проблема всплывает уже после одобрения
- Voice angle: ложное ощущение финала после «одобрили»; отдельные ворота — ДДУ, эскроу, маткапитал
- Finale: бронь снята, плата за бронь потеряна, поиск другого объекта
- Distinct from B09 (ЕГРН обременение сорвало регистрацию после одобрения), B12 (перенос сдачи, деньги уже на эскроу), frozen secondary cluster matkapital_missing_child_shares (здесь — новостройка, семейная ипотека, стоп до эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»

## Anti-dup published titles
B02–B15 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, «ипотеку одобрили + ЕГРН/регистрация» (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 48 часов», «после одобрения»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B19",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-semejnuyu-ipoteku-na-novostrojku-odobrili-eskrou-ne-otkryli",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
