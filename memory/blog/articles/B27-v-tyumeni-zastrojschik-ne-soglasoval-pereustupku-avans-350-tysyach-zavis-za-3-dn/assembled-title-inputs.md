# Title inputs — B27 — 2026-09-15

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avans-350-tysyach-zavis-za-3-dn`

## Scout handoff
- cluster_id: assignment_developer_consent_denied_tyumen
- klyshin_hook: none (checked https://t.me/klyshin_A — not used)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в строящемся ЖК по переуступке прав по ДДУ; цена ниже текущего прайса застройщика
  - risk: без письменного согласования застройщика уступка может не состояться; аванс 350 тыс. ₽ ушёл цеденту, не на эскроу
  - time: отказ за 3 дня до назначенного оформления; аванс переведён 19 дней назад
  - finale: застройщик предложил купить напрямую по текущему прайсу — на 420 тыс. ₽ дороже суммы уступки; цедент вернул 120 тыс. из 350 тыс., остаток назвал комиссией/удержанием; семья отказалась; квартира ушла другому покупателю с согласованной уступкой
- comment_magnet_angle: «350 тысяч аванса по переуступке — это ещё не эскроу: вы бы перевели деньги первому дольщику до письменного согласия застройщика или ждали бы официальный ответ из офиса продаж?»
- title_draft (rework allowed): В Тюмени застройщик не согласовал переуступку — аванс 350 тысяч завис за 3 дня до ДДУ
- story_dup_check: PASS — distinct from assignment_lost_to_faster_buyer; not B22 rate change; not B19 matkapital/escrow; not B09 EGRN
- distinct_plot: переуступка прав по ДДУ в новостройке; аванс цеденту до согласования застройщика; отказ в согласовании за 3 дня до сделки; частичный возврат; не перехват быстрым покупателем

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в Тюмени» — 902 (55+11176; RU225: 1916)
- support: «купить новостройку в тюмени от застройщика» — 456
- support: «новостройки тюмень купить в ипотеку» — 86
- narrow: «переуступка новостройки» — 18
- narrow: «договор переуступки новостройки» — 5

## Research — subject & conflict
- Subject: переуступка прав по ДДУ в новостройке Тюмени; аванс 350 000 ₽ цеденту до согласования застройщика; отказ в согласовании уступки за 3 дня до оформления
- Reader problem: семья нашла квартиру по цене ниже прайса застройщика, перевела крупный аванс «для фиксации», но согласование уступки ещё не получено — деньги на счёте цедента, права по ДДУ не перешли
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, застройщика, точной причины отказа)
- Surprising fact: застройщик может отказать в согласовании, когда аванс уже у цедента 19 дней, а до «оформления в офисе» осталось 3 дня — и предложить купить ту же квартиру напрямую дороже на сотни тысяч
- Voice angle: переуступка кажется «почти готовой квартирой со скидкой», но 350 тысяч на счёте первого дольщика — не эскроу и не защита 214-ФЗ
- Finale: частичный возврат 120 из 350; остаток удержан; прямая покупка у застройщика +420 тыс.; объект ушёл другому с согласованной уступкой
- Distinct from B22 (ставка ипотеки перед ДДУ), B19 (маткапитал/эскроу), B12 (перенос сдачи), B09 (ЕГРН после одобрения)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B26 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие супруги (B15), маткапитал+эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22), апартаменты в ДДУ (B23), чистовая на приёмке (B25), сдача без РВЭ (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 3 дня», «перед ДДУ»)
- One variant only
- Include slug confirmation in angle or separate field if needed
- Do NOT say «до ДДУ» if misleading — casus is about assignment/cession before registration, not signing new DDU; prefer «переуступку», «уступку», «оформление»

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-zastrojschik-ne-soglasoval-pereustupku-avans-350-tysyach-zavis-za-3-dn",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
