# Cover-text inputs — B30

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

**Derouter:** ты уже вызван скриптом `excalibur_blog_derouter_opus_chat.py`. Не возвращай `gate: BLOCK`, не проси запускать скрипты и не отказывайся от роли — **сразу напиши готовый JSON** по схеме ниже (hook, highlight, sticky, phone_cta, inline_labels, meme_picks). Пример hook (6 слов): «В шоу-руме солнце — в черновике север».

## Контекст

- topic_id: B30
- tenant: The Риэлтор, Тюмень
- H1: В шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция
- subject: шоу-рум и проект ДДУ: смена секции при той же площади и этаже
- angle: Семья выбрала «солнечную сторону» в шоу-руме, а за пять дней до ДДУ в проекте договора увидела северную секцию с окнами на соседний корпус — отказались подписывать до эскроу.
- comment_magnet: Если в шоу-руме солнце, а в ДДУ — северная секция за ту же цену, вы бы подписали, чтобы не потерять бронь, или сразу ушли?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, roll_safe, crying_cat, blinking_white_guy, polite_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat, confused_math_lady, cheems, disappointed_black_guy, this_is_fine_dog
- On-topic: боль, WTF, скепсис — шоу-рум с солнцем, в ДДУ север и соседний корпус, «другой подъезд», отказ от ДДУ, часть брони удержали
- Пример допустимых id (не из anti-repeat): james_doakes, wojak, doge, long_cat, sacrednik_priest, capybara_indifference, success_kid, stonks_guy

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая **1–4 слова по split()** (без тире «—» внутри подписи: «До ДДУ — пять дней» = 5 токенов и BLOCK)
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «Солнечная сторона» в шоу-руме и брони
- Солнечная сторона
- Заявка на бронь
- Окна во двор
- Демонстрационная квартира
- Не та секция

### inline_2 — Эталон с окнами во двор
- Окна во двор
- Дневной свет
- Та же планировка
- Другой корпус
- Метраж совпал

### inline_3 — За пять дней до ДДУ секция B
- Пять дней до ДДУ
- Секция B
- Северная сторона
- Окна на корпус
- Площадь та же

### inline_4 — «Та же цена, другой подъезд»
- Та же цена
- Другой подъезд
- Вид из окна
- Не равноценность
- Менеджер успокаивает

### inline_5 — ДДУ не подписали, бронь удержали
- ДДУ не подписали
- Эскроу не открывали
- Часть брони удержали
- Отказ от замены
- Бронь отдельный договор

### inline_6 — Сверка до подписи
- Секция в ДДУ
- Поэтажный план
- Генплан дома
- ID в ЕИСЖС
- наш.дом.рф

### inline_7 — Итог: пауза до подписи
- Исправленный проект
- Переписку сохранить
- Пауза до подписи
- Не спасать бронь
- Окна и вид
