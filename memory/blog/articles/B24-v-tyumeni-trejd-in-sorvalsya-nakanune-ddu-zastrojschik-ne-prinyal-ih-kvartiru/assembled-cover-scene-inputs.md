# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени занизили оценку на 1,2 млн — трейд-ин сорвался перед ДДУ
- hook (cover-text): «Квартиру оценили ниже — бронь сорвалась» (highlight: «ниже»)
- sticky: «Цена оказалась другой»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья забронировала новостройку под trade-in «в зачёт» → за 24–36 часов до ДДУ оценщик снизил старую квартиру на 1,2 млн → первоначального взноса не хватило → ДДУ не подписали → бронь сняли, планировка и акция ушли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4670
- «купить новостройку в тюмени» — 899
- «ипотека новостройка тюмень» — 201

## meme_picks (from cover-text.json)

- cover: distracted_boyfriend
- inline_7: change_my_mind

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось в последних обложках.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room side_eye_chloe
- B22: lemon yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; distracted_boyfriend tiny people-meme sticker; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer trade-in desk with appraisal report and layout model — NOT bank, NOT MFC, NOT handover room).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «В зачёт» обещали — и семья забронировала новостройку (pair with inline_2)
Labels: Север Тюмени | Квартира в зачёт | Ориентир менеджера | Бронь новостройки
NO meme — bright newbuild sales corner: family brochure, reservation receipt, layout plan pinned

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь не выкуп | Партнёр оценивает | Сумма не подтверждена | Договор отдельно
NO meme — two columns: бронь новостройки vs условия выкупа старой квартиры

### inline_3 — realistic_photo — Между бронью и ДДУ trade-in ещё не закрыт
Labels: Минус 1,2 миллиона | За 24–36 часов | До подписания | Бюджет не сходится
NO meme — calendar countdown 24h, appraisal envelope unopened, gap between documents

### inline_4 — realistic_photo — За сутки до подписания оценка упала на 1,2 миллиона
Labels: Взноса не хватило | Ипотека не закрыла | Договор не подписали | Эскроу пустой
NO meme — appraisal report with crossed-out higher sum, empty escrow account printout, DDU folder closed

### inline_5 — process_flow — Первоначального взноса не хватило — ДДУ не подписали
Labels: Бронь сняли | Планировка ушла | Акция сгорела | До эскроу не дошли
NO meme — numbered flow: бронь → оценка ↓ → взнос не сходится → ДДУ отменён → эскроу пуст

### inline_6 — bar_timeline_chart — Бронь сняли, планировка и акция ушли другим
Labels: Два отдельных договора | Минимум выкупа | Срок оценки | Возврат брони
NO meme — bar chart comparing сроки оценки vs срок брони, two contract tracks

### inline_7 — structure_diagram — Что проверить до брони при trade-in — таблица
Labels: Документ на выкуп | Методика оценки | Срок до договора | Не платить вслепую
Meme: change_my_mind tiny corner sticker — blocks/arrows: старая квартира → оценка → взнос → ДДУ

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt" },
    ...
  }
}
```
