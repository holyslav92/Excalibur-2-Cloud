# Title inputs — B23 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B23. verdict: PASS.

## topic_id
B23

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela`

## Scout handoff
- cluster_id: newbuild_trade_in_failed_before_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild trade-in casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке по программе трейд-ин от застройщика; старую квартиру должны были выкупить и зачесть как первоначальный взнос, новую оформить по ДДУ с ипотекой
  - risk: за 24 часа до подписания ДДУ застройщик или партнёр по трейд-ин снижает оценку старой квартиры на 400–600 тыс. ₽ либо отказывает в выкупе (дефекты, ликвидность, сроки); денег на первоначальный взнос не хватает; банк не открывает сделку
  - time: за день до ДДУ, после 2–3 недель бронирования лота, оценки старой квартиры и подготовки ипотечных документов
  - finale: ДДУ не подписали; бронь на новостройку сгорела; деньги за бронирование не вернули; старая квартира непроданной; семья потеряла выбранный лот
- comment_magnet_angle: «Застройщик занизил оценку квартиры в трейд-ин накануне ДДУ — вы бы доплатили разницу из своих или отпустили бы бронь?»
- title_draft (rework allowed): В Тюмени трейд-ин от застройщика сорвался за день до ДДУ — бронь сгорела
- story_dup_check: PASS — distinct from B22 (bank rate before DDU), Sep 3 (approval revoked), B19 (matkapital/escrow), in_pool assignment, acceptance defects
- distinct_plot: срыв из-за **пересмотра/отказа выкупа старой квартиры в трейд-ин**, не банк и не цена новостройки по ДДУ

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «трейд ин новостройка» — 479 (regions 55+11176; RU225 compare)
- child: «новостройки трейд ин от застройщика» — 121 (RU 225)
- rejected probes: переуступка (9), субсидированная ипотека (47, B22 overlap), ипотека от застройщика (402, saturated)

## Research — subject & conflict
- Subject: новостройка в Тюмени, программа трейд-ин от застройщика/партнёра, старая квартира как первоначальный взнос, пересмотр выкупной цены или отказ за день до ДДУ, сгоревшая бронь
- Reader problem: покупатель считает старую квартиру уже «взносом»; оценку и выкуп ведёт отдельный партнёр; до ДДУ цена выкупа может измениться; платная бронь тикает отдельно
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм как факт реального дела)
- Surprising fact: «зафиксировали квартиру» и «зафиксировали первоначальный взнос» — не одно и то же; цена новостройки и оценка старой квартиры живут в разных документах и сроках
- Voice angle: разрыв между рекламой «старая квартира в счёт новой» и моментом, когда выкупная цена ещё может измениться, а бронь уже идёт
- Finale: ДДУ не подписали → бронь сгорела → старая квартира непродана → выбор: доплатить 400–600 тыс. из своих, отпустить лот или бороться за возврат брони
- Distinct from B22 (банк поднял ставку перед ДДУ — бронь сгорела); B09 (ЕГРН); B19 (эскроу/маткапитал); B12 (перенос сдачи)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой механизм срыва)
«Автооценка занизила цену — и квартира подорожала за сутки» (B06 — вторичка, не трейд-ин новостройка)

## Anti-dup published titles
B02–B22 published. B22 already used «бронь сгорела» with bank rate — B23 must center **трейд-ин / выкуп старой квартиры / занижение оценки**, not bank rate. Avoid: расписка, задаток/торги, доверенность, скидка, автооценка (B06), наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), банк+ставка (B22).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за день до ДДУ», «накануне ДДУ»)
- One variant only
- Subject must be clear: трейд-ин / новостройка / выкуп старой квартиры

## Required JSON output
```json
{
  "topic_id": "B23",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-trejd-in-ot-zastrojschika-sorvalsya-za-den-do-ddu-bron-sgorela",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
