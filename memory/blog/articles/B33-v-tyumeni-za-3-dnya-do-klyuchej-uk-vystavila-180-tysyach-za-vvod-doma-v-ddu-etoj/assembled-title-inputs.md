# Title inputs — B33 — 2026-09-21

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B33. verdict: PASS.

## topic_id
B33

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-za-3-dnya-do-klyuchej-uk-vystavila-180-tysyach-za-vvod-doma-v-ddu-etoj`

## Scout handoff
- cluster_id: newbuild_uk_handover_fee_not_in_ddu_tyumen
- klyshin_hook: optional | none (локальный casus самодостаточен)
- top_energy_mirror: number_in_claim_vs_zero_paid
- newbuild_mechanism: дольщик перед приёмкой в сданном ЖК получает от назначенной застройщиком УК отдельный счёт ~180 000 ₽ за «ввод дома», «подключение к сетям», «формирование УК» — в ДДУ и приложениях такой строки нет; оплату связывают с допуском к акту; без акта банк не проводит последний ипотечный транш
- why_newbuild_not_secondary: цепочка дольщик—застройщик—УК при сдаче новостройки (ДДУ, ввод, акт, транш); не вторичка
- dzen_casus_shape: PASS
  - event: семья с двумя детьми, ипотека, ключи от сданного тюменского ЖК
  - risk: счёт 180 000 ₽ сверх цены ДДУ; без оплаты — не допустят к приёмке; без акта — нет последнего транша
  - time: за 3 дня до выдачи ключей, вечером, дата приёмки уже согласована
  - finale: в ДДУ ноль по 180 тыс.; семья не платит без письменного основания; ключи переносят на 2 недели; акт и транш зависли
  - emotional engine: «в договоре — ноль, в счёте перед ключами — 180 тысяч»
- comment_magnet_angle: «Если за три дня до ключей УК присылает счёт на 180 тысяч, которого нет в ДДУ, вы платите, чтобы не сорвать выдачу квартиры, или стопорите приёмку и требуете письменное основание?»
- title_draft (rework allowed): В Тюмени за 3 дня до ключей УК выставила 180 тысяч за ввод дома — в ДДУ этой строки не было
- story_dup_check: PASS — distinct from B25 (отделка), B26 (РВЭ), B32 (эскроу/ИНН), B30 (уступка), B31 (страховка), B12 (перенос сдачи)
- h1_fingerprint: 3_days_before_keys_180k_uk_fee_absent_from_ddu
- formula_spam_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4395 (regions 55+11176)
- probe weak: «управляющая компания новостройка» — 4; «акт приемки передачи квартиры» — 9
- rework: слабый УК-спрос → spine широкий newbuild + casus в H1 (ключи, ДДУ, счёт УК)

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ без строки о платеже УК, счёт ~180 000 ₽ перед ключами, акт приёма-передачи, последний ипотечный транш
- Reader problem: крупный счёт от УК перед ключами, не виден в ДДУ; страх сорвать приёмку и ипотеку
- Casus: композитный (без имён ЖК, УК, банка); 180 000 — параметр фабулы
- Voice angle: не спорить о «типовости» — сверить цену ДДУ, передачу и основание платежа + документы для банка
- Surprising fact: прокуратура Тюменского района 2026 — перерасчёт >2 млн ₽ по НДС в квитанциях УК (другой вид платежа, но контекст проверки строк)
- Constraints: не называть счёт «обязательным тарифом» без документов; не утверждать универсально право УК блокировать передачу

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали» (B25 — другой plot)
«За 2 дня до эскроу банк остановил сделку — в ДДУ чужое юрлицо» (B32 — другой plot)

## Anti-dup published titles
Avoid repeating angles: B25 finishing, B26 RVE, B30 assignment ban, B31 insurance, B32 escrow INN, B12 delay keys, B21 storeroom, B22 rate before DDU.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tail

## Constraints
- Max ~50–70 chars (can stretch slightly if needed for clarity)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal marker («за 3 дня до ключей»)
- One variant only
- Clear subject: счёт УК / ДДУ / ключи новостройки

## Required JSON output
```json
{
  "topic_id": "B33",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-za-3-dnya-do-klyuchej-uk-vystavila-180-tysyach-za-vvod-doma-v-ddu-etoj",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
