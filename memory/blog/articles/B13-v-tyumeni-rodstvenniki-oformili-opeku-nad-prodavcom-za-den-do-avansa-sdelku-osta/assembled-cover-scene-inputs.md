# Cover-scene inputs — B13

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B13
- tenant: The Риэлтор, Тюмень
- H1: Квартиру в Тюмени остановили за день до аванса — родственники пошли в суд
- hook (cover-text): «Чистая выписка не спасла сделку» (highlight: «спасла»)
- sticky: «Аванс остановили вовремя»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: визуально адекватный пенсионер-продавец, чистая выписка ЕГРН; за день до аванса родственники подали заявление о признании недееспособным; риелтор остановил сделку до денег

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «признание недееспособным» — 157
- «заявление о признании недееспособным» — 55
- «разрешение опеки на продажу квартиры» — 77

## meme_picks (from cover-text.json)

- cover: two_buttons, grumpy_cat
- inline_1: blinking_white_guy
- inline_5: expanding_brain
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B12: light blue shirt showroom letter payment right
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NO default keys/desk cliché.

## Anti-repeat used-motifs (14d) — avoid collision

B12 showroom letter; B10 apartment viewing phone; B06 panoramic window price chart.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Квартира согласована — и накануне аванса всплыло заявление в суд»
Labels: Заявления нет в ЕГРН | Автозапрета нет | Продавец дееспособен | Выписка чистая | Сигнал, не стоп-документ
Meme: blinking_white_guy tiny corner

### inline_2 — process_flow — «За день до расчётов: адекватный продавец и семейный сигнал»
Labels: Звонок родственника | Заявление подано в суд | Не оформят за день | Опека — 15 дней
NO meme

### inline_3 — bar_timeline_chart — «Финал: аванс не внесли, регистрацию не открывали»
Labels: Аванс не внесли | Договор не подписали | Регистрацию не открывали | Покупатель без потерь | Один неприятный вечер
NO meme

### inline_4 — structure_diagram — «Три состояния продавца: недееспособный, ограниченно дееспособный и «пока только заявление»»
Labels: Уже признан недееспособным | Ограниченная дееспособность | Заявление подано | Опекун — не попечитель | Автозапрета нет
NO meme

### inline_5 — fact_card — «Статья 171 и статья 177: ничтожность против оспоримости»
Labels: Статья 171 — ничтожность | Статья 177 — оспоримость | Не понимал своих действий | Опекун оспорит позже | Календарь судебного спора
Meme: expanding_brain tiny corner

### inline_6 — labeled_checklist — «Обзор ВС РФ № 12/2026: экспертиза, наследник и реституция»
Labels: Обзор июль 2026 | Экспертиза — центр дела | При жизни не оспорит | Запись в реестре | Отказ от экспертизы
NO meme

### inline_7 — workflow_diagram — «Что проверить до аванса, если родственники начали процедуру недееспособности»
Labels: Бумага, не пересказ | Три состояния — различить | Опека — 15 дней | Деньги не двигать | Стоп до аванса
Meme: disappointed_black_guy tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": "...",
    "joke": "...",
    "outfit": "...",
    "emotion": "...",
    "pose_framing": "...",
    "action": "..."
  },
  "slots": {
    "cover": {
      "scene_hint": "...",
      "alt": "...",
      "cover_emotion": "..."
    },
    "inline_1": { "scene_hint": "...", "alt": "..." },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "..." },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "..." }
  }
}
```

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «спасла», ONE yellow sticky only, ZERO Wordstat strips on canvas.
