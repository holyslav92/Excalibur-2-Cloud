# Description inputs — B34 — 2026-10-01

## Task
You ARE the Description writer (Derouter powerful already invoked you). Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Return ONLY the JSON object below — no markdown fences, no commentary, no BLOCKER, no script instructions. The conductor runs gates separately. verdict must be PASS.

## topic_id
B34

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Школа в рекламе ЖК — в декларации 2030, ДДУ не подписали

**subject:** школа в рекламе новостройки, проектная декларация и ДДУ

**angle:** Семья перед подписанием ДДУ сверила обещанную школу с проектной декларацией и увидела срок, который не подходит её планам.

**comment_magnet_angle:** Если школа в проектной декларации заявлена только к 2030 году, вы бы купили квартиру для ребёнка, поверив рекламе «школа рядом»?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** За четырнадцать дней до ДДУ тюменская семья открыла проектную декларацию и увидела: школа, которую им продавали словом «рядом», в документе заявлена только к 2030 году. А их ребёнку в первый класс через три года. Бронь оформлена, подписание стоит в графике, наутро у них визит в банк обсуждать ипотеку. Спорить с красивой картинкой они не стали, а просто положили её рядом с документом по своему дому. Этого хватило, чтобы остановиться до того, как ушли деньги.

**Para 2 (early CTA):** Я Святослав Шакин, The Риэлтор, Тюмень. Разбираю новостройки до подписи, пока ещё можно спокойно сказать «нет». Если вы стоите перед ДДУ и сомневаетесь в обещаниях про школу, садик или дороги, напишите мне в Telegram или MAX. Откроем декларацию вместе.

## Case hook (from research / article)
- Тюмень, новостройка, семья со школьником, бронь, семейная ипотека в графике
- В рекламе и у менеджера: «школа рядом», рендер с детьми; слово «рядом» склеивает три разных календаря
- За 14 дней до ДДУ вечером открыли проектную декларацию на наш.дом.рф по своему дому
- В разделе социнфраструктуры: школа с плановым сроком к 2030 году
- Ребёнку в первый класс через три года — после заселения пойдёт в другую школу, другим маршрутом
- Менеджер: «подпишите ДДУ, это общий план района, школа будет»
- Семья спросила, где школа как обязательство со сроком под их первый класс; на бумаге ответа не нашлось — ДДУ не подписали
- Смысл: ДДУ про квартиру; реклама «рядом» ≠ обязательство к нужному году; проверка декларации до подписи
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «новостройки тюмень» 3553 (Тюменская область)
- проектная декларация, наш.дом.рф, ЕИСЖС, школа, ДДУ, бронь
- buyer risk: «школа рядом» на рендере vs срок в декларации, возраст ребёнка

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, ЖК

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B34",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
