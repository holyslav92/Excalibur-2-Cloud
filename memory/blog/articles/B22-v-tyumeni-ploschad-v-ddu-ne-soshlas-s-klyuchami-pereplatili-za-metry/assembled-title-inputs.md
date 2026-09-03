# Title inputs — B22 — 2026-09-03

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B22. verdict: PASS.

## topic_id
B22

## slug (confirm or note if h1 implies different slug)
`v-tyumeni-ploshchad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry`

## Scout handoff
- cluster_id: newbuild_ddu_area_mismatch_overpay_tyumen
- klyshin_hook: none (original Tyumen newbuild casus)
- dzen_casus_shape: PASS
  - event: семья в Тюмени купила квартиру в новостройке по ДДУ; цена привязана к площади в договоре
  - risk: при приёмке обмеры показали меньшую площадь, чем в ДДУ — возможна переплата сотни тысяч рублей
  - time: на приёмке квартиры, за две недели до подписания акта передачи
  - finale: застройщик отказал в перерасчёте или предложил символическую скидку; семья не подписала акт либо подписала под давлением срока ипотеки — потеряли деньги или отложили регистрацию
- comment_magnet_angle: «Площадь в ДДУ совпала с ключами — вы вообще сверяете метры до акта или верите цифрам в договоре?»
- title_draft (rework allowed): В Тюмени площадь в ДДУ не сошлась с ключами — переплатили за метры
- story_dup_check: PASS
- distinct_plot: не кладовка по ДДУ (B21), не смена юрлица/эскроу (B20), не маткапитал/семейная ипотека (B19), не перенос сдачи/заморозка эскроу (B12); стоп на расхождении площади в ДДУ и фактических обмерах при передаче квартиры

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить новостройку в тюмени» — 857 (55+11176)
- support: «новостройки тюмень купить от застройщика» — 528
- on-plot secondary: «приемка квартиры в новостройке тюмень» — 35
- weak: «площадь квартиры дду» — 11
- weak: «площадь квартиры новостройка» — 7 (Tyumen)
- RU context: «если площадь квартиры в новостройке меньше» — 12; «замер площади квартиры в новостройке» — 17

## Research — subject & conflict
- Subject: новостройка в Тюмени, ДДУ, расхождение проектной площади в договоре и итоговой площади при передаче квартиры
- Reader problem: семья почти получает ключи, но перед актом обнаруживает, что оплаченная по ДДУ площадь больше фактической; менеджер ссылается на допустимое отклонение и торопит с подписью из-за ипотеки и регистрации
- Casus: собирательный редакционный тюменский сюжет (без имён, ЖК, банка, точных сумм); ориентир 52–56 м², уменьшение ~1,5–3 м²
- Surprising fact: подписанный акт сам по себе не обрывает спор о площади (позиция ВС РФ № 5-КГ23-18-К2)
- Voice angle: конфликт не в рулетке, а в моменте подписи — цифра из ДДУ кажется окончательной, но к ключам нужно сопоставить несколько видов площади и пункт о перерасчёте
- Fresh signal (NOT the family case): 03.09.2026 tenant channels — приёмка новостроек, сверка ДДУ до подписи
- Finale: застройщик ссылается на договорный порог / предлагает неденежную компенсацию / отказывает в перерасчёте; семья перед выбором — подписать под давлением сроков или зафиксировать спор
- Distinct from B21 (кладовка по ДДУ на ключах), B12 (перенос сдачи, деньги на эскроу), B20 (смена юрлица), B19 (маткапитал блокирует эскроу)

## Champion energy (formula, do NOT copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»
«Ипотеку одобрили, а регистрацию отменили через полгода: в выписке висела одна строка»
«В Тюмени застройщик сменил юрлицо — банк не открыл эскроу» (B20 — другой plot)
«V tyumeni oplatili kladovku po ddu na klyuchah pomescheniya ne bylo» (B21 — кладовка, не площадь квартиры)

## Anti-dup published titles
B02–B15, B19–B21 published. Avoid angles: расписка, задаток/торги, доверенность, скидка, автооценка, наследство, ЗАГС/умершая жена, ипотека+ЕГРН (B09), пожилой по телефону, открытая кухня, перенос сдачи/эскроу заморозили (B12), поддельное согласие супруги (B15), маткапитал/семейная ипотека+эскроу (B19), смена юрлица застройщика (B20), кладовка по ДДУ (B21).

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Constraints
- Max ~50–70 chars
- News headline energy, casus arc, Tyumen when relevant
- Strong verb, active voice, temporal marker when it helps («на приёмке», «перед актом», «за две недели до ключей»)
- One variant only
- Include slug confirmation in angle or separate field if needed

## Required JSON output
```json
{
  "topic_id": "B22",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "slug": "v-tyumeni-ploshchad-v-ddu-ne-soshlas-s-klyuchami-pereplatili-za-metry",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
