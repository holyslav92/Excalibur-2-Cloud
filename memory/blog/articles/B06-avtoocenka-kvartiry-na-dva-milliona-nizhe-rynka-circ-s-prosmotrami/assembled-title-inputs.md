# Title inputs — B06 — 2026-08-21

## Task
Invent ONE H1/title for topic B06. Output JSON only per skill schema. verdict: PASS.

## topic_id
B06

## Scout handoff — klyshin_hook
- hook_id: cian_autoprice_minus_million
- original: «автооценка ЦИАН/Домклик минус миллион к рынку»
- angle: автооценка vs живой рынок Тюмени — покупатель не ориентируется на «рекомендованную цену» сервиса
- external_signal: ЦИАН/Домклик/Сбер/Авито дают «рекомендованную цену» на 1–2 млн ниже живого спроса; собственник занижает объявление, получает очередь на показ и авансы, снимает объект и поднимает цену выше рынка
- title_draft (NOT final — rework for Klyshin rhythm): Автооценка показала на два миллиона меньше рынка — и начался цирк с просмотрами

## Wordstat demand spine (do NOT paste raw P0 into H1)
- P0: «купить квартиру в тюмени» — 23066 (Tyumen 55+11176)
- stickers/H2: «вторичка в тюмени» 5799; «купить квартиру в тюмени вторичка» 3943
- weak probe: «оценка квартиры тюмень» 73; «автооценка квартиры» 1 (WORDSTAT PARTIAL)

## Research — subject & conflict
- Subject: автооценка квартиры (ЦИАН.Оценка, Домклик/Сбер, Авито) vs цена реальной сделки на вторичке в Тюмени
- Reader problem: видит в приложении «минус миллион к рынку», бежит на просмотр — очередь, снятие объявления, цена меняется
- Case hook from signal: ~20 млн живой спрос vs ~18 млн в сервисе → ~2000 просмотров за сутки, ~10 записей, ~7 готовы к авансу → собственник снимает и поднимает цену
- Surprising fact: собственник занижает по подсказке сервиса, получает поток, потом выставляет дороже рынка
- NOT the same as B05: там скидка + «задаток сегодня» (риск продавца); здесь — алгоритмическая цена, очередь на просмотр, смена цены

## Voice (H1 only)
- Klyshin rhythm: case hook, две короткие реплики или контраст, разговорная сцена
- Святослав Шакин / Тюмень — факты и город тенанта
- ~50–70 chars, strong verb, active voice
- Clear subject: автооценка / рекомендованная цена сервиса / вторичка
- NO SEO tails, NO «полный гайд», NO «2026», NO colon+keyword label heads
- Dzen: honest, informative, no clickbait

## Anti-dup — published titles (change angle if similar)
| topic_id | title |
|----------|-------|
| B01 | В выписке ЕГРН есть строка, после которой аванс вносить нельзя |
| B02 | В Тюмени расписку за квартиру написали — денег на счёте нет |
| B03 | Почти внесли задаток на торгах — квартиру подарили дочери |
| B04 | Квартиру продавали по доверенности. Хозяин был на СВО |
| B05 | Квартиру уценили на два миллиона и просят задаток сегодня |

CRITICAL anti-dup vs B05: B05 = seller discount + urgent deposit. B06 = algorithm price + viewing queue + price change. Avoid repeating «уценили на два миллиона и просят задаток» pattern. «Два миллиона» OK if tied to автооценка/сервис, not seller discount.

## Good H1 energy (do not copy verbatim)
- «Расписку написали. Денег не получили»
- «Автооценка может стоить миллион» (Klyshin post title — inspire rhythm, own wording)
- «В квартире живёт бабушка. Только бабушки нет»

## Required JSON output
```json
{
  "topic_id": "B06",
  "h1": "…",
  "title": "…",
  "subject": "…",
  "angle": "…",
  "verdict": "PASS"
}
```
One variant only. h1 and title may match.
