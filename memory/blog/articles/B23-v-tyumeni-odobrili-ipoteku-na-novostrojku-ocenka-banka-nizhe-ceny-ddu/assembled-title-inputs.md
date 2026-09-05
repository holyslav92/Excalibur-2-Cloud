# Title inputs — B23 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE Klyshin-style screaming news-casus H1 for topic B23. Must include: casus arc + **digit in second beat** (350–450 тыс. → use «400 тысяч» as editorial round) + punch finale. verdict: PASS.

## topic_id
B23

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-odobrili-ipoteku-na-novostrojku-ocenka-banka-nizhe-ceny-ddu`

## Scout handoff
- cluster_id: newbuild_bank_appraisal_below_ddu_price_tyumen
- klyshin_hook: none (fresh Tyumen newbuild bank-appraisal casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке; банк одобрил ипотеку от цены бронирования; бронь оплатили
  - risk: отчёт банковского оценщика ниже цены в ДДU на **350–450 тыс. ₽** — кредит пересчитали **от оценки**, не хватило собственных средств
  - time: за **5–7 дней** до подписания ДДУ после оплаченной брони
  - finale: ДДУ не подписали; бронь сгорела; оплата оценки не вернулась; лот ушёл в продажу
- comment_magnet_angle: «Одобрение есть, а оценка ниже ДДУ — вы бы за неделю нашли недостающие деньги или развернулись, даже если бронь сгорит?»
- title_draft (rework allowed): В Тюмени одобрили ипотеку на новостройку — банковская оценка оказалась ниже цены в ДДУ
- story_dup_check: PASS — distinct from B22 (rate change before DDU), B19 (escrow/matkapital), B06 (secondary auto-appraisal), B09 (EGRN encumbrance)
- distinct_plot: одобрение ипотеки на новостройку было, но **банковская оценка ниже цены ДДУ** → не хватает ПВ/собственных денег (не изменение ставки, не эскроу, не вторичка)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «оценка квартиры для ипотеки» — 24 (55+11176; RU225: 1578)
- support: «ипотека в тюмени на новостройки» — 41
- support: «оценка квартиры банком для ипотеки» — 10
- child: «сколько стоит оценка квартиры для ипотеки» — 5
- child: «нужна ли оценка квартиры для ипотеки» — 5

## Research — subject & conflict
- Subject: новостройка в Тюмени, предварительное одобрение ипотеки, оплаченная бронь, банковская оценка ниже цены ДДУ на 350–450 тыс. ₽, пересчёт кредита от оценки, срыв сделки
- Reader problem: покупатель считает одобрение и цену в брони гарантией суммы кредита; перед ДДУ банк оценивает объект отдельно; разрыв ложится на покупателя
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка как установленный факт)
- Voice angle: «одобрение в приложении» и цена в брони ≠ финальная сумма кредита по объекту
- Finale: ДДУ не подписали → бронь сгорела → оценка не вернулась → лот снова в продаже
- Distinct from B22 (ставка/платёж перед ДДУ), B09 (ЕГРН после одобрения), B19 (эскроу/маткапитал), B06 (автооценка вторички)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: ставка, не оценка)
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09 — другой plot)

## Anti-dup published titles
B02–B22 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка вторички (B06), наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал+эскроу (B19), смена юрлица (B20), кладовка (B21), **ставка перед ДДУ (B22)**.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, «как устроена», «что такое», спокойные гайды

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за неделю до ДДУ», «перед ДДУ»)
- **Digit in second beat:** 350–450 тыс. → editorial «400 тысяч» OK
- **Second beat punch:** бронь сгорела / сделку сорвали / не хватило денег
- One variant only
- Ban calm explanatory heads

## Required JSON output
```json
{
  "topic_id": "B23",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-odobrili-ipoteku-na-novostrojku-ocenka-banka-nizhe-ceny-ddu",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
