# Scout — guidance для следующих weekday-слотов

**Обновляет:** Scout перед topic lock. **Окно anti-repeat:** 30 дней.

**Owner lock 2026-09-05:** `shared/dzen-top-angle-newbuild-lock.md` — mirror top-10 **energy**, plot **ONLY newbuild**. **4 slots/day (09/12/15/17 YEKT)** — не резать.

**Owner lock 2026-08-31:** `shared/newbuild-focus-lock.md` — **ONLY новостройки
Тюмень** (квартиры + дома от застройщика). Вторичка как сюжет = **BLOCK**.
Frozen secondary clusters ниже — **не retitle** под «новостройку».

## Перед topic lock (HARD)

1. Live `PUBLIC_SITE_URL/blog/` — последние **~20** заголовков (не тела).
2. `shared/published-articles.md` + `shared/published-titles.md` / `published-titles-only.md`.
3. `python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters`
4. `python3 scripts/excalibur_blog_scout_helper.py --check-query "<title + hook + slug>"` — HARD anti-dupe (cluster + fingerprint + formula spam)
5. `python3 scripts/excalibur_blog_topic_focus.py --text "<title>"` — newbuild gate
6. Прочитать `shared/dzen-top-angle-newbuild-lock.md` — назвать top_energy_mirror + newbuild_mechanism

**Klyshin OPTIONAL.** Если берёшь угол из @klyshin_A — только **свежий** пост Telegram или **свежий** YouTube **и только если hook = новостройка**; старые посты не тянуть, если кластер уже закрыт. Wordstat Tyumen (55+11176) — **всегда**. Слабый Wordstat → rework **newbuild** hook (семейная ипотека, эскроу, ДДУ, уступка, срок сдачи, отделка, КП) — **не** вторичка.

## Закрытые кластеры (до ~2026-09-26) — FROZEN secondary, не retitle

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
| forged_spouse_consent | фальшивое согласие супруги | 2026-09-26 |
| registered_persons_block_sale_before_advance | прописанные сорвали сделку | 2026-09-26 |
| communal_share_preemptive_right_neighbor_blocked | соседская доля / преимущественное право | 2026-09-26 |
| matkapital_missing_child_shares | детские доли на вторичке | 2026-09-26 |

Полный машиночитаемый список: `memory/scout/used-clusters.json`.

## Открытые углы — ONLY newbuild (примеры для следующего слота)

Выбирай **другой newbuild plot** с финалом и comment magnet (семьи + инвесторы):

- ДДУ / эскроу / «деньги ушли не на эскроу-счёт»
- долгострой / срыв срока сдачи / штрафы застройщика
- переуступка / цена выросла после брони
- семейная ипотека + маткапитал на новостройку (не вторичка)
- приёмка квартиры: дефекты / отказ от подписания акта
- коттеджный посёлок / ИЖС: границы участка / коммуникации
- инвестор: сдача в аренду vs переуступка до ключей
- застройщик сменил юрлицо / реорганизация ДДУ
- бронь сгорела / условия изменились за 48 часов

**FAIL:** перефраз закрытого secondary-кластера под «новостройку». **FAIL:** вторичка как сюжет. **PASS:** другой newbuild-риск + другой plot + Wordstat Tyumen после rework.
