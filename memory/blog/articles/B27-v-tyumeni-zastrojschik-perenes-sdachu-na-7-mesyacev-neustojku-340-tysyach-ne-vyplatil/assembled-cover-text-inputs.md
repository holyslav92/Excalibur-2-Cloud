# Cover-text inputs — B27

ROLE: cover-text. Выход: только валидный JSON без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил
- subject: задержка передачи квартиры по ДДУ и неустойка застройщика
- angle: застройщик перенёс передачу ключей на семь месяцев, после ключей не выплатил рассчитанную неустойку около 340 тысяч рублей
- hero: Святослав Шакин identity-real (Cover agent, не менять лицо)

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
- Anti-repeat 14д — не использовать недавние: side_eye_chloe, pop_cat, disaster_girl, keyboard_cat, two_buttons, surprised_tom, bad_luck_brian, grumpy_cat, blinking_white_guy, polite_cat, roll_safe, crying_cat, hide_pain_harold, smudge_cat, confused_math_lady, distracted_boyfriend, thinking_cat, woman_yelling_cat, wojak, this_is_fine_dog
- On-topic: боль, WTF, скепсис про перенос сдачи, неустойку 340 тысяч, допсоглашение без выплаты
- **Только id из каталога** — запрещены выдуманные id
- Рекомендуемые валидные id: cover → this_is_fine_dog + surprised_pikachu; inline_1 → james_doakes; inline_5 → change_my_mind; inline_7 → skeleton_shield

## Правила gate

- hook: **5–7** слов (short hook B08-style), простой русский, highlight = одно слово из hook
- prefer слова ≥5 букв для OCR
- sticky: до 5 слов
- phone_cta: +7 922 001 65 05 (обязательно)
- inline_labels: 2–6 подписей на каждую панель inline_1…inline_7, каждая 1–4 слова, ≤28 символов
- Только кириллица (латиница только бренды)
- Не копируй H1 дословно

## Факты из article.html для inline_labels

### inline_1 — За три недели до ключей
- За 3 недели до ключей
- Перенос на 7 месяцев
- Уведомление не меняет ДДУ
- Допсоглашение в приложении
- Ипотека уже идёт

### inline_2 — Просрочка и претензия
- Претензия 340 тысяч
- Расчёт по 214-ФЗ
- Застройщик перенос признал
- Деньги не выплатил
- Снова допсоглашение

### inline_3 — Ключи получили, деньги нет
- Ключи через 7 месяцев
- Эскроу закрыли
- Неустойка отдельно
- Досудебная претензия
- Два разных процесса

### inline_4 — Допсоглашение ради скорости
- Подпишите сейчас
- Срок переносят
- Про неустойку молчат
- Не подписали
- Право сохранили

### inline_5 — Неустойка в 2026
- Мораторий сняли
- Отсрочка до 31.12.2026
- Статья 333 ГК РФ
- 340 тысяч расчёт
- Не гарантия суда

### inline_6 — Таблица проверки ДДУ
- Срок в ДДУ
- Письмо о переносе
- Дата ключей
- Претензия и ответ
- Переписка в мессенджерах

### inline_7 — Финал: подпись ради надежды
- До подписи проверить
- Не спешить с допом
- Ключи получили
- Деньги отдельный спор
- Цена подписи
