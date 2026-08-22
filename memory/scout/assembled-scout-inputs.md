# OUTPUT INSTRUCTION (HARD)

You ARE the Derouter scout utility tier. Your ONLY job: write the scout handoff markdown below. Do NOT say you lack shell access. Do NOT give bash instructions. Output ONLY the handoff block starting with topic_id.

---

# Scout assembled inputs — 2026-08-22

## topic_id: B08

## Title draft
В объявлении бабушка — на сделке всплыла опека: регистрацию в Тюмени отменили

## Klyshin hook
- id: elderly_pnd_serbsky
- original: «бабушка в объявлении — а в квартире её нет»
- signal: https://t.me/klyshin_A (пост про ПНД, старая доверенность, скидка 1→3 млн, «где спит бабушка»)

## Casus (dzen_news_casus PASS)
- event: продажа 1/3 доли по старой доверенности, бабушка в «санатории» (ПНД)
- risk: опека / дееспособность / доверенность без выписки
- time: через две недели после аванса, на регистрации
- finale: Росреестр приостановил → сделку отменили, аванс вернули через суд

## Wordstat live MCP-KV
- preflight: wordstat_get_user_info OK
- probe «доверенность на продажу квартиры» → 97 (55+11176)
- final P0 «купить квартиру в тюмени» → 22880 (RU225 40230)

## Anti-dup: scout_helper PASS, not in story clusters

## Signals
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

Write handoff with fields: topic_id, title, slug suggestion, klyshin_hook, dzen_casus_shape, wordstat_rework, wordstat, wordstat_preflight, external_signal, signal_urls.
