# Cover-text inputs — B20 rewrite WP 9439

**CRITICAL:** Derouter utility tier inside script. Output **only valid JSON** without markdown fences.

## Context
- topic_id: B20, rewrite WP 9439
- H1: На приёмке новостройки в Тюмени нашли мокрую стяжку — ключи не выдали
- scene: приёмка новостройки, ключи на столе, влагомер/мокрая стяжка, акт, Святослав на приёмке
- angle: «подпишите акт — ключи на столе», мокрый пол, 45 дней, не подписали
- comment_magnet: подпишете акт или уйдёте без ключей?

## Required JSON fields
```json
{
  "hook": "5-7 cyrillic words",
  "highlight": "one word from hook",
  "sticky": "up to 5 words",
  "phone_cta": "+7 922 001 65 05",
  "inline_labels": {"inline_1":[],...,"inline_7":[]},
  "meme_picks": {"cover":["id"],"inline_1":["id"],...}
}
```

## Rules
- NO wordstat_stickers field
- hook: 5-7 Cyrillic words, B08-style (e.g. «Мокрая стяжка — ключи на столе»)
- meme catalog: memory/cover/meme-top100.json only; people+cats; ≤15% stickers; never on hook/face/phone
- anti-repeat 14d: avoid roll_safe, crying_cat, hide_pain_harold, smudge_cat, confused_math_lady, woman_yelling_cat, wojak, distracted_boyfriend, this_is_fine_dog, blinking_white_guy, polite_cat, thinking_cat, wide_eyes_cat
- inline_labels: 2-6 labels per inline_1…inline_7, 1-4 words each, Cyrillic

## Cover scene
Святослав (host) at newbuild acceptance: moisture meter on wet screed, keys and act on table, new pose/clothes/emotion — приёмка, влагомер, акт. Phone visible. Small memes not on face/hook/phone.
