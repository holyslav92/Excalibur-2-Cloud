# Description inputs — B33 — 2026-09-25

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B33

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** За 4 дня до ДДУ частичный ввод секции сорвал ипотеку в Тюмени

**subject:** ипотека на новостройку при частичном вводе секции

**angle:** За четыре дня до подписания ДДУ покупатели обнаружили в декларации частичный ввод секции. Банк после этого снял одобрение по ипотеке, и сделку пришлось перестраивать на другую квартиру.

**comment_magnet_angle:** Если в декларации указан частичный ввод, а продавец говорит, что дом уже сдан, подписывать ДДУ ради сохранения брони или ждать полного ввода своей секции?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За четыре дня до подписания ДДУ банк снял предварительное одобрение, и эскроу по выбранной квартире не открыли. Бронь была оплачена, ипотека предварительно согласована, а в офисе застройщика семье говорили: «дом сдаётся, ключи скоро». Вечером перед визитом в банк покупатели открыли проектную декларацию на наш.дом.рф и увидели частичный ввод: секция с их квартирой ещё не была принята. Для ипотеки этого оказалось недостаточно.

**Para 2 (early CTA):** Святослав Шакин, The Риэлтор, Тюмень. Рассказываю, где обычный покупатель видит «дом почти готов», а специалист проверяет корпус, секцию и объект залога.

## Case hook (from research / article)
- Тюмень, многосекционная новостройка, ипотека предварительно одобрена, бронь оплачена
- В офисе: «дом сдаётся, ключи скоро» — про весь проект, не про секцию покупателя
- За 4 дня до ДДУ: в проектной декларации частичный ввод — одна секция введена, их секция нет
- Банк снял одобрение, эскроу не открыли; сделку перестроили на другой лот
- Механика: банк смотрит объект залога по конкретной секции, не на рекламную фразу
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- новостройки, ДДУ, ипотека, проектная декларация, частичный ввод, эскроу, банк, Тюмень

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, банк, наш.дом.рф

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
