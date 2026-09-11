# Cover-scene inputs — B24

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B24
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик продал 1 квартиру 2 семьям — второй ДДУ остановили
- hook (cover-text): «Одну квартиру пообещали сразу двум семьям» (highlight: «квартиру»)
- sticky: «Как так вышло?»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: CRM дважды показала «свободна», первая семья зарегистрировала ДДУ, вторая оплатила бронь и получила ипотеку; второй договор остановили до эскроу; застройщик предложил другой этаж с доплатой

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 3657
- «купить новостройку в тюмени» — 651
- «договор долевого участия» — 274

## meme_picks (from cover-text.json)

- cover: confused_math_lady, long_cat
- inline_1: surprised_pikachu
- inline_5: james_doakes
- inline_7: wojak

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt mustard sweater handover room side_eye_chloe
- B22: yellow shirt bank mortgage desk disaster_girl full-body center
- B20: terracotta overshirt MFC corridor two DDU
- B19: turquoise polo showroom cancel card

**Required:** light/bright #FFF high-key, sun flare; confused_math_lady + long_cat small stickers; NO Wordstat query strips/bars; NO dark cinematic; NO daypart formula; NEW location — bright developer sales office with dual CRM screens showing same apartment number twice, NOT bank/MFC/handover duplicate.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Банк приостановил сделку до выяснения статуса квартиры
Labels: Ипотека на паузе | Эскроу пусто | Деньги не ушли | Сообщение банка
Meme: surprised_pikachu tiny corner — bright bank notification on desk, mortgage paused stamp

### inline_2 — process_flow — pair with inline_1
Labels: Тот же номер | Первый договор подписан | Ипотека одобрена | Два комплекта
NO meme — numbered flow: бронь → ДДУ → регистрация → конфликт

### inline_3 — realistic_photo — Два «свободно» в CRM — и две семьи на одну квартиру
Labels: Север Тюмени | Статус «свободна» | Потом бронь | Бронь оплачена
NO meme — bright sales office monitor with CRM card flipping free→reserved

### inline_4 — realistic_photo — Бронь, ДДУ и эскроу: что подтверждает каждый документ
Labels: Система — статус | Бронь — удержание | Договор — право | Реестр — барьер | Эскроу — деньги
NO meme — documents spread on bright table: CRM printout, booking agreement, DDU, escrow card

### inline_5 — comparison_table — Первая семья подписала ДДУ, вторая получила одобрение ипотеки
Labels: Другой этаж | Просят доплату | Претензия отправлена | Возврат брони
Meme: james_doakes tiny corner — table comparing CRM vs registry vs booking

### inline_6 — bar_timeline_chart — Первый договор зарегистрировали — второй ДДУ остановили
Labels: Запись в реестре | Второй договор остановлен | Тот же номер | Даты сохраните
NO meme — timeline chart with registration milestone blocking second DDU

### inline_7 — structure_diagram — Застройщик предложил другой этаж с доплатой
Labels: Проверьте регистрацию | Сохраните переписку | Не подписывайте вслепую | «Свободна» — не проверка
Meme: wojak tiny corner — diagram: CRM status vs Rosreestr record vs escrow

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
