# Cover-text inputs — B27

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени 28 дней ждали переуступку — квартиру продали другому
- subject: Переуступка прав по ДДУ в тюменской новостройке: ожидание регистрации и потеря квартиры
- angle: 28 дней ожидания регистрации уступки — и за сутки до эскроу лот ушёл другому покупателю. Переуступка в H1 задаёт механизм новостройки; дедлайн эскроу и бронь раскрываются в лиде.
- comment_magnet: 28 дней регистрацию тянули, а лот сняли за сутки до эскроу: вы бы ждали согласие застройщика или сразу искали другую переуступку, даже если цена уже поднялась?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, roll_safe, this_is_fine_dog, stonks, confused_math_lady, cheems, wojak, disappointed_black_guy, james_doakes, long_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat, blinking_white_guy, polite_cat
- On-topic: боль, WTF, скепсис — подписали переуступку, 28 дней без ЕГРН, согласие застройщика тянули, за сутки до эскроу лот у другого
- Пример допустимых id (не из anti-repeat): crying_cat, doge, this_is_fine_dog (inline only if not on cover), sacrednik_priest, capybara_indifference, monkey_puppet, success_kid, bernie_sanders

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды: ДДУ, ЕГРН допустимы как аббревиатуры?)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — Переуступку подписали, в ЕГРН первый дольщик
- Договор уступки
- Выписка ЕГРН
- Первый дольщик
- Бронь отдельно
- Подпись не регистрация

### inline_2 — «Согласие на этой неделе» — четыре недели тишины
- Письменное согласие
- Условие в ДДУ
- Четыре недели
- Пакет не подан
- Дата эскроу

### inline_3 — 28 дней между словами и Росреестром
- 28 дней ожидания
- Нет номера заявления
- Росреестр не принял
- Опись не показали
- Бронь оплачена

### inline_4 — Кто подаёт уступку
- Первый дольщик
- Покупатель вместе
- Согласие получено?
- Опись с номером
- Не «оформляем»

### inline_5 — За сутки до эскроу лот у другого
- Звонок менеджера
- Сутки до эскроу
- Лот у другого
- Статья 15.5
- Нет записи ЕГРН

### inline_6 — Эскроу не открыли, бронь частично
- Эскроу не открыли
- Частичный возврат
- Претензия по уступке
- Лот ушёл
- Цена выросла

### inline_7 — Таблица: бронь, уступка, эскроу
- Три статуса
- Бронь не ДДУ
- Уступка в ЕГРН
- Эскроу после регистрации
- Три вопроса до брони
