# Assembled title inputs — B33 (Derouter powerful tier, role title)

**MANDATORY:** You run inside `excalibur_blog_derouter_opus_chat.py --role title` (gpt-6-astra). Output **only** one valid JSON object — no markdown fences, no commentary — matching the schema in skills/title-excalibur-blog/SKILL.md.

**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень  
**topic_market_focus:** newbuild_only  
**research_date:** 2026-09-22

## Scout handoff (klyshin_hook + demand)

- **cluster_id:** `newbuild_declaration_completion_slip_before_ddu_tyumen`
- **klyshin_hook / draft spine:** за 5 дней до подписания ДДУ в свежей проектной декларации (п. 17.2) срок передачи квартиры сдвинули с II квартала 2027 на IV квартал 2027 (два квартала); в брони и черновике ДДУ ещё старый квартал; банк при повторной проверке объекта **урезал сумму/параметры ипотеки** (не ставка как в B22, не страховка как в B31, не нулевой взнос как в B29).
- **final P0 Wordstat (Tyumen demand spine, не вставлять в H1 дословно):** «купить новостройку в тюмени» — 902; «новостройки тюмень» — 8 234 (snapshot Scout).
- **dzen_casus_shape:** PASS
- **comment_magnet_angle (use verbatim in JSON):** «Если декларацию обновили за неделю до ДДУ и срок сдвинули на полгода — вы подписываете проект или снимаете бронь?»
- **anti_dupe_hard:** PASS

## Casus facts (from research-notes.md — for headline only)

- Composite editorial casus; не называть ЖК, банк, застройщика.
- Момент: **до** подписания и регистрации ДДУ, до эскроу.
- Механика: новая редакция декларации **за 5 дней** до планового ДДУ; раздел **17.2** — сдвиг сдачи на **два квартала**; бронь/черновик с устаревшим кварталом; банк меняет одобрение по объекту (урезание ипотеки / новые документы).
- Контраст: «квартал в рекламе» ≠ п. 17.2 свежей декларации.

## Anti-dup (published-titles-only.md — менять угол, не копировать формулы)

- **B27:** декларация, но земля аренда vs собственность (4 дня до ДДУ) — другая механика.
- **B12:** сдвиг сдачи на год **после** сделки/эскроу — не преддоговорный сюжет.
- **B22:** банк поднял **ставку** перед ДДУ.
- **B29:** снял ипотеку без взноса от застройщика за 6 дней.
- **B31:** страховка + снятие одобрения за 2 дня.
- **B28:** декларация КП, газ/даты — не п. 17.2 сдвиг сдачи + ипотека.

## Title constraints

- Один H1 = title; news-casus Klyshin rhythm; ясный subject (новостройка / ДДУ / декларация / ипотека / Тюмень).
- ~50–70 символов если возможно; допустимо чуть длиннее ради уникальной механики (как B31).
- Сильный глагол, временная метка «за 5 дней до ДДУ».
- Запрещено: чеклист, N шагов, «полный гайд», «2026», SEO-хвост, label head.
- Не копировать дословно scout draft H1 — улучшить ритм и отличить от B27/B31.

## HARD elements in h1/title (all required)

1. «за 5 дней до ДДУ»
2. сдвиг срока **сдачи в проектной декларации** (можно «в декларации» + «на два квартала» или эквивалент)
3. банк **урезал ипотеку** (не «снял одобрение» как B31)
4. явно **новостройка** и **Тюмень** (как в B31: «…на новостройку в Тюмени» или «в новостройке Тюмени»)

## Required JSON output

```json
{
  "topic_id": "B33",
  "h1": "...",
  "title": "...",
  "subject": "...",
  "angle": "...",
  "comment_magnet_angle": "...",
  "verdict": "PASS"
}
```

`comment_magnet_angle` — scout angle above (можно слегка отполировать, смысл тот же). `verdict` must be `"PASS"`.
