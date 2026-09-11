# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени рассрочку у застройщика просрочили на 4 дня — квартира ушла
- hook (cover-text): «Просрочили на четыре дня — квартира ушла» (highlight: «квартира»)
- sticky: «Квартира ушла навсегда»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья внесла 400 тыс., просрочила платёж на 4 дня, получила расторжение, вернули 180 тыс., квартиру показывают другому — «без банка» обманчиво просто

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «рассрочка от застройщика тюмень» — 137
- «квартира в рассрочку от застройщика тюмень» — 64
- «новостройки тюмень» — 4580

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: james_doakes
- inline_5: this_is_fine_dog
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: blue shirt mustard sweater handover room EGRN vs DDU full-body right
- B22: lemon yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom knee-up cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + long_cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/handover/MFC/showroom duplicate; NEW location (bright sunny developer installment consultation nook with payment calendar wall, NOT desk-only office).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — pair with inline_2 — «Вернули 180 тысяч — квартиру уже показывают другому»
Labels: Рассрочка застройщика | Взнос 400 тысяч | Без заявки банка | Бронь или договор | Намерение не право
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Оплата позже четырёх дней | Ждали зарплату | Письмо о расторжении | Деньги отправили | Квартира снова продаётся
NO meme

### inline_3 — realistic_photo — «Без банка» — и первый взнос 400 тысяч в новостройку
Labels: Вернули 180 тысяч | Удержали 220 тысяч | Квартиру показывают другому | Проверьте условия рассрочки
NO meme — bright refund letter 180 vs 400 on table

### inline_4 — realistic_photo — Четыре дня просрочки: письмо о расторжении пришло раньше зарплаты
Labels: Кому ушли деньги | Назначение платежа | Получатель и продавец | Дата зачисления | Бронь или ДДУ
NO meme — payment order on bright desk with +4 days calendar

### inline_5 — process_flow — Законная пеня и договорный штраф — это разные деньги
Labels: Пеня одна трёхсотая | Пеня около ста рублей | Удержали 220 тысяч | Тридцать дней погашения | Не ДДУ — другие правила
Meme: this_is_fine_dog tiny corner

### inline_6 — bar_timeline_chart — Три вопроса по платёжному поручению
Labels: Пакет до взноса | Условие о задержке | Не подписывайте вслепую | Соберите платёжки | Запросите расчёт удержаний
NO meme

### inline_7 — structure_diagram — Что сделать до перевода и если письмо уже пришло
Labels: Сверьте вид договора | Проверьте получателя | Зафиксируйте дату оплаты | Найдите основу штрафа | Ответьте по документам
Meme: wojak tiny corner

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
