# Title inputs — B12 — 2026-08-28

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B12. verdict: PASS.

## topic_id
B12

## Scout handoff
- cluster_id: double_sale_two_buyers_rieltor_poa
- klyshin_hook: none (fresh Tyumen-region casus без Klyshin)
- dzen_casus_shape: PASS
  - event: жительница Ялуторовска купила квартиру через риелтора по доверенности, перевела деньги и жила в квартире
  - risk: риелтор по доверенности заключила сделки с двумя покупателями, продавец получил деньги от обоих
  - time: спустя год после первой сделки появился второй законный владелец
  - finale: продавец выбрал покупателя с большей суммой; первую покупательницу пытаются выселить; доследственная проверка, внешний юрист Роман Матвеев
- comment_magnet_angle: «Кто прав в такой истории: тот, кто первым внёс деньги и въехал в квартиру, или тот, кто заплатил продавцу больше?»
- title_draft (rework allowed): В Ялуторовске квартиру продали двум покупателям — первую пытаются выселить

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «проверка егрн» — 28 (55+11176)
- buyer spine: «аккредитив при покупке квартиры» — 45 (55+11176)
- compare: «двойные продажи квартир» — 281 (RU225)

## Research — subject & conflict
- Subject: квартира в Ялуторовске (Тюменская область), двойная продажа через риелтора по доверенности
- Reader problem: договор, документы и въезд не защищают от второго покупателя с большей суммой
- Casus facts (URA.RU 22.06.2026, lawyer Roman Matveev): риелтор продала одну квартиру двум покупателям; первая жила в квартире; через год — второй владелец; попытка выселения; продавец выбрал более выгодного покупателя
- Surprising angle: выписка ЕГРН могла выглядеть нормально, но не исключает спор о втором договоре
- Finale: выселение первой покупательницы (попытка), не установленный итог суда
- Distinct from B04 (доверенность/СВО), B02 (расписка/деньги), B09 (ЕГРН обременение ипотека)

## Anti-dup published titles
B02–B11 published. Avoid: расписка без денег, задаток на торгах, доверенность СВО, скидка 2 млн, автооценка, наследство сын, умершая жена, ипотека ЕГРН, пожилой по телефону, открытая кухня перепланировка.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора

## Constraints
- H1 max 70 chars, news headline, casus arc, strong verb, active voice
- Tyumen region energy (Ялуторовск / Тюменская область)
- No SEO tails, no label heads, no «2026», no colon+keyword
- Champion energy (not copy): «Сделку оспорили через год: покупатель проверил всё — и потерял»

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
