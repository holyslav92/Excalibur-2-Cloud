# Title inputs — B17 — 2026-08-30

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B17. verdict: PASS.

## topic_id
B17

## Scout handoff
- cluster_id: registered_persons_block_sale_before_advance
- klyshin_hook: none (fresh Tyumen casus without Klyshin)
- dzen_casus_shape: PASS
  - event: «В Тюмени покупатели остановили сделку за три дня до аванса, когда выяснили, что в квартире зарегистрированы бывшая жена продавца и взрослый сын»
  - risk: «зарегистрированные лица могут не выписаться добровольно, а вопрос их выселения способен затянуться»
  - time: «за 3 дня до планируемого аванса»
  - finale: «от сделки отказались до внесения денег, покупатели ничего не потеряли»
- comment_magnet_angle: «Продавец клянётся, что прописанные уйдут сами за неделю — вы бы поверили и внесли аванс?»
- title_draft (rework allowed): В Тюмени перед авансом нашли прописанных — продавец обещал выписать за неделю
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «прописка при покупке квартиры» — 10 (55+11176), RU 477
- rework trail: «выписка из квартиры прописанные» 6 → «прописанные в квартире риски» 4 → «снять с регистрации квартира тюмень» 13
- related: «прописка при продаже покупке квартиры» 54; «нужна ли прописка при покупке квартиры» 52
- regional: «снять квартиру с регистрацией в тюмени» 13

## Research — subject & conflict
- Subject: вторичка Тюмень, зарегистрированные бывшая жена продавца и взрослый сын, обещание «выпишутся за неделю»
- Reader problem: устное обещание продавца принимают за решённый вопрос; аванс передают без проверки, кто зарегистрирован
- Casus: моделируемый/собирательный тюменский кейс (август 2026), без выдуманных имён/адресов
- Surprising fact: переход права собственности не снимает прописанных автоматически; ЕГРН «чистая» не заменяет справку о зарегистрированных
- Finale: сделка остановлена ДО аванса — деньги не потеряны (agency landing, not panic)
- Distinct from B08 (ЗАГС/умершая жена/банк), B07 (наследство), B09 (ЕГРН обременение), B10 (пожилой по телефону), B11 (перепланировка)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B14 published. Avoid: расписка, задаток/торги, доверенность СВО, скидка, автооценка, наследство, ЗАГС/умершая жена, ЕГРН обременение, пожилой по телефону, открытая кухня, новостройка/эскроу, закрытие ипотеки/залог.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~70 chars (~50–70 ideal)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 3 дня», «перед авансом»)
- Subject must be clear: прописанные / регистрация / аванс / вторичка
- One variant only
- Keep cluster registered_persons_block_sale_before_advance

## Required JSON output
```json
{
  "topic_id": "B17",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
