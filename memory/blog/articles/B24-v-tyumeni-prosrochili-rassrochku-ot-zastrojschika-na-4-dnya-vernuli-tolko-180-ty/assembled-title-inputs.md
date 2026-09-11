# Title inputs — B24 — 2026-09-11

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-prosrochili-rassrochku-ot-zastrojschika-na-4-dnya-vernuli-tolko-180-ty`

## Scout handoff
- cluster_id: installment_penalty_developer
- klyshin_hook: none (fresh Tyumen newbuild installment casus without Klyshin)
- top_energy_mirror: clock_ran_out — срок платежа истёк раньше перевода, объект и деньги ушли за четыре дня
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала квартиру в новостройке и подписала договор рассрочки с застройщиком вместо ипотеки
  - risk: жёсткий срок платежа, штрафные последствия и расторжение при просрочке даже на несколько дней; проверить маршрут денег, удержания, возврат, судьбу квартиры
  - time: просрочка одного очередного платежа — четыре дня после первого взноса 400 тыс. ₽
  - finale: застройщик расторг договор, вернул 180 тыс. из 400 тыс., квартиру получил другой покупатель; потеря 220 тыс. и объекта
- comment_magnet_angle: «Рассрочка от застройщика без ипотеки — свобода и экономия или ловушка, где один пропущенный платёж стоит квартиры и сотен тысяч? Вы бы рискнули ради скидки?»
- title_draft (rework allowed): В Тюмени просрочили рассрочку от застройщика на 4 дня — вернули только 180 тысяч из 400
- story_dup_check: PASS — distinct from B22 mortgage rate before DDU, B19 matkapital/escrow, B12 handover delay, B21 storage, rent-before-DDU clusters
- h1_fingerprint: installment_developer_4days_partial_refund_180of400
- newbuild_mechanism: рассрочка от застройщика при покупке квартиры в новостройке (не банковская ипотека, не бронь, не уступка, не вторичка)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «рассрочка от застройщика тюмень» — 137 (55+11176; RU225: 217)
- support: «квартира в рассрочку от застройщика тюмень» — 64
- context spine: «новостройки тюмень» — 4583

## Research — subject & conflict (from handoff + SERP 2026-09-11)
- Subject: новостройка в Тюмени, рассрочка напрямую у застройщика вместо ипотеки, первый взнос 400 тыс. ₽, просрочка очередного платежа на 4 дня
- Reader problem: покупатель считает рассрочку «ипотекой без банка» — меньше бумаг и переплаты; не читает график, момент исполнения обязательства, формулу удержания при расторжении
- Casus: семья внесла 400 тыс., задержала платёж на 4 дня; застройщик применил штрафной сценарий и расторжение; вернули 180 тыс.; квартиру продали другому; утрата 220 тыс. и объекта
- Legal frame (Writer): юридическая конструкция может быть ДДУ с графиком рассрочки, отдельный договор рассрочки или иной документ — не называть всё «ДДУ» без подтверждения; 214-ФЗ и эскроу применимы не ко всем платежам автоматически
- SERP context: в Тюмени рассрочки от застройщика сокращаются; эксперты предупреждают проверять график, штрафы, полную цену; похожие сюжеты о потере скидки/расторжении при задержке платежа на несколько дней
- Voice angle: разрыв между «без банка — проще» и договорным правом застройщика расторгнуть и удержать часть взноса за считанные дни просрочки
- Finale: расторжение → частичный возврат → квартира ушла другому покупателю
- Distinct from B22 (банк меняет ставку перед ДДУ), B19 (эскроу/маткапитал), B12 (перенос сдачи), B21 (кладовка), бронь-кластеры

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«В Тюмени банк поднял ставку ипотеки перед ДДУ — бронь сгорела» (B22 — другой plot)
«В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), квартира vs апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (draft may be trimmed)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («на 4 дня», «за 4 дня»)
- Clear subject: рассрочка от застройщика / новостройка
- One variant only
- Numbers 180/400 or 220 acceptable if they fit rhythm

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-prosrochili-rassrochku-ot-zastrojschika-na-4-dnya-vernuli-tolko-180-ty",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
