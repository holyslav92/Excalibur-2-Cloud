# Title inputs — B24 — 2026-09-07

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemschika-isklyuchili`

## Scout handoff
- cluster_id: newbuild_coborrower_dropped_before_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus; Klyshin not used — avoids duplicate with live ~20)
- top_energy_mirror: stopped_before_money
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, получила одобрение семейной ипотеки на двоих, забронировала объект и пришла подписывать ДДУ
  - risk: банк исключил созаёмщика из одобрения — сумма кредита и первоначального взноса перестала сходиться с ценой в ДДУ и графиком эскроу
  - time: за сутки / в день подписания ДДУ в офисе застройщика
  - finale: подписание остановили до перевода на эскроу; бронь сгорела или застройщик поднял цену; семья не внесла деньги — сделку сорвали на месте (agency: остановились до аванса)
- comment_magnet_angle: «Банк неделю держал одобрение „на двоих", а перед ДДУ созаёмщика исключили. Вы бы подписали договор на оставшийся лимит или забрали бы бронь?»
- newbuild_mechanism: банк одобрил семейную ипотеку на двоих под ДДУ на новостройку; за сутки до подписания убрал созаёмщика из кредита — лимит упал, на эскроу не хватило суммы по договору, подписание остановили до перевода денег
- title_draft (rework allowed): В Тюмени семейную ипотеку одобрили на двоих — перед ДДУ созаёмщика исключили, лимит упал
- story_dup_check: PASS — distinct from B09 (отзыв одобрения/ЕГРН), B19 (маткапитал/эскроу), B22 (изменение ставки перед ДДУ), B23 (апартаменты в ДДУ)
- distinct_plot: одобрение семейной ипотеки **на двоих**, затем **исключение созаёмщика** перед ДДУ и падение лимита (не отзыв одобрения целиком, не эскроу/маткапитал, не смена ставки)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «семейная ипотека в тюмени» — 730 (55+11176; RU225: 1063)
- support: «семейная ипотека тюмень» — 1158
- support: «новостройки тюмень» — 4670
- support: «созаемщик ипотека» — 573 (RU225: 35922)
- child: «семейная ипотека созаемщик супруг» — 12

## Research — subject & conflict
- Subject: семейная ипотека на новостройку в Тюмени, предварительное одобрение на двоих созаёмщиков, банк исключает второго супруга перед ДДУ, лимит кредита падает, срыв подписания и брони
- Reader problem: семья считает предодобрение «на двоих» финалом и едет подписывать ДДУ; банк может пересмотреть состав заёмщиков и снизить лимит в день сделки
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм брони)
- Surprising fact: с 01.02.2026 оба супруга обязаны быть созаёмщиками — слабая КИ второго может «уронить» лимит уже после предварительного одобрения
- Voice angle: ложное ощущение финала после «одобрили на двоих»; отдельные ворота — финальная проверка обоих, сходимость лимита с ДДУ/эскроу, срок брони
- Finale: не подписали ДДУ, не перевели на эскроу; бронь истекла; сделка сорвалась на месте
- Distinct from B22 (ставка/платёж перед ДДУ), B19 (маткапитал блокирует эскроу), B09 (отзыв одобрения/ЕГРН)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: ставка, не созаёмщик)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка перед ДДУ (B22), апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («перед ДДУ», «в день подписания»)
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
  "slug": "v-tyumeni-semejnuyu-ipoteku-odobrili-na-dvoih-pered-ddu-sozaemschika-isklyuchili",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
