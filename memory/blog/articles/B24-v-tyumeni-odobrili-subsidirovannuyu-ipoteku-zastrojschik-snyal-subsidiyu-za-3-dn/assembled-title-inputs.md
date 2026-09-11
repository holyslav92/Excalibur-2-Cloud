# Title inputs — B24 — 2026-09-11

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-odobrili-subsidirovannuyu-ipoteku-zastrojschik-snyal-subsidiyu-za-3-dn`

## Scout handoff
- cluster_id: subsidized_mortgage_revoked_before_ddu_tyumen
- klyshin_hook: none (fresh Tyumen newbuild casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке по рекламируемой субсидированной ставке от застройщика; банк выдал одобрение; квартира забронирована
  - risk: за три дня до ДДУ девелопер снял субсидию или пересчитал коммерческие условия; цена в договоре и платёж выросли на сотни тысяч; одобренной суммы перестало хватать
  - time: после 2–3 недель одобрения, за три дня до назначенного подписания ДДУ
  - finale: банк не пересчитал кредит без повторной заявки; семья остановила сделку до эскроу; бронь сгорела; субсидию не восстановили
- comment_magnet_angle: «Одобрение ипотеки уже на руках, но застройщик снял субсидию за три дня до ДДУ. Вы бы подписали договор, чтобы не потерять квартиру, или остановили сделку и начали искать заново?»
- title_draft (rework allowed): В Тюмени одобрили субсидированную ипотеку — застройщик снял субсидию за 3 дня до ДДУ
- top_energy_mirror: stopped_before_money — семья прошла выбор, одобрение и бронь, но остановилась перед эскроу
- story_dup_check: PASS — distinct from B22 (bank rate hike, not developer subsidy); B19 matkapital/escrow; B12 handover delay
- distinct_plot: банк одобрил субсидированную ипотеку от застройщика, но **девелопер отозвал собственную субсидию** за 3 дня до ДДУ (не банковский пересмотр ставки)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «ипотека от застройщика тюмень» — 514 (55+11176)
- support: «ипотека тюмень новостройки от застройщика» — 98
- child: «субсидированная ипотека от застройщика тюмень» — 27
- RU-wide: «субсидированная ипотека новостройка» — 385

## Research — subject & conflict
- Subject: новостройка в Тюмени, субсидированная ипотека от застройщика, банковское одобрение, бронь; застройщик снимает субсидию за 3 дня до ДДУ; рост цены и платежа; сделка не дошла до эскроу
- Reader problem: семья считает одобрение и бронь гарантией рекламной ставки; перед ДДУ застройщик отменяет субсидию или меняет коммерческие условия
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм)
- Surprising fact: стандарт ЦБ запрещает банку получать вознаграждение от застройщика за пониженную ставку, если это ведёт к росту цены квартиры — рекламную ставку нельзя оценивать отдельно от цены в ДДУ
- Voice angle: до регистрации ДДУ одобрение, бронь, рекламная ставка и цена живут в разных документах
- Finale: отказ от ДДУ → бронь сгорела → субсидию не восстановили
- Distinct from B22: там **банк** поднял ставку; здесь **застройщик** снял собственную субсидию

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — OTHER hero: bank, not developer subsidy)

## Anti-dup published titles
B02–B23 published. B22: «В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» — MUST differ: hero = застройщик + субсидия, not bank rate.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («за 3 дня до ДДУ»)
- One variant only
- Must clearly distinguish developer subsidy revocation from B22 bank rate hike

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-odobrili-subsidirovannuyu-ipoteku-zastrojschik-snyal-subsidiyu-za-3-dn",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
