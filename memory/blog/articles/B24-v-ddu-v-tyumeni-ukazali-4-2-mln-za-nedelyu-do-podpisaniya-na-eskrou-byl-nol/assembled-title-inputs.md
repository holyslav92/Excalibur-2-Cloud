# Title inputs — B24 — 2026-09-12

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier gpt-6-astra). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-ddu-v-tyumeni-ukazali-4-2-mln-za-nedelyu-do-podpisaniya-na-eskrou-byl-nol`

## Scout handoff
- cluster_id: ddu_amount_vs_escrow_zero
- top_energy_mirror: number_in_claim_vs_zero_paid
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, согласовала ипотеку, готовилась к подписанию ДДУ
  - risk: в тексте/проекте ДДУ указана сумма **4,2 млн ₽** к размещению на эскроу, но за **7 дней** до сделки на эскроu-счёте **0 ₽** — ранее переведённые деньги менеджер оформил как «бронь» или «взнос» застройщику, а не на защищённый счёт
  - time: за 7 дней до подписания ДДU и в день назначенной сделки
  - finale: банк не открыл сделку / заморозил ипотеку; застройщик предложил перевести сумму **повторно**; семья остановила подписание; бронь и планировка под угрозой; возможен возврат брони только за вычетом удержания
- comment_magnet_angle: «Если менеджер говорит: "Мы сами потом положим деньги на эскроu", вы всё равно идёте на подписание ДДU — или сначала требуете выписку по счёту?»
- title_draft (rework allowed): В ДДU в Тюмени указали 4,2 млн — за неделю до подписания на эскроu был ноль
- story_dup_check: PASS — cluster ddu_amount_vs_escrow_zero, fingerprint 4_2_mln_ddu_amount_vs_escrow_zero_before_signing
- distinct_plot: сумма в ДДU/проекте vs нулевой остаток на эскроu перед ипотечной сделкой; деньги на бронь/взнос застройщику; риск двойного платежа. **Не** B12 (перенос сдачи / заморозка после внесения), **не** B19 (маткапитал), **не** B20 (смена юрлица), **не** B22 (ставка ипотеки), **не** B02 (расписка/вторичка)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4583 (55+11176), RU225: 8447
- support: «эскроu счет» — 863
- support: «договор долевого участия» — 382
- on-plot: «счет эскроu дду» — 27

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДU с указанной суммой на эскроu, нулевой остаток на счёте перед подписанием
- Reader problem: покупатель перевёл крупную сумму по просьбе менеджера, видит её в проекте ДДU как часть цены, но перед ипотечной сделкой на эскроu — 0 ₽; непонятно, платить ли повторно
- Casus: modeled composite (без имён, ЖК, банка); 4,2 млн и 7 дней — редакционные якоря
- Surprising fact: упоминание суммы в ДДU не превращает ранний перевод застройщику в оплату цены ДДU — по 214-ФЗ обязанность исполнена только при поступлении на эскроu
- Voice angle: несовпадение суммы в ДДU, назначения первого платежа и реального остатка на эскроu
- Finale: банк останавливает сделку; застройщик просит перевести повторно; семья отказывается без выписки
- Distinct from B12 (сдача сдвинута, деньги уже на эскроu), B19 (маткапитал), B20 (смена юрлица), B22 (ставка перед ДДU)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»

## Anti-dup published titles
B02–B23 published. Avoid: расписка без денег (B02), перенос сдачи/эскроu заморозили (B12), ипотеку одобрили + эскроu (B19 маткапитал, B20 юрлицо), ставка перед ДДU (B22), квартира vs апартаменты (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за неделю», «перед подписанием»)
- One variant only
- Include slug confirmation

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-ddu-v-tyumeni-ukazali-4-2-mln-za-nedelyu-do-podpisaniya-na-eskrou-byl-nol",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
