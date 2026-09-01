# Cover-text inputs — B20

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B20
- cluster: newbuild booking price increase
- tenant: The Риэлтор, Тюмень
- H1: Бронь новостройки в Тюмени — за двое суток цена выросла на 380 тысяч
- subject: бронь новостройки в Тюмени
- angle: Пара забронировала двушку бесплатно на двое суток; за 48 часов прайс вырос на 380 тысяч — бронь держала квартиру, не цену
- comment_magnet: Бронь с фиксацией цены — договор или обещание на 48 часов?

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

## Gate retry (BLOCK — fix these)

Previous attempt BLOCKED:
- inline_7 label «Нет цифры — нет фиксации» = 5 tokens (em dash counts) — max 4 words per label
- meme_pick `drake_hotline_bling` — BANNED, not in catalog
- meme_pick `this_is_fine` — invalid id; use `this_is_fine_dog`
- meme_pick `business_cat` — invalid id; use only ids from catalog below

## Meme picks (HARD)

Каталог: `memory/cover/meme-top100.json`. Только реальные id. **Запрещены:** drake_*, this_is_fine (без _dog), business_cat.

**Допустимые примеры id (выбери из каталога):** roll_safe, hide_pain_harold, disappointed_black_guy, confused_math_lady, success_kid, side_eye_chloe, two_buttons, blinking_white_guy, bad_luck_brian, grumpy_cat, smudge_cat, crying_cat, polite_cat, distracted_boyfriend, disaster_girl, this_is_fine_dog, stonks, wojak, surprised_pikachu, keyboard_cat, doge, cheems, pop_cat, surprised_tom, capybara_indifference, james_doakes, sacrednik_priest
- Variety: people + cats (не cats-only)
- Slots: cover (1–2), inline_1, inline_5, inline_7
- Anti-repeat 14д — не использовать недавние: bad_luck_brian, grumpy_cat, roll_safe, crying_cat, hide_pain_harold, smudge_cat, confused_math_lady, blinking_white_guy, polite_cat, woman_yelling_cat, wojak, wide_eyes_cat
- On-topic: скепсис, боль, WTF про «бронь держит квартиру, не цену», +380 тысяч за двое суток

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «Двое суток, которые ничего не держали»
- Бронь одна страница
- Срок двое суток
- Не предварительный договор
- Квартира закреплена
- Цена не закреплена

### inline_2 — «Почему бесплатная бронь — это не про цену»
- Бесплатная бронь ноль рублей
- Квартиру не покажут другим
- Платная бронь с суммой
- Одобрение ипотеки отдельно
- Две независимые бумаги

### inline_3 — «Почему цена уехала, пока бронь ещё действовала»
- Прайс обновился ночью
- Плюс 380 тысяч
- Тот же этаж
- Бронь не про цену
- Одна строка в бланке

### inline_4 — «Чем всё закончилось» (первый beat)
- Три варианта на столе
- Доплатить 380 тысяч
- Другой этаж дешевле
- Отпустить квартиру
- Добрали из бюджета кухни

### inline_5 — «Как держать цену, а не надежду»
- Строка про цену
- Срок под реальный темп
- Письменный след
- Одобрение ≠ сделка
- Четыре пункта до оплаты

### inline_6 — «Что я делаю, когда захожу в бронь»
- Цену письмом
- Не иду без одобрения
- Читаю проект ДДУ
- Полчаса до платежа
- Против 380 тысяч

### inline_7 — «Почему бронь не держит цену»
- Объект и цена разные
- Цена в прайсе
- Без цифры нет цены
- Прайс не стоит
- Неделя до эскроу
