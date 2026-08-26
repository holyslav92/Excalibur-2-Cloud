# Scout assembled inputs — B10 — 2026-08-26

## INSTRUCTION FOR DEROUTER SCOUT (READ FIRST)
You are the Scout utility writer. The Cursor conductor ALREADY ran MCP-KV Wordstat live (`wordstat_get_user_info` OK + all probes below). **Do NOT refuse** for missing MCP tools. **Do NOT** re-run Wordstat. Your only task: write the final `.cursor/excalibur-blog-handoff.md` content in Russian using the structured fields below. Output ONLY the handoff markdown body (no meta-refusal).

## Run context
- topic_id: B10
- EXCALIBUR_TOPIC_SELECTION=needs_scout
- setup_complete=true, dzen_rf_pack=true
- Published ledger: B02–B09 (see shared/published-articles.md)
- Next topic_id confirmed: B10 (scout_helper --suggest-next)
- Live WP drift: 20 slugs not in ledger — do NOT reuse their story clusters

## Forbidden / used story clusters (HARD anti-dup)
- inheritance_son_first_marriage (B07, live WP)
- matkapital_missing_child_shares (live WP na-matkapital-kupili-detskie-doli-proverte)
- doverennost_svo (B04)
- deposit_before_auction / gift before deposit (B03)
- discount_two_million (B05, B06, live PND 3mln)
- mortgage+EGRN line (B09)
- marriage/deceased wife (B08)
- summons stop registration (live WP avans-vnesli-registraciyu-priostanovili-po-povestke)
- notary court cancel (live WP v-tyumeni-notarius)
- clean extract flip 3 months (live WP v-vypiske-vse-chisto)
- elderly PND babushka (live WP skidka-skryla-pnd, B05 overlap)
- receipt no money (B02)

## Selected hook (Klyshin × Wordstat × news-casus)
- hook_id: five_court_schemes (scheme #1 — post-purchase seller bankruptcy)
- original Klyshin: «5 схем — квартиру забирают судом после покупки» — схема 1: продавец ушёл в банкротство, финуправляющий оспаривает сделку за 3 года
- signal: https://t.me/klyshin_A (пост 2026-08 про видео «5 схем»; свежий вебинар 2026-08-26 про проверку до аванса)
- angle: покупатель в Тюмени проверил ЕГРН, внёс аванс, зарегистрировал право — через год продавец признан банкротом, финуправляющий оспорил сделку как подозрительную
- localize: Святослав Шакин / Тюмень (не Москва/Дубай)

## Title draft (news headline, Klyshin rhythm)
Купили квартиру в Тюмени — через год финуправляющий оспорил сделку

## Slug suggestion
kupili-kvartiru-finupravlyayushchiy-osporil-sdelku-cherez-god

## dzen_casus_shape
PASS
- event: «сделка зарегистрирована, покупатель въехал»
- risk: «банкротство продавца, оспаривание финуправляющим (подозрительная сделка)»
- time: «через год после регистрации»
- finale: «суд отменил регистрацию / обязал вернуть квартиру»

## comment_magnet_angle
«Покупатель не знал о долгах продавца — он всё равно должен вернуть квартиру?»

## Wordstat live MCP-KV (regions 55+11176; compare 225)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes:
1. «банкротство продавца квартиры» — 27 (55+11176)
2. «имущество банкротов» — 143 (rework cluster, same risk/story)
3. «купить квартиру в тюмени вторичка» — 3968 (buyer spine)
4. final P0 «купить квартиру в тюмени» — 22652 (55+11176); compare RU225 — 39858

wordstat_rework: probe «банкротство продавца квартиры» 27 → rework «имущество банкротов» 143 → rework «купить квартиру в тюмени вторичка» 3968 → final P0 «купить квартиру в тюмени» 22652 | clusters tried: банкротство продавца, имущество банкротов, вторичка тюмень, buyer spine

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 22652 | probe «банкротство продавца квартиры» 27 | «имущество банкротов» 143 | «купить квартиру в тюмени вторичка» 3968 | RU225 P0 39858

## signal_urls (today)
1. https://t.me/klyshin_A
2. https://dzen.ru/holyslav
3. https://t.me/holyslav92

## scout_helper pre-check
--check-query passed: NO STORY DUPLICATE, TOPIC FOCUS PASS

## Output format required
Write `.cursor/excalibur-blog-handoff.md` with: topic_id, title draft, slug, external_signal summary, signal_urls, klyshin_hook line, dzen_casus_shape line, comment_magnet_angle, wordstat_preflight, wordstat_rework, wordstat lines. Russian prose, engagement bomb for Dzen.
