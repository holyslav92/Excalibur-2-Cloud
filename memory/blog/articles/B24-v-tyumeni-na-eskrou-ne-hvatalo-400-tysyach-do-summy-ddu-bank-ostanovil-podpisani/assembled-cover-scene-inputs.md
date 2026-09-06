# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание
- hook (cover-text): «Банк остановил сделку из-за нехватки денег» (highlight: «нехватки»)
- sticky: «Эскроу открыт — денег мало»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: ипотека одобрена, эскроу открыт, первый транш и маткапитал зачислены — но на счёте 5,8 млн при цене ДДУ 6,2 млн; за 48 часов до подписания банк сверил суммы и остановил сделку; менеджер предлагал «подписать сейчас, доберём потом»

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4663
- «эскроу счет новостройка» — 2
- «семейная ипотека новостройка тюмень» — 28

## meme_picks (from cover-text.json)

- cover: disappointed_black_guy, long_cat
- inline_1: james_doakes
- inline_5: this_is_fine_dog
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: handover room, side_eye_chloe + pop_cat, light blue shirt mustard sweater
- B22: bank mortgage desk, disaster_girl + keyboard_cat, lemon yellow shirt
- B20: MFC corridor, two_buttons + surprised_tom, terracotta overshirt

**Required:** light/bright #FFF high-key, sun flare; disappointed_black_guy people-meme + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright escrow verification glass counter in newbuild sales office, NOT bank mortgage desk duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — За 48 часов до подписания банк сверил счёт (pair with inline_2)
Labels: Ипотека одобрена | Эскроу открыт | Первый транш пришёл | Одобрение не оплата
Meme: james_doakes tiny corner
Bright bank clerk desk with escrow statement printout and stop-stamp on DDU folder

### inline_2 — process_flow — pair with inline_1
Labels: ДДУ 6,2 миллиона | На счёте 5,8 | Не хватает 400 тысяч | Транш не весь кредит
NO meme — numbered flow escrow open → first tranche → DDU price check → 400k gap

### inline_3 — realistic_photo — «Ипотеку одобрили» — семья пошла подписывать ДДУ
Labels: Цена в договоре | Остаток на эскроу | График перечислений | Выписка по счёту
NO meme — happy family at newbuild sales desk with mortgage approval letter, bright Tyumen showroom

### inline_4 — realistic_photo — На эскроу 5,8 млн — в договоре 6,2
Labels: Подписать сейчас | Добрать позже | Нет даты платежа | Устное не график
NO meme — manager hand pushing pen toward DDU while escrow screen shows shortfall, bright office

### inline_5 — comparison_table — Менеджер просил подписать сейчас: «доберём потом»
Labels: Двое суток до подписи | Документы на столе | Сверка не сходится | Пауза не потеря
Meme: this_is_fine_dog tiny corner
Two-column table: «подписать сейчас» vs «дождаться полной суммы»

### inline_6 — bar_timeline_chart — Семья пересчитала график и через неделю подписала ДДУ
Labels: Неделя на расчёт | Внесли 400 тысяч | График согласовали | ДДУ подписали
NO meme — bar chart week timeline from pause to signed DDU

### inline_7 — structure_diagram — Что сверять до подписания ДДУ — таблица
Labels: Цена по ДДУ | Сумма кредита | Деньги на эскроу | График платежей | Маткапитал и взнос
Meme: stonks tiny corner
Five-node checklist diagram with red flag on escrow shortfall

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
