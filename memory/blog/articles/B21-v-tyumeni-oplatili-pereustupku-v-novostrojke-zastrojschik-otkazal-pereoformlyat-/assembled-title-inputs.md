# Title inputs — B21 — 2026-09-02

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B21. verdict: PASS.

## topic_id
B21

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-`

## Scout handoff
- cluster_id: newbuild_assignment_developer_refused_dd_reregistration_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в строящемся ЖК по переуступке — подписала договор с продавцом уступки, внесла аванс и пошла к застройщику переоформлять ДДУ
  - risk: застройщик отказал регистрировать нового дольщика — уступка не согласована или не выполнены требования застройщика/банка; в реестре остался прежний участник, деньги у цедента
  - time: за два дня до визита в банк на эскроу
  - finale: сделку остановили до открытия эскроу, бронь сняли, аванс возвращали через претензию к продавцу уступки; квартира ушла в свободную продажу
- comment_magnet_angle: «Переуступку в новостройке оплачиваете до согласия застройщика — или сначала требуете письмо из офиса продаж, что уступку зарегистрируют?»
- title_draft (rework allowed): В Тюмени оплатили переуступку в новостройке — застройщик отказал переоформлять ДДУ
- story_dup_check: PASS
- distinct_plot: не B12 (перенос сдачи / эскроу после внесения), не B19 (маткапитал / семейная ипотека), не B20 (смена юрлица застройщика), не вторичка; стоп на этапе переуступки до регистрации цессии и до эскроу

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 874 (55+11176; compare RU225 1882)
- support: «купить новостройку в тюмени от застройщика» — 413
- support: «купить новостройку в тюмени в ипотеку» — 93
- context: «переуступка новостройки» — 10 (Tyumen), 2422 (RU225)
- low: «покупка квартиры в новостройке переуступка» — 4; «риски переуступки новостройки» — 2

## Research — subject & conflict
- Subject: переуступка права по ДДУ в новостройке Тюмени — оплата цеденту vs регистрация нового дольщика у застройщика
- Reader problem: покупатель передаёт аванс продавцу уступки, считая что «уже купил», но до госрегистрации цессии не стал новым участником ДДУ; застройщик может отказать в переоформлении
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, сумм)
- Surprising fact (Dvizhenie 31.08.2026): в их выборке переуступка в Тюмени ~на 5% дороже прямого ДДУ — не «скидка»
- Voice angle: разрыв между «подписали с продавцом» и «стали дольщиком» — одна регистрация в Росреестре; офис продаж — отдельный фильтр
- Finale: стоп до эскроу → бронь сняли → аванс через претензию к цеденту → квартира ушла в продажу
- Distinct from B12 (сдвиг сдачи, деньги на эскроу), B19 (маткапитал), B20 (смена юрлица), B09 (ЕГРН после одобрения)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)

## Anti-dup published titles
B02–B15, B19, B20 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу (B12), поддельное согласие супруги (B15), маткапитал (B19), смена юрлица (B20).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («за два дня до эскроу», «до открытия эскроу»)
- One variant only
- Do NOT paste Wordstat P0 «купить новостройку в тюмени» verbatim into H1

## Required JSON output
```json
{
  "topic_id": "B21",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-oplatili-pereustupku-v-novostrojke-zastrojschik-otkazal-pereoformlyat-",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
