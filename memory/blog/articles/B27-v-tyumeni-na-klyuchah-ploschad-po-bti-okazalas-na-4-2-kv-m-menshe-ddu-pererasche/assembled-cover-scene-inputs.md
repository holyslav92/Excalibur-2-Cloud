# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени на ключах площадь по БТИ оказалась на 4,2 кв.м меньше ДДУ
- hook (cover-text): «Квартира стала меньше — цену не снизили» (highlight: «меньше»)
- sticky: «Акт подписывать?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: ДДУ 68,4 кв.м vs БТИ 64,2 (−4,2) на выдаче ключей; застройщик отказывает в перерасчёте; эскроу по старой площади; семья не подписала акт

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4446
- «приемка квартиры в новостройке» — 128
- «купить новостройку в тюмени» — 923

## meme_picks (from cover-text.json)

- cover: roll_safe, grumpy_cat
- inline_1: two_buttons
- inline_5: disappointed_black_guy
- inline_7: blinking_white_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (YESTERDAY — avoid bank desk)
- B25: terracotta shirt kneeling tape measure bare apartment
- B23: light blue shirt handover room keys tray

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk like B26.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «В ДДУ 68,4 кв.м — на ключах техпаспорт БТИ показал 64,2»
Labels: ДДУ 68,4 кв.м | БТИ 64,2 кв.м | Минус 4,2 кв.м | Около 6,1% | Трёхкомнатная квартира
Meme: two_buttons tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: 214-ФЗ статья 5 | Порог отклонения | Общая площадь | Приведённая площадь | Перерасчёт отказали
NO meme

### inline_3 — realistic_photo — «Эскроу уже внесён по старой площади — деньги не пересчитываются сами»
Labels: Полная цена эскроу | Счёт не раскрыт | Цена за кв.м | Претензия застройщику | Банк не пересчитает
NO meme — escrow statement + DDU area on bright desk

### inline_4 — realistic_photo — «Банк напоминает о сроке регистрации права — давление подписать акт»
Labels: Два часа до акта | Срок регистрации | Давление подписать | Ипотека ждёт акт | Спор после подписи
NO meme — handover counter clock + unsigned act folder

### inline_5 — process_flow — «Семья не подписала акт: претензия и независимый обмер»
Labels: Акт не подписан | Ключи не получили | Акт осмотра | Независимый обмер | Претензия письмом
Meme: disappointed_black_guy tiny corner

### inline_6 — structure_diagram — «Что сверять на приёмке — таблица проектная vs БТИ vs приведённая»
Labels: Проектная в ДДУ | Фактическая БТИ | Коэффициент лоджии | Формула цены | Три источника цифр
NO meme

### inline_7 — bar_timeline_chart — closing practical beat (formula before keys)
Labels: Пункт о погрешности | Письменный расчёт | Не подписывать вслепую | Ипотечные сроки | Формула до ключей
Meme: blinking_white_guy tiny corner

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
