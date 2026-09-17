# Title inputs — B27 — 2026-09-17

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier, gpt-6-astra). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-bank-ocenil-novostrojku-na-900-tysyach-nizhe-ddu-ipoteku-porezali-za-s`

## Scout handoff
- cluster_id: bank_appraisal_below_ddu_price
- klyshin_hook: none (fresh Tyumen newbuild bank-appraisal casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени забронировала квартиру в новостройке, получила ипотечное одобрение «под ключ» и пришла на подписание ДДУ
  - risk: банк в последний день снизил сумму кредита из-за оценки залога ниже цены ДДУ на 900 тыс. ₽; разница легла на покупателя
  - time: отчёт оценщика пришёл за сутки до подписания ДДУ и открытия эскроу; до этого менеджер называл оценку формальностью
  - finale: ДДУ не подписан, эскроу не открыт; через 48 часов бронь сняли; застройщик повысил цену на 200 тыс. ₽; семья не внесла разницу собственными деньгами
- comment_magnet_angle: «Оценку банка можно попытаться пересмотреть или обратиться в другой банк — но вы бы внесли 900 тысяч из своих, если менеджер до последнего дня называл оценку формальностью? Или отказались бы от квартиры и брони?»
- title_draft (rework allowed): В Тюмени банк оценил новостройку на 900 тысяч ниже ДДУ — ипотеку порезали за сутки до подписания
- top_energy_mirror: paper_clean_then_broke — бронь, одобрение, цена ДДУ, выход на подписание; отчёт об оценке в последний день сократил кредитный лимит
- story_dup_check: PASS — distinct from B06 (вторичка, автооценка), B22 (ставка перед ДДУ), B19 (маткапитал/эскроу), B26 (РВЭ + второй транш)
- distinct_plot: банковская оценка будущего залога по новостройке ниже цены ДДУ → сокращение ипотечного лимита до открытия эскроу (не ставка, не вторичка, не РВЭ)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «ипотека от застройщика тюмень» — 519 (55+11176)
- parent: «ипотека от застройщика» — 732
- context: «новостройки тюмень» — 4475 (too broad for H1)
- child: «ипотека тюмень новостройки от застройщика» — 96
- weak technical: «оценка квартиры банк ипотека» — 14; «банк ипотека квартира оценка» — 14

## Research — subject & conflict
- Subject: новостройка в Тюмени по ДДУ, предварительное одобрение ипотеки, банковская оценка залога ниже цены договора на 900 тыс. ₽, сокращение кредитного лимита за сутки до подписания
- Reader problem: «одобрено» не значит «вся цена ДДУ профинансирована»; бронь ≠ зарегистрированный ДДУ с эскроу
- Casus: редакционный сценарий (без имён, ЖК, банка, оценочной компании); 900 тыс. и 200 тыс. — не «среднерыночные» цифры
- Surprising fact: разрыв цены ДДУ и принятой банком оценки может возникнуть до готовой квартиры — оценщик работает без осмотра по проектной документации
- Voice angle: не «обман банка/застройщика», а момент когда покупатель понимает, что одобрение ≠ финальная сумма кредита
- Finale: отказ от ДДУ → бронь снята через 48 ч → цена +200 тыс. ₽
- Distinct from B22 (ставка/платёж перед ДДУ), B06 (автооценка вторички), B19 (эскроу/маткапитал), B26 (РВЭ/транш)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой механизм)
«Автооценка занизила цену — и квартира подорожала за сутки» (B06 — вторичка, не банк)

## Anti-dup published titles
B02–B26 published. Avoid: расписка, задаток/торги, доверенность, скидка, автооценка (B06), наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал+эскроу (B19), смена юрлица (B20), ставка перед ДДУ (B22), чистовая в ДДУ (B25), РВЭ без разрешения (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (prefer shorter Klyshin punch like B22/B26)
- **MUST start with «В Тюмени»** — локальный buyer-intent (как B22, B26)
- **MUST name concrete stakes:** 900 тысяч (или «на 900 тысяч ниже ДДУ») — это fingerprint кластера
- **MUST show mortgage-cut mechanism:** «ипотеку порезали» / «сократили кредит» — не слабый финал «не вышла на сделку»
- Temporal marker when it fits: «за сутки до ДДУ», «перед подписанием»
- News headline energy, casus arc, новостройка (не вторичка)
- Strong verb, active voice
- One variant only
- Include slug confirmation in JSON

## Reference titles that PASS (energy only, do not copy)
- B22: «В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела»
- B26: «В Тюмени новостройку сдали без РВЭ — банк заблокировал 520 тысяч»
- Scout draft (too long, shorten): «В Тюмени банк оценил новостройку на 900 тысяч ниже ДДУ — ипотеку порезали за сутки до подписания»

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-bank-ocenil-novostrojku-na-900-tysyach-nizhe-ddu-ipoteku-porezali-za-s",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
