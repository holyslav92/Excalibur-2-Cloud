# Cover-scene inputs — B11

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B11
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени купили квартиру с открытой кухней — Росреестр отказал в регистрации
- hook (cover-text): «Скидка за кухню остановила сделку» (highlight: «Скидка»)
- sticky: «Сначала сверка, потом аванс»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: покупатели взяли вторичку с открытой кухней, скидка продавца, аванс до сверки плана; МФЦ 9–14 дней; Росреестр приостановил регистрацию — факт не совпал с ЕГРН; спор про стену и кто платит согласование

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «перепланировка квартиры тюмень» — 86
- «квартира с неузаконенной перепланировкой» — 17
- «риски покупки квартиры с неузаконенной перепланировкой» — 72

## meme_picks (from cover-text.json)

- cover: roll_safe, grumpy_cat
- inline_1: roll_safe
- inline_5: grumpy_cat
- inline_7: roll_safe

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B10: sage cardigan left, elderly phone viewing
- B06: lemon yellow shirt medium right window
- B05: terracotta sweater right entrance steps

**Required:** light/bright #FFF high-key, sun flare; roll_safe people-meme + grumpy_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B10 apartment viewing phone; B06 panoramic window price chart; B05 entrance discount tag.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table_ui — «Скидка за «красивую» кухню — и аванс уже ушёл»
Labels: Скидка за кухню | Аванс до сверки | План не сверили | До аванса — сверка
Meme: roll_safe tiny corner

### inline_2 — bar_timeline_chart — «Документы в МФЦ — ждали ключи через 9–14 дней»
Labels: МФЦ принял пакет | Ждали 9–14 дней | Право ещё не ваше | Деньги уже в игре
NO meme

### inline_3 — workflow_diagram — «Финал: Росреестр приостановил регистрацию перехода права»
Labels: Статья 26 — пауза | План не совпал | Собственником не стали | Спор про стену
NO meme

### inline_4 — checklist_board — «Открытая кухня сама по себе не приговор»
Labels: Не всегда нарушение | Ненесущую согласуют | Штраф 2–2,5 тыс. | Инженер, не фото
NO meme

### inline_5 — comparison_table — «Что сравнивают: ЕГРН, техдокументы и фактическая планировка»
Labels: Выписка ЕГРН | Техпаспорт и план | Факт на осмотре | Три слоя сверки | До аванса — инженер
Meme: grumpy_cat tiny corner

### inline_6 — schema_faq_ui — «Приостановление по ст. 26 и отказ по ст. 27 — в чём разница»
Labels: Ст. 26 — пауза | До 3 месяцев | Ст. 27 — отказ | Не собственник до записи | 207-ФЗ с 2026
NO meme

### inline_7 — tool_screenshot — «Согласование перепланировки в Тюмени: куда идти и сколько ждать»
Labels: Не Госжилинспекция | Управы четырёх округов | Проект в управу | До 45 дней | В ЕГРН — финал
Meme: roll_safe tiny corner

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «Скидка», ONE yellow sticky only, ZERO Wordstat strips on canvas.
