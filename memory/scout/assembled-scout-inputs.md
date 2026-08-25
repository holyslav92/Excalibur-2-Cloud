# Scout assembled inputs — B10 run 2026-08-24 (YEKT ~12:00)

## Assignment

- topic_id: **B10** (next after B09)
- tenant: The Риэлтор / Святослав Шакин / **Тюмень**
- goal: Dzen engagement — hot news-casus с финалом + comment magnet (NOT checklist)

## Selected hook (triple gate PASS)

- hook_id: `phone_scammers_notary`
- original Klyshin: «Нотариус не спасает от мошенников. И теперь это подтверждают цифры» + fresh post «Дед приехал из Израиля… вынес сейф мошенникам» (август 2026)
- angle: пожилой продавец под телефонным/мошенническим влиянием; нотариальная форма ≠ проверка; исследование: из нотариальных сделок с телефонными мошенниками устояли только 40%; суд может отменить сделку (ВС РФ 10.03.2026 № 84-КГ26-1-К3 — реституция)
- localize: кейс в **Тюмени**, не Москва/Израиль как герой — использовать как энергию риска, факты Шакина

## Title draft (news headline — for handoff)

«В Тюмени нотариус удостоверил сделку — а через год суд отменил продажу: продавца вели по телефону»

## slug suggestion

`notarialnaya-sdelka-sud-otmenil-prodavca-vedi-po-telefonu`

## article_dir

`memory/blog/articles/B10-notarialnaya-sdelka-sud-otmenil-prodavca-vedi-po-telefonu`

## dzen_casus_shape (PASS)

- event: нотариальная продажа квартиры в Тюмени завершена, право зарегистрировано
- risk: продавец действовал под влиянием телефонных мошенников / обмана; нотариус не видит давление
- time: «через год после регистрации» (или несколько месяцев — в рамках срока оспаривания)
- finale: суд признал сделку недействительной, покупатель возвращает квартиру (реституция)
- victim logic: «нотариус же проверил — значит безопасно»

## comment_magnet_angle

«Если пожилой продавец странно реагирует на звонки и не отпускает телефон — вы всё равно идёте к нотариусу или останавливаете сделку?»

## Anti-dup (verified)

scout_helper --check-query → NO CANNIBALIZATION, TOPIC FOCUS PASS

Published ledger B02–B09: расписка, торги/задаток, доверенность СВО, скидка/бабушка, автооценка, наследство сын, умершая жена, ипотека/ЕГРН — **другой plot** (мошенническое влияние + нотариус 40%).

Live WP recent Aug 22–24 duplicate risk avoided: повестка, уставший покупатель, бабушка на осмотре, наследство, ипотека, ЕГРН строка — NOT this cluster.

NOT duplicate: matkapital cluster (на сайте), notarius +70k (Дзен), B02 расписка.

## Wordstat preflight

wordstat_get_user_info → OK (MCP-KV Yandex Cloud API)

## Wordstat live probes (regions 55+11176; compare RU 225)

| probe | volume 55+11176 |
|-------|-----------------|
| мошенники при покупке квартиры | 1 |
| проверка квартиры перед покупкой | 8 |
| юридическая проверка квартиры | 5 |
| купить квартиру в тюмени вторичка | 3996 |
| купить квартиру в тюмени (final P0) | **22660** |
| купить квартиру в тюмени (RU 225) | **39961** |

## wordstat_rework log (for handoff)

probe «мошенники при покупке квартиры» 1 → probe «проверка квартиры перед покупкой» 8 → probe «купить квартиру в тюмени вторичка» 3996 → final P0 «купить квартиру в тюмени» 22660 (RU225 39961) | clusters tried: мошенники 1, проверка 8, вторичка 3996

## signal_urls (required)

1. https://t.me/klyshin_A — обязательно (live 2026-08-24: посты про мошенники/нотариус 40%, дед и сейф, «нотариус не спасает»)
2. https://dzen.ru/holyslav — карточки про риски вторички, ВС по мошенникам (август 2026)
3. https://t.me/holyslav92

## external_signal (сегодня)

- Klyshin @klyshin_A: исследование — из нотариальных сделок с телефонными мошенниками устояли 40%; нотариус не психиатр и не видит давление; пожилой продавец может быть «режиссирован» по телефону (кейс деда с сейфом — красный флаг для сделок с жильём)
- Дзен holyslav: разбор оспаривания сделки под влиянием обмана, позиция ВС РФ (июль 2026) — добросовестность покупателя надо доказывать
- ГАРАНТ / ВС: определение 10.03.2026 № 84-КГ26-1-К3 — недействительность сделки под влиянием мошенников, реституция

## CRITICAL instruction for Derouter Scout

You are **writing** the handoff file content now. Wordstat preflight and all frequencies are **already fetched** in this document (MCP-KV live by thin conductor). **Do NOT** refuse or emit `DEROUTER SCOUT BLOCKER`. **Do NOT** ask for CallMcpTool. Output **only** the complete handoff markdown below.

## Output format required

YAML frontmatter keys: `topic_id`, `title`, `slug`, `article_dir`, `status: PASS`

Body starts with `=== SCOUT ===` then lines:

- wordstat_preflight: mcp-kv wordstat_get_user_info OK
- klyshin_hook: phone_scammers_notary | original: «…» | angle: … | signal: https://t.me/klyshin_A
- dzen_casus_shape: PASS | event: «…» | risk: «…» | time: «…» | finale: «…»
- comment_magnet_angle: «…?»
- wordstat_rework: (full log with numeric frequencies from table above)
- wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22660 | RU225 39961 | secondary probes…
- signal_urls: (bullet list of 3 URLs)
- external_signal: (2–4 sentences Russian)

Add 1 short paragraph `scout_rationale` — why this plot vs B02–B09 anti-dup.

Russian prose, Klyshin news energy, no checklist hook.
