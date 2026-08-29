# Title inputs — B13 — 2026-08-29

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B13. verdict: PASS. Max ~70 chars. News headline with finale. Tyumen when it strengthens.

## topic_id
B13

## Scout handoff
- cluster_id: matkapital_missing_child_shares
- klyshin_hook: none (fresh Tyumen casus without Klyshin)
- dzen_casus_shape: PASS
  - event: семья в Тюмени выбрала вторичку, ипотеку одобрили, в ЕГРН только два взрослых собственника
  - risk: квартиру покупали с маткапиталом, детские доли не выделили — сделку могут оспорить
  - time: за два дня до задатка, на финальной юридической проверке
  - finale: юрист нашёл след маткапитала и отсутствие детских долей; сделку развернули до денег; покупатели ушли к другому объекту
- comment_magnet_angle: «Если в выписке только родители, а продавец клянётся, что маткапитала не было — вы верите или уходите?»
- title_draft (rework allowed): Маткапитал потратили, а детям доли не выделили — в Тюмени сделку развернули до денег
- slug: v-tyumeni-matkapital-detskie-doli-ne-vydelili-sdelku-razvernu-li

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «доли маткапитала детей» — 94 (55+11176)
- compare225: 7457
- rework trail: «маткапитал доли детей» 94 → «выделить доли детям маткапитал» 16
- buyer spine: детские доли после маткапитала, выписка ЕГРН только родители

## Research — subject & conflict
- Subject: вторичка Тюмень, маткапитал при первой покупке, детские доли не зарегистрированы
- Reader problem: в ЕГРН только родители — выглядит чисто, но выписка не показывает историю маткапитала
- Casus: моделируемый тюменский кейс (август 2026), без выдуманных имён/адресов/судов
- Finale: остановили до задатка и передачи денег; покупатели выбрали другой объект
- Distinct from matkapital_opieka_kids_cancel_3y (опека, отмена через 3 года) — здесь доли никогда не выделили

## Anti-dup published titles
B02–B12 published. Avoid: наследство, открытая кухня, пожилой по телефону, ипотека+ЕГРН обременение, новостройка эскроу, доверенность СВО, скидка 2 млн, автооценка, ЗАГС умершая жена.

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора

## Required JSON output
```json
{
  "topic_id": "B13",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "comment_magnet_angle": "…",
  "verdict": "PASS"
}
```
