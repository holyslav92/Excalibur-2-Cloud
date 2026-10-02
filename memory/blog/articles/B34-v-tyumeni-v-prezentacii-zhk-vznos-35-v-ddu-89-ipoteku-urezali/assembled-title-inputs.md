# Title inputs — B34 — 2026-10-02

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B34. verdict: PASS.

## topic_id
B34

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-prezentacii-zhk-vznos-35-v-ddu-89-ipoteku-urezali`

## Scout handoff
- slot_rubric: novostroyki
- cluster_id: newbuild_management_fee_ddu_appendix_vs_sales_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus without Klyshin)
- top_energy_mirror: paper_clean_then_broke
- viral_mechanism: договор vs реальность
- newbuild_mechanism: в презентации отдела продаж «плата за содержание с ключей — от 35 ₽/м²»; в приложении №3 к проекту ДДУ — 89 ₽/м² с ежегодной индексацией и отдельной строкой на капремонт; банк после пересчёта полной нагрузки снизил одобренную сумму ипотеки ~620 тыс. ₽; семья не подписала ДДУ, эскроу не открывали; бронь 150 тыс. ₽ вернули после претензии
- why_newbuild_not_secondary: бронь застройщика, презентация ЖК, приложение к ДДU, ипотечная нагрузка, неоткрытый эскроу — без вторичного продавца и ДКП
- dzen_casus_shape: PASS
  - event: семья выбрала трёшку в строящемся ЖК; в PDF/презентации 35 ₽/м² содержание, на предподписании ДДU в приложении 89 ₽/м²
  - risk: полная долговая нагрузка (ипотека + содержание) уменьшает ипотечный лимит до фиксации сделки
  - time: предподписание ДДU за несколько дней до планового открытия эскроу — **не** использовать countdown «за N дней до эскроу» в H1
  - finale: банк урезал лимит ~620 тыс.; семья отказалась от ДДU; бронь 150 тыс. вернули после претензии; в другой корпус не переходили
- comment_magnet_angle (preserve or sharpen): «Если в презентации 35 ₽, а в ДДU 89 ₽ за квадрат — вы подписали бы, чтобы не потерять бронь, или развернулись бы сразу?»
- title_draft (rework allowed): В Тюмени в презентации ЖК обещали взнос 35 рублей — в приложении к ДДU вышло 89, ипотеку урезали
- story_dup_check: PASS — distinct from B25 (чистовая на приёмке), B27 (земля в аренде), B31 (страховка), B32 (реквизиты эскроу), B22 (ставка перед ДДU), booking price hike
- h1_fingerprint: 35→89 ₽/m² + приложение к ДДU + снижение ипотечного лимита ~620 тыс.

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4360 (regions 55+11176)
- support: «купить новостройку в тюмени» — 905
- weak probes: «плата за содержание жилья» 6; «управляющая компания новостройка» 2; «договор долевого участия тюмень» 3
- rework: casus spine = расхождение тарифа содержания презентация vs приложение ДДU + урезание ипотеки; buyer demand через newbuild Тюмень

## Research — subject & conflict
- Subject: новостройка Тюмень, презентация отдела продаж vs приложение к ДДU о плате за содержание, ипотечное одобрение и полная нагрузка, бронь 150 тыс.
- Reader problem: семья внесла бронь, ипотека предварительно одобрена; перед ДДU в приложении другая ежемесячная нагрузка, чем в презентации — подписывать или остановить сделку
- Casus numbers (editorial composite): 35 vs 89 ₽/m², ~620 тыс. снижение лимита, 150 тыс. бронь возврат
- Voice angle: спокойный разбор — сравнить обещание с приложениями до подписания и эскроу
- Surprising fact: официальный минимальный взнос на капремонт в ТО — 14,62 ₽/m²; 89 ₽/m² в сюжете — содержание, не только капремонт
- Finale: ДДU не подписали; эскроу не открывали; бронь вернули после претензии

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДU — бронь сгорела» (B22 — другой механизм)
«В Тюмени в ДДU обещали чистовую — на приёмке 3 расхождения, акт не подписали» (B25 — другой plot)

## Anti-dup published titles (angle only — do not copy)
B12 перенос сдачи; B19 маткапитал/эскроу; B20 смена юрлица; B21 кладовка; B22 ставка перед ДДU; B25 чистовая приёмка; B27 земля аренда; B28 газ КП; B29 нулевой взнос; B30 запрет уступки; B31 страховка; B32 чужое юрлицо эскроу; B33 долг за свет вторичка

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, «за N дней до эскроу» countdown

## Constraints
- Max ~50–70 chars Cyrillic headline
- News-casus headline, Klyshin rhythm (event + contradiction + consequence), Tyumen newbuild
- Strong verb, active voice; temporal marker OK («на предподписании», «перед ДДU») but not fake countdown
- One variant only
- Clear subject: содержание/взнос в презентации vs ДДU, ипотека, новостройка
- h1 and title identical unless strong reason

## Required JSON output
```json
{
  "topic_id": "B34",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-prezentacii-zhk-vznos-35-v-ddu-89-ipoteku-urezali",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
