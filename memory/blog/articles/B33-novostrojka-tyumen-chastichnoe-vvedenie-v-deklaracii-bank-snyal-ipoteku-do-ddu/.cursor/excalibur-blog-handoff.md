# Scout handoff — B33

- **run_date:** 2026-09-25
- **slot:** ~15:00 YEKT
- **tenant:** The Риэлтор — Святослав Шакин, Тюмень
- **topic_market_focus:** newbuild_only
- **dzen_rf_pack:** true
- **topic_id:** B33
- **article_dir:** `memory/blog/articles/B33-za-4-dnya-do-ddu-v-tyumeni-v-deklaracii-vsplylo-chastichnoe-vvedenie-doma-bank-snyal-ipoteku`
- **slug:** `za-4-dnya-do-ddu-v-tyumeni-v-deklaracii-vsplylo-chastichnoe-vvedenie-doma-bank-snyal-ipoteku`
- **title_draft:** **За 4 дня до ДДУ в Тюмени в декларации всплыло частичное введение дома — банк снял ипотеку на новостройку**

## Lock

- **cluster_id:** `newbuild_partial_commissioning_declaration_before_ddu_tyumen`
- **top_energy_mirror:** `paper_clean_then_broke`
- **newbuild_mechanism:** Семья покупает квартиру в многосекционной новостройке Тюмени по ДДУ с ипотекой. В брони и на визуализации — «дом сдан, ключи скоро». За 4 дня до подписания ДДУ юрист сверил проектную декларацию на dom.rf: в реестре указано частичное введение в эксплуатацию — введён только один корпус или секция, а секция с выбранной квартирой ещё не введена. При проверке объекта залога банк пересчитал риск срока и снял одобрение ипотеки; эскроу не открыли, бронь оказалась под удержанием.
- **why_newbuild_not_secondary:** Сюжет касается только покупки квартиры у застройщика по ДДУ и связан с проектной декларацией, вводом секций, 214-ФЗ, эскроу и ипотечным одобрением. Продавца-физлица, вторичной ЕГРН-сделки и вторичного рынка в сюжете нет.
- **klyshin_hook:** optional — none; оригинальный Klyshin-hook не используется.
- **frozen_secondary_check:** PASS — вторичный рынок и frozen secondary clusters не затрагиваются.

## Anti-repeat preflight

- **anti_repeat_preflight:** live_blog_20 + ledger + used-clusters sync OK
- **closed_clusters учитывались:** parking DDU / машино-место; investor assignment; last-floor mortgage; matkapital SFR escrow; kindergarten on render; family mortgage child 7 years; cottage forest / КП gas; land lease; furniture pack; co-borrower freeze; showroom ceiling; window courtyard; delivery shift; insurance requote; escrow wrong entity; assignment resale ban; acceptance/handover defects; B26 — отсутствие разрешения на ввод всего дома; B22 — перенос срока сдачи; B27 — земельные права.
- **anti_repeat_result:** предложенный сюжет не повторяет закрытые кластеры: речь не об отсутствии разрешения на ввод всего дома, а о частичном вводе многосекционного объекта до подписания ДДУ.
- **dzen_casus_shape:** PASS
  - **event:** семья с ипотекой выбрала квартиру в ЖК Тюмени; менеджер говорил, что дом уже сдаётся.
  - **risk:** частичный ввод означает, что секция с квартирой формально ещё не введена; банк может не принять объект в залог и снять одобрение, а деньги не уйдут на эскроу вовремя.
  - **time:** 4 дня до назначенного подписания ДДУ; вечером перед визитом в банк семья открыла проектную декларацию.
  - **finale:** в декларации обнаружился частичный ввод. Застройщик предложил подписать ДДУ, а остальное «довести позже». Семья отказалась; часть брони удержали, ипотеку пришлось пересобирать на другой лот.
- **comment_magnet_angle:** «Если в декларации частичный ввод, а вам обещали “уже сдано”, вы подпишете ДДУ ради сохранения брони или дождётесь полного ввода секции?»

## Wordstat

