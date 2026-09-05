# Cover-scene inputs — B23

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B23
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени трейд-ин сорвался за день до ДДУ — бронь сгорела
- hook (cover-text): «Оценку квартиры снизили — бронь сгорела» (highlight: «снизили»)
- sticky: «Минус 600 тысяч за сутки»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: трейд-ин как первоначальный взнос → бронь новостройки → три недели ожидания → за сутки до ДДУ партнёр пересмотрел выкупную цену −400–600 тыс. → взнос не сходится → ДДУ не подписали → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «трейд ин новостройка» — 479
- «новостройки трейд ин от застройщика» — 121
- «трейд ин тюмень» — локальный сигнал

## meme_picks (from cover-text.json)

- cover: confused_math_lady, woman_yelling_cat
- inline_5: woman_yelling_cat
- inline_7: confused_math_lady

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B22: lemon yellow shirt bank mortgage desk disaster_girl (center full-body)
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card
- B15: white shirt sand vest envelope center

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + woman_yelling_cat cat-half tiny stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NOT bank office duplicate (B22); NEW location = bright trade-in evaluation nook at newbuild sales lounge with two property folders and messenger valuation screenshot on tablet.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Старая квартира в счёт новой» — и семья забронировала лот (pair with inline_2)
Labels: Две сделки | Предварительная оценка | Лот забронировали вечером | Взнос из выкупа | Юридически это бронь
NO meme — bright sales lounge, two separate contract folders, reservation receipt

### inline_2 — comparison_table — pair with inline_1
Labels: Три недели ожидания | Цена не заморожена | Ипотеку одобрили | Оценка имеет срок
NO meme — two columns: бронь новостройки vs оценка вторички

### inline_3 — realistic_photo — Три недели между бронью и датой ДДУ
Labels: Брусника: месяц оценки | Паритет меняет условия | Квартира не взнос | Цепочка может рваться
NO meme — calendar wall + aging preliminary valuation printout

### inline_4 — realistic_photo — За сутки до подписания — повторная оценка трейд-ин
Labels: Звонок вечером | ДДУ утром | Новая сумма | Минус 400–600 тысяч | Предварительная оценка
NO meme — smartphone messenger with lower valuation screenshot on bright kitchen table

### inline_5 — structure_diagram — пересчёт оценки / дисконт (pair context)
Labels: Оценку пересчитали | Дисконт 15–25% | Два договора | Разрыв трейд-ина | Нет письменных гарантий
Meme: woman_yelling_cat tiny corner (cat half only)

### inline_6 — process_flow — ДДУ не подписали — бронь сгорела, лот ушёл
Labels: ДДУ не подписали | Бронь истекла | Плата ушла | Лот забрали | Банк ни при чём
NO meme — numbered chain breaking at trade-in step

### inline_7 — labeled_checklist — Что проверить до брони и ДДУ — таблица
Labels: Кто покупает старую | Срок оценки | Кто меняет цену | Связь брони и трейд-ина | Комиссия и дисконт
Meme: confused_math_lady tiny corner

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
