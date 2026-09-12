# Title inputs — B24 — 2026-09-12

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## Scout handoff
- cluster_id: bank_appraisal_below_ddu_price
- klyshin_hook: none (fresh Tyumen bank-appraisal-below-DDU casus without Klyshin — preferred)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, оформила бронь, подписала ДДУ и получила предварительное одобрение ипотеки под сумму договора
  - risk: банк заказал оценку объекта в строящемся доме; в отчёте стоимость на **680 000 ₽ ниже цены ДДУ**; банк пересчитал лимит кредита
  - time: за **5 дней** до открытия эскроу-счёта и первого платежа по графику
  - finale (editorial): денег на эскроу в срок не хватило; застройщик поставил вопрос о сохранении брони и условий; семья остановила сделку либо вынужденно искала доплату
- comment_magnet_angle: «Цена в ДДУ уже подписана, а банк после оценки режет сумму: вы бы внесли недостающие 680 тысяч из накоплений или расторгли сделку с застройщиком, даже если квартира уже "ваша" по брони?»
- title_draft (rework allowed): В Тюмени банк оценил новостройку на 680 тысяч ниже ДДУ — ипотеку урезали
- top_energy_mirror: number_in_claim_vs_zero_paid — в договоре уже стоит цена, покупатели считают квартиру почти своей, но цифра в ДДУ ≠ сумме, которую банк реально профинансирует
- newbuild_mechanism: банковская оценка квартиры в строящемся доме перед выдачей ипотеки по ДДУ; если оценочная стоимость ниже договорной, банк сокращает кредитный лимит; покупателю нужно закрыть разницу до наполнения эскроу
- anti_dupe_hard: PASS | distinct from B19 (escrow/matkapital), B22 (rate change before DDU), B06 (secondary auto-appraisal)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 3593 (55) / 4560 (55+11176) / 8430 (RU225)
- secondary: «купить новостройку в тюмени» — 688 (55)
- secondary: «ипотека новостройка» — 398 (55)
- low: «оценка квартиры для ипотеки» — 20 (55) — explain as risk inside deal, not as headline jargon

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, банковская оценка ниже цены договора, урезание ипотечного лимита перед эскроу
- Reader problem: ДДУ подписан, одобрение есть — за 5 дней до эскроу банк режет кредит на 680 тыс.; не хватает собственных денег
- Casus: моделируемый/собирательный тюменский кейс (сентябрь 2026), без выдуманных имён/адресов/банков
- Surprising fact: подписанный ДДУ фиксирует цену с застройщиком, но не заставляет банк профинансировать её целиком
- Distinct from B22 (ставка перед ДДУ), B19 (эскроу/маткапитал), B06 (автооценка вторички), B12 (перенос сдачи)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B23 published. Avoid: расписка, задаток/торги, доверенность СВО, скидка/задаток, автооценка вторички (B06), наследство, ЗАГС/умершая жена, ЕГРН обременение (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), эскроу/маткапитал (B19), ставка перед ДДУ (B22), юрлицо/эскроу (B20), кладовка (B21), апартаменты (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~70 chars (~50–70 ideal)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps (e.g. «за 5 дней до эскроу»)
- One variant only
- Slug already fixed: v-tyumeni-bank-ocenil-novostrojku-na-680-tysyach-nizhe-ddu-ipoteku-urezali

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
