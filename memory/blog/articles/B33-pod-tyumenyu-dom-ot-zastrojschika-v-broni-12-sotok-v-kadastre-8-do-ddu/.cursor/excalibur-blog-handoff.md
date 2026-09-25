## Scout handoff — B33 / 2026-09-25 / slot 15:09 YEKT

**topic_id:** B33  
**cluster_id:** `newbuild_kp_land_area_mismatch_cadastre_before_ddu_tyumen`  
**slug:** `kp-uchastok-12-sotok-v-kadastre-8-do-ddu`

### Title draft
**Под Тюменью в брони обещали 12 соток — в кадастре оказалось 8 до подписания ДДУ**

### Demand spine
- **P0:** «купить новостройку в тюмени» — **892**
- Mechanism: «купить дом в тюмени от застройщика» — **118**
- Local support: «дома с участком от застройщика тюмень» — **24**
- Regions: Tyumen **55** + Tyumen Oblast **11176**; RU comparison **225**.
- `wordstat_preflight: mcp-kv wordstat_get_user_info OK`

### Editorial casus
Семья выбирает дом с участком в коттеджном посёлке под Тюменью. В презентации застройщика и документе о бронировании указан участок площадью 12 соток. За несколько дней до оформления договора семья получает кадастровые документы: площадь — 8 соток. Подписание останавливают, пока не будут сверены границы, площадь участка, приложения к договору и цена дома с землёй.

**Важно для Writer:** это композитный редакционный casus; не выдавать его за конкретную публично подтверждённую историю семьи или за новость о названном застройщике.

### Required handoff fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK

top_energy_mirror: paper_clean_then_broke

newbuild_mechanism: КП / дом от застройщика под Тюменью — расхождение площади земельного участка между бронью, презентацией и кадастровыми сведениями до подписания договора на дом и землю.

why_newbuild_not_secondary: сюжет только о покупке нового дома с участком у застройщика в КП / ИЖС; не о перепродаже готового участка, дома или вторичной недвижимости.

klyshin_hook: none | original: не использовался (свежий Klyshin не требовался)

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; recent conflicting plots excluded: partial ввод, parking DDU, отменённая переуступка, последний этаж, маткапитал/эскроу, рендер детсада, семейная ипотека 7 лет, забор КП, мебельный пакет, созаёмщик/эскроу, высота потолков, окна во двор.

dzen_casus_shape: PASS
event: в брони и презентации дома в КП указано 12 соток, а перед подписанием кадастровые документы показывают 8.
risk: покупатель может согласиться на меньший участок при прежней цене; разница влияет на ценность объекта, планирование коммуникаций и залоговую оценку.
time: расхождение обнаружено за несколько дней до подписания договора.
finale: семья не подписывает документы до сверки площади, границ, приложений к договору и пересчёта условий.

comment_magnet_angle: «Если в брони 12 соток, а в выписке 8 — вы требуете пересчёт цены или всё равно подписываете договор?»

wordstat_rework: probe «участок коттеджный поселок тюмень» — weak → rework through «дом от застройщика тюмень» and «дома с участком от застройщика тюмень» → final demand bridge P0 «купить новостройку в тюмени» 892.

wordstat: mcp_kv live | regions 55,11176, compare 225 | P0 «новостройки тюмень купить» 1157 / «купить новостройку в тюмени» 892 | дду+егрн angle | mechanism «купить дом в тюмени от застройщика» 118 | local «дома с участком от застройщика тюмень» 24.

story_dup_check: PASS | cluster_id: newbuild_kp_land_area_mismatch_cadastre_before_ddu_tyumen

h1_fingerprint_check: PASS | fingerprint: 12 соток в брони → 8 соток в кадастре до договора на дом от застройщика.

formula_spam_check: PASS | last3_mechanisms: partial ввод / parking DDU / отменённая переуступка; land-area mismatch is distinct.

anti_dupe_hard: PASS
```

### Writer angle
Не превращать материал в спокойный чеклист по ЕГРН. Начать с момента, когда семья уже почти выбрала дом и увидела «12 соток» в брони, но перед сделкой цифра стала «8». Конфликт строить вокруг вопроса: ошибка в рекламе и брони — повод отказаться, требовать новую цену или можно подписать, если сам дом устраивает?

---

=== EXCALIBUR BLOG PUBLISH ===
topic_id: B33
slug: pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu
article_dir: memory/blog/articles/B33-pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu
publish_date: 2026-09-25
verdict: PASS
permalink: /blog/vtorichka-i-riski/pod-tyumenyu-dom-ot-zastrojschika-v-broni-12-sotok-v-kadastre-8-do-ddu/
post_id: 10978
featured_image: 10979
inline_images: 10980-10986 (7)
schema_meta: ok
blockers: none
PIPELINE DONE (publish)
