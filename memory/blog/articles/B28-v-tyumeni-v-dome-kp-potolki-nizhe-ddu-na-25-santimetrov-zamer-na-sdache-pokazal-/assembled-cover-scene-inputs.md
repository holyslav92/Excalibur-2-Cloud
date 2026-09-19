# Cover-scene inputs — B28

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B28
- tenant: The Риэлтор, Тюмень
- H1: Под Тюменью дом в КП не приняли — потолки на 25 см ниже обещанного
- hook (cover-text): «Потолки оказались ниже договора на двадцать пять» (highlight: «ниже»)
- sticky: «Акт не подписали»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья + инвестор, дом в КП по ДДU, в приложении 2,7 м → на передаче лазер 2,45 м в гостиной и спальнях → «конструктивный допуск» + 80 000 ₽ за подпись акта → акт не подписан, ключи не выданы, транш на эскроу не ушёл → через 9 дней вернули задаток 250 000 ₽, без регистрации

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4430
- «коттеджные поселки тюмень» — 1455
- «дома в тюмени от застройщика» — 253

## meme_picks (from cover-text.json)

- cover: james_doakes, long_cat
- inline_1: roll_safe
- inline_5: two_buttons
- inline_7: capybara_indifference

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B27: sales office terracotta overshirt declaration section 12
- B26: bank desk olive vest hide_pain_harold
- B25: kneeling empty apartment tape measure confused_math_lady

**Required:** light/bright #FFF high-key, sun flare; james_doakes people-meme + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NEW location — **светлый черновой коттедж в КП под Тюменью на приёмке** (не офис продаж, не банк, не пустая квартира с рулеткой на коленях).

## Inline slots (scene_hint + alt; NO host face on inline)

### inline_1 — realistic_photo — pair with inline_2 — «Два метра семьдесят» в приложении к ДДУ
Labels: Приложение к ДДУ | Высота 2,7 метра | Дом в посёлке | Не буклет | Черновое состояние
Meme: roll_safe tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Лазерный дальномер | Гостиная 2,45 | Две спальни | Жилые комнаты | Повтор замера
NO meme — таблица: договор 2,7 м vs замер 2,45 м

### inline_3 — realistic_photo — «Конструктивный допуск» и скидка 80 тысяч
Labels: Конструктивный допуск | Скидка 80 тысяч | Подпись акта | Пункт в документе | От плиты вверх
NO meme — стол с актом и карточкой скидки, без лиц

### inline_4 — realistic_photo — День передачи, лазер в черновой гостиной
Labels: Допуск отделки | Миллиметры ровности | Не четверть метра | Нормативы высоты | Опора приложение
NO meme — лазерный дальномер у потолка черновой комнаты

### inline_5 — process_flow — Акт не подписали, ключи и эскроу
Labels: Акт без подписи | Ключи не выдали | Транш на эскроу | Замечания письменно | Фото и видео
Meme: two_buttons tiny corner

### inline_6 — bar_timeline_chart — 9 дней, задаток 250 тысяч
Labels: Девять дней | Задаток 250 тысяч | Не эскроу | Без регистрации | Вышли из сделки
NO meme

### inline_7 — structure_diagram — Замер до акта: 2,7 м и допуск отделки
Labels: Договорные 2,7 м | Допуск отделки | Замер до акта | Сверка с документом | Не только слова
Meme: capybara_indifference tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
