# Cover-scene inputs — B28

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B28
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени за 5 дней до ДДУ сорвалась фиксация цены
- hook (cover-text): «Квартиру забронировали — перед подписанием подняли цену» (highlight: «подняли»)
- sticky: «Обещали: «Цена ваша»»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: акция «до конца квартала» → устная фиксация «пока бронь — цена ваша» → ипотека и эскроу готовы → за 5 дней до ДДУ новый расчёт с индексацией → бюджет не сходится → семья не подписывает ДДУ, деньги на эскроу не уходят

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки Тюмень цена» — topic demand
- «бронирование квартиры новостройка» — topic demand
- «договор долевого участия цена» — topic demand

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, surprised_tom
- inline_1: this_is_fine_dog
- inline_5: success_kid
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold
- B25: terracotta shirt kneeling tape measure bare apartment
- B23: light blue shirt mustard sweater handover room
- B22: lemon shirt bank mortgage desk disaster_girl

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + surprised_tom cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk duplicate; NEW location (bright sales office with two price sheets / DDU project on table).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «До конца квартала цена ваша» — и семья поверила акции (pair with inline_2)
Labels: Акция до 30 сентября | Менеджер обещал фиксацию | Пока бронь цена ваша | Скидка на паркинг | Цена конкретной квартиры
Meme: this_is_fine_dog tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Кредит одобрен | Взнос посчитан | Счёт эскроу открыт | Банк цену не фиксирует | Остался проект ДДУ
NO meme

### inline_3 — realistic_photo — Ипотека готова, эскроу открыли: остался проект ДДУ
Labels: До подписания: 5 дней | Прислали новый расчёт | Кредита не хватает | Цену обещали устно | Нужен письменный ответ
NO meme — bright sales office desk with two different price calculations

### inline_4 — realistic_photo — За 5 дней до подписания прислали другой расчёт
Labels: Цена квадратного метра | Оговорка об индексации | Закон 214-ФЗ | Пересмотр цены по договору | ДДУ ещё не подписан
NO meme — DDU project pages with indexation clause highlighted

### inline_5 — process_flow — В проекте ДДУ — индексация и сумма, которой не было в офисе
Labels: Отказ от новых условий | ДДУ не подписали | На эскроу не перевели | Спор о брони отдельно | Исход брони неизвестен
Meme: success_kid tiny corner

### inline_6 — bar_timeline_chart — Семья развернулась: ДДУ не подписали, на эскроу деньги не ушли
Labels: Эскроу без перевода | Возврат брони под вопросом | Сохранить переписку | Две версии расчёта | Пауза до подписи
NO meme

### inline_7 — structure_diagram — Что проверить до брони и ДДУ — таблица
Labels: Срок акции в рекламе | Номер квартиры в брони | Итоговая сумма в ДДУ | Условия возврата брони | Сравнить три документа
Meme: expanding_brain tiny corner

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
