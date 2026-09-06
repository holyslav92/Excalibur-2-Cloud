# Title inputs — B24 — 2026-09-06

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-na-eskrou-ne-hvatalo-400-tysyach-do-summy-ddu-bank-ostanovil-podpisani`

## Scout handoff
- cluster_id: `newbuild_escrow_shortfall_vs_ddu_amount_tyumen`
- klyshin_hook: none (fresh Tyumen newbuild escrow casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени покупает новостройку; ипотека одобрена, счёт эскроу открыт; внесены первый транш и маткапитал
  - risk: за 24–48 часов до подписания/регистрации ДДУ банк сверяет документы и деньги; цена в ДДУ 6,2 млн ₽, на эскроу 5,8 млн ₽ — дефицит 400 тыс. ₽
  - time: накануне подписания ДДУ, после одобрения ипотеки и открытия эскроу
  - contradiction: менеджер предлагал «подписывайте сейчас, сумму потом доберём»; банк fail-closed
  - finale: банк не пропустил сделку до сведения сумм и графика; семья остановила подписание, добрала 400 тыс., через неделю подписала ДДУ без потери квартиры
- comment_magnet_angle: «На эскроу не хватает 400 тысяч до суммы в ДДУ, а менеджер говорит: “Подписывайте, потом доберём”. Вы бы поставили подпись или ждали полного совпадения сумм?»
- title_draft (rework allowed): В Тюмени на эскроу не хватало 400 тысяч до суммы ДДУ — банк остановил подписание
- story_dup_check: PASS — distinct from B19 (эскроу не открыли / маткапитал), B20 (смена юрлица), B12 (перенос сдачи), B22 (ставка перед ДДУ)
- distinct_plot: счёт эскроу **открыт**, но фактическая сумма на счёте **меньше цены ДДУ** на 400 тыс. ₽ — банк остановил подписание (не «эскроу не открыли», не ставка, не юрлицо)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4663 (regions 55+11176)
- support: «семейная ипотека новостройка тюмень» / «новостройки тюмени семейная ипотека» — 28
- narrow: «эскроу счет новостройка» — 2; «эскроу счета новостройки» — 2
- Scout rework: прямой спрос «эскроу» узкий; spine = новостройки Тюмень; механизм эскроу/ДДУ/400 тыс. — в casus H1, не SEO-хвост

## Research — subject & conflict
- Subject: новостройка в Тюмени, ипотека, открытый эскроу, расхождение между ценой ДДУ и суммой на счёте (400 тыс. ₽), банк останавливает подписание
- Reader problem: покупатель считает, что одобренная ипотека и открытый эскроу достаточны; банк сверяет цену ДДУ, график, кредит и фактический остаток на эскроу
- Casus: редакционный тюменский сюжет (без имён, ЖК, банка)
- Surprising fact: открытие эскроу ≠ исполнение обязанности по оплате цены ДДУ; юридически значимо поступление полной суммы
- Voice angle: разрыв между «менеджер — подпишем, доберём потом» и банковской fail-closed проверкой накануне ДДУ
- Finale: остановка подписания → добор 400 тыс. → подписание ДДУ через неделю без потери квартиры
- Distinct from B19 (эскроу не открыли), B20 (юрлицо), B12 (сдача), B22 (ставка)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)

## H1 MUST include (user requirement)
- escrow 400k shortfall vs DDU sum
- bank stopped signing
- Tyumen / newbuild context
- news-casus rhythm, not checklist

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал+эскроу не открыли (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), квартира/апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (prefer shorter if clear)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («накануне ДДУ», «за 48 часов»)
- One variant only
- h1 and title must match

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-na-eskrou-ne-hvatalo-400-tysyach-do-summy-ddu-bank-ostanovil-podpisani",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
