# Cover-scene inputs — B22

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B22
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени банк снял одобрение ипотеки за 72 часа до ДДУ — бронь сгорела
- hook (cover-text): «Банк снял ипотеку перед сделкой» (highlight: «снял»)
- sticky: «Бронь уже не спасти»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение ипотеки на новостройку; банк перепроверил доход за 72 часа до ДДУ и снял решение; бронь истекла, квартиру купил другой

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «одобрение ипотеки» — 224
- «купить квартиру в тюмени новостройка ипотека» — 86
- «ипотека в тюмени на новостройки» — 41

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, pop_cat
- inline_1: this_is_fine_dog
- inline_5: sacrednik_priest
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20: MFC corridor terracotta overshirt two_buttons waist right
- B19: showroom turquoise polo bad_luck_brian knee shot
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + pop_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT MFC corridor duplicate of B20.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Три дня до ДДУ: семья у выбранной квартиры в новостройке»
Labels: Плата за бронь | Не эскроу | Предварительное одобрение | Три календаря | 57% ипотек
Meme: this_is_fine_dog tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: За 72 часа | Новая рассрочка | След МФО | Нагрузка выросла | Решение сняли
NO meme

### inline_3 — realistic_photo — «Бронь сгорела: квартиру купил другой покупатель»
Labels: До 8 дней | Бронь по календарю | Срок истёк | Продали в среду | Возврат частичный
NO meme — sales desk sold sticker on apartment plan

### inline_4 — realistic_photo — «Ипотеку одобрили» не равно «кредит точно дадут»
Labels: Четыре шага банка | Проверка объекта | 90 дней на документы | 30 дней на выдачу | Рассрочка перед сделкой
NO meme — bank approval letter vs final credit contract split

### inline_5 — structure_diagram — «Что в соглашении о бронировании определяет возврат денег»
Labels: Не в Росреестре | Ещё не дольщик | Отказ не вернут | Срок указан датой | Продление по тексту
Meme: sacrednik_priest tiny corner

### inline_6 — process_flow — «До брони и до ДДУ: что проверить в одном узле»
Labels: Сначала срок брони | Спросить про отказ | Четыре этапа банка | Два срока вписать | План второй
NO meme

### inline_7 — bar_timeline_chart — «Что реально в руках покупателя»
Labels: Сверить два статуса | Дом аккредитован | Бронь с продлением | Без рассрочки | Остановиться до брони
Meme: stonks tiny corner (ironic)

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
