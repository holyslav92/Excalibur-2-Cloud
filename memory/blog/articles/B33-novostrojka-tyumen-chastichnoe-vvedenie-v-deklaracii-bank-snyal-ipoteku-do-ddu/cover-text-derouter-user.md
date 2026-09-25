# Cover-text — B33 (Derouter output request)

Ты — роль cover-text. **Сразу верни один JSON-объект** без markdown fences, без пояснений.

## Задача

Надписи для обложки и inline-панелей B33: Тюмень, новостройка по ДДУ, в декларации частичный ввод секции, банк снял ипотеку за 4 дня до ДДУ, эскроу не открыли, семья отказалась подписывать «ради брони».

## Обязательный JSON

```json
{
  "hook": "5-7 русских слов",
  "highlight": "одно слово из hook",
  "sticky": "до 5 слов",
  "phone_cta": "+7 922 001 65 05",
  "wordstat_stickers": ["купить новостройку в тюмени", "новостройки тюмень"],
  "inline_labels": {
    "inline_1": ["...", "...", "..."],
    "inline_2": ["...", "...", "..."],
    "inline_3": ["...", "...", "..."],
    "inline_4": ["...", "...", "..."],
    "inline_5": ["...", "...", "..."],
    "inline_6": ["...", "...", "..."],
    "inline_7": ["...", "...", "..."]
  },
  "meme_picks": {
    "cover": ["people_id", "cat_id"],
    "inline_1": ["people_id"],
    "inline_5": ["people_id"],
    "inline_7": ["people_id"]
  }
}
```

## Правила

- hook: 5–7 слов, не копировать H1 дословно. Форма: «Частичный ввод сорвал ипотеку перед ДДУ»
- highlight: одно слово из hook
- sticky: до 5 слов
- phone_cta: ровно +7 922 001 65 05
- inline_labels: 2–6 подписей на inline_1…inline_7, 1–4 слова, кириллица
- meme_picks: cover = 1 people + 1 cat; inline_1, inline_5, inline_7 — people из catalog
- Запрещённые id: drake, drake_no_yes, salt_bae, stock_handsome_man
- Anti-repeat 14д — избегать: roll_safe, hide_pain_harold, smudge_cat, two_buttons, crying_cat, confused_math_lady, disappointed_black_guy, this_is_fine_dog, grumpy_cat
- Предпочесть: stonks, wojak, expanding_brain, blinking_white_guy, surprised_pikachu, polite_cat, cheems, james_doakes, sacrednik_priest

## Факты для inline_labels

inline_1: бронь оплачена, «дом сдаётся», многосекционный дом, карточка на наш.дом.рф, объект залога
inline_2: четыре дня до ДДУ, вечером декларация, частичный ввод, одна секция введена, спросить банк
inline_3: ввод по секции, не ваша секция, разрешение vs декларация, фасад не равен вводу
inline_4: «дом сдан» не документ, очередь корпус секция, сверка с ДДУ
inline_5: одобрение сняли, эскроу не открыли, предварительное не финал, письменное основание
inline_6: подпишите остальное потом, отказ от ДДУ, часть брони удержали, другой лот
inline_7: таблица декларация, разрешение, ДДУ, ипотека, эскроу, бронь

Верни ТОЛЬКО JSON.
