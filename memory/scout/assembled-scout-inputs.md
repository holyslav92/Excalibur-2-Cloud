# Scout task — DIRECTOR PRE-RUN ALL GATES (write handoff only)

**ВАЖНО для Derouter:** дирижёр уже выполнил все tool-gates. Тебе НЕ нужны MCP, файлы или скрипты.
**Задача:** на основе данных ниже напиши готовый `.cursor/excalibur-blog-handoff.md` в формате skill.
**ЗАПРЕЩЕНО** выдавать DEROUTER SCOUT BLOCKER — все проверки PASS.

---

## wordstat_preflight
mcp-kv wordstat_get_user_info OK (Yandex Cloud API, folder b1g6bq34gkivjj20be06)

## klyshin_hook
- id: five_court_schemes_fictitious
- original: «По документам сделка была. А по факту денег никто не передавал. Потом наследники идут в суд и говорят: сделка фиктивная»
- angle: фиктивная внутрисемейная продажа → наследники оспаривают → покупатель теряет квартиру
- signal: https://t.me/klyshin_A (пост «5 схем», схема №3, август 2026)

## dzen_casus_shape
PASS
- event: родственники оформили продажу квартиры между собой — расписки и договор есть, денег по факту не передавали
- risk: фиктивная сделка / оспаривание наследниками
- time: через год после регистрации
- finale: суд признал сделку недействительной, квартиру забрали у добросовестного покупателя

## comment_magnet_angle
«Если продавец когда-то «продавал» родственнику без денег — вы бы рискнули покупать у него сейчас?»

## wordstat_rework
probe «фиктивная сделка квартира» → API empty
probe «банкротство продавца квартиры» → 28 (SKIP: dup live Dzen «чистая выписка + банкротство»)
probe «маткапитал при покупке квартиры» → 17 (SKIP: dup live WP matkapital)
probe «аккредитив при покупке квартиры» → 47
→ final P0 «купить квартиру в тюмени» **22660** (regions 55+11176; RU225 compare **39961**)
clusters tried: банкротство, маткапитал, флиппер 3 мес, фиктивная сделка

## wordstat line (handoff)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22660 | RU225 39961 | rework: фиктивная→аккредитив 47→P0 22660

## story_duplicate
scout_helper --check-query PASS (no overlap ledger/live WP)
avoided clusters: matkapital, inheritance_son, notary+pensioner, clean EGRN+bankruptcy, flip 3 months

## topic assignment
- topic_id: **B10**
- title_draft: **Договор подписали — а денег не было: в Тюмени наследники забрали квартиру**
- slug: dogovor-podpisali-deneg-ne-bylo-nasledniki-zabrali-kvartiru
- wp_category: vtorichka-i-riski (fictitious deal / heirs dispute)

## external_signal_urls (≥2)
1. https://t.me/klyshin_A
2. https://dzen.ru/holyslav
3. https://t.me/holyslav92

## published anti-dup (titles only, do not read bodies)
B02–B09 published. Live WP Aug 23–24: бабушка на осмотре, повестка+аванс, уставший покупатель 4 мес, чистая выписка+банкротство, нотариус+суд 4,3 млн.

## tenant facts
- brand: The Риэлтор / Святослав Шакин / Тюмень
- dzen engagement goal: likes, comments, subscriptions
- news-casus shape required (NOT checklist lead)

---

**OUTPUT:** полный handoff markdown с frontmatter (topic_id, title, slug, signal_urls) и всеми обязательными строками из skill.
