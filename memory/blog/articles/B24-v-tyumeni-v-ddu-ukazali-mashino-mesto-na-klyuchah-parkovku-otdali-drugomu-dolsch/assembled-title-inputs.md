# Title inputs — B24 — 2026-09-13

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-ukazali-mashinomesto-na-klyuchah-parkovku-otdali-drugomu-dolschiku`

## Scout handoff
- cluster_id: newbuild_parking_spot_double_sold_tyumen
- klyshin_hook: optional | original: none | signal: none (fresh Tyumen newbuild parking casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в новостройке с машино-местом в приложении к ДДУ и внесла оплату на эскроу
  - risk: в день выдачи ключей парковочное место из договора занято другим дольщиком; застройщик предлагает «аналог» или отказывается передавать
  - time: в день выдачи ключей / через 3 дня после подписания акта приёма квартиры
  - finale: семья отказалась от замены, подала претензию; застройщик ссылается на опечатку в приложении; регистрация права на машино-место не прошла
- comment_magnet_angle: «Машино-место в приложении к ДДУ — это такая же собственность, как квартира, или вы бы подписали акт без парковки, если ключи уже на столе?»
- title_draft (rework allowed): В Тюмени в ДДУ указали машино-место — на ключах парковку отдали другому дольщику
- story_dup_check: PASS — distinct legal plot: машино-место в приложении к ДДУ новостройки; семья оплатила объект по договору долевого участия, но на выдаче ключей место занято другим автомобилем / продано повторно
- distinct_plot: двойная реализация/занятость машино-места при выдаче ключей; не B21 (кладовка по ДДУ), не B23 (апартаменты вместо квартиры), не B22 (ставка перед ДДУ), не B19 (маткапитал/эскроу), не B12 (перенос сдачи)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 8430 (55+11176; compare RU225)
- mechanism: «машиноместо в новостройке» — 971
- support: «машиноместо дду» / «дду машиноместо» — 207
- weak: «машиноместо новостройка тюмень» — 0 (do not use as sole spine)

## Research — subject & conflict
- Subject: новостройка в Тюмени, машино-место в приложении к ДДУ (условный номер, план, этаж), семья оплатила парковку, на выдаче ключей место занято другим дольщиком
- Reader problem: покупатель принимает квартиру и обнаруживает, что указанное в зарегистрированном ДДУ машино-место занято либо оформлено на другого дольщика; застройщик называет это опечаткой и предлагает менее удобный «аналог»
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, застройщика, банка)
- Surprising fact: покупатели обнаруживали смену нумерации и расположения проданных машино-мест только при сдаче паркинга — после регистрации ДДУ застройщик менял план
- Voice angle: момент после выдачи ключей, когда семья видит чужую машину на месте, за которое заплатила; можно ли принять квартиру, но не принять парковку
- Finale: отказ от «аналога» → претензия → застройщик ссылается на опечатку → регистрация права на машино-место не прошла
- Distinct from B21 (кладовка по ДДУ на ключах), B23 (апартаменты в ЕГРН), B22 (ставка ипотеки перед ДДУ), B19 (маткапитал/эскроу), B12 (перенос сдачи)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени оплатили кладовку по ДДУ — на ключах помещения не было» (B21 — другой объект)
«В Тюмени в ДДУ написали квартиру — в выписке оказались апартаменты» (B23 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка ипотеки перед ДДУ (B22), апартаменты вместо квартиры (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на ключах», «в день выдачи», «при выдаче ключей»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-ukazali-mashinomesto-na-klyuchah-parkovku-otdali-drugomu-dolschiku",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
