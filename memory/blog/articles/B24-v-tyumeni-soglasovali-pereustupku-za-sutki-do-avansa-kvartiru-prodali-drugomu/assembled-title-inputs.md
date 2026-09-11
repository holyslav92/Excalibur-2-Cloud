# Title inputs — B24 — 2026-09-11

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-soglasovali-pereustupku-za-sutki-do-avansa-kvartiru-prodali-drugomu`

## Scout handoff
- cluster_id: assignment_lost_to_faster_buyer_tyumen
- klyshin_hook: none (fresh Tyumen newbuild assignment casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени нашла квартиру в строящемся ЖК по переуступке, согласовала схему с застройщиком и продавцом-уступщиком, подготовила аванс и ипотеку
  - risk: за сутки до перевода аванса застройщик сообщил, что квартира уже закреплена за другим покупателем; переуступка сорвана, планировка потеряна
  - time: 24 часа до запланированного внесения аванса по договору переуступки
  - finale: объект потерян; задаток уступщику возвращён полностью; аванс по цессии не переводили; другую квартиру в этом ЖК семья не купила
- comment_magnet_angle: Переуступку согласовали, аванс готовили — а квартиру продали другому за сутки: вы бы винили уступщика, застройщика или себя за паузу?
- title_draft (rework allowed): В Тюмени согласовали переуступку — за сутки до аванса квартиру продали другому
- story_dup_check: PASS — distinct from burned reservation, price hike on assignment, escrow freeze, DDU termination
- distinct_plot: переуступка прав по ДДУ в строящемся ЖК — согласование получено, но другой покупатель обогнал до аванса (не бронь сгорела, не долг 94 тыс., не +280 тыс. на другой планировке)
- top_energy_mirror: someone_else_took_object
- newbuild_mechanism: переуступка прав по ДДУ в строящемся ЖК — другой покупатель обогнал сделку и забрал квартиру до внесения аванса

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «переуступка новостройки» — 16 (55+11176; compare225 anchor «новостройки тюмень» — 4583 / 8705 RU)
- support: «договор переуступки новостройка» — 1 (too narrow)
- rejected probes: «расторжение ДДУ» (escrow cluster), «приемка квартиры в новостройке тюмень» (bank tranche cluster)

## Research — subject & conflict
- Subject: переуступка прав по ДДУ в строящемся ЖК Тюмени; письменное согласие застройщика на схему; проект договора цессии; за сутки до аванса объект закрепили за другим покупателем
- Reader problem: согласие застройщика ≠ резерв конкретного лота; без письменной фиксации срока и статуса объекта более быстрый покупатель может занять квартиру по внутренней процедуре девелопера
- Casus: modeled composite editorial Tyumen story (no names, ЖК, bank, deposit amount in article)
- Surprising fact: письменное согласие застройщика подтверждает допустимость схемы, но не мешает закрепить квартиру за другим до регистрации уступки, если резерв лота не оформлен
- Voice angle: «согласовали» звучит как победа, но до госрегистрации покупатель может остаться в очереди с теми, кто прошёл процедуру застройщика быстрее
- Finale locked: уступка не состоялась; аванс не переводили; задаток возвращён; планировка потеряна; другую в этом ЖК не купили
- NOT: аванс внесён (only prepared); задаток ≠ аванс по цессии; secondary market / ЕГРН plot

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Почти внесли задаток на торгах — квартиру подарили дочери» (B03 — other plot)
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — other plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН, пожилой по телефону, открытая кухня, перенос сдачи/эскроу, поддельное согласие супруги, маткапитал/эскроу, смена юрлица, кладовка, ставка перед ДДУ, apartamenty в выписке.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, Klyshin rhythm, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («за сутки», «за 24 часа»)
- Clear subject: переуступка / новостройка / квартира
- One variant only
- No SEO tail, no label head

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-soglasovali-pereustupku-za-sutki-do-avansa-kvartiru-prodali-drugomu",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
