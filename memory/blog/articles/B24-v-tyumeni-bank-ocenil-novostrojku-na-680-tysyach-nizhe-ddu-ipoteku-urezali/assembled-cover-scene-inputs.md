# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: За 5 дней до эскроу — банк урезал ипотеку на 680 тысяч
- hook (cover-text): «Банк урезал ипотеку перед эскроу» (highlight: «урезал»)
- sticky: «Одобрение ещё не кредит»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предварительное одобрение → ДДУ подписан → банк заказал оценку строящейся квартиры → оценка на 680 тыс. ниже ДДУ → за 5 дней до эскроу кредит урезали → своих денег не хватило → бронь сгорела

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3593
- «ипотека новостройка» — 398
- «купить новостройку в тюмени» — 688

## meme_picks (from cover-text.json)

- cover: hide_pain_harold, smudge_cat
- inline_1: roll_safe
- inline_5: disappointed_black_guy
- inline_7: confused_math_lady

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room (side_eye_chloe)
- B22: yellow shirt bank mortgage office (disaster_girl)
- B20: terracotta overshirt MFC corridor
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; hide_pain_harold people-meme + smudge_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location (bright appraisal desk with DDU vs appraisal report contrast, NOT duplicate B22 bank office).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья подписала ДДУ в новостройке (pair with inline_2)
Labels: Север Тюмени | Бронь оплачена | ДДУ подписан | Одобрение предварительное | Лимит не финальный
Meme: roll_safe tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Оценка квартиры | Документы проекта | Цена застройщика | Меньшая база | Отчёт не всегда нужен
NO meme

### inline_3 — realistic_photo — Между договором и эскроу банк заказал оценку строящейся квартиры
Labels: Минус 680 000 ₽ | Цена в ДДУ | Банк считает иначе | Кредит не зафиксирован | Нужен расчёт банка
NO meme — bright appraisal documents on desk

### inline_4 — realistic_photo — Оценка оказалась на 680 тысяч ниже цены в ДДУ
Labels: Пять дней | До эскроу | Новый лимит утром | Денег не хватило | Повторная оценка
NO meme — calendar 5 days + reduced credit letter

### inline_5 — structure_diagram — За пять дней до эскроу кредит урезали
Labels: Покупку остановили | Бронь сгорела | Квартира снова продаётся | Бронь не вернули | ДДУ подписан
Meme: disappointed_black_guy tiny corner

### inline_6 — process_flow — Сделку остановили: бронь сгорела
Labels: Эскроу не открыли | Бронь оплачена | Договор не отменён | Не хватило 680 тысяч | Срыв не бесплатный
NO meme

### inline_7 — bar_timeline_chart — Что сверять до открытия эскроу
Labels: Цена в ДДУ | Лимит банка | Оценка квартиры | Свои средства | Условия брони
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
