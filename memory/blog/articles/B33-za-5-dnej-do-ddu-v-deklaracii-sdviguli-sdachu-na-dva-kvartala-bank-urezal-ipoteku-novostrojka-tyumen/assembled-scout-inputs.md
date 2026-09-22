# Assembled scout inputs — B33 slot 12 YEKT 2026-09-22

**MANDATORY:** Derouter utility tier `gpt-5.6-terra`. Output full handoff markdown body per SKILL.md only.

**run_date:** 2026-09-22  
**slot:** 12:00 Asia/Yekaterinburg (automation ~10:03 MSK)  
**topic_id:** B33  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень — newbuild_only  
**topic_market_focus:** newbuild_only

## HARD anti-dupe (avoid recent live WP + ledger)

Do NOT reuse recent plots: кладовая отдельный ДДУ, взнос 15→25%, терраса на картинке, УК 180к, КП −14 кв.м, эскроу чужое юрлицо, страховка, переуступка запрет, B32/B31/B30 chain, acceptance defects (B25), keys_delay penalty unpaid cluster, installment_penalty_developer (просрочка платежа), B12 post-escrow year slip.

`python3 scripts/excalibur_blog_scout_story_dup.py --sync-used-clusters` → 28 active locks (2026-09-22).

## Proposed lock (pre-checked 2026-09-22)

- **cluster_id:** `newbuild_declaration_completion_slip_before_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke` + `clock_ran_out`
- **newbuild_mechanism:** семья с одобренной ипотекой на квартиру в ЖК Тюмени; за **5 дней до подписания ДДУ** на dom.rf вышла **новая редакция проектной декларации** — срок передачи объекта сдвинут с **II кв. 2027** на **IV кв. 2027** (два квартала); в брони и черновике ДДУ оставался старый квартал; банк после сверки **урезал одобренную сумму** / потребовал новый пакет; семья **остановила сделку до эскроу**; бронь ~150–200 тыс ₽ под угрозой удержания (composite)
- **why_newbuild_not_secondary:** только цепочка ДДУ/проектная декларация 214-ФЗ на строящийся объект; нет продавца вторички, ЕГРН, наследников, опеки
- **title draft (H1):** «За 5 дней до ДДУ в декларации сдвинули сдачу на два квартала — банк урезал ипотеку на новостройку в Тюмени»
- **slug:** `za-5-dnej-do-ddu-v-deklaracii-sdviguli-sdachu-na-dva-kvartala-bank-urezal-ipoteku-novostrojka-tyumen`
- **article_dir:** `memory/blog/articles/B33-za-5-dnej-do-ddu-v-deklaracii-sdviguli-sdachu-na-dva-kvartala-bank-urezal-ipoteku-novostrojka-tyumen`
- **comment_magnet_angle:** «Если декларацию обновили за неделю до ДДУ и срок сдвинули на полгода — вы подписываете проект или снимаете бронь?»
- **scout_helper.py --check-query:** PASS 2026-09-22 (anti_dupe_hard PASS, topic focus PASS)
- **formula_spam_check:** last3 live B30 assignment ban, B31 insurance, B32 escrow entity — this is declaration completion date vs bank limit, new skeleton

## Wordstat MCP-KV (live 2026-09-22)

wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API)

| probe | regions | freq (phrase total) |
|-------|---------|---------------------|
| купить новостройку в тюмени | 55,11176 | **902** |
| купить новостройку в тюмени | 225 (compare) | **1914** |
| новостройки тюмень | 55,11176 | 8234 (context spine) |
| срок сдачи новостройка тюмень | 55,11176 | empty / API flake |
| срок сдачи новостройки | 55,11176 | API 499 flake |

**wordstat_rework:** probe «срок сдачи новостройка тюмень» empty → «срок сдачи новостройки» 499 → anchor buyer spine **«купить новостройку в тюмени» 902** (55+11176) + declaration slip mechanism in H1; RU compare **1914** (225)

**klyshin_hook:** optional | original: none

## dzen_casus_shape: PASS

- event: семья готовится к ДДУ на новостройку в Тюмени
- risk: сдвиг срока сдачи в декларации ломает ипотечный график и платёж
- time: 5 дней до подписания
- finale: стоп до эскроу; agency — сверять dom.rf vs бронь vs проект ДДУ

## signal_urls

- https://dzen.ru/holyslav
- https://www.domrf.ru/
- https://t.me/Tyumen_Rieltor
- {{SITE_BASE}}/blog/

Write complete Scout handoff with all required fields including `anti_dupe_hard: PASS`.
