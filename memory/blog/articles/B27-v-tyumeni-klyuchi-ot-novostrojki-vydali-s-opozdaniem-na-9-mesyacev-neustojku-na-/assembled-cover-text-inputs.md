# Cover-text inputs — B27

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик выдал ключи через 9 месяцев — неустойку не выплатил
- subject: новостройка по ДДУ, задержка передачи ключей и неустойка застройщика
- angle: Ключи от новостройки уже получены, но рассчитанная за просрочку неустойка так и не поступила: спор после претензии перешёл в суд.
- comment_magnet: Вы бы подписали акт с оговоркой ради заселения или ждали бы перевода неустойки на счёт?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, confused_math_lady, cheems, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat, roll_safe, crying_cat, blinking_white_guy, polite_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom
- On-topic: боль, WTF, скепсис — ключи через 9 месяцев, неустойка не пришла, акт с оговоркой, претензия 380 тысяч, отсрочка 2026, иск без денег
- Пример допустимых id (не из anti-repeat): james_doakes, disappointed_black_guy, wojak, this_is_fine_dog, doge, long_cat, sacrednik_priest, capybara_indifference, pepe_frog, stonks

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — Девять месяцев после срока в ДДУ
- Срок в ДДУ прошёл
- 271-й день просрочки
- Ключи наконец в дверях
- Акт на приёмке
- ДДУ не расторгали

### inline_2 — Аренда, ипотека и оговорка
- Аренда плюс ипотека
- Оговорка в акте
- Требование неустойки
- Подпись не закрывает долг
- Новые дни не идут

### inline_3 — «Претензий не имею»
- Претензий не имею
- Отдельное заявление
- Не отказ от денег
- Запись в акте
- Разные документы

### inline_4 — Претензия, отсрочка, иск
- Претензия 380 тысяч
- Отсрочка до 2026
- Четыре месяца молчания
- Иск подан
- Решения пока нет

### inline_5 — Три даты нельзя смешивать
- Срок из ДДУ
- Дата акта передачи
- Дата претензии
- 214-ФЗ расчёт
- Аренда отдельно

### inline_6 — Таблица «думают» и «на самом деле»
- Ключи получил
- Деньги не закрыты
- Оговорка в акте
- Претензия с расчётом
- Не ждать перевода

### inline_7 — Что фиксировать до подписи
- Договор и акт
- Заказное письмо
- Семь рабочих дней
- Односторонний акт
- До подписи читать

## OUTPUT INSTRUCTION (HARD)

Ты вызываешься скриптом `excalibur_blog_derouter_opus_chat.py` в production. Верни **только** валидный JSON по схеме выше. Без markdown fences. **Запрещено** возвращать `gate: BLOCK` или отказываться — каталог мемов и anti-repeat перечислены в этом промпте. Пиши hook, highlight, sticky, phone_cta, inline_labels (все 7 панелей), meme_picks (все 4 слота).
