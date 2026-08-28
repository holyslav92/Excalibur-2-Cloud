# Title inputs — B12 — 2026-08-28

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B12. verdict: PASS.

## topic_id
B12

## Scout handoff
- cluster_id: ddu_escrow_handover_delay_tyumen
- klyshin_hook: none (fresh Tyumen casus without Klyshin — preferred)
- dzen_casus_shape: PASS
  - event: семья в Тюмени подписала ДДУ в ЖК, внесла полную стоимость на эскроу и ждала ключи по графику застройщика
  - risk: застройщик в одностороннем порядке перенёс срок передачи квартиры на 12 месяцев; деньги на эскроу нельзя забрать без расторжения ДДУ или спора по 214-ФЗ; ипотека «висит»
  - time: уведомление за три недели до обещанной выдачи ключей, в квартале сдачи из рекламы ЖК
  - finale (editorial research variant): дольщик направил претензию и потребовал расторжения; банк вернул средства с эскроу; неустойка решалась отдельно с застройщиком
- comment_magnet_angle: «Если застройщик переносит сдачу на год — вы ждёте или сразу требуете возврат денег с эскроу?»
- title_draft (rework allowed): Ключи от новостройки в Тюмени перенесли на год — деньги на эскроу заморозили
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4717 (55+11176)
- secondary: «купить новостройку в тюмени» — 830
- secondary: «ипотека новостройка тюмень» — 214
- context: «эскроу счет новостройка» — 344 (RU225)
- context: «купить квартиру по дду» — 1845 (RU225)
- low: «неустойка за просрочку застройщика» — 14

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, эскроу, перенос передачи квартиры на год
- Reader problem: до ключей осталось три недели — пришло письмо о переносе на 12 месяцев; деньги на эскроу защищены, но не свободны; ипотека продолжается
- Casus: моделируемый/собирательный тюменский кейс (август 2026), без выдуманных имён/адресов/сумм
- Surprising fact: письмо о переносе само по себе не даёт автоматического одностороннего выхода с возвратом эскроу
- Fresh regional signal (NOT the family case): арендный дом Защитников Отечества 36 — перенос сроков, 27.08.2026
- Finale: претензия → расторжение → возврат с эскроу; неустойка отдельно
- Distinct from B09 (ЕГРН обременение ипотека), B11 (перепланировка/Росреестр)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B11 published. Avoid: расписка, задаток/торги, доверенность СВО, скидка/задаток, автооценка, наследство, ЗАГС/умершая жена, ЕГРН обременение ипотека (B09), пожилой по телефону, открытая кухня (B11).

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
  "topic_id": "B12",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
