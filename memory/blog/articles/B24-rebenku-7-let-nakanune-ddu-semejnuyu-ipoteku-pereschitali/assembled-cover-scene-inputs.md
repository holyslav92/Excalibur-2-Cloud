# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени ребёнку исполнилось 7 лет накануне ДДУ — семейную ипотеку пересчитали
- hook (cover-text): «Ребёнок вырос — банк изменил платёж» (highlight: «платёж»)
- sticky: «Одобрение не равно кредиту»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека одобрена при ребёнке 6 лет → бронь новостройки → за 6 дней до ДДУ ребёнку 7 → банк пересчитал льготу → платёж не влез → отказ до эскроу → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень» — 1210
- «семейная ипотека в тюмени» — 752
- «новостройки тюмени семейная ипотека» — 27

## meme_picks (from cover-text.json)

- cover: confused_math_lady
- inline_7: surprised_pikachu

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt handover room DDU vs EGRN keys
- B22: lemon shirt bank mortgage desk rate letter calculator
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme small sticker; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright home kitchen-living with birthday calendar + mortgage papers, NOT bank desk duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Семейную ипотеку одобрили — и семья забронировала новостройку (pair with inline_2)
Labels: Ребёнку было шесть | Предварительное одобрение | Плата за бронь | Платёж в бюджете | Одобрение не кредит
NO meme — bright newbuild sales corner with reservation receipt and approval stamp

### inline_2 — comparison_table — pair with inline_1
Labels: Заявка, бронь, ДДУ | Дата кредитного договора | ДДУ не заменяет дату | День рождения в календаре | Бронь по сроку
NO meme

### inline_3 — realistic_photo — За шесть дней до подписания ребёнку исполнилось семь лет
Labels: Шесть дней до ДДУ | Исполнилось семь лет | Кредит ещё не подписан | До шести включительно | Банк смотрит дату
NO meme — wall calendar with birthday circle and DDU date marked

### inline_4 — realistic_photo — Банк пересчитал семейную ипотеку — платёж и лимит разъехались с бронью
Labels: Право на льготу | Ставка до 6% | Платёж не влез | Рыночный кредит отдельно | Бронь не спасает
NO meme — bright desk with two payment calculations side by side

### inline_5 — structure_diagram — Банк пересчитал (pair section with inline_4)
Labels: Льготная часть 6 млн | Комбинированный кредит | Цена не равна лимиту | Пересчитали весь платёж | Одна льготка на семью
NO meme

### inline_6 — process_flow — Семья остановилась: бронь сгорела, до эскроу деньги не дошли
Labels: Отказ от кредита | Срок брони кончился | До эскроу не дошли | Квартира ушла | Неподъёмный платёж
NO meme

### inline_7 — labeled_checklist — Что проверить до брони и подписания — таблица
Labels: День рождения ребёнка | Дата кредитного договора | Условия брони | Полный расчёт платежа | Проверки банка впереди
Meme: surprised_pikachu tiny corner

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
