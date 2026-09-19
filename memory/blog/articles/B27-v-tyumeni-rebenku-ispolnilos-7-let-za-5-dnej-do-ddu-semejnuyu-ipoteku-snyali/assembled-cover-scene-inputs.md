# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ребёнку исполнилось 7 лет — семейную ипотеку сняли
- hook (cover-text): «Ребёнку исполнилось семь — льготу сняли» (highlight: «льготу»)
- sticky: «Пять дней всё изменили»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья получила предварительное одобрение семейной ипотеки и бронь новостройки → за 5 дней до ДДУ ребёнку исполнилось 7 лет → банк пересмотрел право на льготу по дате кредитного договора → ставка ушла с 6% на рынок → платёж неподъёмный → ДДУ и эскроу не состоялись

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека в Тюмени» — 1060
- «семейная ипотека ребёнку 7 лет» — 26
- «новостройки Тюмени семейная ипотека» — 24

## meme_picks (from cover-text.json)

- cover: roll_safe, crying_cat
- inline_1: wojak
- inline_5: disappointed_black_guy
- inline_7: blinking_white_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold waist-up right
- B25: terracotta shirt kneeling empty apartment tape measure
- B23: light blue shirt handover room side_eye keys
- B22: lemon shirt bank rate panel full-body center
- B20: terracotta overshirt MFC corridor two DDU

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright newbuild family lounge with birthday calendar + mortgage papers — NOT bank desk duplicate, NOT empty apartment, NOT showroom model).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья забронировала квартиру (pair with inline_2)
Labels: Семейная ипотека | Ставка до 6% | Предварительное одобрение | Бронь квартиры | Ребёнок до 7 лет
Meme: wojak tiny corner — bright newbuild sales desk with reservation receipt and family mortgage badge

### inline_2 — comparison_table — pair with inline_1
Labels: Дата кредитного договора | За 5 дней | Пятница — день рождения | Среда — подписание | Финальная проверка банка
NO meme — two-column table: approval date vs credit contract date vs birthday

### inline_3 — realistic_photo — Между одобрением и ДДУ календарь семьи разошёлся с банком
Labels: Одобрение не кредит | Бронь не эскроу | Льгота на дату кредита | Три разных документа | Календарь сделки
NO meme — wall calendar with three colored markers for approval, birthday, DDU signing

### inline_4 — realistic_photo — За пять дней до подписания ребёнку исполнилось 7 лет
Labels: Исполнилось 7 лет | Договор в среду | Кредит не заключён | Возрастной порог | Банк пересмотрел
NO meme — birthday number 7 candle on table next to unsigned credit contract stack

### inline_5 — structure_diagram — Банк снял семейную ставку — ДДУ и эскроу не состоялись
Labels: Льготу сняли | Рыночная 18–20% | Платёж неподъёмный | Пересчёт сделки | Ставка до 6% ушла
Meme: disappointed_black_guy tiny corner — flow diagram 6% → 18% → payment spike → DDU stop

### inline_6 — process_flow — Что проверить до брони: возраст ребёнка и дата кредитного договора
Labels: Договор не подписали | Эскроу не открыли | Бронь отдельно | Деньги не внесли | Остановились раньше
NO meme — numbered checklist flow before booking deposit

### inline_7 — bar_timeline_chart — Между одобрением и ДДУ календарь семьи разошёлся с банком
Labels: День рождения ребёнка | Срок одобрения | Дата кредитного договора | Лимит 6 миллионов | Взнос от 20%
Meme: blinking_white_guy tiny corner — bar timeline with birthday bar crossing 7-year threshold

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_2": { "scene_hint", "alt" },
    "inline_3": { "scene_hint", "alt" },
    "inline_4": { "scene_hint", "alt" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_6": { "scene_hint", "alt" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
