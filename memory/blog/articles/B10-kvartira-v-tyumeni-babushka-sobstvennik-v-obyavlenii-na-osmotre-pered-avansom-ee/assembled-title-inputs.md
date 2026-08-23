# Title inputs — B10 — 2026-08-23

## Task
Invent ONE H1/title for topic B10. Output JSON only per skill schema. verdict: PASS.

## topic_id
B10

## Scout handoff — klyshin_hook
- hook_id: elderly_pnd_serbsky
- original: «В квартире живет бабушка. Только бабушки нет»
- klyshin_signal_url: https://t.me/klyshin_A
- angle: **физическое отсутствие пожилого собственника 1/3 + ПНД + старая доверенность без полномочий на снятие с регистрации** — НЕ скидка 2–3 млн (B05), НЕ «очередь в Сербского» (live WP)
- dzen_casus_shape: PASS
  - event: осмотр сталинки в Тюмени; в объявлении «живёт бабушка-собственник 1/3», в квартире нет её вещей/спального места
  - risk: ПНД, дееспособность, старая доверенность без снятия с регистрации, продажа доли без бабушки на сделке
  - time: «на осмотре» / «перед авансом»
  - finale: сделку остановили до аванса; риск оспаривания если бы внесли деньги
  - buyer thought safe: «бабушка в санатории, доверенность есть»

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить квартиру в тюмени» — 22753 (Tyumen 55+11176; RU225 40097)
- stickers/H2: «купить квартиру в тюмени вторичка» 3983; «выписка из егрн на квартиру» 124; «доверенность на продажу квартиры» 72; «опека при продаже квартиры» 28
- rework path: weak probe «бабушка в объявлении пнд» → доверенность 72 + опека 28 + егрн 124 → buyer spine «купить квартиру в тюмени» 22753

## Research — subject & conflict
- Subject: покупка вторички в Тюмени, когда в объявлении указана проживающая бабушка-собственник 1/3 доли, но на осмотре перед авансом её нет — ни спального места, ни вещей
- Reader problem: адекватная цена, «бабушка в санатории, есть доверенность» — покупатель готов к авансу
- Case hook: сталинка под ремонт; 2 детские кровати и двуспальная — нет места/вещей бабушки; она владеет 1/3, давно не живёт в квартире, в учреждении (ПНД), зарегистрирована; доверенность несколько лет назад без полномочия на выписку с учёта
- Surprising fact: бытовая деталь на просмотре — нет кровати и вещей женщины, которую объявление называло собственницей
- Correct action: остановить сделку до аванса, не торговаться скидкой
- NOT the same as B05: там скидка 2 млн + срочный задаток; здесь — отсутствие собственника + ПНД + доверенность
- NOT the same as B04: там доверенность и хозяин на СВО; здесь — пожилая собственница доли, ПНД, отсутствие в квартире

## Voice (H1 only)
- Klyshin rhythm: news-casus headline — завершённое событие + противоречие + следствие
- Святослав Шакин / Тюмень — факты и город тенанта
- ~50–70 chars, strong verb, active voice
- Clear subject: бабушка-собственник / квартира / осмотр перед авансом
- Tyumen when strengthens local intent
- NO SEO tails, NO «полный гайд», NO «2026», NO colon+keyword label heads
- FORBIDDEN main hook: «чеклист», «N шагов», «стоит ли покупать», «как купить без риелтора»
- Dzen: honest, informative, no clickbait; do not copy Klyshin post verbatim

## Anti-dup — published titles (change angle if similar)
| topic_id | title |
|----------|-------|
| B02 | В Тюмени расписку за квартиру написали — денег на счёте нет |
| B03 | Почти внесли задаток на торгах — квартиру подарили дочери |
| B04 | Квартиру продавали по доверенности. Хозяин был на СВО |
| B05 | Квартиру уценили на два миллиона и просят задаток сегодня |
| B06 | Автооценка занизила цену — и квартира подорожала за сутки |
| B07 | Наследству на квартиру два года. Сын от первого брака отказ не писал |
| B08 | Справка ЗАГС была чистой — банк отказал из-за доли умершей жены |
| B09 | Ипотеку одобрили, но обременение в ЕГРН сорвало регистрацию |

CRITICAL anti-dup vs B05: B05 = seller discount + urgent deposit + elderly cluster. B10 = absent grandma owner on inspection + PND + old POA without registration powers. No «уценили на два миллиона», no «задаток сегодня».
CRITICAL anti-dup vs B04: B04 = POA + owner on SVO. B10 = elderly 1/3 owner absent from apartment, PND, inspection before advance.

## Title draft (NOT final — rework for Klyshin rhythm)
В объявлении жила бабушка-собственник — в квартире её следов не нашли, сделку в Тюмени остановили до аванса

## Good H1 energy (do not copy verbatim)
- «В квартире живёт бабушка. Только бабушки нет» (Klyshin — inspire rhythm, own wording)
- «Сделку с квартирой оспорили через год: покупатель проверил всё — и потерял» (champion formula)
- «Расписку написали — денег не получили»

## Required JSON output
```json
{
  "topic_id": "B10",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "verdict": "PASS"
}
```
One variant only. h1 and title may match.
