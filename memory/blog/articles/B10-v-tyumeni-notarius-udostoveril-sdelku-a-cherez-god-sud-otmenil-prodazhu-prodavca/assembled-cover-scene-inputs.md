# Cover-scene inputs — B10

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B10
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени суд отменил продажу: продавец должна вернуть 4,3 млн
- hook (cover-text): «Сделку отменили — продавец должна вернуть миллионы» (highlight: «миллионы»)
- sticky: «Денег уже нет»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: пенсионерку вели по телефону; суд отменил сделку через полтора года; реституция 4,3 млн, денег у продавца нет; нотариус не видит скрытый звонок

## meme_picks (from cover-text.json — meme-top100.json only)

- cover: roll_safe, crying_cat
- inline_1: hide_pain_harold
- inline_5: grumpy_cat
- inline_7: disappointed_black_guy

## wordstat_stickers (manifest log ONLY — NEVER paint on cover)

- «нотариус при покупке квартиры» — 2636
- «купить квартиру в тюмени» — 39961
- «оспорить сделку купли продажи квартиры» — 388

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, host right, price jump phone
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04/B03: black blazer left bust board

**Required:** light/bright #FFF high-key, sun flare; roll_safe + crying_cat small stickers; NO dark cinematic; NO daypart formula; NO Wordstat query strips on canvas; yellow sticky from hook only.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon yellow right price jump.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table_ui — «Как в Тюмени продали квартиру пенсионерки, которую вели по телефону»
Labels: Лето 2023 | Тюмень | Пенсионерка 70 лет | 12 млн мошенникам | Звонки о безопасности | Смотрите на телефон
Meme sticker: hide_pain_harold (small corner)

### inline_2 — workflow_diagram — «Суд отменил продажу — и продавец должна вернуть 4,3 млн»
Labels: Три экспертизы | Институт Сербского | 20 января 2025 | Полтора года | Реституция в обе стороны | Денег нет
NO meme

### inline_3 — checklist_board — «Нотариус не видит звонок: контрастные дела и позиция Верховного суда»
Labels: Красноуфимск: сделка устояла | Тюмень: возврат денег | 48 дел | 19 устояли | Около 40 процентов | Две развязки
NO meme

### inline_4 — schema_faq_ui — «Что проверить покупателю, если продавец пожилой и телефон не отпускает»
Labels: Реакция на звонок | Куда пойдут деньги | Единственное жильё | Цена ниже рынка | История права | Не скрывайте сделку
NO meme

### inline_5 — process_flow — «Таблица: когда сделку оспорят и кто останется с долгом»
Labels: Тюмень: долг 4,3 млн | Верховный суд: 1,9 млн | Красноуфимск: без долга | 40 процентов устояли | Суд смотрит экспертизу | Долг не деньги
Meme sticker: grumpy_cat (small corner)

### inline_6 — tool_screenshot — «Двусторонняя реституция: почему суд не создаёт деньги»
Labels: Суд не печатает деньги | Исполнительный лист | На счёте ноль | Единственное жильё | Занижение против покупателя | Полтора года риска
NO meme

### inline_7 — comparison_table — «Напишите до аванса — или сразу к делу»
Labels: Проверка до аванса | Не после суда | Документы на разбор | Подключусь в сделку | Тюмень: вторичка | Телеграм и МАКС
Meme sticker: disappointed_black_guy (small corner)

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "wordstat_stickers": ["...", "...", "..."],
  "meme_picks": { "cover": ["roll_safe", "crying_cat"], ... },
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
    "cover": { "scene_hint": "...", "alt": "...", "cover_emotion": "..." },
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «миллионы», ZERO Wordstat on canvas.
