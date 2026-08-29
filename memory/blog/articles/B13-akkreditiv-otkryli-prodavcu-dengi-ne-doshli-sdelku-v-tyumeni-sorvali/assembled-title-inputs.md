# Title inputs — B13 — 2026-08-29

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Invent ONE H1/title for topic B13. verdict: PASS.

## topic_id
B13

## Scout handoff
- cluster_id: letter_of_credit_seller_no_money_tyumen
- klyshin_hook: none
- dzen_casus_shape: PASS
  - event: семья в Тюмени, безотзывный аккредитив открыт, стороны на регистрации в МФЦ
  - risk: банк не раскрыл аккредитив — расхождение ДКП/реквизитов/описания объекта; продавец без денег
  - time: в день подачи на регистрацию
  - finale: сделку развернули, аккредитив закрыли без выплаты, покупатели потеряли недели и комиссию
- comment_magnet_angle: «Если банк уже открыл аккредитив — вы считаете, что деньги „на месте“, или ждёте раскрытия после регистрации?»
- title_draft: Аккредитив открыли — продавцу деньги не дошли, сделку в Тюмени сорвали
- story_dup_check: PASS

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «аккредитив при покупке квартиры» — 44 (55+11176), RU225 3799
- secondary: «аккредитив в банке при покупке квартиры» — 11
- context: «купить квартиру в тюменi» — 22699

## Research — subject & conflict
- Subject: вторичка Тюмень, безотзывный аккредитив, регистрация прошла, раскрытие не прошло
- Reader problem: «аккредитив открыт = продавец получил деньги?»
- Casus: моделируемый тюменский кейс (август 2026), без выдуманных имён/адресов
- Surprising fact: регистрация в Росреестре может пройти, а деньги продавцу — нет
- Distinct from B12 (эскроу/ДДУ), B09 (ЕГРН строка), B02 (расписка)

## FORBIDDEN H1 hooks
чеклист, N шагов, стоит ли покупать, полный гайд, как купить без риелтора

## Constraints
- News headline energy, Tyumen when it helps
- Clear subject (аккредитив / сделка / продавец)
- max 70 chars preferred
- No SEO tail, no year

## Output JSON schema
```json
{
  "topic_id": "B13",
  "verdict": "PASS",
  "title": "...",
  "title_ru": "...",
  "hook_energy": "...",
  "comment_magnet_seed": "...",
  "forbidden_markers_checked": true
}
```
