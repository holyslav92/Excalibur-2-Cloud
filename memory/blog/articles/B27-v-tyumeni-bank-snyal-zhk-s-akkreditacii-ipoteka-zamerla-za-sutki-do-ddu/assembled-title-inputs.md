# Title inputs — B27 — 2026-09-15

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-bank-snyal-zhk-s-akkreditacii-ipoteka-zamerla-za-sutki-do-ddu`

## Scout handoff
- cluster_id: bank_accreditation_revoked_before_ddu
- top_energy_mirror: stopped_before_money
- klyshin_hook: none (fresh Tyumen newbuild accreditation casus without Klyshin; Klyshin rhythm only)
- dzen_casus_shape: PASS
  - event: семья в Тюмени бронирует квартиру в новостройке; ипотека предварительно одобрена; при брони корпус был в списке аккредитованных
  - risk: за ~24 часа до подписания ДДУ банк снимает ЖК/корпус с аккредитации для новых сделок — ипотека по этому объекту в этом банке не выдаётся
  - time: за сутки до назначенного ДДУ; бронь тикает отдельно от банка
  - finale: предодобрение не продвигается к кредитному договору; эскроу не открыт; деньги застройщику не ушли — остановка до аванса
- newbuild_mechanism: банк снял застройщика/ЖК с списка аккредитации накануне ДДУ — одобренная ипотека замерла, семья не дошла до эскроу
- why_newbuild_not_secondary: ДДУ/ипотека от застройщика; риск в аккредитации банком, не в ЕГРН вторички
- comment_magnet_angle: «Вы бы успели переехать в другой банк за сутки или сняли бы бронь?»
- title_draft (rework allowed): В Тюмени банк снял ЖК с аккредитации — ипотека замерла за сутки до ДДУ
- story_dup_check: PASS — distinct from B22 (ставка перед ДДУ), B19 (эскроу/маткапитал), B20 (смена юрлица), B26 (РВЭ/транш), B09 (ЕГРН после одобрения)
- distinct_plot: одобрение заёмщика было, но **банк снял объект с аккредитации** — блок по корпусу, не по человеку; не изменение ставки (B22), не эскроу/маткапитал (B19)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 909 (55+11176)
- support: «новостройки в тюмени от застройщика» — 668
- support: «ипотека новостройка тюмень» — 189 (cluster)
- support: «квартиры в тюмени новостройка ипотека» — 100
- support: «тюмень застройщик новостройка ипотека» — 96
- support: «новостройки тюмень купить в ипотеку» — 87
- partial: «аккредитация новостройка ипотека» — empty API

## Research — subject & conflict
- Subject: новостройка в Тюмени, предварительное одобрение ипотеки, банк снимает ЖК/корпус с аккредитации за ~24 часа до ДДУ — ипотека «замерла», эскроу не открыт
- Reader problem: покупатель думает «ипотеку уже одобрили»; не перепроверил аккредитацию корпуса в день сделки; бронь и одобрение живут по разным срокам
- Casus: модельный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм)
- Surprising fact: аккредитацию могут отозвать за несколько дней до ДДУ, хотя при бронировании корпус ещё был в списке — это блок по объекту, не отмена одобрения «по человеку»
- Voice angle: разрыв между «ипотеку уже одобрили» и тем, что банк в последний момент закрывает объект; бронь отсчитывает часы
- Finale: остановка до эскроу, не потеря денег на счёте застройщика; вилка — другой банк, продление брони, смена объекта
- Distinct from B22 (банк поднял ставку перед ДДУ — бронь сгорела), B09 (ЕГРН после одобрения), B19 (маткапитал блокирует эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09 — другой plot)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot: ставка, не аккредитация)

## Anti-dup published titles
B02–B26 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21), ставка перед ДДУ (B22), апартаменты в ДДУ (B23), чистовая на приёмке (B25), РВЭ/транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за сутки до ДДУ», «накануне ДДУ»)
- One variant only
- Include slug confirmation in angle or separate field if needed
- Klyshin rhythm: завершённое событие + противоречие + следствие; не копипаст канала

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-bank-snyal-zhk-s-akkreditacii-ipoteka-zamerla-za-sutki-do-ddu",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
