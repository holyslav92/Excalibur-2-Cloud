# Cover-scene inputs — B22

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B22
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени на приёмке не хватило метров — застройщик отказал в пересчёте
- hook (cover-text): «В квартире пропали два метра» (highlight: «пропали»)
- sticky: «Это не допуск»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: приёмка новостройки — фактическая площадь меньше ДДУ на 2 м²; менеджер «в пределах допуска»; ключи на столе; шестизначная переплата

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 857
- «приемка квартиры в новостройке тюмень» — 35
- «площадь квартиры дду» — 11

## meme_picks (from cover-text.json)

- cover: disaster_girl, capybara_indifference
- inline_1: disappointed_black_guy
- inline_5: this_is_fine_dog
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20: MFC corridor terracotta overshirt two documents
- B19: turquoise polo showroom cancel card
- B15: white shirt sand vest envelope center
- B12: light blue shirt showroom waist right

**Required:** light/bright #FFF high-key, sun flare; disaster_girl people-meme + capybara_indifference cat sticker; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; empty newbuild acceptance scene NOT showroom NOT desk office.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — На приёмке не хватило двух метров — а в ДДУ оплачивали больше
Labels: Минус два метра | Площадь по договору | Обмер инженера | Шестизначная разница
Meme: disappointed_black_guy tiny corner
Pair with inline_2 on same H2 — buyer hands with tape measure on bare floor, DDU pages, keys on stool, sun through window, no host face

### inline_2 — comparison_table — pair with inline_1
Labels: Допуск в договоре | Цена твёрдая | Допуск не пересчёт | Подпишите сейчас
NO meme — white-gold collage table contrasting «допуск» vs «пересчёт»

### inline_3 — realistic_photo — «В пределах допуска»: как менеджер закрывает вопрос пересчёта
Labels: Три разные площади | Лоджия с коэффициентом | Толще стены | Сравнить методику
NO meme — three paper sheets with different area numbers on bright clipboard in empty room

### inline_4 — realistic_photo — Общая, приведённая, лоджия: где путают цифры
Labels: Цена за метр | Пересчёт в одну сторону | Пять процентов | Пункт до сделки
NO meme — balcony door + floor plan highlighting balcony coefficient, high-key Tyumen newbuild interior

### inline_5 — process_flow — Акт подписали с замечанием — застройщик отказал в возврате
Labels: Замечание в акте | Требование с суммой | Заказное письмо | Ключи не рычаг
Meme: this_is_fine_dog tiny corner — flow from weak remark to formal claim with sum

### inline_6 — bar_timeline_chart — Что сверять до подписи — таблица
Labels: Три документа | Техплан инженера | Цена из договора | Балкон с коэффициентом
NO meme — checklist timeline before signing act

### inline_7 — structure_diagram — Порог в ДДУ и техплан: где заканчивается «норма»
Labels: Пять процентов | Техплан и расчёт | Пересчёт только вверх | Сверка до акта
Meme: stonks tiny corner (ironic — meters went down not up)

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
