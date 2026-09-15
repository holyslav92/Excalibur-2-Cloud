# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ
- hook (cover-text): «Банк заблокировал ипотеку перед сделкой» (highlight: «заблокировал»)
- sticky: «Одобрили — и всё изменилось»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: предодобрение ипотеки + бронь 180 тыс → за 24 часа до ДДУ банк снял корпус с аккредитации → ипотека «замерла» → эскроу не открыли → выбор: другой банк / продление брони / смена квартиры

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «купить новостройку в тюмени» — 909
- «новостройки в тюмени от застройщика» — 668
- «ипотека новостройка тюмень» — 189

## meme_picks (from cover-text.json)

- cover: woman_yelling_cat
- inline_1: surprised_pikachu
- inline_5: crying_cat
- inline_7: (agent may add one tiny meme if fits bar_timeline_chart — optional drake_hotline_bling or distracted_boyfriend; keep ≤15%)

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive knit vest bank mortgage desk hide_pain_harold waist-up right
- B25: terracotta shirt kneeling bare apartment confused_math_lady
- B23: light blue shirt mustard sweater handover room
- B22: lemon shirt bank rate letter full-body center

**Required:** light/bright #FFF high-key, sun flare; woman_yelling_cat people-meme + cat sticker small; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NEW location (bright developer sales lounge with accreditation board OR sunny balcony overlooking construction + bank push notification).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Что проверить в день сделки — таблица (pair with inline_2)
Labels: Предварительное одобрение | Корпус в списке | Аккредитация корпуса | Не весь застройщик | Логотип не гарантия
Meme: surprised_pikachu tiny corner

### inline_2 — process_flow — pair with inline_1
Labels: Квартира забронирована | Одобрение отдельно | Сроки не совпали | Договор бронирования | Продление письменно
NO meme

### inline_3 — realistic_photo — «Ипотеку одобрили» — и корпус был в списке банка
Labels: Сообщение от банка | Новые сделки остановлены | Бронь продолжает идти | ДДУ без денег | Подпись не спасает
NO meme — bright phone screen bank push + DDU folder on kitchen table

### inline_4 — realistic_photo — Между бронью и ДДУ тикают два разных срока
Labels: Заёмщик без изменений | Корпус сняли | Эскроу не открыт | Другой банк | Возврат брони
NO meme — dual countdown calendars reservation vs approval expiry

### inline_5 — structure_diagram — За сутки до подписания банк снял корпус с аккредитации
Labels: ДДУ не подписан | Эскроу не открыт | Деньги не ушли | Бронь отдельно | Без спешки
Meme: crying_cat tiny corner

### inline_6 — comparison_table — Одобрение на человека есть — а объект из списка исчез
Labels: Кредит не оформлен | Продление брони | Другой банк | Смена квартиры | Не подписывать вслепую
NO meme — columns borrower OK vs building removed from list

### inline_7 — bar_timeline_chart — Семья остановилась: эскроу не открыли, деньги не ушли
Labels: Аккредитация корпуса | Срок предодобрения | Причина снятия | Условия брони | Путь до эскроу | Другие банки напрямую
Optional tiny meme corner if utility clear

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
