# Cover-scene inputs — B21

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B21
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени в КП обещали газ и воду — на ключах коммуникации не подвели
- hook (cover-text): «У забора пусто — ключи не взяли» (highlight: «пусто»)
- sticky: «Акт не подписали»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семья приехала за ключами от дома в коттеджном посёлке; у забора нет точек газа и воды; граница участка не совпала с генпланом; мотивированный отказ от акта; спор про односторонний акт и ипотечный транш

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «коттеджные поселки тюмень купить дом» — 59
- «расторжение дду» — 123
- «дом в коттеджном поселке» — demand spine

## meme_picks (from cover-text.json)

- cover: this_is_fine_dog, capybara_indifference
- inline_1: side_eye_chloe
- inline_5: yelling_at_clouds
- inline_7: change_my_mind

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20 (YESTERDAY): terracotta overshirt MFC corridor two_buttons — avoid MFC/office duplicate
- B19: turquoise polo showroom
- B15: white shirt sand vest envelope

**Required:** light/bright #FFF high-key, sun flare; countryside fence/gate setting NOT office; this_is_fine_dog people-meme + capybara_indifference cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; host NOT default black blazer left bust.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «В субботу у забора пусто: семья пришла на «ключи» и не подписала акт»
Labels: Суббота утром | У забора пусто | Нет точки газа | Нет точки воды | Акт не подписали
Meme: side_eye_chloe tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Газ в посёлке | Вода на улице | Труба мимо участка | Техническая возможность | Разрешение не ввод
NO meme — five formula rows comparing marketing phrases vs actual utility readiness

### inline_3 — realistic_photo — «Газ в посёлке» и вода «на улице» — не одно и то же с вводом на участок
Labels: Граница не совпала | Генплан из офиса | Выписка ЕГРН | Кадастровый номер | Буклет не договор
NO meme — bright countryside plot: colorful sales brochure vs cadastral map mismatch at fence

### inline_4 — realistic_photo — «Генплан в буклете и участок в выписке: второй спор в тот же осмотр»
Labels: Мотивированный отказ | Фото у забора | Видео обхода | Односторонний акт | Транш не выдали
NO meme — phone showing video timestamp + unsigned acceptance act on car hood at fence

### inline_5 — process_flow — «Ключи не взяли: застройщик надавил на односторонний акт»
Labels: Деньги у застройщика | Десять рабочих дней | Ввод комплекса | Платежи идут | Кредитный договор
Meme: yelling_at_clouds tiny corner — flowchart motivated refusal vs one-sided act vs mortgage tranche

### inline_6 — bar_timeline_chart — «Что сверять перед покупкой дома в КП — таблица формул и документов»
Labels: ДДУ с приложениями | Проектная декларация | Выписка на участок | Точка подключения | Письменный ответ
NO meme — checklist bar chart of five document sources before advance payment

### inline_7 — structure_diagram — «Эскроу, ипотека и отказ от акта: что не зависит от вашей подписи»
Labels: Договор на столе | Перечень несоответствий | До аванса проверка | Позиция на бумагах | Не устное обещание
Meme: change_my_mind tiny corner — diagram escrow release vs buyer signature vs mortgage tranche

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
