# Cover-scene inputs — B22

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B22
- tenant: The Риэлтор, Тюмень
- H1: В Тюмени застройщик потребовал акт с дефектами — иначе без ключей
- hook (cover-text): «Ключи требуют — дефекты оставляют вам» (highlight: «дефекты»)
- sticky: «Подписывать не спешите»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: приёмка новостройки в Тюмени — длинный список дефектов, ультиматум «подписывайте сегодня, иначе ключей не будет», семья фиксирует акт осмотра, ключи не выдали, ипотека не остановилась

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «приемка квартиры в новостройке» — 6287
- «новостройки тюмень» — 4683
- «акт приемки квартиры в новостройке» — 256

## meme_picks (from cover-text.json)

- cover: sacrednik_priest, pop_cat
- inline_1: side_eye_chloe
- inline_5: zhirinovsky
- inline_7: expanding_brain

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B20: terracotta overshirt MFC corridor right three-quarter (YESTERDAY — avoid MFC duplicate)
- B19: turquoise polo showroom knee-up right cancel card
- B15: white shirt sand vest waist center envelope
- B12: light blue shirt showroom waist right

**Required:** light/bright #FFF high-key, sun flare; sacrednik_priest people-meme + pop_cat cat small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT showroom/MFC like B19/B20; scene = пустая квартира на приёмке с дефектами.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — Устное «всё устраним» и почему ключи зависят от бумаги
Labels: Два часа обхода | Десятки дефектов | Акт в двух экземплярах | Ключи не выдали
Meme: side_eye_chloe tiny corner
Pair with inline_2 on same H2

### inline_2 — comparison_table — pair with inline_1
Labels: Передаточный акт — передача | Акт осмотра — дефекты | Два экземпляра с датой | Отказ в документе
NO meme

### inline_3 — realistic_photo — Финал: отказ от «чистого» акта — ключи не выдали, ипотека не остановилась
Labels: Обещание не обязательство | Ипотека не остановится | Каникул не дадут | Платежи на два месяца
NO meme — closed apartment door, mortgage payment notification on phone screen, no people hero

### inline_4 — realistic_photo — Что проверить на приёмке: документы, дефекты и ипотека
Labels: Без замечаний не подписали | Переписка вместо суда | Платеж по графику | Повторный осмотр
NO meme — checklist folder on windowsill in bright empty newbuild apartment

### inline_5 — process_flow — Два часа на приёмке: длинный список и требование подписать «как есть»
Labels: Отказ фиксируют в акте | Фото по комнатам | Письмо с описью | Перечень недостатков
Meme: zhirinovsky tiny corner

### inline_6 — bar_timeline_chart — Передаточный акт и акт осмотра — что вы реально подписываете
Labels: Статья 8 часть 6 | Приехали в назначенный день | Постановление 2226 | Независимая фиксация | Не уклонялись от приемки
NO meme

### inline_7 — structure_diagram — Существенные и несущественные недостатки: где проходит черта
Labels: ДДУ со спецификацией | Уведомление за месяц | Специалист НОСТРОЙ | Рулетка и уровень | Лимит три процента
Meme: expanding_brain tiny corner

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
