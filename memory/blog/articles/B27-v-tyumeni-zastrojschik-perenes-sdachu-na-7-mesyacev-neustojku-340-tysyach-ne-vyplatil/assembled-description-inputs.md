# Description inputs — B27 — 2026-09-05

## Task
Write 1–2 sentences for Dzen card teaser (~120–220 chars, max 250). Output JSON only per skill schema. verdict: PASS. No BLOCKER text — return valid JSON only.

## topic_id
B27

## title-brief.json — H1 (DO NOT copy verbatim)
**H1:** Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил

**subject:** Задержка передачи квартиры по ДДУ и неустойка застройщика

**angle:** Конкретная тюменская история: застройщик перенёс передачу ключей на семь месяцев, но после получения квартиры не выплатил рассчитанную неустойку в 340 тысяч рублей.

**comment_magnet_angle:** Вы бы подписали допсоглашение о переносе срока, если в нём нет ни слова о неустойке — ради надежды быстрее получить ключи?

## article.html — opening (DO NOT truncate — double card forbidden)
**Para 1:** Застройщик в Тюмени задержал передачу квартиры на 7 месяцев, а после ключей семья не получила около 340 тысяч рублей неустойки. За три недели до договорной даты людям прислали уведомление: срок сдвигается. Ипотека при этом продолжала идти, а дата передачи квартиры в ДДУ уже была определена. Когда срок прошёл, семья предъявила застройщику претензию, но вместо денег услышала предложение подписать перенос без единого слова о неустойке.

**Para 2:** Ключи в итоге получили. Эскроу закрыли. А вопрос с деньгами пришлось оставлять для досудебной претензии и суда.

## Case hook (from research / article)
- Тюмень, новостройка, ДДУ, ипотека
- За три недели до договорной даты — письмо о переносе на 7 месяцев
- Уведомление о переносе ≠ изменение срока в ДДУ
- Претензия ~340 тыс. руб. неустойки — расчёт по 214-ФЗ, не гарантия суда
- Застройщик предлагает допсоглашение без пункта о неустойке — «ради скорости ключей»
- Семья допсоглашение не подписала
- Ключи получили, эскроу раскрыли — неустойку не выплатили
- Получить квартиру и получить неустойку — два разных процесса
- Автор: Святослав Шакин, The Риэлтор, Тюмень

## Wordstat demand spine (hint only, no SEO tail in description)
- «неустойка застройщика» 234; «перенос срока сдачи новостройки» 89; «дополнительное соглашение дду» 67
- buyer risk: ДДУ, перенос ключей, допсоглашение, неустойка, эскроу

## Dzen description rules (mandatory)
1. ≠ title — different wording, not H1 copy
2. ≠ truncated lead — not substring of first two paragraphs; don't start like para 1
3. Klyshin rhythm: case hook, conversational first line, intrigue before click
4. Geo/facts: Тюмень / Шакин context OK
5. No label head («Риэлтор Тюмень» alone), no checklist spoiler
6. Cyrillic; brands OK: ДДУ, эскроу, 214-ФЗ

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
