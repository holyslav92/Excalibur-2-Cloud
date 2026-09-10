# Description inputs — B24 — 2026-09-10

## CRITICAL EXECUTION CONTEXT
You are running inside `excalibur_blog_derouter_opus_chat.py` (utility tier). Output **JSON only** per schema below. No BLOCKER refusals.

## Task
Write a Dzen card teaser (description) for topic B24. **1–2 sentences**, ~120–220 characters (max 250). verdict: PASS.

## topic_id
B24

## title-brief (description MUST NOT copy h1/title verbatim)
```json
{
  "h1": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "title": "В Тюмени трейд-ин сорвался накануне ДДУ — квартиру не приняли",
  "subject": "трейд-ин старой квартиры у застройщика перед подписанием ДДУ на новостройку в Тюмени",
  "angle": "Финальная оценка старой квартиры лишила семью первоначального взноса: ДДУ не подписали, а бронь и выбранную планировку потеряли.",
  "comment_magnet_angle": "Вы бы вносили бронь на новостройку, если условия трейд-ин озвучены менеджером и в рекламе, но не закреплены отдельным приложением?"
}
```

## article.html — opening (description MUST NOT truncate or repeat this lead)
First paragraph only (for anti-dup reference):
«В Тюмени семья остановила покупку новостройки за сутки до подписания ДДУ. Старую квартиру, которую планировали отдать в trade-in, оценили на 1,2 млн ₽ ниже ориентира, названного в офисе продаж. Новая квартира на севере города уже была забронирована. Ипотека — предварительно одобрена. Но первоначальный взнос складывался из денег за прежнее жильё, поэтому после оценки в семейном расчёте появилась дыра. Договор участия в долевом строительстве не подписали, деньги на эскроу не ушли.»

## Casus spine (for energy, not copy-paste)
- Event: семья в Тюмени забронировала новостройку, ипотека предварительно одобрена, первоначальный взнос — из trade-in старой квартиры
- Twist: за 24–36 часов до ДДУ партнёр застройщика оценил старую квартиру на 1,2 млн ₽ ниже суммы, которую менеджер называл в офисе
- Stakes: не хватило первоначального взноса → ДДУ не подписали → бронь сняли, планировка и акция ушли другому покупателю; на эскроу деньги не ушли
- Voice: Святослав Шакин / Тюмень — разрыв между маркетинговым «возьмём в зачёт» и финальной оценкой перед подписанием

## Wordstat demand spine (hint only, no SEO tail)
- P0: «новостройки тюмень» — 4670
- support: «купить новостройку в тюмени» — 899; «ипотека новостройка тюмень» — 201

## dzen-description-rules (HARD)
1. ≠ title — other wording, same news energy
2. ≠ truncated lead — not substring of first two paragraphs; don't start with same phrase as first <p>
3. Klyshin rhythm: case hook, conversational intrigue, hint at consequence
4. No checklist blurb («N шагов», «полный чеклист», «как купить»)
5. No label head («Риэлтор Тюмень» as sole meaning)
6. Cyrillic; Latin only for brands (ДДУ, trade-in OK)
7. ~120–220 chars preferred

## Champion energy examples (do NOT copy verbatim)
- «Одобрение было в телефоне, но ставку это не закрепило. Перед ДДУ тюменская семья увидела новый платёж…» (B22 — bank rate, different plot)
- «Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное…» (generic)

## Required JSON output
```json
{
  "topic_id": "B24",
  "description": "…",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
