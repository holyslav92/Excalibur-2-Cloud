# Title inputs — B13 — 2026-08-30

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B13. verdict: PASS.

## topic_id
B13

## Scout handoff
- cluster_id: seller_mortgage_not_discharged_bank_lien_blocks_deal
- klyshin_hook: none (fresh Tyumen casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала вторичную квартиру с бывшей ипотекой продавца; продавец показал банковскую справку «кредит погашен» и обещал снять залог «в день сделки»
  - risk: ипотечное обременение всё ещё не снято в ЕГРН; банк не выдал согласие на сделку; справка о погашении ≠ снятие записи из реестра
  - time: за 24–48 часов до планируемого внесения аванса, финальная проверка свежей выписки ЕГРН и статуса в банке
  - finale: сделку остановили до аванса; покупатели отказались ждать и выбрали другой объект; продавцу — ориентир 2–4 недели до снятия обременения
- comment_magnet_angle: «Справку банка о закрытии кредита вы бы приняли за достаточную — или только свежую выписку ЕГРН без обременения?»
- title_draft (rework allowed): В Тюмени продавец показал справку о закрытии ипотеки — банк всё ещё держал залог
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить квартиру в тюмени вторичка» — 3225 (55+11176); live MCP also 4165
- secondary: «купить квартиру в тюмени» — 22699 (55+11176)
- secondary: «купить квартиру вторичка» — 5298 (55)
- context: «выписка из егрн на квартиру» — 190 (scout) / 92 (live MCP)
- context: «снятие обременения с квартиры» — 31 (55)
- low seller-side: «продажа квартиры при ипотеке» — 25; «как продать ипотечную квартиру» — 22

## Research — subject & conflict
- Subject: вторичка Тюмень, ипотека продавца, справка о погашении vs запись об ипотеке в ЕГРН
- Reader problem: справка о закрытии кредита выглядит как «квартира свободна», но выписка ЕГРН всё ещё показывает ипотеку
- Casus: собирательный/моделируемый тюменский кейс (август 2026), без имён/адресов/банка/сумм
- Surprising fact: 3 рабочих дня по ст. 25 102-ФЗ — от заявления в Росреестр, не от последнего платежа или справки; Домклик указывает до 30 дней на подготовку документов
- Voice angle: не «продавец обманул», а «два документа говорят о разных вещах»
- Finale: остановили до аванса, ушли на другой объект
- Distinct from B09: там ипотека покупателя и регистрация после одобрения; здесь ипотека продавца, кредит закрыт по справке, залог в ЕГРН до сделки

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B12 published. Avoid: расписка, задаток/торги, доверенность СВО, скидка, автооценка, наследство, ЗАГС/умершая жена (B08), ЕГРН обременение ипотека покупателя (B09), пожилой по телефону (B10), открытая кухня (B11), эскроу/новостройка перенос (B12).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps
- One variant only

## Required JSON output
```json
{
  "topic_id": "B13",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
