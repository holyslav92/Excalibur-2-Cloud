# Description inputs — B13 — 2026-08-29

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only. verdict: PASS.

## topic_id
B13

## H1
Аккредитив открыли, сделку зарегистрировали — продавец без денег

## Case hook
- Тюмень, вторичка, безотзывный аккредитив открыт
- Росреестр зарегистрировал право покупателя
- Банк отказал в раскрытии: описание объекта в ДКП и заявлении не совпало
- Продавец без денег, покупатель уже собственник
- comment magnet: открытый аккредитив = выплата?

## Rules
≠ title, ≠ truncated lead, news energy, no checklist

## JSON output
{"topic_id":"B13","verdict":"PASS","description":"...","description_chars":N}
