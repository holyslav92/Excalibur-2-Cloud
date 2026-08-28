# Cover-scene inputs — B12

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B12
- tenant: The Риэлтор, Тюмень
- H1: В Ялуторовске квартиру продали двоим — покупательнице грозит выселение
- hook (cover-text): «Квартиру продали двоим — кто останется?» (highlight: «двоим»)
- sticky: «Суда ещё нет»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: Ялуторовск — риелтор по доверенности продала одну квартиру двум покупателям; первой въехала, через год второй заплатил больше; попытка выселения; доследственная проверка; «хитрый пункт» о расторжении; ЕГРН не отвечает на вопрос «чей договор»

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «двойная продажа квартиры» — 281
- «аккредитив при покупке квартиры» — 45
- «проверка егрн» — 28

## meme_picks (from cover-text.json)

- cover: two_buttons, crying_cat
- inline_1: bad_luck_brian
- inline_5: blinking_white_guy
- inline_7: surprised_pikachu

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B10: sage cardigan left, elderly phone viewing
- B06: lemon yellow shirt medium right window
- B05: terracotta sweater right entrance steps
- B11: teal vest kitchen plan comparison

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + crying_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B10 apartment viewing phone; B06 panoramic window price chart; B05 entrance discount tag; B11 open kitchen plan.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — process_flow — «Ялуторовск: привлекательная цена — и сделка без подозрений»
Labels: Цена привлекательная | Сделка без задержек | Справки на руках | Почему дёшево?
Meme: bad_luck_brian tiny corner

### inline_2 — comparison_table_ui — «Через год: у той же квартиры появился второй покупатель»
Labels: Год спустя — второй | Два договора | Второй заплатил больше | Пытаются откатить сделку
NO meme

### inline_3 — workflow_diagram — «Риелтор по доверенности и «хитрый пункт» в договоре»
Labels: Выселение пока попытка | Доследственная проверка | Суда ещё нет | Вернут деньги — уйти
NO meme

### inline_4 — checklist_board — «Финал: покупательницу пытаются выселить — суда ещё нет»
Labels: Риелтор по доверенности | Продала двоим сразу | Деньги от обоих | Пункт о расторжении
NO meme

### inline_5 — structure_diagram — «Два договора и ЕГРН: почему выписка не отвечает на главный вопрос»
Labels: Выписка не всё покажет | Спор в договорах | Право на момент выдачи | Фактическое владение важно
Meme: blinking_white_guy tiny corner

### inline_6 — labeled_checklist — «Аккредитив и банковский расчёт: что могло бы изменить риск»
Labels: Расчёт не назван | Деньги через посредника | Аккредитив 3400 ₽ | Раскрытие после регистрации | Договор не отменит
NO meme

### inline_7 — comparison_table — «Что проверить до аванса: таблица и порядок действий»
Labels: Кто подписывает | ЕГРН заказал сам | Деньги после регистрации | Проверь расторжение | Акт и ключи
Meme: surprised_pikachu tiny corner

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «двоим», ONE yellow sticky only, ZERO Wordstat strips on canvas.
