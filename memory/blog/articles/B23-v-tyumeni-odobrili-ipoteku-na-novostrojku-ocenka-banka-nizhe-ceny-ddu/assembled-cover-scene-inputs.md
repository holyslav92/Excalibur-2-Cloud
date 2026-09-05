# Cover-scene inputs — B23

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B23
- tenant: The Риэлтор, Тюмень
- H1: Ипотеку в Тюмени одобрили: оценка ниже на 400 тысяч — бронь сгорела
- hook (cover-text): «Банк урезал ипотеку на 400 тысяч» (highlight: «урезал»)
- sticky: «Бронь уже не вернуть»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение + бронь новостройки → за неделю до ДДУ банковская оценка ниже цены ДДУ на ~400 тыс → кредит урезали → собственных не хватило → ДДУ не подписали → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «ипотека в тюмени на новостройки» — 41
- «оценка квартиры для ипотеки» — 24
- «оценка квартиры банком для ипотеки» — 10

## meme_picks (from cover-text.json)

- cover: confused_math_lady, pop_cat
- inline_1: wojak
- inline_5: james_doakes
- inline_7: disappointed_black_guy

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B22: bank mortgage desk full-body center lemon shirt (disaster_girl) — НЕ повторять банковский кабинет
- B20: terracotta overshirt MFC corridor
- B19: turquoise polo showroom knee-up
- B15: white shirt sand vest waist center envelope

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady people-meme + pop_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright appraisal pickup zone / developer contract lounge with floor plan — NOT bank office duplicate).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### cover
Host waist-right at bright newbuild contract lounge table; holds appraisal report with lower number vs DDU price card; incredulous pointing; confused_math_lady + pop_cat tiny stickers; hook + phone sacred zone left.

### inline_1 — realistic_photo — pair with inline_2 — «Ипотеку одобрили» — семья забронировала
Labels: Семейная ипотека 6% | Взнос 20% | Бронь оплачена | Одобрение не договор
Meme: wojak tiny corner — bright sales office reservation receipt + mortgage pre-approval letter on white desk

### inline_2 — comparison_table — pair with inline_1
Labels: Бронь не фиксирует цену | Банк проверяет залог | Оценка после брони | Стоимость решает банк
NO meme — two-column table reservation vs bank collateral check

### inline_3 — realistic_photo — Между одобрением и ДДУ банк смотрит на объект
Labels: Отчёт в пятницу | Подписание уже назначено | Два разных числа | Цена и оценка
NO meme — appraisal envelope on bright table next to calendar with signing date circled

### inline_4 — realistic_photo — За неделю до подписания пришёл отчёт об оценке
Labels: Минус 400 тысяч | Кредит от оценки | До 85% стоимости | Четыре дня решения
NO meme — open appraisal report showing lower valuation, red minus 400k annotation, bright editorial

### inline_5 — process_flow — Разрыв 400 тысяч — кредита не хватило, бронь сгорела
Labels: Бронь истекла в среду | Деньги не вернули | ДДУ не подписали | Оценка 3–6 тысяч
Meme: james_doakes tiny corner — numbered failure chain with expired reservation stamp

### inline_6 — bar_timeline_chart — Что проверить до ДДУ
Labels: Спросить про оценку | Проверить сумму кредита | Срок отчёта 3–6 месяцев | Прочитать договор брони
NO meme — horizontal checklist timeline bars before DDU signing

### inline_7 — structure_diagram — Между одобрением и ДДУ банк смотрит на объект
Labels: Вопрос банку заранее | До эскроу можно стоп | Один звонок менеджеру | Бронь дороже месяца
Meme: disappointed_black_guy tiny corner — flowchart approval → appraisal → credit limit → escrow gate

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
