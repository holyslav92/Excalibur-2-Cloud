You are Derouter cover-text. Output ONLY valid JSON (no markdown, no BLOCKER object). All context is inline.

Gate rules (HARD):
- hook: 4-7 Russian words, ≤56 chars, ≥2 words with ≥5 letters
- highlight: exactly one word that appears inside hook
- sticky: ≤5 words
- phone_cta: "+7 922 001 65 05"
- each inline label: 1-4 words AND ≤28 characters
- 2-6 labels per inline_1 … inline_7

Story: Tyumen newbuild family mortgage; booking promised one borrower; 3 days before escrow bank demands spouse coborrower; family refused DDU.

Use hook (6 words): "Банк потребовал супруга созaёмщиком за три дня"
highlight: "потребовал"
sticky: "В брони был один"

wordstat_stickers: ["семейная ипотека тюмень", "купить новостройку в тюмени"]

inline_labels (keep short; you may tweak wording but must pass char/word limits):
inline_1: ["Семейная ипотека", "Один заёмщик", "Предодобрение", "Бронь держит"]
inline_2: ["Переписка в чате", "Один в брони", "Без созaёмщика", "Обещали так"]
inline_3: ["Три дня", "Супруг в кредит", "Доход срочно", "Запрос банка"]
inline_4: ["Одобрение стоп", "ДДU не подписали", "Эскроu нет", "Сделку сняли"]
inline_5: ["Состав семьи", "Письмо банка", "До подписи", "Не спешить"]
inline_6: ["Бронь", "Предодобрение", "Финал банка", "Сверка"]
inline_7: ["Сохранить чат", "Пауза сделки", "Ручка до аванса", "Тюмень"]

meme_picks:
cover: roll_safe, smudge_cat
inline_1: hide_pain_harold
inline_5: two_buttons
inline_7: this_is_fine_dog

Return JSON object with keys: hook, highlight, sticky, phone_cta, wordstat_stickers, inline_labels, meme_picks.
