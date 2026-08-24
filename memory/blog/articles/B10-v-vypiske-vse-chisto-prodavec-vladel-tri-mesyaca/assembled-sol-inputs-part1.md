# Sol B10 PART 1/2 — лиды, история, финал casus (H2 1–3)

Выход: **только HTML** (p, h2, figure, div excalibur-cta-early). Без markdown fences.

## H1 (контекст, не в вывод)
Чистая выписка на квартиру — через полгода сделку оспорили

## HARD
- Прозаический лид **4–6 предложений**, без TL;DR, без ul/ol до первого H2
- После лида — **excalibur-cta-early** (TG https://t.me/Tyumen_Rieltor, MAX https://max.ru/id561413315447_biz)
- **3 H2** с figure inline_1..inline_3 сразу после каждого h2
- Слог SOUL: короткие абзацы, «я веду сделку», Тюмень, без мата
- Interlink в части 1: /blog/vtorichka-i-riski/raspisku-na-kvartiru-napisali-deneg-na-schete-net/ и /blog/ipoteka/ipoteku-odobrili-a-registraciyu-otmenili-stroka-v-egrn/
- Факты только ниже. Не выдумывать.

## Факты casus
- Покупатель Тюмень: чистая выписка ЕГРН, один собственник, аккредитив, регистрация ОК, заехал, ремонт
- Через ~6 мес.: конверт арбитража — финуправляющий оспаривает ДКП (банкротство продавца, ст. 61.2 вред кредиторам)
- Выписка не соврала — снимок на дату; не видит будущее банкротство
- Выписка о переходе прав: продавец владел **3 месяца** (купил фев, продал май), основание — ДКП
- Короткий срок ≠ недействительность; индикатор: флип или избавление от долгов
- Финал: иск в арбитраже; покупатель ответчик; аккредитив, рыночная цена, нет связей с продавцом
- **Исход:** сделку сохранил; цена — год судов, юрист, нервы; при наличных/занижении/связях — могли бы забрать квартиру

## H2 (часть 1)
1. Выписка была чистой — а через полгода пришёл иск из арбитража [inline_1]
2. Три месяца владения: что покупатель увидел в переходе прав [inline_2] — interlink скидка: /blog/vtorichka-i-riski/skidku-dva-milliona-obeschali-a-v-kvartire-pryatali-risk/
3. Финал: финуправляющий оспорил сделку — и что из этого вышло [inline_3]

## figure шаблон
```html
<figure class="inline-quad" data-slot="inline_N"><img src="cover/inline-0N.png" alt="…" loading="lazy"></figure>
```

## early CTA
```html
<div class="excalibur-cta-early">
<p><b>Я — Святослав Шакин, The Риэлтор в Тюмени.</b> Лично веду сделку от звонка до регистрации.</p>
<p>Полный разбор кейсов и как я это ловлю до аванса — в <a href="https://t.me/Tyumen_Rieltor">Telegram</a> и <a href="https://max.ru/id561413315447_biz">MAX</a>.</p>
<p><a href="https://t.me/Tyumen_Rieltor">Telegram</a> · <a href="https://max.ru/id561413315447_biz">MAX</a></p>
</div>
```
