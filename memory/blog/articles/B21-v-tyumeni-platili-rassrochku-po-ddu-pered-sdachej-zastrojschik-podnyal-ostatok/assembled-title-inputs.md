# Title inputs — B21 — 2026-09-02

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B21. verdict: PASS.

**TITLE PRIORITY:** Refine scout `title_draft` — keep the payment arc («платили рассрочку по ДДУ») + temporal twist («перед сдачей» / «за месяц до сдачи») + consequence (остаток подняли / угроза расторжения). Do NOT drop the human beat «платили 14 месяцев». Champion shape: event → contradiction → hint of finale. 50–72 chars OK.

## topic_id
B21

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok`

## Scout handoff
- cluster_id: newbuild_developer_installment_balance_increased_before_handover_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в новостройке с рассрочкой от застройщика по графику в ДДУ
  - risk: за месяц до сдачи корпуса застройщик прислал допсоглашение — остаток вырос примерно на 400 тысяч рублей, сроки оплаты сжались; семье пригрозили расторжением ДДУ
  - time: 14 месяцев платили по графику → за месяц до сдачи
  - finale: семья отказалась подписывать допсоглашение, застройщик пригрозил расторжением; внесённые деньги и очередь на квартиру оказались под угрозой, поэтому за разбором обратились до подписи
- comment_magnet_angle: «Если в ДДУ прописан график рассрочки — застройщик вообще имеет право поднять остаток за месяц до ключей?»
- title_draft (rework allowed): В Тюмени платили рассрочку по ДДУ — перед сдачей застройщик поднял остаток
- story_dup_check: PASS
- distinct_plot: не перенос сдачи/заморозка эскроу (B12), не смена юрлица/новый ДДУ (B20), не маткапитал/семейная ипотека (B19), не бронь/рост цены при брони; стоп на переписывании остатка рассрочки перед сдачей через допсоглашение

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4649 (55+11176)
- support: «рассрочка от застройщика» — 213 (Tyumen), 21115 (RU225)
- support: «рассрочка от застройщика тюмень» — 142
- support: «квартира в рассрочку от застройщика тюмень» — 88
- rejected: «долгострой тюмень» 91 (overlap B12), «штраф застройщику» 42 (weak)

## Research — subject & conflict
- Subject: новостройка в Тюмени, рассрочка по зарегистрированному ДДУ, проект допсоглашения с повышением остатка и сжатием сроков перед сдачей
- Reader problem: 14 месяцев платили по графику (~40% цены), за месяц до сдачи пришло допсоглашение с +400 000 ₽ к остатку и угрозой расторжения при отказе
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, застройщика)
- Surprising fact: проект допсоглашения не заменяет зарегистрированный ДДУ; отказ от подписи ≠ автоматическая просрочка по ст. 9 214-ФЗ
- Voice angle: граница между законным перерасчётом по формуле в ДДУ и попыткой переписать остаток перед ключевым этапом; «не подпишете — расторгнем» требует проверки по документам
- Finale: отказ от подписи под давлением → спор об остатке и риск расторжения → обратились до подписи
- Distinct from B12 (перенос сдачи, эскроу заморожен), B20 (смена юрлица, новый ДДУ), B19 (маткапитал блокирует эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B15, B19, B20 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал+эскроу (B19), смена юрлица/новый ДДУ (B20).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («14 месяцев», «за месяц до сдачи»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B21",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
