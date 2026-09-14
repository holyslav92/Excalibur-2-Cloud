# Title inputs — B27 — 2026-09-14

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B27. verdict: PASS.

## topic_id
B27

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-matkapital-na-novostrojku-zavis-nakanune-eskrou-rebenku-ispolnilos-7-l`

## Scout handoff
- cluster_id: newbuild_matkapital_child_age_limit_before_escrow_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- top_energy_mirror: clock_ran_out — семья считала, что маткапитал уже одобрен и успеет в сделку, но возрастной порог ребёнка пересёкся с окном брони и подписания ДДУ
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала двушку в новостройке, получила одобрение по семейной ипотеке и подала заявление на распоряжение маткапиталом для оплаты по ДДУ через эскроу
  - risk: без действующего распоряжения СФР банк не открывает эскроу и не подписывает ДДУ на условиях расчёта с маткапиталом; сделка остаётся без полного источника первоначального взноса
  - time: за 9 дней до запланированного подписания ДДУ и открытия эскроу ребёнку исполнилось 7 лет; день рождения попал в действующее окно брони
  - finale: банк прислал предупреждение и отказался выдавать кредит без полного пакета с маткапиталом. Застройщик дал пять дней на замену программы. Семья остановила ДДУ, пересчитала кредит без маткапитала — ежемесячный платёж вырос на 18 тыс. рублей. Через три дня бронь сняли, деньги на эскроу не ушли
- comment_magnet_angle: «Ребёнку исполнилось 7 лет за неделю до эскроу, а менеджер говорил: "Маткапитал успеем". Вы бы подписали ДДУ без сертификата, если банк уже прислал предупреждение, или снимали бронь и пересчитывали ипотеку?»
- title_draft (rework allowed): В Тюмени маткапитал на новостройку завис накануне эскроу — ребёнку исполнилось 7 лет, ДДУ сорвали
- story_dup_check: PASS
- distinct_plot: не B18 (вторичка, доли), не B19 (эскроу не открыли из-за прошлого маткапитала/детских долей), не B22 (ставка перед ДДУ), не двойная бронь / площадь / downgrade планировки

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «семейная ипотека тюмень» — 1227 (55+11176), RU225: 1740
- support: «семейная ипотека» — 9962
- support: «новостройки тюмень» — 8390
- support: «материнский капитал на покупку жилья» — 72
- low: «материнский капитал новостройка» — 11; «маткапитал новостройка тюмень» — 3

## Research — subject & conflict
- Subject: семейная ипотека на новостройку в Тюмени, маткапитал в первоначальном взносе, ребёнку исполнилось 7 лет до кредитного договора
- Reader problem: семья считает, что предварительное одобрение, бронь и поданное заявление на маткапитал уже гарантируют покупку — но ребёнок достигает 7 лет между одобрением и подписанием кредитного договора
- Casus: редакционный собирательный тюменский сюжет (без имён, ЖК, банка)
- Critical fact: возраст ребёнка проверяется на дату **кредитного договора**, не на дату одобрения или брони; при одном ребёнке 7+ лет основания для семейной ипотеки нет; маткапитал не «пропадает», но льготная схема с ПВ разваливается
- Voice angle: «одобрение» и «маткапитал уже подали» звучат как финал — но банк проверяет возраст в день кредитного договора
- Finale: бронь снята через 3 дня, платёж +18 тыс. ₽/мес без прежней схемы, деньги на эскроу не ушли
- Distinct from B19 «ипотеку одобрили — эскроу сорвал маткапитал» (там прошлый маткапитал/детские доли); здесь — возраст ребёнка 7 лет накануне эскроу, семейная ипотека

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»

## Anti-dup published titles
B02–B26 published. Avoid: расписка, задаток, доверенность, скидка, автооценка, наследство, ЗАГС, «ипотеку одобрили + ЕГРН» (B09), открытая кухня, перенос сдачи (B12), поддельное согласие (B15), «ипотеку одобрили — эскроу сорвал маткапитал» (B19 — другой механизм!), смена юрлица (B20), ставка перед ДДУ (B22), чистовая (B25), РВЭ+транш (B26).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars (title_draft is too long — shorten)
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker («за 9 дней», «накануне эскроу», «перед ДДУ»)
- Do NOT imply «СФР заблокировал маткапитал из-за 7 лет» — correct angle: семейная ипотека/сделка сорвались из-за возраста на дату кредитного договора
- **HARD newbuild gate:** H1 MUST contain at least one of: эскроу, ДДУ, новостройк*, застройщик, ЖК — otherwise `NEWBUILD FOCUS BLOCKER`
- **FAILED anti-dupe:** do NOT use «перед ДДУ» — triggers B22 cluster `mortgage_rate_hike_before_ddu`. Use «накануне эскроу» instead.
- Must differ from published B19 «В Тюмени ипотеку одобрили — эскроу сорвал маткапитал» (other mechanism: child age 7, not past matkapital)
- Preferred PASS titles (use TARGET unless you can beat it on news-casus energy):
  - **TARGET:** «В Тюмени маткапитал завис накануне эскроу — ребёнку исполнилось 7 лет» (69) — matches slug + scout draft, all gates PASS
  - «В Тюмени накануне эскроу ребёнку 7 лет — семейную ипотеку сорвали» (65)
  - «Ребёнку исполнилось 7 лет накануне эскроу — в Тюмени сорвали бронь» (66)
- MUST write «7 лет», never bare «исполнилось 7»
- slug_confirmed: true (slug fixed above)
- One variant only

## Required JSON output
```json
{
  "topic_id": "B27",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-matkapital-na-novostrojku-zavis-nakanune-eskrou-rebenku-ispolnilos-7-l",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
