# Cover-text inputs — B27

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

**MANDATORY:** Derouter powerful tier `gpt-6-astra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role cover-text`. Do **NOT** output `DEROUTER COVER-TEXT BLOCKER` or refuse. Output the full cover-text JSON object only per SKILL.md from the facts below.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались
- subject: одобрение ипотеки на новостройку и подписание ДДУ
- angle: Семья получила одобрение ипотеки, но почти трёхмесячная очередь на подписание ДДУ съела срок решения банка. Переодобрение оказалось хуже, и покупатели отказались от сделки.
- comment_magnet: Кто должен был заметить риск раньше: застройщик, ипотечный брокер или сама семья, ожидавшая ДДУ почти три месяца?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, confused_math_lady, cheems, side_eye_chloe, pop_cat, disaster_girl, keyboard_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom, blinking_white_guy, polite_cat, roll_safe, crying_cat
- On-topic: боль, WTF, скепсис — одобрили ипотеку, ждали ДДУ почти три месяца, на 87-й день банк закрыл решение, переодобрение хуже, бронь сняли
- Пример допустимых id (не из anti-repeat): bad_luck_brian уже занят; используй wojak, this_is_fine_dog, disappointed_black_guy, james_doakes, two_buttons занят; doge, long_cat, grumpy_cat занят; sacrednik_priest, wojak, this_is_fine_dog, disappointed_black_guy, james_doakes, doge, long_cat, woman_cat_yelling_cat_half, polite_cat занят

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды: ДДУ допустимо как аббревиатура? — нет, только бренды из whitelist; пиши «договор долевого участия» или контекст без латиницы где можно)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «Ипотеку одобрили» — семья в очереди на ДДУ
- Бронь оформлена
- Предварительное одобрение
- Ставка и платёж
- Ждут проект договора
- Одобрение ≠ выдача

### inline_2 — «На следующей неделе» трижды — почти три месяца
- Три переноса срока
- Переписка с менеджером
- Даты подписания нет
- Банковский отсчёт идёт
- Не «примерно 90 дней»

### inline_3 — На 87-й день пришёл ДДУ, банк закрыл решение
- Проект договора наконец
- Старое решение закрыто
- Личный кабинет банка
- Файл ≠ сохранение ставки
- Эскроу не открывали

### inline_4 — Переодобрение: меньше сумма, выше ставка
- Новая заявка в банк
- Сумма кредита меньше
- Ставка выше
- Платёж не тянут
- Бронь сняли до аванса

### inline_5 — Жалко останавливаться после ожидания
- Почти три месяца ждали
- Договор наконец прислали
- Новый платёж посчитать
- Условия брони читать
- Отказ до подписи

### inline_6 — Таблица: что проверить, пока ждёте ДДУ
- Срок одобрения
- Продление у менеджера
- Готовность договора
- Условия брони
- Расчёт покупки

### inline_7 — Бронь, одобрение и эскроу — три календаря
- «Квартира за нами»
- Разные сроки
- Банк уже закрыл решение
- Пауза до аванса
- Проверка до подписи
