# Description inputs — B27 — 2026-09-18

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no explanation, no BLOCKER. Derouter API is live; your job is to write the teaser text. verdict: PASS.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** В Тюмени БТИ «съело» 4,2 кв.м ДДУ — в перерасчёте отказали

**subject:** Расхождение площади БТИ и ДДУ в новостройке

**angle:** На выдаче ключей площадь квартиры оказалась на 4,2 кв.м меньше, но застройщик отказал в перерасчёте.

**comment_magnet_angle:** Вы бы подписали акт ради ключей или заблокировали регистрацию, пока застройщик не пересчитает цену?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В Тюмени семья обнаружила в новостройке минус 4,2 кв. м: в ДДУ было 68,4, а в техпаспорте БТИ на выдаче ключей — 64,2. Представитель застройщика уже ждал подписи передаточного акта, а банк напоминал о сроке регистрации права по ипотеке. До оформления оставалось два часа, но покупатели решили сначала понять, куда исчезли метры и должен ли измениться расчёт по квартире. На столе лежали ДДУ и документы БТИ, и спор быстро перестал быть разговором о «небольшой погрешности».

**Para 2 (early CTA):** Я разбираю такие ситуации в Telegram и MAX — без рекламного тумана, на языке обычной сделки и документов. Подписывайтесь, если принимаете новостройку в Тюмени или только готовитесь к ключам.

## Case hook (from research / article)
- Тюмень, новостройка, семья, выдача ключей
- В ДДУ проектная площадь 68,4 кв.м; техпаспорт БТИ на приёмке — 64,2 кв.м (−4,2 кв.м, ~6,1%)
- Застройщик: «в пределах закона», перерасчёт не нужен; ссылка на 214-ФЗ
- Полная цена уже на эскроу по старой площади; деньги не пересчитываются сами
- Давление: банк напомнил о сроке регистрации права по ипотеке; до подписания акта ~2 часа
- Семья не подписала акт, ключи не получила; спор ушёл в претензию и независимый обмер
- «До пяти процентов ничего не возвращаем» — не универсально; нужно читать свой пункт ДДУ
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «приемка квартиры в новостройке тюмень» 35 (регион 55+11176)
- «площадь квартиры по бти» / «перерасчет площади дду» — buyer risk
- buyer risk: БТИ vs ДДУ, перерасчёт, эскроу, передаточный акт, ипотека

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, БТИ, 214-ФЗ

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

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
