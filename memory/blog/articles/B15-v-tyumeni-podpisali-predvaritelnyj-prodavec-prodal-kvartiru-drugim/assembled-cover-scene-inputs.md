# Cover-scene inputs — B15

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B15
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени подписали предварительный договор — квартиру продали другим
- hook (cover-text): «Договор подписали — квартиру продали другим» (highlight: «продали»)
- sticky: «Деньги не вернут квартиру»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительный + задаток + ипотека одобрена; через 2 недели продавец заключил основной с другими; задаток вернули по штрафу, квартиру — нет

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «предварительный договор купли продажи квартиры» — 62 (55+11176)
- «с задатком» — 3166
- «предварительный договор купли продажи» — 20590

## meme_picks (from cover-text.json)

- cover: two_buttons, polite_cat
- inline_1: side_eye_chloe
- inline_5: wojak
- inline_7: pepe_frog

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B12: light blue shirt sand chinos waist right letter payment
- B10: sage cardigan left elderly phone viewing
- B06: lemon yellow shirt medium right window

**Required:** light/bright #FFF high-key, sun flare; two_buttons people-meme + polite_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula.

## Anti-repeat used-motifs (14d) — avoid collision

B12 showroom letter payment; B10 apartment viewing phone; B06 panoramic window price chart.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Подписали предварительный — ипотеку одобрили, дату сделки назначили»
Labels: Предварительный подписан | Задаток передан | Ипотека одобрена | Дата сделки в календаре | Статья 429 — обещание
Meme: side_eye_chloe tiny corner

### inline_2 — process_flow — «Через две недели продавец заключил основной договор с другими»
Labels: Через две недели | Три дня до сделки | Основной с другими | Документы на регистрацию | Выписка без красного флага
NO meme

### inline_3 — bar_timeline_chart — «Финал: квартиру зарегистрировали за другими, задаток вернули по штрафу»
Labels: Право за другими | Задаток по штрафу | Не двойной возврат | Ипотечный аванс остановили | Квартиру не вернули
NO meme

### inline_4 — structure_diagram — «Предварительный договор — обещание, а не запись в ЕГРН»
Labels: Не запись в ЕГРН | Госрегистрации нет | Собственник распоряжается | Пункт шесть — тихий | Без срока — год
NO meme

### inline_5 — labeled_checklist — «Задаток, аванс и ипотечный аванс — три разных платежа»
Labels: Задаток или аванс | Штраф вместо удвоения | Три разных платежа | Ипотечный аванс отдельно | Текст договора решает
Meme: wojak tiny corner

### inline_6 — fact_card — «Понуждение, штраф и убытки: что реально можно требовать»
Labels: Понуждение шесть месяцев | После регистрации — деньги | Убытки доказываются | Три трека отдельно | Оспаривание — исключение
NO meme

### inline_7 — workflow_diagram — «Таблица: что покупатель ожидает от ПДКП и что даёт закон»
Labels: Ожидание — бронь | Закон — обещание | Выписка без вашей сделки | Суд не вернёт квартиру | Предложение письменно в срок
Meme: pepe_frog tiny corner

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
  "wordstat_stickers": ["...", "...", "..."],
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, gold highlight «продали», ONE yellow sticky only, ZERO Wordstat strips on canvas.
