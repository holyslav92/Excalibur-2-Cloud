# Cover-text inputs — B29

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

**RUNTIME:** ты уже вызываешься из `excalibur_blog_cover_text_derouter.py` с рабочим DEROUTER API. **Запрещено** возвращать `{ "gate": "BLOCK", "error": "DEROUTER ..." }` — это не валидный cover-text. Верни только объект с hook, highlight, sticky, phone_cta, inline_labels, meme_picks.

## Контекст

- topic_id: B29
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени обещали скидку 4% — проект ДДУ без неё остановил сделку
- subject: обещанная скидка 4% в переписке и полная цена в проекте ДДУ
- angle: Скидку подтвердили в CRM и мессенджере, в присланном проекте ДДУ — прайсовая цена без скидки; семья остановила сделку за три дня до эскроу
- comment_magnet: Застройщик должен выполнить обещание скидки в переписке — или покупатель вправе рассчитывать только на цену, указанную в ДДУ?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, roll_safe, grumpy_cat, confused_math_lady, cheems, disappointed_black_guy, this_is_fine_dog, crying_cat, blinking_white_guy, polite_cat, bad_luck_brian, two_buttons, surprised_tom, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat
- On-topic: боль, WTF, скепсис — минус 4% в чате, полная цена в ДДУ, «оформим потом», три дня до эскроу, CRM и мессенджер
- Пример допустимых id (не из anti-repeat): james_doakes, wojak, doge, long_cat, sacrednik_priest, capybara_indifference, keyboard_cat (если не в anti-repeat — pop_cat banned), this_is_fine — banned; use wojak, doge, long_cat, james_doakes, capybara_indifference, sacrednik_priest

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды CRM)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «Минус четыре процента» — CRM и переписка
- CRM-чат
- Мессенджер
- Минус четыре процента
- Семейная ипотека
- Сохранить переписку

### inline_2 — За три дня до эскроу: вечером открыли проект ДДУ
- Три дня до эскроу
- Вечерняя проверка
- Проект ДДУ
- Строка с ценой
- Подписи ещё нет

### inline_3 — В договоре полная прайсовая цена
- Полная прайсовая
- Скидки в тексте нет
- Статья пять 214-ФЗ
- Итоговая сумма
- Чат не исправляет

### inline_4 — «Подпишите сейчас, скидку оформим потом»
- Оформим потом
- Полная стоимость сначала
- Часть два статьи пять
- Сказали нет
- Три дня до эскроу

### inline_5 — (inline_5 slot после inline_2 в HTML — схема/мем к блоку «прайсовая цена»)
- Прайсовая в ДДУ
- Без пункта скидки
- Расчёт по чату
- Подпись не подтверждение
- Пауза до аванса

### inline_6 — Эскроу не открывали
- Эскроу не открывали
- Сумма из ДДУ
- Статьи 15.4–15.5
- CRM не уменьшает
- После регистрации ДДУ

### inline_7 — Одна таблица до подписи
- Проект ДДУ
- Ипотечное одобрение
- Договор бронирования
- Коммерческое предложение
- CRM и мессенджер
