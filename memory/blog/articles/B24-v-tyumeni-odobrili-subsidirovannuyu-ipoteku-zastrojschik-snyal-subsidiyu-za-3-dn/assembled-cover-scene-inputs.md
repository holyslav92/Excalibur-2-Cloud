# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик снял субсидию за 3 дня до ДДУ — бронь сгорела
- hook (cover-text): «Застройщик снял субсидию перед сделкой» (highlight: «субсидию»)
- sticky: «Одобрение не спасло сделку»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: банк одобрил субсидированную ипотеку → бронь новостройки → за 3 дня до ДДУ застройщик отозвал субсидию → цена в ДДУ выросла → одобрения не хватило → до эскроу не дошли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «ипотека от застройщика тюмень» — 514
- «ипотека тюмень новостройки от застройщика» — 98
- «субсидированная ипотека от застройщика тюмень» — 27

## meme_picks (from cover-text.json)

- cover: confused_math_lady, woman_yelling_cat
- inline_1: surprised_pikachu
- inline_5: disappointed_black_guy
- inline_7: distracted_boyfriend

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: blue shirt mustard sweater handover room DDU vs EGRN
- B22: lemon shirt bank rate letter full-body center
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + woman_yelling_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer pavilion with subsidy banner peeled off / sales desk with crossed subsidy rate chart — NOT bank, NOT handover room, NOT MFC).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья забронировала квартиру под субсидию (pair with inline_2)
Labels: Новостройка в Тюмени | Предварительное одобрение | Бронь оплачена | Платёж в бюджете | Одобрение не гарантия
Meme: surprised_pikachu tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Субсидия не госпрограмма | Реклама и проект ДДУ | Бронь не фиксирует ставку | Три разных механизма | До подписи не закреплено
NO meme

### inline_3 — realistic_photo — Рекламная ставка и цена жили в разных документах
Labels: Три дня до подписи | Уведомление застройщика | После одобрения банка | Банк ставку не поднял | Субсидию убрали
NO meme — bright desk: ad flyer with rate vs DDU price sheet mismatch

### inline_4 — realistic_photo — За три дня до ДДУ застройщик снял субсидию
Labels: Цена выше одобрения | Сотни тысяч прибавки | Взноса не хватило | Банк не добавит | Нужен пересчёт
NO meme — calculator showing insufficient down payment, crossed subsidy sticker

### inline_5 — process_flow — Цена в проекте ДДУ выросла — одобрения не хватило
Labels: Стандарт ЦБ 2025 | Комиссия за ставку | Семейная не та же | Срок акции не ставка | Сверить расчёты
Meme: disappointed_black_guy tiny corner

### inline_6 — bar_timeline_chart — Семья развернулась: до эскроу не дошли, бронь сгорела
Labels: ДДУ не подписали | Бронь истекла | Деньги не на эскроу | Плата за бронь | Остановились вовремя
NO meme

### inline_7 — structure_diagram — Что проверить до подписания ДДУ — таблица
Labels: Реклама и проект ДДУ | Условия акции письменно | Договор бронирования | Новое одобрение банка | Сверка до подписи
Meme: distracted_boyfriend tiny corner

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
