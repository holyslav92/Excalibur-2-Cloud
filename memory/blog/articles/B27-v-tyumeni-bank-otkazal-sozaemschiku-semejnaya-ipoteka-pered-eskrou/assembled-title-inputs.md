# Title inputs — B27 — 2026-09-16

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier, gpt-6-astra). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou`

## Scout handoff
- cluster_id: newbuild_coborrower_rejected_family_mortgage
- klyshin_hook: none (fresh Tyumen newbuild casus without Klyshin)
- dzen_casus_shape: PASS
  - event: тюменская семья выбрала двушку в новостройке; семейную ипотеку предварительно одобрили на двоих; застройщик держал бронь до открытия эскроу
  - risk: без подтверждённого созаёмщика банк не выдаёт нужный лимит; отказ не «задержка» — не хватает суммы на выбранную квартиру; цепочка ДДУ и эскроу останавливается
  - time: за 4 дня до открытия эскроу; до окончания брони — 6 дней
  - finale: семья не подписала ДДУ без финансирования; бронь сняли без штрафа; замена созаёмщика родителем не прошла скоринг; через 11 дней квартира ушла другому покупателю
- comment_magnet_angle: «Семейную ипотеку одобрили на двоих, а за четыре дня до эскроу банк “зарубил” созаёмщика: вы бы пытались срочно подобрать другого человека или сразу снимали бы бронь, чтобы не рисковать?»
- title_draft (rework allowed): В Тюмени банк отказал созаёмщику по семейной ипотеке — за 4 дня до эскроу сделку остановили
- story_dup_check: PASS — distinct from B19 matkapital/escrow, B22 rate change before DDU, B12 handover delay, B09 EGRN after approval
- distinct_plot: предварительное одобрение семейной ипотеки на двоих, но **финальный отказ одному созаёмщику** за несколько дней до эскроу (не маткапитал, не изменение ставки, не отзыв одобрения основного заёмщика)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «семейная ипотека тюмень» — 1240 (55+11176; RU225: 1745)
- support: «созаемщик ипотека» — 515
- support: «купить новостройку в тюмени» — 902
- support: «ипотека жена созаемщик» — 52
- tail: «семейная ипотека есть ли созаемщики» — 15

## Research — subject & conflict
- Subject: новостройка в Тюмени, семейная ипотека, муж — основной заёмщик, жена — созаёмщик; банк отклоняет созаёмщика за 4 дня до эскроу; без второго дохода лимита не хватает
- Reader problem: семья считает предварительное одобрение «на двоих» почти завершённой покупкой; финальная проверка каждого созаёмщика — отдельный этап; бронь истекает, деньги на эскроу ещё не ушли
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм)
- Surprising fact: с 01.02.2026 супруги обязаны быть созаёмщиками по семейной ипотеке — нельзя оформить льготный кредит на одного, чтобы не учитывать КИ второго
- Voice angle: «одобрили на двоих» ≠ гарантия сделки; отказ созаёмщику останавливает всю заявку, если без его дохода не сходится лимит
- Finale: квартира ушла другому покупателю; семья остановила сделку до перевода денег; штрафа за неподписанный ДДУ не было
- Distinct from B19 (маткапитал блокирует эскроу), B22 (банк поднял ставку перед ДДУ), B09 (ипотека+ЕГРН)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)

## Anti-dup published titles (do NOT repeat angle)
B02–B26 published. Close neighbors to avoid:
- B19: «В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (маткапитал, не созаёмщик) — **FORBIDDEN echo:** «эскроу сорвал(ся)» в H1
- B22: «В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (ставка, не созаёмщик) — **FORBIDDEN echo:** «бронь сгорела»
- **HARD REQUIRED in H1:** «банк отказал созаёмщику» + «семейной ипотеке» + «за 4 дня до эскроу»; ≤70 chars
- **FORBIDDEN awkward phrasing:** «созаёмщик не прошёл семейную ипотеку»; «эскроу сорвался» (B19 echo)
- **Target energy (adapt, do not copy verbatim):** «В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу»
- B12: перенос сдачи / эскроу заморозили
- B09: ипотека + ЕГРН

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 4 дня до эскроу», «перед эскроу»)
- Subject must be clear: семейная ипотека / созаёмщик / новостройка
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-bank-otkazal-sozaemschiku-semejnaya-ipoteka-pered-eskrou",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
