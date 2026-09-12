# Title inputs — B24 — 2026-09-09

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## Scout handoff (2026-09-09, slot ~15:00 YEKT)
- cluster_id: `newbuild_developer_penalty_unpaid_acceptance_stopped_tyumen`
- klyshin_hook: none | original Tyumen newbuild casus preferred
- dzen_casus_shape: PASS
  - event: семья ждала ключи около года, затем получила уведомление о приёмке
  - risk: без акта не закрываются ипотечные/эскроу-процедуры; с актом без оговорок семья рискует потерять рычаг для взыскания неустойки
  - time: дедлайн приёмки; уведомление застройщика (ч. 4 ст. 8 214-ФЗ — не универсальное «14 дней на претензию»)
  - finale: семья остановила подписание, письменно зафиксировала просрочку и требования к застройщику
- comment_magnet_angle (from Scout): «Подписали бы акт без претензий, если бы застройщик обещал выплатить неустойку потом — или сначала потребовали бы деньги/письменный зачёт?»
- newbuild_mechanism: застройщик просрочил срок передачи ключей по ДДУ ~на год; дольщик насчитал неустойку ориентировочно 450–600 тыс. руб.; застройщик не выплатил / предложил зачесть в отделку; семья отказалась подписывать акт приёмки без письменного расчёта и фиксации требований
- anti_dupe_hard: PASS | distinct from B12 (перенос срока до наступления просрочки / заморозка эскроу), B21 (кладовка), acceptance_defects cluster
- title_draft (refine allowed): «В Тюмени застройщик год не передавал ключи и не выплатил неустойку — семья остановила приёмку»
- alt scout title: «В Тюмени за год просрочки ключей застройщик не выплатил неустойку — приёмку остановили»

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «неустойка за просрочку застройщика» — 1036 (RU225)
- «взыскание неустойки с застройщика за просрочку» — 218 (RU225)
- «неустойка за просрочку сдачи квартиры застройщика» — 137 (RU225); 3 (Tyumen 55+11176)
- «акт приемки квартиры в новостройке» — 9 (Tyumen 55+11176)

## Research — subject & conflict
- Subject: новостройка Тюмень, ДДУ, годовая просрочка передачи ключей, неустойка ~450–600 тыс. (оценка семьи), акт приёмки
- Reader problem: ключи наконец зовут на приёмку, но неустойку не выплатили / предлагают зачёт в отделку; подписать «чистый» акт страшно, не приходить — риск уклонения
- Casus: редакционный собирательный casus Тюмени 2026, без имён/ЖК/застройщика/банка
- Surprising fact: 214-ФЗ освобождает застройщика от неустойки при уклонении дольщика от акта при надлежащей готовности квартиры
- Distinct from B12: там перенос **до** дедлайна и заморозка эскроу; B24 — просрочка **уже случилась**, конфликт на финишной черте (деньги vs подпись акта)
- Finale: письменная претензия с расчётом, не паника, agency not dread

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Anti-dup published titles
B02–B15, B19–B23 published. **Avoid B12 angle** (перенос сдачи на год / эскроу заморозили). B24 = неустойка не выплачена + остановка приёмки после фактической просрочки.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tails

## Constraints
- Max ~50–70 chars preferred
- News-casus headline, Tyumen newbuild, clear subject (застройщик / семья / неустойка / приёмка)
- Strong verb, active voice, temporal marker «за год» / «год» when it helps
- One variant only; h1 === title

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
