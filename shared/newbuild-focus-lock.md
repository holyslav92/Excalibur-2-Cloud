# Newbuild Focus Lock (HARD — owner permanent)

**Владелец:** Святослав Шакин  
**Дата:** 2026-08-31  
**Статус:** `LOCKED_ON_MAIN` — не ослаблять без явного owner override.

## Мандат

Пишем **только для читателей**, которые в дальнейшем обращаются к Святославу за
**покупкой новостройки** — квартиры **или** дома (коттедж / КП / ИЖС / таунхаус
от застройщика) **в Тюмени**.

- **Аудитория:** семьи с детьми + инвесторы.
- **Конверсия:** пишут в TG / MAX / звонят — купить новостройку через Святослава.
- **Стиль:** news-casus голосом Святослава — **не ломать** (см. `shared/SOUL.md`,
  `shared/dzen-news-casus.md`, `shared/quality-bar-9.md`).

CTA (не менять):  
TG https://t.me/Tyumen_Rieltor · MAX https://max.ru/id561413315447_biz · +7 922 001 65 05

## Topic (Scout / research_start)

### ONLY — новостройки Тюмень

Квартиры **и** дома от застройщика: ЖК, ДДУ, эскроу, переуступка, срок сдачи,
отделка, семейная ипотека, коттеджный посёлок, таунхаус, ИЖС.

### DENY — вторичка как сюжет

Запрещены **самостоятельные** темы про вторичный рынок, даже с сильным Wordstat.
Слабый спрос → **rework** Tyumen newbuild hook (семейная ипотека, эскроу, ДДУ,
уступка, срок сдачи, отделка, КП) — **не** drop на вторичку.

Gate: `scripts/excalibur_blog_topic_focus.py` при `topic_market_focus: newbuild_only`.

### Klyshin

Опционально, только свежий TG/YouTube, **и только если hook = новостройка**.

### Anti-repeat 30 дней

Без изменений. **Frozen secondary clusters** остаются закрытыми — не retitle
вторичный casus под «новостройку»:

ЕГРН/банкротство, опека/маткапитал-вторичка, 4 месяца поиска, жёлтое заключение,
повестка, бабушка/доверенность, ПНД, супружеская доля, нотариус «всё проверил»,
соседская доля, прописанные, детские доли на вторичке, фальшивое согласие супруги.

См. `shared/scout-story-clusters.json`, `memory/scout/used-clusters.json`.

## Style — DO NOT BREAK

| Сохраняем | Запрещено |
|-----------|-----------|
| news-casus: казус, stakes, финал, comment magnet | English TL;DR, «Быстрый инсайт», bullet-dump в лиде |
| Прозаический лид 4–6 предложений → early TG+MAX | Чеклисты / «10 советов как выбрать ЖК» как каркас |
| One-breath ~1800–2200 слов (~10 мин) | 14+ мин, вода, один beat трижды |
| Ending: agency not panic (бронь/ДДУ до денег) | Brochure застройщика, how-to guide |
| Interlink 2–4 sibling (без plot из старой вторички) | Переписывать старые published HTML |

**Images:** realistic newbuild (стройка, офис продаж, ДДУ, эскроу, КП) + diagrams.
Cover identity rules **не трогать** (см. `memory/cover/cover-canon.json` — grsai standard only, no VIP, Святослав only on cover).

## Кто читает этот lock

Scout, Research, Title, Writer, Sol, Description, Director, AGENTS.md, CLOUD-AUTOMATION.
