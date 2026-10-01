# Cover-scene inputs — B34

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B34
- tenant: The Риэлтор, Тюмень
- H1: Школа в рекламе ЖК — в декларации 2030, ДДУ не подписали
- hook (cover-text): «Реклама обещает школу — документы ставят срок» (highlight: «срок»)
- sticky: «Сначала смотрим декларацию»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: рендер/буклет «школа рядом» → ~14 дней до ДДУ вечером открыли PD на наш.дом.рф → школа к 2030, первый класс через 3 года → «подпишите, это общий план района» → ДДУ не подписали, деньги не ушли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3553
- «купить новостройку в тюмени» — 686
- «проектная декларация застройщика» — (узкий спрос, topic anchor)

## meme_picks (from cover-text.json)

- cover: confused_math_lady, polite_cat
- inline_1: james_doakes
- inline_5: capybara_indifference
- inline_7: surprised_tom

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B33: kitchen utility debt olive vest waist-up
- B27: sales office declaration land lease disappointed_black_guy
- B28: cottage gas pavilion sand jacket
- B29: lobby mortgage 0% two_buttons

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady + polite_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright showroom with school render vs printed PD section 22 — NOT kitchen/bank duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — ДДУ не подписали, оформление остановили до денег по сделке (pair with inline_2)
Labels: Рендер со школой | Буклет рядом | Шаговая доступность | Три календаря | Наш дом точка рф
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Четырнадцать дней | Вечер на кухне | Декларация по дому | Не презентация | Бронь на руках
NO meme — table: реклама «школа рядом» vs PD срок 2030

### inline_3 — realistic_photo — «Школа рядом» — на рендере, в буклете и у менеджера
Labels: Школа к 2030 | Первый класс три года | Поиск по документу | Возраст ребёнка | Другой маршрут
NO meme — showroom wall render + booklet stack

### inline_4 — realistic_photo — За четырнадцать дней до ДДУ: вечером открыли проектную декларацию
Labels: Общий план района | Распечатка с датой | Нет на бумаге | Сейчас не подписываем | Без скандала
NO meme — evening kitchen table laptop наш.дом.рф glow

### inline_5 — process_flow — В декларации школа к 2030 — а первый класс через три года
Labels: ДДУ не подписали | Визит перенесли | Ни рубля | План три года | Решение за вами
Meme: capybara_indifference tiny corner

### inline_6 — bar_timeline_chart — «Подпишите ДДУ, это общий план района» — семья сказала нет
Labels: Договор не подписали | Банк перенесли | Деньги не ушли | План на класс | Пауза до аванса
NO meme — timeline child age vs school year 2030 bars

### inline_7 — structure_diagram — Раздел 22 и три смысла «школы» — таблица до подписи
Labels: Раздел двадцать два | Три смысла школы | Дата обновления | Возраст ребёнка | До подписи
Meme: surprised_tom tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
