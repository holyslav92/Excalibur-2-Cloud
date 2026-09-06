# Title inputs — B24 — 2026-09-06

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B24. verdict: PASS. **Keep aligned with scout title draft** — refine rhythm only if needed, do not change the plot.

## topic_id
B24

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-semyam-vtoroj-ddu-ostanovili`

## Scout handoff
- cluster_id: `newbuild_double_sale_same_unit_tyumen`
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: Семья в Тюмени выбрала квартиру в строящемся ЖК, оформила бронь и подписала ДДУ. Через несколько дней менеджер застройщика связывается со второй семьёй, которой показали и забронировали тот же номер квартиры.
  - risk: Двойная продажа одного лота. У второй семьи уже одобрена ипотека и переведён аванс; у первой семьи ДДУ зарегистрирован или проходит регистрацию. Застройщик объясняет конфликт «ошибкой CRM» либо изменением планировки.
  - time: Конфликт вскрывается за 48–72 часа до подписания второго ДДУ и до внесения остатка средств на эскроу.
  - finale: Банк второй семьи останавливает сделку. Первая семья подаёт документы в Росреестр. Застройщик предлагает второй семье «аналогичную» квартиру этажом выше, но с доплатой; семья отказывается, получает бронь обратно не в полном объёме и начинает досудебный спор.
- comment_magnet_angle: «Если после двойной продажи менеджер предлагает "точно такую же, но этажом выше" и просит доплатить — вы соглашаетесь или требуете именно номер квартиры, который был в брони и ДДУ?»
- title_draft (scout — keep this plot): **В Тюмени застройщик продал одну квартиру двум семьям — второй ДДУ остановили**
- story_dup_check: PASS
- distinct_plot: две семьи на **один лот** в новостройке, конфликт брони/ДДУ/учёта застройщика, остановленный второй ДДУ. Не вторичка, не переуступка (B09/B22), не смена юрлица (B20), не апартаменты (B23), не кладовка (B21), не ставка (B22), не эскроу-маткапитал (B19).

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «новостройки тюмень» — 3657 (55) / 8691 (225)
- support: «купить новостройку в тюмени» — 651 (55)
- support: «договор долевого участия» — 274 (related)
- context: «ДДУ новостройка» — 14 (55); «эскроу застройщик» — 68 (55)
- low/niche: «бронь новостройка» — 3 (55); «двойная продажа квартира» too niche — demand spine stays broad «новостройки тюмень»

## Research — subject & conflict
- Subject: новостройка в Тюмени, застройщик продал один лот двум семьям, конфликт брони/ДДУ/CRM vs госрегистрация, второй ДДУ остановлен
- Reader problem: покупатель оставил деньги за бронь, получил одобрение ипотеки — но перед подписанием ДДУ выясняет, что тот же номер квартиры уже ушёл другой семье
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, сумм)
- Surprising fact: если первый ДДУ уже зарегистрирован, Росреестр не зарегистрирует второй на тот же лот — конфликт всплывает до эскроу у второго покупателя
- Voice angle: «Два "да" в CRM — не два ДДУ в реестре»; драма в разрыве между отделом продаж и регистрацией
- Finale: банк останавливает вторую сделку; застройщик предлагает «аналог» с доплатой; неполный возврат брони; досудебная претензия
- Distinct from B20 (смена юрлица), B12 (перенос сдачи), B19 (маткапитал/эскроу), B22 (ставка ипотеки), B09 (ЕГРН вторичка)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию» (B09 — другой plot)
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B23 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи (B12), поддельное согласие (B15), маткапитал+эскроу (B19), смена юрлица (B20), кладовка (B21), ставка перед ДДУ (B22), апартаменты в ДДУ (B23).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026, SEO tails, label heads

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за 48 часов», «перед ДДУ»)
- One variant only
- **Prefer scout title_draft** unless a minor rhythm fix improves Klyshin news-casus hook without changing facts

## Required JSON output
```json
{
  "topic_id": "B24",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-zastrojschik-prodal-odnu-kvartiru-dvum-semyam-vtoroj-ddu-ostanovili",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
