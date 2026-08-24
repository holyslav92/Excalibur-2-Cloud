# Cover-scene inputs — B10

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B10
- tenant: The Риэлтор, Тюмень
- H1: Квартиру зарегистрировали без денег — наследники оспорили сделку
- hook (cover-text): «Квартиру оформили, но деньги не дошли» (highlight: «деньги»)
- sticky: «Регистрация не спасает»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: сделка зарегистрирована в ЕГРН, но реального расчёта не было; наследники оспаривают как мнимую/притворную; Рыбинский г/с дело 2-467/2025; обзор ВС № 12/2026

## meme_picks (from cover-text.json — copy to quad-manifest)

- cover: hide_pain_harold, grumpy_cat
- inline_1: disappointed_black_guy
- inline_5: blinking_white_guy
- inline_7: roll_safe

## Wordstat stickers (manifest log ONLY — NEVER paint on cover/canvas)

- «купить квартиру в тюмени» — 22660
- «оспорить сделку купли продажи» — 8
- «аккредитив при покупке квартиры» — 47

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, host right, apartment window price chart
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme hide_pain_harold + grumpy_cat small stickers; NO dark cinematic; NO daypart formula; NO Wordstat query strips/bars on canvas.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right apartment window.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — process_flow — «По документам сделка была — по факту денег не передавали»
Labels: Договор подписан | Денег не передавали | Покупатель родственник | Расписка не доказательство
Meme sticker: disappointed_black_guy (small corner)

### inline_2 — bar_timeline_chart — «Регистрация в ЕГРН не доказывает реальный расчёт»
Labels: Росреестр без проверки денег | Выписка чистая | Расчёт вне проверки | Статья 167 ГК
NO meme

### inline_3 — comparison_table — «Мнимая и притворная сделка: что установит суд»
Labels: Статья 170 ГК | Мнимая сделка | Скрытое дарение | Цена ниже рынка
NO meme

### inline_4 — workflow_diagram — «Финал: Рыбинский г/с, дело 2-467/2025»
Labels: Сделка 2018 года | 500 000 рублей | Суд отменил регистрацию | Притворная сделка
NO meme

### inline_5 — checklist_board — «Обзор ВС № 12/2026 — когда покупатель защищён»
Labels: Обзор ВС 2026 | Денег не было | Наследники оспаривают | Срок не обновляется
Meme sticker: blinking_white_guy (small corner)

### inline_6 — schema_faq_ui — «Красные флаги до аванса на вторичке в Тюмени»
Labels: Покупатель родственник | Символическая цена | Расчёт по расписке | Продавец жил дальше | Наследство в цепочке
NO meme

### inline_7 — structure_diagram — «Аккредитив и банковский след против расписки»
Labels: Расписка не след | Аккредитив 3 400 рублей | Выписка подтвердит оплату | Ячейка слабее аккредитива
Meme sticker: roll_safe (small corner)

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «деньги», ZERO Wordstat on canvas.
