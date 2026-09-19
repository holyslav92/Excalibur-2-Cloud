# Description inputs — B28 — 2026-09-19

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B28

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного

**subject:** Дом от застройщика в КП под Тюменью: потолки ниже указанной в ДДУ высоты на 25 см.

**angle:** Обещанная высота потолков столкнулась с замером на сдаче, покупатели отказались подписывать акт. Заголовок раскрывает предмет спора и последствие, не повторяя сюжеты об отделке или земле.

**comment_magnet_angle:** Согласились бы вы принять дом с потолками на 25 см ниже договорных за скидку 80 тысяч рублей — или отказались бы от сделки?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** В день передачи дома в КП под Тюменью потолки оказались на 25 см ниже обещанного — семья с двумя детьми остановила приёмку перед подписью акта. Покупатели приехали за новым домом от застройщика, а получили вопрос, который скидкой с порога не закрыть. В приложении к договору была указана одна высота, на дисплее лазерного дальномера — другая. Передаточный акт лежал на столе, но подписывать его, пока расхождение не объяснили, семья не стала. Сначала нужно было понять, что им передают: дом по договору или дом, к которому теперь предлагают привыкнуть.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Разбираю покупку домов от застройщиков так, чтобы за красивым показом были видны условия сделки. Мои разборы — в Telegram и MAX.

## Case hook (from research / article)
- Тюмень и пригород, коттеджный посёлок, индивидуальный дом по ДДУ
- В приложении к ДДУ — высота потолков 2,7 м; лазер на сдаче — 2,45 м в гостиной и спальнях (минус 25 см)
- Представитель: «конструктивный допуск»; предложение — 80 000 ₽ скидки за немедленную подпись акта
- Семья не подписала акт, ключи не взяла; финальный транш на эскроу не перевели
- Через 9 дней вернули задаток 250 000 ₽
- Моделируемый composite кейс; не называть КП, застройщика, банк
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «приемка дома от застройщика» / новостройка / ДДУ / коттеджный посёлок
- buyer risk: высота в приложении, замер до акта, скидка vs договорное условие

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, КП

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B28",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
