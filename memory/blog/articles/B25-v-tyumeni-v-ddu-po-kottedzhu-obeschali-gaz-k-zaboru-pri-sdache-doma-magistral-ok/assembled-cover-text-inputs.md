# Cover-text inputs — B25

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B25
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ДДУ на коттедж обещал газ у забора — он был в 180 м
- subject: коттедж по ДДУ и обещанный газ
- angle: В ДДУ газ обещали у границы участка, но при сдаче магистраль оказалась в 180 метрах, что привело к доплате в 620 тысяч рублей
- comment_magnet: Газ в 180 метрах от забора — это выполнение ДДУ или отдельная услуга застройщика?

## Обязательные поля JSON

```json
{
  "hook": "...",
  "highlight": "...",
  "sticky": "...",
  "phone_cta": "+7 922 001 65 05",
  "inline_labels": {
    "inline_1": [...],
    "inline_2": [...],
    "inline_3": [...],
    "inline_4": [...],
    "inline_5": [...],
    "inline_6": [...],
    "inline_7": [...]
  },
  "meme_picks": {
    "cover": ["...", "..."],
    "inline_1": ["..."],
    "inline_5": ["..."],
    "inline_7": ["..."]
  }
}
```

## Wordstat stickers

**ЗАПРЕЩЕНО** — не включать поле `wordstat_stickers` (NO Wordstat query strips на обложке).

## Meme picks (HARD — все слоты обязательны)

Каталог: `memory/cover/meme-top100.json`. Только реальные id.
- **ОБЯЗАТЕЛЬНО заполнить все 4 слота:** cover (1–2 ids), inline_1, inline_5, inline_7
- **cover:** ровно 1 people-meme + 1 cat-meme (не cats-only, не people-only)
- Variety: people + cats на cover
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, roll_safe, crying_cat, blinking_white_guy, polite_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat, success_kid, doge, this_is_fine_dog
- On-topic: WTF, скепсис, боль — «газ к забору» vs труба в 180 м, доплата 620 тысяч, акт не подписан
- Пример допустимых id (не из anti-repeat): confused_math_lady, james_doakes, sacrednik_priest, wojak, cheems, long_cat, cheems, wojak, pepe_sad

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «Газ к забору» в презентации — и семья подписала ДДУ на коттедж
- Коттедж под Тюменью
- ДДУ на новый дом
- Газ к забору
- Проектная декларация
- Не рекламный буклет

### inline_2 — За две недели до акта на участке — труба в 180 метрах
- Две недели до акта
- Труба в 180 м
- Точка подключения
- Схема сетей
- Где заканчивает работа

### inline_3 — Застройщик назвал доплату 620 тысяч за «дотянуть до границы»
- Доплата 620 тысяч
- Можно в рассрочку
- Дотянуть до границы
- Не тариф ГРО
- Сверить с ДДУ

### inline_4 — Акт не подписали: точки подключения в документах нет
- Акт не подписан
- Точки нет в бумагах
- Письменная претензия
- Фото и схема
- До своей подписи

### inline_5 — «Газ в посёлке» и «газ у забора» — не одно и то же
- Газ в посёлке
- Газ у забора
- 94% до границы
- 59% подключены
- Догазификация ≠ ДДУ

### inline_6 — (pair slot) три состояния «газа»
- Сеть в посёлке
- У границы участка
- Газ в доме
- Карта gazprommap.ru
- Не приложение к ДДУ

### inline_7 — Что сверить до акта приёмки — таблица
- ДДУ и приложения
- наш.дом.рф
- Схема с привязкой
- Техусловия
- Ведомость недостатков
