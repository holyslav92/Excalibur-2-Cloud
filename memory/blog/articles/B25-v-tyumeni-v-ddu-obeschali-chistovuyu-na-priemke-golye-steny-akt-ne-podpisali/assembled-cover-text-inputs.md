# Cover-text inputs — B25

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B25
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в ДДУ обещали чистовую — на приёмке 3 расхождения, акт не подписали
- subject: Чистовая отделка в ДДУ и приёмка квартиры в новостройке
- angle: Завершённый казус показывает расхождение между приложением к ДДУ и фактическим состоянием квартиры: вместо обещанной чистовой отделки покупатели увидели white box и отказались подписывать передаточный акт
- comment_magnet: Вы бы подписали акт с голыми стенами, если в ДДУ указана чистовая отделка?

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
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, roll_safe, crying_cat, blinking_white_guy, polite_cat, bad_luck_brian, grumpy_cat, two_buttons, surprised_tom, disaster_girl, keyboard_cat, side_eye_chloe, pop_cat
- On-topic: боль, WTF, скепсис — обещали чистовую в ДДУ, на приёмке white box, три расхождения, акт не подписали, «доделаем потом»
- Пример допустимых id (не из anti-repeat): confused_math_lady, james_doakes, this_is_fine_dog, wojak, cheems, doge, long_cat, disappointed_black_guy, sacrednik_priest, capybara_indifference

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «В рекламе под ключ», в приложении к ДДУ — чистовая
- Реклама «под ключ»
- Приложение к ДДУ
- Пол, стены, сантехника
- Межкомнатные двери
- Не только шоурум

### inline_2 — На приёмке white box: три расхождения
- Белая коробка
- Стены без финиша
- Пол — стяжка
- Санузел без плитки
- Три направления

### inline_3 — Менеджер: подпишите акт, доделаем
- «Доделаем потом»
- Передаточный акт
- Акт осмотра
- Устное обещание
- Разные документы

### inline_4 — Семья отказалась подписать
- Акт не подписан
- Акт осмотра
- Фото и видео
- Односторонняя фиксация
- Претензия письмом

### inline_5 — Претензия, сроки, лимит 3%
- Статья 214-ФЗ
- Лимит 3% цены
- 60 дней устранение
- Заказное письмо
- Семь рабочих дней

### inline_6 — Таблица чистовая vs white box
- Пол с покрытием
- Стены с отделкой
- Санузел с плиткой
- ГОСТ Р 72509
- По приложению

### inline_7 — Итог: не подписывать вслепую
- Сверка перечня
- Расхождения до подписи
- Не начинать ремонт
- Документальная позиция
- Консультация до акта
