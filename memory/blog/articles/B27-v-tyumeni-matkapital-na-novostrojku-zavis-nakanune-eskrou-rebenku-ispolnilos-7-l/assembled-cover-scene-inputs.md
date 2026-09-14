# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: Ребёнку исполнилось 7 лет накануне эскроу — семейная ипотека сорвалась
- hook (cover-text): «Ребёнку семь лет — льготная ипотека сорвалась» (highlight: «сорвалась»)
- sticky: «Одобрили, но не успели»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: семейная ипотека одобрена → бронь двушки → ребёнку 7 лет за 9 дней до кредитного договора → банк срывает льготку → маткапитал во взносе не реализован → платёж +18 тыс. → бронь снята → эскроу не открыли

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «семейная ипотека тюмень» — 1227
- «новостройки тюмень» — 8390
- «материнский капитал на покупку жилья» — 72

## meme_picks (from cover-text.json)

- cover: pepe_frog, doge
- inline_1: stonks
- inline_5: this_is_fine_dog
- inline_7: surprised_pikachu

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B26: olive vest bank mortgage desk hide_pain_harold (tranche/RVE)
- B25: terracotta shirt kneeling bare apartment cheems
- B23: light blue shirt mustard sweater handover room side_eye_chloe
- B22: lemon shirt mortgage desk disaster_girl

**Required:** light/bright #FFF high-key, sun flare; pepe_frog people-meme + doge cat-meme small stickers; NO Wordstat query strips/bars; NO dark cinematic; NEW location (family mortgage desk with birthday calendar + matkapital certificate + cancelled reservation — NOT duplicate bank desk from B26/B22).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «Ипотеку одобрили» — и семья забронировала двушку (pair with inline_2)
Labels: Семейная ипотека 6%, Взнос от 20%, Лимит 6 млн, Маткапитал во взнос, Одобрение не гарантия
Meme: stonks tiny corner — bright newbuild sales office reservation receipt

### inline_2 — comparison_table — pair with inline_1
Labels: Семь лет через неделю, ДДУ подписывают позже, Возраст на дату кредита, Не на дату заявки, До шести лет
NO meme — gold paper table approval date vs credit date vs child birthday

### inline_3 — realistic_photo — День рождения ребёнка попал между одобрением и кредитным договором
Labels: Банк перепроверяет программу, Льготное основание пропало, Возраст не заморозили, Ребёнок без инвалидности, Эскроу приостановили
NO meme — calendar with 7th birthday circled between approval letter and credit contract dates

### inline_4 — realistic_photo — Банк на финальной сверке: ребёнку уже 7
Labels: Заявление через банк, Семь лет не отмена, Ограничение для льготки, СФР до 12 дней, Заявление можно отозвать
NO meme — bright bank desk SFR matkapital application folder + age check stamp

### inline_5 — process_flow — Маткапитал в первоначальном взносе
Labels: Пять дней на смену, Платёж плюс 18 тысяч, Бронь сняли на третий, Деньги не ушли, Платёж стал неподъёмным
Meme: this_is_fine_dog tiny corner — flow: matkapital → down payment → family rate → STOP at age 7

### inline_6 — bar_timeline_chart — Финал: застройщик снял бронь
Labels: День рождения ребёнка, Дата кредитного договора, Срок окончания брони, Заявление на маткапитал, Сверить до брони
NO meme — timeline bars with birthday, credit date, booking expiry

### inline_7 — structure_diagram — Какие даты сверить до брони
Labels: Собственные на взнос, Платёж без льготки, Статус заявления СФР, Условия возврата брони, Сначала календарь
Meme: surprised_pikachu tiny corner — date checklist diagram

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
