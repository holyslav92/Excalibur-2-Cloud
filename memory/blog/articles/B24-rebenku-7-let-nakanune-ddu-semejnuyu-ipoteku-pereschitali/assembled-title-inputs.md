# Title inputs — B24 — 2026-09-09

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`rebenku-7-let-nakanune-ddu-semejnuyu-ipoteku-pereschitali`

## Scout handoff
- cluster_id: newbuild_family_mortgage_child_age_clock_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus without Klyshin; avoids family-mortgage+escrow B19 cluster)
- dzen_casus_shape: PASS
  - event: семья в Тюмени получила предварительное одобрение семейной ипотеки на квартиру в новостройке, внесла бронь и готовилась к подписанию ДДУ
  - risk: накануне подписания (за 5–7 дней) младшему ребёнку исполнилось 7 лет — банк снял льготную ставку/урезал лимит кредита; разница в ежемесячном платеже и недостающий первоначальный взнос
  - time: «за шесть дней до ДДУ» / «накануне подписания»
  - finale: банк отказал выдавать кредит на прежних условиях; бронь сгорела, застройщик не продлил цену — семья остановилась до перевода на эскроу
- comment_magnet_angle: «Ребёнку исполнилось 7 лет за неделю до ДДУ: вы бы торопили подпись или снимали бронь и искали другой банк?»
- title_draft (rework allowed): В Тюмени ребёнку исполнилось 7 лет накануне ДДУ — семейную ипотеку пересчитали
- story_dup_check: PASS — distinct from B22 (bank raised rate before DDU), B19 (matkapital/escrow), B12 (handover delay)
- distinct_plot: семейная ипотека на новостройку — **возрастной порог ребёнка 7 лет** наступил между одобрением и подписанием; банк пересчитал льготу (не изменение ключевой ставки B22, не маткапитал B19)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «семейная ипотека в тюмени» — 752 (55+11176; RU225 compare: 1099)
- support: «семейная ипотека тюмень» — 1210
- support: «новостройки тюмени семейная ипотека» — 27
- child: «семейная ипотека в тюмени условия 2026» — 256 (context only, do not put 2026 in H1)

## Research — subject & conflict
- Subject: новостройка в Тюмени, семейная ипотека, один ребёнок; предварительное одобрение и бронь не фиксируют право на льготу; возрастной критерий — ребёнок до 6 лет включительно на дату **кредитного договора** (практически совпадает с цепочкой ДДУ)
- Reader problem: семья не сверила дату седьмого дня рождения с датой кредитного договора; платёж и взнос уже рассчитаны под семейную программу
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм)
- Surprising fact: предварительное одобрение при ребёнке 6 лет не замораживает право на ставку до 6%; критерий перепроверяют перед кредитным договором
- Voice angle: «часы на стене» — бронь и одобрение идут по своим срокам, а право привязано к другой дате
- Finale: пересчёт/отказ на прежних условиях → бронь сгорела или доплата из резерва
- Distinct from B22 (банк поднял ставку, не возраст ребёнка), B19 (маткапитал блокирует эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: ставка, не возраст)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid: расписка, задаток, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), открытая кухня, перенос сдачи (B12), согласие супруги (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), банк поднял ставку перед ДДУ (B22), апартаменты вместо квартиры (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («накануне ДДУ», «за неделю до ДДУ»)
- Clear subject: семейная ипотека / новостройка / возраст ребёнка
- One variant only
- Must differ from B22 angle (не «банк поднял ставку» — здесь возраст 7 лет и пересчёт семейной ипотеки)
- **HARD:** в H1 обязательно «семейную ипотеку» (не голое «ипотеку»); Tyumen optional if length tight

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "rebenku-7-let-nakanune-ddu-semejnuyu-ipoteku-pereschitali",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
