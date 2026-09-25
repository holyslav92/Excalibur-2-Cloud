# Assembled research inputs — B33 (Derouter research role)

**MANDATORY:** Derouter utility tier `gpt-5.6-terra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role research`. Do **NOT** output `DEROUTER RESEARCH BLOCKER`, meta-commentary, or refuse synthesis. Output the **complete** Russian `research-notes.md` body only (markdown). No preamble.

**research_date:** 2026-09-25  
**article_dir:** memory/blog/articles/B33-novostrojka-tyumen-chastichnoe-vvedenie-v-deklaracii-bank-snyal-ipoteku-do-ddu  
**cluster_id:** newbuild_partial_commissioning_declaration_before_ddu_tyumen

## Scout handoff (mechanism, casus, constraints)
- Tyumen newbuild only: family buys apartment in multi-section ЖК from developer, DDU + mortgage + escrow planned.
- Sales promise: «дом сдаётся / ключи скоро»; 4 days before scheduled DDU signing, lawyer checks project declaration on dom.rf / ЕИСЖС.
- Registry shows **partial commissioning** (частичный ввод): one corpus/section commissioned, buyer's section not yet commissioned.
- Bank reassesses collateral risk, withdraws mortgage approval; escrow not opened; booking deposit partly retained; family reworks mortgage on another lot.
- **Distinct from B26:** B26 = no RVE for whole building / tranche blocked. B33 = partial commissioning of multi-section project; buyer's section not in commissioned part.
- **Distinct from B27:** land rights in declaration (lease vs ownership), not commissioning status.
- Composite casus: no specific ЖК, developer, bank, address, surnames, exact booking amounts unless labeled editorial.
- comment_magnet: sign DDU to keep booking vs wait for full section commissioning?

## Wordstat MCP-KV (region 55 Tyumen oblast, 2026-09-25)
| phrase | volume | note |
|--------|--------|------|
| новостройки тюмень | 3504 | market context |
| купить новостройку в тюмени | 678 | P0 anchor (scout cited 892 — API variance) |
| новостройки в тюмени от застройщика | 469 | support |
| ввод в эксплуатацию новостройки | 334 | RU 225 — mechanism weak vs P0 |
| разрешение на ввод в эксплуатацию новостройки | 31 | in RU top under parent |
| проектная декларация застройщика | 1157 | RU 225 |
| дом рф проектные декларации застройщиков | 370 | demand to check dom.rf |

## SERP / fresh signals (research-serp.json + live fetch)
- **nashgorod.ru 2026-09-25** (SERP): regional news on new family mortgage rules; snippet — mid-September 2026 Tyumen family stopped buying 3-room newbuild on east side (context: mortgage/access, not this exact casus).
- **mperspektiva.ru** article on Tyumen developer tax bankruptcy (428 mln); page **updated 2026-09-25**; mentions ЖК «Акватория» infrastructure problems in 2026 — local newbuild risk atmosphere, not casus proof.
- **dzen.ru/holyslav** — tenant channel; sibling posts on DDU/bank stops before signing (accreditation, insurance) — same emotional lane «paper clean then broke».
- **t.me/Tyumen_Rieltor** — tenant Telegram, active newbuild channel (community signal week of 2025-09-25).

## Legal / official (214-FZ, EИСЖС, form)
### Art. 8 214-FZ — transfer
- Developer transfers apartment **not earlier than** obtaining permission to put the object into operation (RVE / ввод в эксплуатацию). (Standard reading used in B26 research; Consultant LAW_51038.)

### Art. 19 ч. 4 214-FZ — declaration & partial projects
- Developer must update declaration monthly by 10th of following month.
- **If project provides several buildings:** after EИСЖС publishes commissioning data for one MKD/object, **changes to declaration regarding that commissioned object are no longer required**; disclosure continues for remaining stages.
- After commissioning of **all** objects in the project, changes to declaration for the project are no longer required.

### Art. 21 214-FZ — project information in declaration
- Must include data on construction project, including **terms of obtaining commissioning permit** for MKD/objects (per structure of art. 21 + Minstroy form).

### Art. 15.5 214-FZ — escrow
- Escrow funds released to developer after RVE presented to bank or appears in EИСЖС (typically within 10 working days) — ties buyer financing to real construction/commissioning status.

### Minstroy order 239/пр (04.04.2022) — declaration form
- Separate sections for project objects; fields for **date of commissioning permit** per object/stage.
- Multi-corpus projects: check declaration for **the specific building/section** of the chosen apartment, not marketing of «whole ЖК».

### EИСЖС / dom.rf
- Public portal: **наш.дом.рф** / www.dom.rf — project declarations, object cards, commissioning/RVE data (Scout signal_urls).
- Buyer path: find object in catalog → open **project declaration** PDF/HTML → match **корпус/секция/строительный адрес** to DDU draft → check commissioning status and dates for **that** object.

## Mortgage / bank (generic, not one bank's tariff)
- Mortgage **approval** is preliminary; bank checks collateral (future apartment in specific building), developer accreditation, project stage.
- If object is in **non-commissioned** section while marketing says «already handed over», bank may **withdraw or suspend approval** until status clarifies — bank-specific credit policy, not a single 214-FZ article.
- **Do not** state partial commissioning makes DDU automatically void — DDU can be signed for uncommissioned objects in many projects; risk is mismatch with promises, financing, and transfer timing under art. 8.
- Escrow opening is separate step from approval; without approval, family may not reach escrow funding.

## Overlap (published-titles-only.md)
- No duplicate title for partial commissioning + declaration + bank before DDU.
- Near siblings: B26 (no RVE whole building), B27 (land lease in decl.), B22/B29/B31 (bank moves before DDU other mechanisms).

## Writer constraints from handoff
- News-casus only; no neutral N-step guide.
- Preserve: sales promise → declaration check → 4-day deadline → bank → family decision.
- No invented ЖК/bank/developer names.

## Output instructions for Derouter
Produce `research-notes.md` in Russian with sections:
research_date, topic_id, reader_problem, reader_outcome, casus_boundary, practical_facts, constraints, local_context, voice_angle, surprising_fact, official_verifications (table), source_table (id|title|url|type|what|accessed_at), writer_safe_urls.
NO h2_outline, lead, FAQ, action_outline.
All accessed_at = 2026-09-25.
