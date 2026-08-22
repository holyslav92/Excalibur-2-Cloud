# Cover-scene inputs — B08

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B08
- tenant: The Риэлтор, Тюмень
- H1: Справка ЗАГС была чистой — банк отказал из-за доли умершей жены
- hook (cover-text): «Банк отказал: доля умершей жены» (highlight: «отказал»)
- sticky: «Справка не спасла»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: справка ЗАГС с 2004 года не отвечала про брак 1998; невыделенная доля умершей супруги → отказ банка до аванса

## Wordstat stickers (manifest log only — **FORBIDDEN on canvas**)

- «купить квартиру в тюмени вторичка» — 4023
- «наследство квартиры продажа» — 157
- «согласие супруга на продажу квартиры» — 49

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B07: soft blue henley, waist-up left, family tree board
- B06: lemon yellow shirt, host right, panoramic window
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04/B03: black blazer left bust board

**Required:** light/bright #FFF high-key, sun flare; meme cat + catalog people-meme small stickers; NO dark cinematic; NO daypart formula; **NO Wordstat query strips/bars on canvas**; optional one yellow sticky from hook only.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon shirt right window; B07 blue henley left tree board.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — process_flow — «Коротко: справка была «чистой», а сделка — нет»
Labels: ДКП 1998 года | справка с 2004 | шесть лет разрыва | документ бесполезен
Meme sticker: yes (small cat corner)

### inline_2 — comparison_table — «В браке не состояли»: что показала справка
Labels: форма №15 | срез на сегодня | ЕГР ЗАГС с 2018 | 1998 года нет
NO meme

### inline_3 — process_flow — Умершая супруга и наследники
Labels: брак на дату покупки | долю не выделяли | наследники разных браков | наследник умер
NO meme

### inline_4 — structure_diagram — Почему «в ЕГРН чисто» не закрыл риск
Labels: ЕГРН показывает записи | доля вне реестра | статья 34 СК РФ | наследство приняли
NO meme

### inline_5 — process_flow — Финал: банк отказал, вышел до аванса
Labels: ипотеку не одобрили | до передачи аванса | деньги не ушли | отказ банка
Meme sticker: yes (small hide_the_pain_harold corner)

### inline_6 — labeled_checklist — Что проверить до аванса
Labels: дата покупки | период справки ЗАГС | брак на дату ДКП | наследники | до аванса
NO meme

### inline_7 — comparison_table — Супружеская доля и наследство: две линии права
Labels: две линии права | совместное в браке | половина супруге | шесть месяцев | отказ не вернуть
Meme sticker: yes (small wojak corner)

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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA, pink highlight «отказал», ZERO Wordstat on canvas, optional yellow sticky «Справка не спасла».
