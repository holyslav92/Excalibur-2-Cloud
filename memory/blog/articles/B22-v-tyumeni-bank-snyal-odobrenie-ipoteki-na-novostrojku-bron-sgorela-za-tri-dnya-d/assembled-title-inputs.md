# Title inputs — B22 — 2026-09-03

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B22. verdict: PASS.

## topic_id
B22

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela`

## Scout handoff
- cluster_id: newbuild_mortgage_approval_withdrawn_booking_lost_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке, внесла плату за бронь, получила предварительное ипотечное одобрение; схема сделки согласована с застройщиком
  - risk: за 72 часа до ДДУ банк повторно проверил доход, кредитную историю или нагрузку и снял одобрение; без нового кредитора подписать ДДУ нельзя, бронь истекает
  - time: 72 часа до дедлайна бронирования и подписания ДДУ, уже после первоначального одобрения
  - finale: бронь сгорела, квартиру купил другой покупатель; плату за бронь вернули частично либо не вернули; семья заново выбирала новостройку и банк ещё 2–3 недели
- comment_magnet_angle: «Банк снял одобрение за три дня до ДДУ — вы успели бы найти другой банк или отказались бы от этой квартиры?»
- title_draft (rework allowed): В Тюмени банк снял одобрение ипотеки на новостройку — бронь сгорела за три дня до ДДУ
- story_dup_check: PASS
- distinct_plot: не семейная ипотека/маткапитал/эскроу (B19), не смена юрлица (B20), не кладовка по ДДУ (B21), не ЕГРН после одобрения (B09), не перенос сдачи (B12); стоп — отзыв ипотечного решения до ДДУ и потеря брони

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить квартиру в тюмени новостройка ипотека» — 86 (55+11176)
- support: «одобрение ипотеки» — 224
- support: «ипотека в тюмени на новостройки» — 41
- support: «после одобрения ипотеки» — 30
- support: «сколько действует одобрение ипотеки» — 24
- low: «бронь новостройки» — 3 (раскрывать внутри casus, не в H1)

## Research — subject & conflict
- Subject: предварительное одобрение ипотеки на новостройку в Тюмени, бронь, ДДУ
- Reader problem: покупатель считает «ипотеку одобрили» гарантией сделки, вносит бронь — но банк может перепроверить заёмщика до выдачи кредита; при отзыве решения за дни до ДДУ бронь сгорает, квартира уходит другому
- Casus: типовой локальный тюменский сценарий (без имён, ЖК, банка)
- Surprising fact: срок действия предварительного решения не равен гарантии выдачи кредита в дату ДДУ; новый банк не успевает за 1–3 дня
- Voice angle: обратный отсчёт 72 часа между «одобрили» и подписанием ДДУ; несовпадение сроков брони и банковской процедуры
- Finale: бронь потеряна, квартира продана другому, частичный/нулевой возврат брони, 2–3 недели на новый объект и банк
- Distinct from B09 (ЕГРН/регистрация после одобрения), B19 (эскроу/маткапитал), B20 (юрлицо/эскроу), B21 (кладовка по ДДУ)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»

## Anti-dup published titles
B02–B21 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, «ипотеку одобрили + ЕГРН/регистрация» (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), семейная ипотека/эскроу/маткапитал (B19), смена юрлица (B20), кладовка по ДДУ (B21).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, **«В Тюмени»** in H1 (local buyer-intent)
- Strong verb, active voice, **обязательная** временная метка «за три дня» или «за 72 часа»
- **Em dash (—) only** — NO colon (:) in H1
- One variant only
- Include slug confirmation in angle or separate field if needed
- Prefer pattern like B19: «В Тюмени … одобрили — … сорвал/сгорела …»

## Required JSON output
```json
{
  "topic_id": "B22",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-bank-snyal-odobrenie-ipoteki-na-novostrojku-bron-sgorela",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
