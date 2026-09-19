# Description inputs — B30 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B30

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция

**subject:** шоу-рум и проект ДДУ: смена секции при той же площади и этаже

**angle:** Семья выбрала «солнечную сторону» в шоу-руме, а за пять дней до ДДУ в проекте договора увидела северную секцию с окнами на соседний корпус — отказались подписывать до эскроу.

**comment_magnet_angle:** Если в шоу-руме солнце, а в ДДУ — северная секция за ту же цену, вы бы подписали, чтобы не потерять бронь, или сразу ушли?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За пять дней до подписания ДДУ семья обнаружила в проекте договора северную секцию вместо южной — покупать предлагали квартиру с окнами на соседний корпус, а не во двор. Площадь и этаж совпадали, поэтому на первый взгляд всё было на месте. В шоу-руме запомнились большие окна и солнечный свет, а в заявке на бронь остались слова «солнечная сторона». Теперь на экране ноутбука стояла секция B, и менеджер объяснял разницу спокойно: «Та же цена, просто другой подъезд». Только семья выбирала не подъезд по той же цене, а квартиру, в которой собиралась жить.

**Para 2 (early CTA):** В Telegram разбираю, где в документах на новостройку расходятся обещания и сама покупка. В MAX можно прислать вопрос по конкретному объекту в Тюмени — до того, как договор окажется на подписи.

## Case hook (from research / article)
- Тюмень, новостройка, семья с «солнечной стороной» в брони и шоу-руме
- Шоу-рум: юг, свет, вид во двор; бронь/презентация — «солнечная сторона»
- За 5 дней до ДДУ: проект — та же площадь и этаж, секция B, север, окна на соседний корпус
- Менеджер: «та же цена, просто другой подъезд»
- Семья не подписала ДДУ; часть брони удержали; эскроу не открывали
- Механика: одинаковые метры ≠ та же квартира; показ vs объект в договоре
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 4430; «квартиры с отделкой тюмень» 79
- buyer risk: шоу-рум, бронь, проект ДДУ, секция, эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B30",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
