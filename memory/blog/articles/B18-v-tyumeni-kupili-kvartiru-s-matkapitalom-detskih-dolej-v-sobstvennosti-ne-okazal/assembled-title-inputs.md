# Title inputs — B18 — 2026-08-30

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B18. verdict: PASS.

## topic_id
B18

## Scout handoff
- cluster_id: matkapital_missing_child_shares
- klyshin_hook: none (fresh Tyumen matkapital child-shares casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала вторичку, продавец подтвердил использование маткапитала при покупке, покупатели запросили документы о выделении долей детям
  - risk: в ЕГРН и пакете документов нет зарегистрированных детских долей — без согласия опеки и выделения долей сделку нельзя провести легально; риск оспаривания и отмены регистрации
  - time: за несколько дней до аванса, после одобрения ипотеки и согласования цены
  - finale: сделку развернули до передачи денег; покупатели ушли искать другой объект; продавец должен выделить доли и пройти опеку (месяцы), покупатели не стали ждать
- comment_magnet_angle: «Если продавец говорит „доли выделены“, но в ЕГРН их нет — вы верите на слово или ждёте свежую выписку до аванса?»
- title_draft (rework allowed): В Тюмени купили квартиру с маткапиталом — детских долей в собственности не оказалось
- story_dup_check: PASS — distinct from matkapital_opieka_kids_cancel_3y (опека молчала 3 года / дети оспорили)

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0 final: «продажа квартиры с материнским капиталом» — 43 (55+11176); compare RU225 4752
- rework log: «маткапитал детские доли» 6; «маткапитал при покупке квартиры» 22; «доля ребенка в квартире по материнскому капиталу» 77
- buyer spine: проверка квартиры с маткапиталом при покупке; продажа квартиры с материнским капиталом

## Research — subject & conflict (research_start; research-notes pending)
- Subject: вторичка Тюмень, продавец использовал маткапитал, покупатели проверяют детские доли в ЕГРН
- Reader problem: продавец говорит «доли выделены», но в выписке их нет — сделка юридически под угрозой
- Casus: моделируемый тюменский кейс (август 2026), без выдуманных имён/адресов
- Finale: сделку остановили ДО аванса — покупатели не внесли деньги, ушли к другому объекту
- Distinct from: matkapital_opieka 3y plot (дети оспорили через 3 года); B15 seller mortgage lien; B17 registered persons

## Anti-dup published titles
B02–B14 published (+ B15–B17 live 30 Aug). Avoid: наследство, банкротство, доверенность СВО, пожилой по телефону, ПНД, повестка, открытая кухня B11, seller mortgage B15, communal share B16, registered persons B17.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора, 2026

## Champion energy (formula, do not copy verbatim)
«Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял»

## Required JSON output
```json
{
  "topic_id": "B18",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
