# Writer inputs — B05

topic_id: B05  
slug: skidku-dva-milliona-obeschali-a-v-kvartire-pryatali-risk  
H1 (не пиши в output): Квартиру уценили на два миллиона и просят задаток сегодня

## Задача

Напиши **смысл** longform HTML-фрагмент для `drafts/writer.html`. Без `<h1>`.  
Цель после Sol: **2000–2600 слов**, 7+ H2, 7 inline figure slots (Sol добавит figure с data-slot).

## Hook (сохранить тему)

«Два миллиона скидка» + продавец просит **задаток сегодня**. Скидка = тариф на риск, не подарок. Кейс: трёшка в Тюмени, в документах — **банкротство продавца**, скидка как аргумент для оспаривания.

## H2 план (все 7)

## Скидка — это цена риска, которую вам предлагают взять на себя
## Что было в той квартире за минус два миллиона
## За что реально дают скидку (и это нормально)
## За что скидку дают, а платить будете вы
## Четыре вопроса, после которых скидка объясняется сама
## Что я проверяю до задатка
## Если торопят с задатком — как не купить риск по скидке

## Conversion (HARD)

После hook + TL;DR (первый экран до первого H2):

```html
<div class="excalibur-cta-early">
<p><b>Я — Святослав Шакин, The Риэлтор в Тюмени.</b> Лично веду сделку от звонка до регистрации.</p>
<p>Полный разбор кейсов и как я это ловлю до аванса — в <a href="https://t.me/Tyumen_Rieltor">Telegram</a> и <a href="https://max.ru/id561413315447_biz">MAX</a>.</p>
<p><a href="https://t.me/Tyumen_Rieltor">Telegram</a> · <a href="https://max.ru/id561413315447_biz">MAX</a></p>
</div>
```

**Mid** после главного чеклиста (список «платите вы»):

```html
<div class="excalibur-cta-mid">
<p>Такие кейсы разбираю в <a href="https://t.me/Tyumen_Rieltor">Telegram</a> и <a href="https://max.ru/id561413315447_biz">MAX</a> — напишите ссылку на объявление.</p>
</div>
```

**End** — dual CTA консультация / сразу в сделку + полный набор:

```html
<div class="excalibur-cta-end">
<p><b>Напишите на консультацию</b> — разберём ваше объявление до задатка. Или <b>подключаюсь в сделку</b> и веду от звонка до регистрации.</p>
<p><a href="https://t.me/Tyumen_Rieltor">Telegram</a> · <a href="https://max.ru/id561413315447_biz">MAX</a> · <a href="{{SITE_BASE}}/">Сайт</a> · <a href="{{SITE_BASE}}/gajdy/">Гайды</a> · <a href="https://dzen.ru/holyslav">Дзен</a> · <a href="https://vk.ru/tymenrieltor">VK</a></p>
<p>Телефон: <a href="tel:+79220016505">+7 922 001 65 05</a> (один раз в теле).</p>
</div>
```

## Interlink (2–4, контекстно)

- <a href="/blog/vtorichka-i-riski/raspisku-na-kvartiru-napisali-deneg-na-schete-net/">расписка без денег на счёте</a>
- <a href="/blog/vtorichka-i-riski/pochti-vnesli-zadatok-za-48-chasov-do-torgov-kvartiru-podarili-docheri/">задаток на торгах и дарение в ЕГРН</a>
- <a href="/blog/vtorichka-i-riski/doverennost-ne-bronya-prodavec-priletel-odin-a-kvartiru-prodavali-chetvero/">доверенность не броня</a>

## Таблицы

Сравнительные таблицы: левый столбец ≠ правый (объяснимая vs необъяснимая скидка; ошибка vs что делать).

## Inline placeholders

После каждого H2 оставь маркер для Sol:
`<figure class="inline-quad" data-slot="inline_N">` с img src cover/inline-0N.png — Writer может поставить пустой figure с data-slot только.

## Research

См. research-notes.md в этой папке. Факты только оттуда. Не выдумывать адреса/лоты.

## Стиль смысла

Короткие абзацы, Klyshin rhythm (реплики, контраст). Первое лицо Святослав, Тюмень. Без research-даты в лиде.
