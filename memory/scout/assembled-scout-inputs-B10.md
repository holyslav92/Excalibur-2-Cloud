# Scout handoff task — B10 — 2026-08-24

Ты Scout Excalibur BLOG. Сформируй **полный текст handoff** для директора (markdown, русский). Не пиши инструкции «запустите скрипт» — только готовый handoff.

## topic_id
B10

## title draft (news headline)
Аванс внесли в Тюмени — регистрацию приостановили: у продавца истекли 20 дней по повестке

## primary_query / P0
купить квартиру в тюмени

## suggested slug
avans-vnesli-registraciyu-priostanovili-povestka-prodavca-20-dney

## article_dir
memory/blog/articles/B10-avans-vnesli-registraciyu-priostanovili-povestka-prodavca

## external_signal (2–4 предложения)
Klyshin @klyshin_A (март 2026): после неявки по повестке через 20 дней могут приостановить кадастровый учёт и регистрацию прав. Покупатель вносит аванс, ЕГРН чистая — а между авансом и сделкой ограничение влетает в систему. В Тюмени кейс: аванс внесли, ипотека одобрена, на регистрации встало приостановление — сделка сорвана, деньги в заложнике.

## signal_urls
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92
- {{SITE_BASE}}/blog/

## Обязательные строки (включи в handoff verbatim)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: summons_registration_stop | original: «повестка → стоп регистрации» | angle: реестр повесток, 20 дней неявки, блок Росреестра между авансом и сделкой | signal: https://t.me/s/klyshin_A
dzen_casus_shape: PASS | event: «аванс внесли, документы на сделку собрали» | risk: «реестр повесток / приостановление регистрации» | time: «между авансом и регистрацией / 20 дней после даты в повестке» | finale: «Росреестр приостановил регистрацию — сделка сорвана, аванс в заложнике»
comment_magnet_angle: «Нужно ли теперь запрашивать выписку из реестра повесток у продавцов-мужчин — или это уже паранойя?»
wordstat_rework: probe «повестка регистрация недвижимости» 3 → «реестр повесток» 3675 → «запрет на регистрационные действия» 423 → «приостановление регистрации права» 26 → final P0 «купить квартиру в тюмени» 22753 | clusters tried: повестка+регистрация, реестр повесток, запрет регдействий, приостановление, buyer spine
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22753 | stickers: «реестр повесток» 3675, «запрет на регистрационные действия» 423, «выписка из реестра повесток» 80, «купить квартиру в тюмени вторичка» 3983

## Структура handoff
topic_id, title draft, primary_query, slug, article_dir, angle, external_signal, signal_urls (список), klyshin_hook line, dzen_casus_shape line, comment_magnet_angle line, wordstat_rework line, wordstat line, overlap/anti-dup note (B02–B09, story clusters PASS), next_step research_start command.

Город и герой: Святослав Шакин / Тюмень. Не Москва как P0.
