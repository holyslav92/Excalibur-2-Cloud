# Cover-scene inputs — B08

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B08
- tenant: The Риэлтор, Тюмень
- H1: В объявлении бабушка — на сделке всплыла опека: регистрацию в Тюмени отменили
- hook (cover-text): «Скидка застряла из-за опеки» (highlight: «опеки»)
- sticky: «Аванс не спас сделку»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: продажа 1/3 доли по доверенности, бабушка 84 лет, скидка 2 млн, на регистрации всплыла опека — сделку отменили

## Wordstat stickers (manifest log only — NOT painted on canvas)

- «доверенность на продажу квартиры» — 97
- «купить квартиру в тюмени» — 22880

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow linen shirt, host right, panoramic window, price jump 18→20
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; NO Wordstat query strips on canvas.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right window.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — process_flow — «Коротко: что случилось в Тюмени»
Labels: Доля одна треть | Бабушке 84 года | Аванс 300 тысяч | Девятый день | Скидка 2 миллиона | Доверенность три года
Meme sticker: yes (small cat corner)

### inline_2 — comparison_table — «Живёт бабушка» — не одна проблема
Labels: Просто прописана | Совладелец квартиры | Пожизненное проживание | Опека и недееспособность | Не видно в ЕГРН
NO meme

### inline_3 — labeled_checklist — Доверенность три года
Labels: Есть в реестре | Не гарантирует сегодня | Смерть прекращает | Отмена в любой день | Недееспособность прекращает
NO meme

### inline_4 — structure_diagram — ПНД, санаторий, опека
Labels: ПНД не опека | Ограничение — попечитель | Недееспособность — опекун | Разрешение опеки нужно | Кто подпишет сделку
Meme sticker: yes (small confused_math_lady corner)

### inline_5 — bar_timeline_chart — Аванс внесли — регистрация встала
Labels: Первый день — осмотр | Третий день — аванс | Девятый день — нотариус | Двенадцатый день — подача | Приостановление три месяца
NO meme

### inline_6 — process_flow — Финал: отменили, суд год
Labels: Суд признал недееспособность | Доверенность прекратилась | Опека отказала | Аванс через суд | Судился целый год | Скидка против покупателя
Meme sticker: yes (small this_is_fine cat corner)

### inline_7 — labeled_checklist — Что проверить до аванса
Labels: Свежая выписка ЕГРН | Встреча с собственником | Проверить доверенность | Спросить про опеку | Не спешить с авансом
NO meme

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": {
    "composition": "...",
    "location": "...",
    "meme": "...",
    "prop_set": "...",
    "sticker_set": "...",
    "joke": "...",
    "outfit": "...",
    "emotion": "...",
    "pose_framing": "...",
    "action": "..."
  },
  "slots": {
    "cover": {
      "scene_hint": "...",
      "alt": "...",
      "cover_emotion": "..."
    },
    "inline_1": { "scene_hint": "...", "alt": "..." },
    "inline_2": { "scene_hint": "...", "alt": "..." },
    "inline_3": { "scene_hint": "...", "alt": "..." },
    "inline_4": { "scene_hint": "...", "alt": "..." },
    "inline_5": { "scene_hint": "...", "alt": "..." },
    "inline_6": { "scene_hint": "...", "alt": "..." },
    "inline_7": { "scene_hint": "...", "alt": "..." }
  }
}
```

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «опеки», ZERO Wordstat strips on canvas.
