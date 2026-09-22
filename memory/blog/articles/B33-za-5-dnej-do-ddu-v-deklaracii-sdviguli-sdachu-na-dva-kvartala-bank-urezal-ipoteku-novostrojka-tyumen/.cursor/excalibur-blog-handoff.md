# Scout Handoff — B33

- **run_date:** 2026-09-22
- **slot:** 12:00 Asia/Yekaterinburg
- **topic_id:** B33
- **tenant:** The Риэлтор / Святослав Шакин, Тюмень
- **topic_market_focus:** newbuild_only
- **article_dir:** `memory/blog/articles/B33-za-5-dnej-do-ddu-v-deklaracii-sdviguli-sdachu-na-dva-kvartala-bank-urezal-ipoteku-novostrojka-tyumen`

## Topic lock

- **cluster_id:** `newbuild_declaration_completion_slip_before_ddu_tyumen`
- **title draft / H1:**  
  **«За 5 дней до ДДУ в декларации сдвинули сдачу на два квартала — банк урезал ипотеку на новостройку в Тюмени»**
- **slug:**  
  `za-5-dnej-do-ddu-v-deklaracii-sdviguli-sdachu-na-dva-kvartala-bank-urezal-ipoteku-novostrojka-tyumen`
- **final P0:** `купить новостройку в Тюмени`
- **market:** Тюмень + Тюменская область
- **audience:** семьи с детьми и инвесторы, выбирающие строящуюся квартиру

## Required handoff fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK

top_energy_mirror: paper_clean_then_broke + clock_ran_out

newbuild_mechanism: семья с одобренной ипотекой готовится подписать ДДУ на квартиру в строящемся ЖК Тюмени; за 5 дней до подписания на dom.rf появляется новая редакция проектной декларации; срок передачи объекта меняется с II квартала 2027 года на IV квартал 2027 года; в брони и черновике ДДУ остается прежний срок; после сверки банк урезает одобренную сумму или требует новый пакет документов; семья останавливает сделку до перечисления денег на эскроу; бронь ориентировочно 150–200 тыс. рублей оказывается под угрозой удержания

why_newbuild_not_secondary: сюжет построен только на покупке строящегося объекта по ДДУ, проектной декларации, сроке передачи, ипотечном одобрении и эскроу по 214-ФЗ; вторичный рынок, продавец-физлицо, ЕГРН, наследство и опека отсутствуют

klyshin_hook: optional | original: none | signal: none

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: 28 active locks на 2026-09-22, включая кладовую отдельным ДДУ, взнос 15→25%, террасу на картинке, УК 180к, КП −14 кв.м, эскроу чужого юрлица, страховку, запрет переуступки, B32/B31/B30 chain, acceptance defects B25, keys_delay penalty unpaid, installment_penalty_developer и B12 post-escrow year slip

dzen_casus_shape: PASS | event: семья готовится к ДДУ на новостройку в Тюмени | risk: изменение срока передачи в проектной декларации ломает ипотечный график и платёжные параметры | time: 5 дней до подписания ДДУ | finale: семья останавливает сделку до эскроу; проверка dom.rf, брони и проекта ДДУ становится решающей

comment_magnet_angle: «Если декларацию обновили за неделю до ДДУ и срок сдвинули на полгода — вы подписываете проект или снимаете бронь?»

wordstat_rework: probe «срок сдачи новостройка тюмень» <empty/API flake> → «срок сдачи новостройки» <API 499 flake> → buyer-demand anchor «купить новостройку в тюмени» <902, регионы 55+11176> → final P0 «купить новостройку в Тюмени» <902>

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в Тюмени» <902> | RU compare «купить новостройку в тюмени» <1914> | context spine «новостройки тюмень» <8234>

story_dup_check: PASS | cluster_id: newbuild_declaration_completion_slip_before_ddu_tyumen

h1_fingerprint_check: PASS | fingerprint: 5_days_before_DDU + declaration_completion_date_slip + bank_mortgage_limit

formula_spam_check: PASS | last3_mechanisms: assignment_ban, insurance_requirement, escrow_entity_mismatch | current mechanism: declaration completion-date change before DDU affecting bank approval

anti_dupe_hard: PASS
```

## Editorial angle

The story is not a checklist about reading a declaration. The news-casus is a last-minute change before signing: the family believes the deal is ready, then a new declaration changes the delivery date, the bank recalculates the mortgage parameters, and the transaction stops before escrow.

The central dispute for comments:

- Is a new declaration with a later delivery date a sufficient reason to abandon the deal?
- Should the developer preserve the booking terms and the earlier mortgage parameters?
- Who bears the risk when the booking document and draft DDU still show the old quarter?

## Newbuild-only plot guard

The article must remain about a **Тюменская новостройка** and the chain:

`проектная декларация → срок передачи → ДДУ → ипотечное одобрение → эскроу`.

Do not retitle or redirect the plot toward secondary housing, a clean EGRN extract, a private seller, inheritance, guardianship, bankruptcy of a seller, or other secondary-market mechanisms.

## Signal URLs

- `https://dzen.ru/holyslav`
- `https://www.domrf.ru/`
- `https://t.me/Tyumen_Rieltor`
- `{{SITE_BASE}}/blog/`

## Verification note for Writer

Before presenting the case as a real-world news incident, verify the publication date and exact revision history of the project declaration on `dom.rf`, the wording of the booking terms, the draft DDU, and the bank’s recalculation. If those documents are not available, label the scenario as a composite case rather than attributing it to a named family or developer.
