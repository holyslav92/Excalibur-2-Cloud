# Title inputs — B20 — 2026-09-01

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B20. verdict: PASS.

## topic_id
B20

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot`

## Scout handoff
- cluster_id: newbuild_developer_legal_entity_change_ddu_escrow_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени подписала ДДУ с одним ООО застройщика, получила одобрение ипотеки под эскроу
  - risk: реорганизация застройщика → новый ДДУ от другого ООО с иными ИНН/ОГРН и реквизитами эскроу; банк приостановил открытие эскроу на нового контрагента до переаккредитации
  - time: через 4 месяца после первого ДДУ, за 72 часа до дедлайна брони
  - finale: отказались переподписывать вслепую; бронь сгорела; взнос за бронь вернули не полностью; очередь потеряна; деньги на эскроу ещё не внесены
- comment_magnet_angle: «Застройщик сменил юрлицо и прислал новый ДДУ — вы подписываете или выходите из сделки, даже если квартира „та же“?»
- title_draft (rework allowed): В Тюмени застройщик сменил юрлицо — дольщикам прислали новый ДДУ, эскроу не открыли
- story_dup_check: PASS
- distinct_plot: не перенос сдачи/заморозка эскроу после оплаты (B12), не маткапитал/семейная ипотека (B19), не вторичка; стоп на этапе смены юрлица застройщика и нового ДДУ до внесения на эскроу

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки в тюмени от застройщика» — 651 (55+11176)
- support: «купить новостройку в тюмени от застройщика» — 413
- support: «новостройки тюмени от застройщика в ипотеку» — 87
- context: «дду эскроу» — 38 (overlap B12/B19 — не дублировать угол)
- low: «реорганизация застройщика» — 3 (Tyumen), 34 (RU225)

## Research — subject & conflict
- Subject: новостройка в Тюмени, смена юрлица застройщика при реорганизации, новый ДДУ с другими ИНН/ОГРН, банк не открывает эскроу
- Reader problem: после одобрения ипотеки семья считает сделку почти закрытой — но застройщик меняет ООО, присылает новый ДДУ, а банк останавливает эскроу на нового контрагента, пока истекает бронь
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, сумм)
- Surprising fact: смена вывески ≠ смена юрлица; реальный перелом — когда меняются ИНН и ОГРН
- Voice angle: офис продаж называет изменения «техническими», но три срока сталкиваются: зарегистрированный ДДУ, банковская проверка нового контрагента, дедлайн брони
- Finale: отказ от слепой подписи → бронь сгорела → частичный возврат платы за бронь → очередь потеряна
- Distinct from B12 (перенос сдачи, деньги уже на эскроу), B19 (маткапитал блокирует эскроу), B09 (ЕГРН после одобрения)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B15, B19 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («через 4 месяца», «за 72 часа»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B20",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
