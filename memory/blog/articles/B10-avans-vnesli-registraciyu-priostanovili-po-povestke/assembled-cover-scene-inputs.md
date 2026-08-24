# Cover-scene inputs — B10

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B10
- tenant: The Риэлтор, Тюмень
- H1: Аванс внесли — регистрацию приостановили по повестке
- hook (cover-text): «Аванс внесли — сделка встала внезапно» (highlight: «встала»)
- sticky: «Чистая выписка не спасла»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: покупатель внёс аванс, ЕГРН чистая, но Росреестр приостановил регистрацию — у продавца истекли 20 дней по повестке военкомата; Самара апрель 2026

## meme_picks (from cover-text.json — HARD)

- cover: roll_safe + smudge_cat (people+cats, small stickers ≤15%)
- inline_1: hide_pain_harold
- inline_5: blinking_white_guy
- inline_7: two_buttons

## Wordstat stickers (manifest log ONLY — FORBIDDEN on cover canvas)

- «купить квартиру в тюмени» — 40097
- «реестр повесток» — 312121
- «выписка из реестра повесток» — 6648

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд — повторялось B03/B04.

**Recent covers to differ from:**
- B06: lemon yellow shirt, host right, price jump 18→20
- B05: terracotta sweater + grey overcoat, host right, entrance steps
- B04: black blazer left bust side-eye investigation board
- B03: black blazer left bust jaw-drop board

**Required:** light/bright #FFF high-key, sun flare; meme roll_safe + smudge_cat small stickers; NO dark cinematic; NO daypart formula; NO Wordstat query strips/bars on canvas.

## Anti-repeat used-motifs (14d) — avoid collision

B01 navy blazer EGRN atrium; B02 charcoal blazer bank; B03/B04 black blazer left bust board; B05 terracotta right entrance; B06 lemon yellow right price jump.

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — comparison_table — «Аванс внесли — и Росреестр поставил на паузу»
Labels: Выписка без ограничений | Не арест, не обременение | Военкомат → Росреестр | Пауза, не отказ | Проверка по дате
Meme sticker: hide_pain_harold (small corner)

### inline_2 — workflow_diagram — «Хронология: от чистой выписки до приостановления»
Labels: Выписка чистая | Ипотека одобрена | Аванс передан | Повестка продавцу | 20 дней без явки | Регистрация на паузе
NO meme

### inline_3 — process_flow — «Финал: сделка зависла, аванс не вернули сам по себе»
Labels: Приостановление не отказ | Сроки покупателя горят | Аванс сам не вернётся | Только текст соглашения | Самара, апрель 2026
NO meme

### inline_4 — bar_timeline_chart — «Двадцать дней по повестке»
Labels: ст. 7.1 53-ФЗ | 20 календарных дней | Мера не пожизненная | Без уведомления покупателя | До подачи как все
NO meme

### inline_5 — structure_diagram — «Чистая ЕГРН и момент проверки — разные даты»
Labels: Выписка — фото минуты | Росреестр смотрит сейчас | Зазор до 1,5 мес | Пауза после подачи | Заранее не видно
Meme sticker: blinking_white_guy (small corner)

### inline_6 — checklist_board — «Выписка из реестра повесток»
Labels: Заказать за продавца нельзя | Только сам гражданин | Просить можно добровольно | Дата близко к подаче | Отказ — сократить сроки
NO meme

### inline_7 — labeled_checklist — «Как распределить риск в соглашении об авансе»
Labels: Возврат до подписания | Срок устранения ограничения | Срок ипотеки — расторгнуть | Выписка в договоре | Короткий срок до подачи
Meme sticker: two_buttons (small corner)

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
  "wordstat_stickers": ["...", "...", "..."],
  "meme_picks": { "cover": ["roll_safe", "smudge_cat"], "inline_1": ["hide_pain_harold"], "inline_5": ["blinking_white_guy"], "inline_7": ["two_buttons"] },
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

scene_hint cover: 80–140 chars, name emotion, light/bright, phone CTA +7 922 001 65 05, pink highlight «встала», roll_safe+smudge_cat stickers, ZERO Wordstat on canvas.
