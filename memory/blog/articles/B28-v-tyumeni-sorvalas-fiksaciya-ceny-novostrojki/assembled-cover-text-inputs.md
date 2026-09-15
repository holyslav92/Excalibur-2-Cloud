# Cover-text inputs — B28

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## КРИТИЧНО (Derouter gpt-6-astra)

Ты — Derouter powerful tier, роль **cover-text**. Это твоя прямая задача по контракту `shared/derouter-opus-brain-contract.md`.
Верни **только** валидный JSON с полями `hook`, `highlight`, `sticky`, `phone_cta`, `inline_labels`, `meme_picks`.
Gate (`cover_text_gate`) и stamp выполнит оркестратор **после** твоего ответа — тебе не нужно запускать скрипты.
**Запрещено** отказываться, возвращать BLOCKER или объяснять отсутствие доступа к файлам.

Разрешённые meme id (выбери из списка, anti-repeat — не брать недавние):
`disappointed_black_guy`, `stonks`, `two_buttons`, `this_is_fine_dog`, `wojak`, `pepe_frog`, `surprised_pikachu`, `expanding_brain`, `change_my_mind`, `gigachad`, `crying_jordan`, `success_kid`, `sacrednik_priest`, `zhirinovsky`, `blinking_white_guy`, `bad_luck_brian`, `grumpy_cat`, `smudge_cat`, `crying_cat`, `doge`, `cheems`, `polite_cat`, `pop_cat`, `long_cat`, `keyboard_cat`, `woman_yelling_cat`, `roll_safe`, `hide_pain_harold`, `confused_math_lady`, `side_eye_chloe`, `disaster_girl`, `capybara_indifference`, `trollface`, `yelling_at_clouds`, `surprised_tom`, `nyan_cat`

## Контекст

- topic_id: B28
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 5 дней до ДДУ сорвалась фиксация цены
- subject: фиксация цены на новостройку в Тюмени перед подписанием ДДУ
- angle: В офисе обещали «пока бронь действует — цена ваша»; ипотеку одобрили, эскроу открыли; за 5 дней до подписания в проекте ДДУ появилась индексация и сумма выросла — семья остановила сделку до перевода на эскроу
- comment_magnet: Устная фиксация цены в офисе продаж — уже обязательство или лишь рекламная фраза, пока в брони и ДДУ не указана конкретная сумма?

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

## Meme picks (HARD)

Каталог: `memory/cover/meme-top100.json`. Только реальные id.
- Variety: people + cats (не cats-only)
- Slots: cover (1–2), inline_1, inline_5, inline_7
- Anti-repeat 14д — не использовать: hide_pain_harold, smudge_cat, confused_math_lady, cheems, side_eye_chloe, pop_cat, disaster_girl, keyboard_cat, bad_luck_brian, grumpy_cat, two_buttons, blinking_white_guy, polite_cat, roll_safe, crying_cat, wojak, woman_yelling_cat
- On-topic: скепсис к «цена ваша», боль перед ДДУ, WTF от индексации, «обещали одно — в договоре другое», семья развернулась до эскроу

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — «До конца квартала цена ваша» — и семья поверила акции
- Акция до 30 сентября
- Менеджер: цена зафиксирована
- Пока бронь — стоимость ваша
- Скидка на паркинг
- Цена к конкретной квартире

### inline_2 — Ипотека готова, эскроу открыли: остался проект ДДУ
- Кредит одобрен
- Взнос посчитан
- Счёт эскроу открыт
- Банк не фиксирует цену
- Остался проект ДДУ

### inline_3 — За 5 дней до подписания прислали другой расчёт
- Новый расчёт с проектом
- За 5 дней до подписи
- Кредита не хватает
- «Цена ваша» устно
- Письменный ответ нужен

### inline_4 — В проекте ДДУ — индексация и сумма, которой не было в офисе
- Цена за квадратный метр
- Оговорка об индексации
- Закон 214-ФЗ
- Пересмотр по договору
- Не подписанный ДДУ

### inline_5 — Семья развернулась: ДДУ не подписали, на эскроу деньги не ушли
- Отказ от новых условий
- ДДУ не подписали
- На эскроу не перевели
- Спор о брони отдельно
- Исход брони неизвестен

### inline_6 — (пара с inline_5 — схема/документы)
- Эскроу без перевода
- Бронь не возврат
- Сохранить переписку
- Две версии расчёта
- Пауза до подписи

### inline_7 — Что проверить до брони и ДДУ — таблица
- Срок акции в рекламе
- Номер квартиры в брони
- Итоговая сумма в ДДУ
- Условия возврата брони
- Сравнить три документа
