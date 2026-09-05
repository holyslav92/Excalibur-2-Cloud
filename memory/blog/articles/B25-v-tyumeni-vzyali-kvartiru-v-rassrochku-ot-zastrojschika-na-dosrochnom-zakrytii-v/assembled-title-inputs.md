# Title inputs — B25 — 2026-09-05

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE Klyshin-style screaming clickbait H1/title for topic B25. verdict: PASS.

## topic_id
B25

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-vzyali-kvartiru-v-rassrochku-ot-zastrojschika-na-dosrochnom-zakrytii-v`

## Scout handoff
- cluster_id: newbuild_developer_installment_early_payoff_penalty_tyumen
- klyshin_hook: none (fresh Tyumen newbuild installment casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке и оформила беспроцентную рассрочку от застройщика вместо ипотеки — менеджер обещал «можно закрыть досрочно без штрафов»
  - risk: при попытке досрочного погашения (или перехода на ипотеку перед ДДУ) в договоре всплывает пункт о комиссии за досрочное закрытие / пересчёте цены без скидки / штрафе 8–15% от остатка — скидка «сгорает», итоговая цена выше
  - time: через 3–6 месяцев после брони, за 2–4 недели до подписания ДДУ, когда семья собрала сумму на закрытие
  - finale: семья отказалась подписывать ДДУ на пересчитанных условиях; бронь сгорела, внесённые платежи частично удержаны; квартира ушла в продажу по новой цене
- comment_magnet_angle: «Рассрочка без процентов — вы бы поверили менеджеру на слово или сразу искали бы пункт про досрочное закрытие в договоре?»
- title_draft (rework allowed): В Тюмени взяли квартиру в рассрочку от застройщика — на досрочном закрытии всплыла комиссия
- story_dup_check: PASS — distinct from B22 rate-change before DDU; B23 bank appraisal; B24 assignment price hike; trade-in / rental-ban / escrow / acceptance clusters
- distinct_plot: рассрочка от застройщика на новостройку (без ипотеки), досрочное закрытие или переход на ипотеку → скрытая комиссия/пересчёт цены без скидки → бронь сгорела

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «рассрочка от застройщика тюмень» — 143 (55+11176; RU225: 21301)
- support: «купить квартиру в рассрочку от застройщика» — 33
- support: «квартира в рассрочку от застройщика тюмень» — 82
- parent: «рассрочка от застройщика» — 226 (55+11176)

## Research — subject & conflict
- Subject: новостройка в Тюмени, беспроцентная рассрочка от застройщика вместо ипотеки, устное обещание «закрыть без штрафов», досрочное погашение или переход на ипотеку перед ДДУ
- Reader problem: покупатель верит менеджеру; при досрочном расчёте всплывает комиссия, скидка отменяется, цена пересчитывается; часть платежей удерживается до ДДУ
- Casus: редакционная модель семьи в Тюмени (без имён ЖК/застройщика); 8–15% — модельный параметр, не статистика
- Surprising fact: будущий законопроект Минстроя о праве досрочного погашения — не действует до 01.09.2027; сейчас условия только в договоре
- Voice angle: «верить обещанию менеджера или читать пункт о досрочном закрытии»; беспроцентная рассрочка ≠ бесплатный выход
- Finale: отказ от ДДУ на пересчитанных условиях → бронь сгорела → платежи частично удержаны
- Local: ~900 расторжений рассрочки в Тюмени в 2025; доля рассрочки упала с 31,7% до 13,5%
- Distinct from B22 (ставка ипотеки перед ДДУ), B19 (маткапитал/эскроу), B20 (смена юрлица)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B22 published. Avoid: расписка, задаток/торги, доверенность, скидка-задаток, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, как устроена, 2026

## Constraints
- Klyshin-style: casus + figure + punch in second beat
- Max ~50–70 chars
- News headline energy, Tyumen, newbuild installment early payoff commission trap
- Strong verb, active voice, temporal marker when it helps
- Truth from research facts only — no invented stats as market data
- One variant only

## Required JSON output
```json
{
  "topic_id": "B25",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-vzyali-kvartiru-v-rassrochku-ot-zastrojschika-na-dosrochnom-zakrytii-v",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
