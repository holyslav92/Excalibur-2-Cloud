# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риёлтор, Тюмень
- H1: В Тюмени второй транш ипотеки вырос на 480 тысяч — ДДУ остановили
- hook (cover-text): «Второй транш увеличил платёж на сорок тысяч» (highlight: «сорок»)
- sticky: «ДДУ остановили вовремя»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: траншевая ипотека на новостройку → маленький платёж на стройке → за день до ДДУ полный график показал +40 тыс/мес после второго транша (+480 тыс/год нагрузки) → ставка не менялась → семья остановила ДДУ до эскроу

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4560
- «ипотека на новостройки тюмень» — 49
- «траншевая ипотека новостройка» — 4

## meme_picks (from cover-text.json)

- cover: confused_math_lady, doge
- inline_1: disappointed_black_guy
- inline_5: long_cat
- inline_7: stonks

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater newbuild handover side_eye_chloe full-body right
- B22: lemon yellow shirt mortgage bank desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two_buttons
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + doge cat-meme small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank desk duplicate (B22); NOT showroom cancel card (B19); NEW location — bright newbuild sales lounge with construction view and tranche payment timeline on table.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### cover
Hook zone sacred upper-right. Host kneeling at glass coffee table with two-column tranche payment chart (small first payment vs huge second). Yellow sticky «ДДУ остановили вовремя». Phone CTA bottom. confused_math_lady top-left corner, doge bottom-left tiny.

### inline_1 — realistic_photo — «Платёж на стройке» — семья забронировала новостройку (pair with inline_2)
Labels: Бронь оформлена | Ипотека одобрена | Малый платёж | Не весь кредит
Meme: disappointed_black_guy tiny corner
Bright Tyumen newbuild sales desk, reservation receipt, low payment quote on tablet — NO host face

### inline_2 — comparison_table — pair with inline_1
Labels: Одобрение не платёж | Деньги частями | Проценты на выдачу | График до подписи | Дата второго транша
NO meme — two-column table first tranche vs full loan

### inline_3 — realistic_photo — Между одобрением и ДДУ: что показывали в расчёте
Labels: За день до ДДУ | Плюс сорок тысяч | 480 тысяч в год | Ставка не менялась | Временный платёж
NO meme — bright office printout with crossed-out small payment and red arrow to larger monthly sum

### inline_4 — realistic_photo — За день до подписания: второй транш пересчитали
Labels: ДДУ не подписали | Эскроу не открыли | Бронь отдельно | До перевода денег | Бюджет не сошёлся
NO meme — unopened DDU folder with STOP sticky, escrow form blank, keys still in envelope

### inline_5 — process_flow — Семья развернулась: ДДУ не подписали, эскроу не открыли
Labels: Деньги частями | Второй через месяц | До ключей бывает | Аренда плюс ипотека | Доход не перепроверят
Meme: long_cat tiny corner — flow diagram two tranches arrow to full payment while crane still on site

### inline_6 — bar_timeline_chart — Как устроен второй транш — и почему платёж скачет
Labels: Полный график | Проект ДДУ | Задержка сдачи | Расчёт программы | Договор брони
NO meme — bar chart low bar then spike at second tranche date

### inline_7 — structure_diagram — Что проверить до ДДУ — таблица
Labels: До подписания ДДУ | График траншей | Платёж после остатка | Проверка до аванса
Meme: stonks tiny corner — checklist diagram four boxes with gold tape corners

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    "inline_2": { "scene_hint", "alt" },
    "inline_3": { "scene_hint", "alt" },
    "inline_4": { "scene_hint", "alt" },
    "inline_5": { "scene_hint", "alt", "meme_picks" },
    "inline_6": { "scene_hint", "alt" },
    "inline_7": { "scene_hint", "alt", "meme_picks" }
  }
}
```
