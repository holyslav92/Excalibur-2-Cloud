# Title inputs — B13

## topic_id
B13

## Scout H1 draft
В Тюмени приставы наложили арест за два дня до регистрации — аванс ещё не вносили

## cluster_id
fssp_arrest_day_before_registration_tyumen

## klyshin_hook
none (fresh Tyumen FSSP casus without Klyshin)

## dzen_casus_shape (PASS)
- **event:** пара в Тюмени выбрала вторичку, проверила продавца в ФССП «чисто», ипотека одобрена, дата МФЦ согласована
- **risk:** судебный пристав внёс запрет на регистрационные действия по долгу продавца — Росреестр приостановил сделку
- **time:** за два дня (48 часов) до подачи на регистрацию
- **finale:** сделку развернули ДО аванса; деньги на аккредитиве не раскрывались; покупатели ушли к другому объекту
- **human who thought safe:** покупатели проверили ФССП заранее и увидели «чисто»

## comment_magnet_angle (from Scout)
Если сегодня в ФССП чисто — вы всё равно вносите аванс до регистрации или ждёте финальной проверки в день сделки?

## Wordstat P0 (demand spine — NOT for H1 verbatim)
- «фссп проверить задолженность» — 232 (regions 55+11176; compare RU 225: 18776)
- «купить квартиру в тюмени вторичка» — 4165 (local buyer context)
- probe «пристав арест квартира» — 38 (on-plot but narrow)

## Research core conflict
Покупатель проверил продавца по ФССП заранее — исполнительных производств не было. Между проверкой и регистрацией появился запрет на регистрационные действия. «Чисто сегодня» ≠ гарантия в день МФЦ. Покупатели остановились до аванса — без финансовых потерь.

## surprising_fact
Долг продавца сам по себе не блокирует регистрацию. Критично отдельное действие пристава — арест/запрет, после чего сведения попадают в ЕГРН.

## Published titles (anti-dup — do NOT repeat angle)
- B02: расписку написали — денег нет
- B09: ипотеку одобрили, обременение в ЕГРН сорвало регистрацию
- B10: пожилого продавца вели по телефону — родственники сорвали сделку
- B11: открытая кухня остановила регистрацию
- B12: застройщик сдвинул сдачу — ипотека осталась

## Requirements
- News-casus headline, Klyshin rhythm (event + contradiction + consequence)
- Tyumen, clear subject (проверка ФССП / арест приставов / вторичка)
- ~50–70 characters
- Active voice, strong verb
- NO SEO tails, NO checklist hooks, NO «полный гайд», NO «2026»
- NO label heads («Проверка ФССП»)
- Champion energy reference (do NOT copy): «Сделку с квартиру оспорили через год: покупатель проверил всё — и потерял»

## Output format
Output ONLY valid JSON for title-brief.json:
{
  "topic_id": "B13",
  "h1": "...",
  "title": "...",
  "subject": "...",
  "angle": "...",
  "comment_magnet_angle": "...",
  "verdict": "PASS"
}

One variant only. h1 and title should be the same.
