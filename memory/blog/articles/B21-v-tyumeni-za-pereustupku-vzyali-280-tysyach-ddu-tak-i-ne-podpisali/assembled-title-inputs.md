# Title inputs — B21 — 2026-09-01

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B21. verdict: PASS.

## topic_id
B21

## slug
`v-tyumeni-za-pereustupku-vzyali-280-tysyach-ddu-tak-i-ne-podpisali`

## Scout handoff
- cluster_id: newbuild_assignment_deposit_scam_tyumen
- klyshin_hook: energy only — casus+number+punch (280 тысяч, ДДУ не подписали)
- dzen_casus_shape: PASS
  - event: пара нашла переуступку дешевле застройщика на ~400 тыс.; уступающий взял 280 тыс. «на подготовку цессии» до Росреестра
  - risk: перевод по СБП, обещание 14 дней; через 21 день уступающий пропал; застройщик — квартира на первом дольщике
  - time: август 2026
  - finale: ДДУ/цессия не зарегистрированы; 280 тыс. под угрозой; ипотека и эскроу не открывались
- comment_magnet_angle: «Переуступка: перевели бы 280 тысяч до регистрации цессии, если скидка к застройщику — 400?»
- title_draft: В Тюмени за переуступку взяли 280 тысяч — ДДУ так и не подписали
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 1882 (55+11176)
- support: «новостройки в тюмени от застройщика» — 1268
- niche: «переуступка новостройки» — 10

## Research — subject & conflict
- Subject: переуступка (цессия) прав по ДДУ в новостройке Тюмени; аванс частному уступающему до регистрации
- Casus: 280 000 ₽ по СБП 12.08.2026; 21 день — контакт потерян; цессия не в Росреестре
- Surprising fact: право не переходит от расписки/SBP — только от госрегистрации цессии (214-ФЗ ст. 11)
- Distinct from 9465 (бронь у застройщика +380k), B20 (юрлицо), 9452 (ипотека+эскроу), 9439 (стяжка), 9411 (траншевая)

## Champion energy (Klyshin rhythm: casus + number + punch)
«В Тюмени за переуступку взяли 280 тысяч — ДДУ так и не подписали»
«Ипотеку одобрили, а регистрацию отменили через полгода» (formula only)

## Anti-dup
Avoid angles from B19, B20, 9465, 9452, 9439, 9411, B12.

## FORBIDDEN H1
чеклист, N шагов, полный гайд, 2026, как купить без риелтора

## Constraints
- ~50–70 chars, news headline, strong verb, Tyumen, temporal marker if helps
- One variant

## JSON schema (output exactly this structure)
```json
{
  "topic_id": "B21",
  "verdict": "PASS",
  "h1": "...",
  "slug": "v-tyumeni-za-pereustupku-vzyali-280-tysyach-ddu-tak-i-ne-podpisali",
  "comment_magnet_angle": "...",
  "wordstat_p0_phrase": "купить новостройку в тюмени",
  "wordstat_p0_volume": 1882,
  "angle_ru": "...",
  "forbidden_overlap": ["9465","9452","9439","9411","B20","B19"]
}
```
