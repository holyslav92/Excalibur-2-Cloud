# Title inputs — B35 — 2026-09-11

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B35. verdict: PASS.

## topic_id
B35

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-v-ddu-zapretili-arendu-do-klyuchej-investor-poteryal-dvuh-arendatorov`

## Scout handoff
- cluster_id: newbuild_rental_banned_until_keys_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild investor casus without Klyshin)
- top_energy_mirror: paper_clean_then_broke
- newbuild_mechanism: «запрет сдачи в аренду до ключей/регистрации права в приложении к ДДУ новостройки»
- why_newbuild_not_secondary: «ограничение только в договоре долевого участия с застройщиком; на вторичке такого пункта в ДДУ не бывает — это чисто newbuild-механика для инвестора»
- dzen_casus_shape: PASS
  - event: инвестор в Тюмени выбрал студию в новостройке под сдачу, внёс бронь, согласовал двух арендаторов на дату после сдачи дома
  - risk: в приложении к ДДУ запрет передачи в аренду до регистрации права — нарушение = штраф + расторжение; арендаторы уходят к конкурентам, окупаемость срывается
  - time: за 5–7 дней до подписания ДДУ, когда юрист прочитал приложение целиком
  - finale: инвестор отказался подписывать ДДУ в текущей редакции; застройщик не согласился вычеркнуть пункт — бронь сгорела, один арендатор уже внёс задаток на другую квартиру
- comment_magnet_angle: «В ДДУ мелким шрифтом „аренда запрещена до ключей“ — вы бы всё равно подписали под сдачу или считаете, что „все так делают неофициально“?»
- title_draft (rework allowed): В Тюмени в ДДУ запретили аренду до ключей — инвестор потерял двух арендаторов
- story_dup_check: PASS — distinct plot: инвестор покупает новостройку под сдачу, в приложении к ДДУ пункт «не сдавать до регистрации права/получения ключей»; два арендатора уже согласовали заезд — застройщик предупреждает о расторжении при нарушении
- anti_dupe_hard: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 4670 (55+11176; RU225: 8607)
- support: «договор долевого участия» — 378
- support: «дду эскроу» — 45
- support: «дду новостройка» — 20
- weak niche: «аренда новостройка тюмень» — 5 (reworked to P0 spine)
- rework: probe «аренда новостройка тюмень» ~5 → «купить новостройку для сдачи» 0 → final P0 «новостройки тюмень» 4670

## Research — subject & conflict
- Subject: новостройка в Тюмени, инвестор под сдачу, ДДУ + приложение, запрет аренды до ключей/регистрации права, два арендатора, бронь
- Reader problem: инвестор бронирует студию под сдачу, договаривается с арендаторами, но в приложении к ДДУ находит запрет на аренду до ключей — теряет контроль над датой заезда и окупаемостью ещё до подписания ДДУ
- Casus: собирательный редакционный тюменский сюжет 2026 (без имён, ЖК, застройщика, суммы штрафа)
- Surprising fact: риск появляется раньше просрочки строительства — из-за условия приложения, которое делает дату первого заселения неопределённой ещё до подписания ДДУ
- Voice angle: приложение к ДДУ может разрушить модель аренды раньше, чем инвестор перечислит деньги по договору
- Finale: отказ от ДДУ → бронь сгорела → арендаторы ушли (один уже внёс задаток на другую квартиру)
- Distinct from B12 (перенос сдачи/эскроу), B21 (кладовка), B22 (ставка ипотеки перед ДДУ), B23 (квартира vs апартаменты в ДДУ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«Застройщик сдвинул сдачу ЖК в Тюмени на год — ипотека осталась» (B12 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН, пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/эскроу (B19), смена юрлица (B20), кладовка (B21), ставка ипотеки перед ДДУ (B22), квартира/апартаменты (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («до ключей», «перед ДДУ»)
- Newbuild only — не вторичка
- One variant only
- Klyshin rhythm: завершённое событие + противоречие + следствие

## Required JSON output
```json
{
  "topic_id": "B35",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-v-ddu-zapretili-arendu-do-klyuchej-investor-poteryal-dvuh-arendatorov",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
