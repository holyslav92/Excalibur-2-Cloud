# Title inputs — B22 — 2026-09-04

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B22. verdict: PASS.

## topic_id
B22

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi`

## Scout handoff
- cluster_id: newbuild_mortgage_rate_changed_before_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild mortgage-rate casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке; банк одобрил ипотеку с фиксированной ставкой в расчёте платежа; застройщик забронировал лот до даты подписания ДДУ
  - risk: за 24–48 часов до подписания ДДУ банк уведомил об изменении процентной ставки или отмене льготной программы; ежемесячный платёж вырос примерно на 15–20 тыс. ₽; первоначальный взнос со схемой эскроу перестали сходиться
  - time: накануне подписания ДДУ, после месяцев одобрения и действия брони
  - finale: семья отказалась подписывать ДДУ на новых условиях; бронь сгорела; плата за бронирование не вернулась или вернулась частично; квартира ушла в продажу; повторное одобрение
- comment_magnet_angle: «Банк поднял ставку накануне ДДУ — вы бы всё равно подписали договор или развернулись бы, даже если бронь сгорит?»
- title_draft (rework allowed): В Тюмени накануне ДДУ банк поднял ставку ипотеки — платёж вырос, сделку остановили
- story_dup_check: PASS — distinct from Sep 3 plot (bank revoked approval 72h before DDU); B19 matkapital/escrow; B12 handover delay; B09 EGRN after approval
- distinct_plot: одобрение ипотеки на новостройку было, но **изменились ставка/платёж** непосредственно перед подписанием ДДУ (не отзыв одобрения, не эскроу/маткапитал, не перенос ключей)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «ипотека на новостройку процентная ставка» — 21 (55+11176; RU225: 960)
- support: «ипотека в тюмени на новостройки» — 41
- support: «ставка ипотеки новостройка» — 54
- child: «ипотека процентная ставка на сегодня новостройка» — 13
- child: «ипотека на новостройки 2026 процентная ставка» — 6

## Research — subject & conflict
- Subject: новостройка в Тюмени, предварительное одобрение ипотеки, банк меняет ставку/условия за 24–48 часов до ДДУ, рост платежа, срыв сделки и брони
- Reader problem: покупатель считает ипотеку окончательно одобренной и строит бюджет вокруг ставки и платежа; до кредитного договора банк может пересмотреть условия; бронь тикает отдельно
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм брони)
- Surprising fact: банк может уведомить о новой ставке за день-два до ДДУ, когда застройщик уже ждёт подпись; одобрение формально может ещё действовать, а плата за бронь — невозвратна по договору
- Voice angle: разрыв между «ипотеку уже одобрили» и преддоговорной реальностью — цифра в смс ещё не зафиксирована кредитным договором
- Finale: отказ от ДДУ на новых условиях → бронь сгорела → поиск другого лота и повторное одобрение
- Distinct from B09 (ЕГРН после одобрения), B19 (маткапитал блокирует эскроу), Sep 3 cluster (отзыв одобрения, не изменение ставки)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B21 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («накануне ДДУ», «за 48 часов»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B22",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-nakanune-ddu-bank-podnyal-stavku-ipoteki-platezh-vyros-sdelku-ostanovi",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