- **wordstat_preflight:** mcp-kv `wordstat_get_user_info` OK
- **wordstat:** mcp_kv live | regions 55, 11176, compare 225 | P0 **«купить новостройку в тюмени» — 892** запросов
- **wordstat_context:** «новостройки тюмень» — 3504, регион 55; используется как контекстный рыночный ориентир, не как замена P0.
- **wordstat_rework:** probe «ввод в эксплуатацию новостройки» — API low / sparse → probe «разрешение на ввод новостройки» — weak → anchor P0 **«купить новостройку в тюмени» — 892**; механизм частичного ввода сохраняется в H1 и сюжете, но не используется как самостоятельный demand spine.
- **demand_note:** слабая частота узкого механизма не является причиной менять news-casus на чеклист или уходить от новостроек.

## Gate results

- **story_dup_check:** PASS
- **story_dup_cluster_id:** `newbuild_partial_commissioning_declaration_before_ddu_tyumen`
- **story_dup_note:** distinct from B26 permission-to-commission cluster: B26 concerned no permit for the whole building; B33 concerns partial commissioning of a multi-section building before DDU, with the selected apartment in a non-commissioned section.
- **h1_fingerprint_check:** PASS
- **h1_fingerprint:** `4-дня-до-ДДУ + частичное-введение-секции + банк-снял-ипотеку`
- **formula_spam_check:** PASS
- **formula_spam_note:** mechanism is not a repeat of the last three slots; the story uses a declaration/status mismatch before DDU, not parking, assignment, floor, matkapital, rendering, or handover-defect mechanics.
- **anti_dupe_hard:** PASS
- **topic_focus:** PASS — newbuild only
- **dzen_news_casus:** PASS — completed event, concrete risk, deadline, finale, and comment magnet present.

## Research handoff

Research role must verify the mechanism and keep the article tied to a real newbuild purchase in Tyumen.

### Research angles

1. **Project declaration status**
   - Check how dom.rf displays the commissioning status of a multi-section or multi-corpus project.
   - Establish the difference between the whole residential complex being marketed as “ сдаётся / дом сдан” and the specific section containing the buyer’s apartment being commissioned.
   - Confirm whether the declaration records partial commissioning and what wording is used.

2. **DДУ and 214-ФЗ**
   - Verify which project and apartment details should be matched before signing a DDU: building, корпус, секция, apartment, expected completion or commissioning status.
   - Use the current 214-ФЗ source from Consultant as the legal reference; do not turn the article into a general legal checklist.
   - Avoid asserting that partial commissioning automatically makes a DDU unlawful unless the source directly supports that conclusion.

3. **Mortgage and escrow mechanics**
   - Verify why a bank can reassess or withdraw mortgage approval when the collateral is in a section that has not been commissioned.
   - Separate mortgage approval from the opening or funding of the escrow account.
   - Mark any bank-specific practice as bank-specific; do not present one lender’s internal rule as universal.

4. **Tyumen buyer scenario**
   - Keep the event local: family, Tyumen ЖК, apartment bought from a developer, DDU and mortgage.
   - Check whether the title’s “4 days” is supported by the case materials available to Research. If it is a reconstructed editorial scenario, label the details carefully and do not invent a developer, ЖК, bank, or exact amount.
   - Clarify the final outcome: family did not sign the DDU, part of the booking payment was retained, and mortgage was reworked for another lot only if supported by the source pack.

5. **Comment conflict**
   - Present the dispute without a calm how-to structure: one side argues that the buyer should trust the developer and preserve the booking; the other argues that the declaration status of the exact section must prevail over sales language.
   - End with the stated question about signing for the sake of the booking versus waiting for full commissioning.

## Signal URLs

- `https://www.domrf.ru/` — project declarations and commissioning status
- `https://www.consultant.ru/document/cons_doc_LAW_51040/` — 214-ФЗ
- `https://dzen.ru/holyslav`
- `{{SITE_BASE}}/blog/`
- `https://t.me/Tyumen_Rieltor`

## Editorial constraints for Research and Writer

- Plot only a Tyumen newbuild purchase from a developer.
- Do not retitle into a secondary-market story.
- Do not recycle the B26 “no permit for the whole building” plot.
- Do not make the article a neutral “N steps” or general buyer guide.
- Preserve the news-casus sequence: sales promise → declaration check → four-day deadline → bank reaction → family’s decision.
- Keep the top-energy emotional shape: documents appeared clean at the sales stage, then the financing broke immediately before signing.
- Any legal, banking, or dom.rf claim must be checked against the cited source before publication.
