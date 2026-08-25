# Cover-text — OUTPUT ONLY VALID JSON

Ты УЖЕ вызван Derouter cover-text. Верни **ТОЛЬКО** JSON объект (без markdown, без пояснений).

hook: 5-7 кириллических слов, одна строка. Пример формата B09.
phone_cta: +7 922 001 65 05
meme_picks: cover roll_safe + smudge_cat (people+cats), inline_1 hide_pain_harold, inline_5 grumpy_cat, inline_7 confused_math_lady
wordstat_stickers: [] (EMPTY — NO Wordstat strips on cover)
sticky: optional yellow sticky short phrase

Title: Скидка в 3 млн скрыла ПНД: сделку с квартирой в Тюмени остановили

Template:
{
  "hook": "Скидка три миллиона — бабушка в ПНД",
  "highlight": "ПНД",
  "sticky": "Сделку остановили",
  "phone_cta": "+7 922 001 65 05",
  "wordstat_stickers": [],
  "meme_picks": {
    "cover": ["roll_safe", "smudge_cat"],
    "inline_1": ["hide_pain_harold"],
    "inline_5": ["grumpy_cat"],
    "inline_7": ["confused_math_lady"]
  }
}

Adjust hook/labels to article but keep JSON shape exactly.
