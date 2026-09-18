# Title inputs — B27 — 2026-09-18

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj`

## Scout handoff
- cluster_id: assignment_lost_to_faster_buyer
- klyshin_hook: none (original Tyumen newbuild assignment casus)
- top_energy_mirror: someone_else_took_object
- newbuild_mechanism: покупатель держит переуступку по новостройке — договор уступки прав требования по ДДУ с согласованием застройщика; застройщик 28 дней не регистрирует уступку; за сутки до открытия эскроу лот снимают с брони и продают другому покупателю
- why_newbuild_not_secondary: цепочка ДДУ → согласование переуступки → регистрация уступки → эскроу; не вторичка
- dzen_casus_shape: PASS
  - event: семья в Тюмени нашла переуступку в строящемся ЖК, подписала договор уступки и внесла бронь
  - risk: без регистрации переуступки эскроу не открывают, лот могут продать повторно
  - time: 28 дней ожидания регистрации; за сутки до открытия эскроу — лот в брони у другого
  - finale: эскроу не открыли; бронь вернули частично; претензия; лот потерян; искали более дорогую планировку
- comment_magnet_angle: «28 дней регистрацию тянули, а лот сняли за сутки до эскроу: вы бы ждали согласие застройщика или сразу искали другую переуступку, даже если цена уже поднялась?»
- title_draft (rework allowed): В Тюмени 28 дней ждали регистрацию переуступки — за сутки до эскроу лот забрал другой
- story_dup_check: PASS — distinct from assignment with 350k advance; from «бронь против секции ДДУ»; from expired mortgage approval; from DDU/escrow amount comparison plots
- h1_fingerprint: 28 дней регистрации + дедлайн эскроу + лот забрал другой покупатель

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 923 (55+11176); compare RU225 — 1936
- support: «переуступка квартиры» — 63; «переуступка новостройка» — 19
- rework: weak переуступка queries → spine через новостройка + переуступка + эскроу + застройщик (casus hook)

## Research — subject & conflict
- Subject: переуступка прав по ДДУ в тюменской новостройке, 28-дневная задержка регистрации уступки, дедлайн эскроу, потеря лота другому покупателю
- Reader problem: подписанная переуступка и бронь ≠ закреплённый лот; пока уступка не в ЕГРН, застройщик может отдать квартиру другому
- Casus: собирательный тюменский сюжет 2026 (без имён, ЖК, банка, сумм)
- Voice angle: «28 дней на словах» — обещали регистрацию «на этой неделе», а за сутки до эскроу лот уже у другого
- Finale: эскроу не открыли; бронь частично; претензия; лот потерян
- Distinct from B19 (эскроу/маткапитал), B20 (смена юрлица/эскроу), B22 (ставка перед ДДУ/бронь), B12 (перенос сдачи/эскроу), B26 (РВЭ/транш)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B15, B19–B26 published. Avoid: расписка, задаток, доверенность, автооценка, наследство, ЗАГС, ипотека+ЕГРН, открытая кухня, перенос сдачи (B12), маткапитал/эскроу (B19), смена юрлица (B20), ставка перед ДДУ (B22), апартаменты (B23), чистовая (B25), РВЭ/транш (B26). B27 = переуступка + 28 дней регистрации + лот другому перед эскроу.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tails, label heads

## Constraints
- Max ~50–70 chars (scout draft ~88 — tighten while keeping stakes + newbuild marker)
- **HARD:** include «новостройк» or «застройщик» or «ДДУ» or «эскроу» or «переуступк» in h1 (topic_focus gate)
- News headline energy, Klyshin rhythm casus arc, Tyumen newbuild
- Strong verb, active voice, temporal markers («28 дней», «за сутки до эскроу»)
- One variant only
- Clear subject: переуступка / регистрация уступки / эскроу / лот / застройщик

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-28-dnej-ne-registrirovali-pereustupku-lot-zabral-drugoj",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
