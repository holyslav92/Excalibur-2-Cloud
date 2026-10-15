Верни только JSON для cover/cover-text.json. Надписи на русском, которые нарисуют на обложке.

Сюжет: продавец вторички в Тюмени остановил продажу, потому что до нулевого налога не хватило 15 месяцев. Аванс не перевели. Это не наценка к цене.

hook: одна строка, 5–7 кириллических слов, предпочтительно слова от 5 букв. Длинное тире можно. Не роман. Не Wordstat. Не H1 целиком.
Пример ритма (не копировать дословно): «Пятнадцать месяцев съели аванс»

highlight: одно слово из hook.
sticky: до 5 слов.
phone_cta: +7 922 001 65 05

wordstat_stickers: ровно 2 короткие фразы спроса, их НЕ рисовать на картинке, только поле JSON:
- налог с продажи квартиры
- срок владения квартирой

meme_picks объект, не список. Люди плюс кот. Не коты одни. Не думать-полосатый-кот. Не эти id: two_buttons, crying_cat, hide_pain_harold, smudge_cat, roll_safe, grumpy_cat, drake, salt_bae, stock_handsome_man.
cover: blinking_white_guy и polite_cat
inline_1: disappointed_black_guy
inline_5: capybara_indifference
inline_7 не обязателен; если есть — yelling_at_clouds

inline_labels: ключи inline_1 … inline_7. В каждом 4–5 коротких русских строк, каждая 2–4 слова, без латиницы. Факты статьи:
1 показ и три года
2 выписка и пять лет
3 разница и 146900
4 аванс не ушёл
5 дата в выписке
6 другое жильё
7 пятнадцать месяцев

Запрещено на надписях: семейная ипотека, ДДУ, бронь, эскроу, застройщик, аренда, Wordstat как фраза на хуке.

JSON с полями hook, highlight, sticky, phone_cta, wordstat_stickers, meme_picks, inline_labels, verdict PASS.
