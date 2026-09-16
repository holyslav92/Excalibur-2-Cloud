# Description inputs — B27 — 2026-09-16

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier, gpt-6-astra). Output **JSON only** per schema below. No BLOCKER refusals. The `description` field MUST contain the teaser text (non-null string).

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени банк отказал созаёмщику по семейной ипотеке за 4 дня до эскроу

**subject:** Семейная ипотека в новостройке: отказ банка созаёмщику перед эскроу

**angle:** Предварительное одобрение на двоих не гарантировало сделку: финальный отказ созаёмщику остановил оформление, и квартира ушла другому покупателю.

**comment_magnet_angle:** Пытаться ли срочно искать другого созаёмщика или безопаснее отказаться от сделки, пока деньги не ушли на эскроу?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени банк отказал жене-созаёмщику за 4 дня до открытия эскроу — покупка новостройки остановилась, хотя квартиру уже забронировали. Предварительное одобрение семья получила на двоих: муж — основной заёмщик, жена — созаёмщик. За кухонным столом считали будущий платёж и готовились к подписанию, а после звонка менеджера пришлось разбираться, дадут ли вообще нужную сумму. До конца брони оставалось шесть дней, дохода мужа для выбранной квартиры не хватало. Слова «ипотеку одобрили» уже прозвучали, но окончательную проверку прошли ещё не все.

**Para 2 (CTA block skipped):** early TG+MAX CTA — not part of lead for gate purposes.

**Para 3 (first body after H2):** Квартиру выбрали, предварительное решение получили, бронь оформили. Дальше собирали документы к договору участия в долевом строительстве — ДДУ — и открытию счёта эскроу. Для покупателя это уже похоже на подготовку к покупке, а не на ожидание ответа банка: осталось собрать бумаги, согласовать время и приехать на подпись.

## Case hook (from research / article)
- Тюмень, новостройка, семейная ипотека: муж — заёмщик, жена — созаёмщик
- «Одобрили на двоих» ≠ окончательное решение по каждому участнику
- За 4 дня до эскроу банк отклонил жену-созаёмщика; без её дохода лимита не хватило
- С февраля 2026 супругов нельзя «выключить» из семейной ипотеки ради обхода
- Родителя как третьего созаёмщика тоже не пропустили; бронь сняли без штрафа (по письму)
- Через 11 дней квартира ушла другому покупателю
- Семья не подписала ДДУ, деньги на эскроу не перечисляли — остановка до потери денег
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «семейная ипотека тюмень» 1240; «созаемщик ипотека» 515; «купить новостройку в тюмени» 902
- Buyer risk: предварительное одобрение, созаёмщик, бронь, эскроу, лимит без второго дохода

## Anti-dup neighbors (do NOT echo their teaser energy)
- B19: маткапитал блокирует эскроу — не «эскроу сорвался»
- B22: банк поднял ставку перед ДДУ — не «бронь сгорела»
- This plot: **финальный отказ созаёмщику**, нельзя убрать супруга, лимит не сходится

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1 («В Тюмени банк отказал…»)
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler, no how-to blurb
6. Cyrillic; brands OK: ДДУ, эскроу

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- B19 teaser: «В Тюмени семья уже выбрала квартиру, а банк на финальной проверке увидел старый маткапитал без детских долей. Бронь сгорела, зато эскроу не успели пополнить.»

## Required JSON output
```json
{
  "topic_id": "B27",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
