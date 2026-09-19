# Description inputs — B29 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B29

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку

**subject:** Обещанная скидка 4% на новостройку, которую не включили в проект ДДУ

**angle:** В составном тюменском кейсе обещанную в переписке скидку противопоставляем полной цене в проекте ДДУ. Следствие конкретное: семья остановила сделку до подписания и открытия эскроу.

**comment_magnet_angle:** Застройщик должен выполнить обещание скидки в переписке — или покупатель вправе рассчитывать только на цену, указанную в ДДУ?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья остановила покупку новостройки: обещанную скидку 4% не включили в проект ДДУ, а подписать предложили полную цену. Подтверждение менеджера было в переписке, и покупатели уже пересчитали под него семейный бюджет и ипотеку. Квартиру выбрали, стоимость обсудили — оставалось увидеть договорённость на бумаге. Но вечером, когда открыли присланный документ, цифры не сошлись. До планового открытия эскроу оставалось примерно три дня, и вместо подготовки к расчётам пришлось выяснять, почему подписывать нужно одно, а рассчитывать предлагают на другое.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Напишите в Telegram — подключусь до аванса и разберу проект ДДУ до эскроу. Связь также в MAX.

## Case hook (from research / article)
- Тюмень, новостройка по ДДУ, ипотека, эскроу, семья
- Менеджер подтвердил скидку 4% в CRM-чате и мессенджере на выбранную квартиру
- Бюджет и ипотеку пересчитали под «минус четыре процента»
- За ~3 дня до эскроу прислали проект ДДУ: полная прайсовая цена, пункта о скидке нет
- Предложили: «Подпишите сейчас, скидку оформим потом» — семья отказалась
- ДДУ не подписали, эскроу не открывали; запросили исправленный проект или письменное оформление до подписи
- Масштаб (иллюстрация): 4% от условных 14,5–15,5 млн ≈ 580–620 тыс. ₽ — не ущерб семьи
- Смысл: чат ≠ цена в договоре; 214-ФЗ ст. 5; эскроу не вернёт недостающую скидку
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень», скидка застройщика, проект ДДУ, эскроу, семейная ипотека
- buyer risk: обещание в переписке vs строка цены в ДДУ, «оформим потом»

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, CRM

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B29",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
