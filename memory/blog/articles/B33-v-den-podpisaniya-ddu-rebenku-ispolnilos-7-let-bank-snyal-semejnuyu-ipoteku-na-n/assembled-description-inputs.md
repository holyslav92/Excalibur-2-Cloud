# Description inputs — B33 — 2026-09-23

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени ребёнку исполнилось 7 в день подписания ДДУ — семейная ипотека под угрозой

**subject:** Семейная ипотека на новостройку в Тюмени при семилетии ребёнка в день подписания ДДУ

**angle:** Составной кейс: семья получила одобрение, но на финале банк пересматривает право на льготу. Возраст учитывают на дату кредитного договора — день рождения в дату ДДУ сам по себе не означает потерю льготы. Семья останавливает подписание; бронь 150–250 тыс. ₽ под риском.

**comment_magnet_angle:** Кто должен заранее заметить возрастную границу — семья или банк, уже одобривший ипотеку? И на ком должен оставаться риск потери брони?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Бронь на 150–250 тыс. ₽ уже оплачена, а в день планового подписания ДДУ ребёнку исполняется семь — семейная ипотека в тюменской новостройке может перестать сходиться по ставке и первоначальному взносу. Семья видит в предварительном одобрении льготную ставку, взнос от 20% и привычный платёж, но это ещё не финальное подтверждение кредита. Для семьи с одним ребёнком возраст проверяют на дату заключения кредитного договора. Поэтому день рождения в день сделки не означает автоматическую потерю льготы, однако финальная банковская проверка способна остановить привычный сценарий.

**Para 2 (early CTA):** Такие сделки я разбираю по датам и документам — в Telegram и MAX.

## Case hook (from research / article)
- Тюмень, новостройка по ДДУ, семейная ипотека
- Предварительное одобрение + оплаченная бронь 150–250 тыс. ₽
- Плановый день ДДУ совпал с седьмым днём рождения ребёнка
- Банк на финале не подтвердил право на семейную программу (возраст на дату кредитного договора)
- Ставка/ПВ пересчитаны; ДДУ и эскроу остановили до письменного подтверждения
- Три даты нельзя путать: день рождения, кредитный договор, подписание ДДУ
- Отличие от B22/B29/B31: не ставка накануне и не страховка — возрастная граница 6/7 лет
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «семейная ипотека возраст детей» 2758; «семейная ипотека новостройка тюмень» 10
- buyer risk: предварительное одобрение ≠ кредитный договор, бронь vs эскроу, возраст ребёнка

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, банк, семейная ипотека

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B33",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
