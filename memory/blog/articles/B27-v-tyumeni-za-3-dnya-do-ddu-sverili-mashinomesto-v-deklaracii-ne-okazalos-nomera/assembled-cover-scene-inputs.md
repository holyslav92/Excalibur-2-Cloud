# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени забронировали машино-место — его номера не было в декларации
- hook (cover-text): «Парковку забронировали — номера нет» (highlight: «номера»)
- sticky: «Проверьте место до сделки»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: за 3 дня до ДДУ семья сверила номер машино-места с проектной декларацией на наш.дом.рф — в разделе 15.3 номера нет; банк поставил пакет «квартира + место» на паузу, эскроу не открыли; остановились до аванса

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4475
- «дду машиноместо» — 217
- «машино-место новостройка» — 89

## meme_picks (from cover-text.json)

- cover: sacrednik_priest, surprised_pikachu
- inline_1: stonks
- inline_5: this_is_fine_dog
- inline_7: doge

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold smudge_cat
- B25: kneeling bare apartment terracotta shirt confused_math_lady
- B22: yellow shirt bank desk disaster_girl keyboard_cat
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; sacrednik_priest people-meme + surprised_pikachu cat sticker; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (underground parking sales nook / bright parking plan wall / newbuild sales office with parking scheme — NOT bank desk duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Банк поставил пакет на паузу (pair with inline_2)
Labels: Бронь места | Номер парковки | Проверка до ДДУ
Meme: stonks tiny corner

### inline_2 — structure_diagram — pair with inline_1
Labels: Проектная декларация | Раздел 15.3 | Данные на наш.дом.рф
NO meme

### inline_3 — realistic_photo — «Номер на брони» — семья к ДДУ
Labels: Три дня до подписи | Номер не найден | Пакет на паузе
NO meme — bright parking plan on wall or laptop our.dom.rf

### inline_4 — realistic_photo — В декларации не нашли машино-место
Labels: Квартира и место | Семейная ипотека | Условия банка
NO meme — laptop showing declaration section 15.3, bright desk

### inline_5 — comparison_table — Бронь, ПД и ДДУ — три языка
Labels: Эскроу не открыли | Проверка документов | Риск задержки
Meme: this_is_fine_dog tiny corner

### inline_6 — process_flow — Что сверять до аванса
Labels: Подпись ДДУ | Данные застройщика | Парковочное место
NO meme

### inline_7 — bar_timeline_chart — Машино-место, эскроу и ипотека
Labels: Сверьте номер | Проверьте декларацию | До открытия эскроу
Meme: doge tiny corner

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
