# Description inputs — B16 — 2026-09-01

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B16

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали

**subject:** Приёмка квартиры в новостройке: мокрая стяжка и другие дефекты

**angle:** Семья отказалась подписывать акт из-за дефектов, зафиксировала нарушения, но осталась без ключей и продолжила платить ипотеку.

**comment_magnet_angle:** Если застройщик обещает всё исправить после подписи — вы подпишете акт или уйдёте без ключей?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Ключи лежали на столе в переговорной — и остались лежать на столе. На приёмке новостройки в Тюмени семья нашла в дальней комнате мокрую стяжку, трещину в стене выше метра и подоконник, который был холоднее воздуха в квартире. Представитель застройщика предложил вариант, звучащий почти по-дружески: подписываете передаточный акт сегодня, недостатки устраняем потом, «в рабочем порядке». Семья не подписала — вписала дефекты в перечень, сняла фото и видео, забрала свой экземпляр с датой и подписями. Выдачу ключей после этого сдвинули на 45 дней, а ипотека продолжила списываться по графику — без заселения.

**Para 2:** (early CTA block — skip for lead check)

## Case hook (from research / article)
- Тюмень, новостройка, приёмка квартиры с ипотекой и отделкой от застройщика
- Дефекты: мокрая стяжка, трещина в стене, холодный подоконник
- Застройщик: «подпишите акт сегодня — исправим потом, в рабочем порядке»
- Ключи на столе, но не выдали — пока нет подписи
- Семья отказалась подписывать; зафиксировала дефекты в двух экземплярах с фото/видео
- Ключи перенесли на 45 дней; ипотека списывается без заселения
- Casus собирательный/моделируемый — не конкретный ЖК
- Автор: Святослав Шакин, The Риэлтор, Тюмень
- Distinct from B12 (перенос сдачи/эскроу) — здесь дефекты на приёмке и отказ от акта

## Wordstat demand spine (hint only, no SEO tail in description)
- «приемка квартиры в новостройке тюмень» 29; «подписание акта приемки квартиры в новостройке» 58
- buyer risk: мокрая стяжка, акт приёмки, ключи, ипотека без заселения

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1 («Ключи лежали…»)
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head, no checklist spoiler («5 шагов», «полный чеклист»)
6. Cyrillic; brands OK: ДДУ, 214-ФЗ if needed
7. News energy — hint at consequence (ключи/ипотека), not how-to blurb

## Good energy (do not copy verbatim)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.»
- «Договор подписан, расписка на столе. А деньги так и не пришли — потому что расчёт начали не с того конца.»

## Required JSON output
```json
{
  "topic_id": "B16",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
One variant only. description field = teaser text for Dzen card.
