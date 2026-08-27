# Scout — guidance для следующих weekday-слотов

**Обновляет:** Scout перед topic lock. **Окно anti-repeat:** 30 дней.

## Перед topic lock (HARD)

1. Live `PUBLIC_SITE_URL/blog/` — последние **~20** заголовков (не тела).
2. `shared/published-articles.md` + `shared/published-titles.md` / `published-titles-only.md`.
3. `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters`
4. `python3 scripts/excalibur_blog_scout_helper.py --check-query "<title + hook + slug>"`

**Klyshin OPTIONAL.** Если берёшь угол из @klyshin_A — только **свежий** пост Telegram или **свежий** YouTube; старые посты не тянуть, если кластер уже закрыт. Wordstat Tyumen (55+11176) — **всегда**. Новый hot Tyumen casus **без** Klyshin предпочтителен, когда Klyshin дублировал бы закрытый кластер.

## Закрытые кластеры (до ~2026-09-26)

Каждый weekday-слот (09/12/15/17 YEKT) = **другой** кластер равного engagement-качества (news-casus, не checklist).

| cluster_id | Сюжет (кратко) | locked_until |
|------------|----------------|--------------|
| marital_share_heirs_notary_checked | супружеская доля / наследники / нотариус «всё проверил» | 2026-09-26 |
| court_took_apartment_relatives_contested | суд забрал квартиру ~2 года спустя / родственники оспорили | 2026-09-26 |
| four_months_search_yellow_opinion_lawyers_refused | 4 месяца поиска / жёлтое заключение / юристы отказали | 2026-09-22 |
| matkapital_opieka_kids_cancel_3y | маткапитал + опека молчала + дети через 3 года | 2026-09-25 |
| seller_bankruptcy_finmanager_clean_egrn | банкротство / финуправляющий / чистая ЕГРН / короткое владение | 2026-09-25 |
| elderly_seller_led_by_phone | пожилого вели по телефону | 2026-09-25 |
| pnd_3mln_discount | ПНД + скидка ~3 млн | 2026-09-24 |
| military_summons_stopped_registration | повестка остановила регистрацию | 2026-09-23 |
| grandma_owner_missing_viewing_old_poa | бабушка не на осмотре / старая доверенность | 2026-09-22 |
| inheritance_son_first_marriage_no_refusal | сын первого брака без отказа | 2026-09-20 |
| egrn_line_blocks_advance | строка ЕГРН / обременение сорвало сделку | 2026-09-21 |
| deceased_spouse_share_surprise | доля умершего супруга всплыла | 2026-09-21 |
| deposit_before_auction | задаток перед торгами | 2026-09-19 |
| discount_two_million_hidden_risk | уценка ~2 млн + скрытый риск | 2026-09-19 |
| doverennost_svo_seller | доверенность + СВО | 2026-09-19 |

Полный машиночитаемый список: `memory/scout/used-clusters.json`.

## Открытые углы (примеры для следующего слота)

Выбирай **другой legal plot** с финалом и comment magnet:

- эскроу / аккредитив / «деньги ушли не туда»
- новостройка / ДДУ / долгострой / переуступка
- неузаконенная перепланировка / снос балкона
- соседское самовольное присоединение / спор о границе
- машино-место / кладовка «в подарок», которой нет в ЕГРН
- аренда с выкупом / договор найма с правом выкупа
- мошенничество с двойной продажей / «два покупателя»
- опека над взрослым собственником (не детская доля)

**FAIL:** перефраз закрытого кластера под новый H1. **PASS:** другой риск + другой family-plot + Wordstat Tyumen после rework.
