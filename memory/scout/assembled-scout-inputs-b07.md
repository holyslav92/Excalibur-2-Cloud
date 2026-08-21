# ЗАДАЧА Scout B07

Напиши **только готовый handoff-документ** для `.cursor/excalibur-blog-handoff.md`.
**Запрещено:** bash-команды, чеклисты «как запустить scout», meta-инструкции дирижёру.
**Разрешено:** финальные поля handoff + title draft + external_signal + signal_urls + краткий angle (2–3 предложения).

---

## Tenant
The Риэлтор / Святослав Шакин · Тюмень · topic_id **B07** · ru

## Anti-dup (published)
B01 ЕГРН/аванс · B02 расписка · B03 торги/дарение · B04 доверенность СВО · B05 скидка/бабушка · B06 автооценка ЦИАН

## Klyshin hook (выбран)
- hook_id: **heirs_first_marriage_3y**
- original: «дети от первого брака и отказы — три года не прошло»
- angle: наследники без отказа, срок 3 года, предавансовая проверка, «покупайте так»
- signal post: https://t.me/s/klyshin_A — отчёт 2900 ₽, папа умер, ребёнок от 1-го брака, отказа нет, СВО

## signal_urls (≥2 сегодня)
1. https://t.me/klyshin_A
2. https://dzen.ru/holyslav — «Наследству на квартиру два года. Сын от первого брака отказ не писал»
3. https://t.me/holyslav92
4. {{SITE_BASE}}/blog/

## Wordstat MCP-KV (live, regions 55+11176, compare 225)
preflight: wordstat_get_user_info OK

rework chain (numeric freqs only):
«наследство квартира продажа» 167 → «наследник квартиры» 203 → «отказ от наследства квартира» 4 → rework «наследственное дело» 1647 (проверить 170; наследственное дело тюмень 90) → rework «вступление в наследство» 1223 → **final P0 «наследство квартира» 942** (RU225 105443)

stickers: наследник квартиры 203 · реестр наследственных дел 601 · купить квартиру в тюмени 22990

## Title direction
H1 draft (Klyshin rhythm, Tyumen): «Наследству на квартиру два года — сын от первого брака отказ не писал»
slug: nasledstvo-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal

---

## ОБЯЗАТЕЛЬНЫЙ ФОРМАТ ВЫВОДА (скопируй структуру, заполни своими формулировками)

topic_id: B07
title_draft: …
slug: nasledstvo-dva-goda-syn-ot-pervogo-braka-otkaz-ne-pisal
external_signal: …
signal_urls: …
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: heirs_first_marriage_3y | original: «…» | angle: … | signal: https://t.me/s/klyshin_A
wordstat_rework: probe «…» <freq> → … → final P0 «…» <freq> | clusters tried: …
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «наследство квартира» 942 | …
