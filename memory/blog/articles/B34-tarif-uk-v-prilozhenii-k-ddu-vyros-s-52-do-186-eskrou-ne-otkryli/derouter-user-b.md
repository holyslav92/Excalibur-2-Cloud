# Assembled research inputs — B34 (2026-10-11)

## Scout handoff summary
- topic_id: B34, slot_rubric: novostroyki, cluster: newbuild_hoa_tariff_ddu_appendix_vs_sales_broni_tyumen
- H1 draft: В Тюмени за 3 дня до ДДУ тариф управляющей компании в приложении вырос с 52 до 186 рублей — эскроу не открыли
- Composite casus (Scout): studio in Tyumen newbuild for future rent; bron promises ~52 ₽/m² maintenance; 3 days before DDU signing app.2 shows UK 186 ₽/m² + mandatory “smart home” 320 000 ₽; mortgage/rent model breaks; refuse DDU/escrow; bron 150k returned partially (~80k withheld).
- fact_boundary: NO verified press report of this exact deal. Numbers 52, 186, 320k, 150k, 80k are editorial scenario parameters unless separately sourced.
- P0 Wordstat (Scout, live dynamics 2025-10): «новостройки тюмень» 5670 (regions 55, 11176); compare «новостройки» RU 225 — 1 263 808. wordstat_get_top_requests failed 400 on 2026-10-11 — WORDSTAT PARTIAL.
- signal_urls: https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://www.domrf.ru/, https://dzen.ru/a/YA7B343-ezstBMCs (energy only)
- comment_magnet: sign DDU to save bron vs walk losing part of bron

## Fresh external signals (accessed 2026-10-11, prefer post 2026-10-01)

### RIA Novosti 2026-10-01
- URL: https://ria.ru/20261001/uslugi-2121338307.html
- From 1 Oct 2026 second indexation of utility payments in Russia; govt approved Jan + Oct 2026 indexations.
- Regional cap index 8–22%; not uniform per line in bill; regions may set lower; municipal deviation ranges 2.1–21.9% (0% deviation cap for Moscow, SPb, Sevastopol).

### NGS.ru 2026-10-01
- URL: https://ngs.ru/text/economics/2026/10/01/76670405/
- Second 2026 indexation 8–22%; Bank of Russia estimates ~17% cumulative tariff growth in 2026.
- **Important for angle:** indexation does NOT cover “плата за содержание и ремонт общего имущества” and capital repair — other rules apply.

### АиФ Тюмень 2026-10-01 08:02
- URL: https://tmn.aif.ru/society/novye-rascenki-s-1-oktyabrya-2026-goda-vyrosli-tarify-zhkh-na-chem-sekonomit
- Tyumen region cap index for communal services **17.2%** (among highest nationally).
- Tyumen city water +32.4%, wastewater +28.3% cited; USTEK heat tariff example 2193.72 → 2746.32 ₽/Gcal (~25.2%).
- Electricity with electric stove first tier up to 3900 kWh: **3.37 ₽/kWh** (day/night zones described).

### Federal index table (gov distribution PDF mirror)
- URL: https://gkh24.ru/upload/file/25112025_3413_r.pdf (Распоряжение Правительства РФ от 25.11.2025 № 3413-р)
- Tyumen oblast: Jan index 1.7%, Oct index **17.2%**; municipal deviation band 0–9.9%.

### 72.ru / E1.ru network 2026-09-29/30 (Tyumen context)
- Tyumen oblast +17.2% communal index from Oct 2026; example +~1000 ₽/month on ~6000 ₽ bill.
- Note: separate piece mentions Tyumen city utilities can rise stronger (up to ~27.9% cited in 72.ru cross-ref) — verify as media estimate not single legal rate.

## Legal / official mechanics (for Writer — not lead prose)

### 214-ФЗ (Consultant official text)
- URL: https://www.consultant.ru/document/cons_doc_LAW_51038/
- Art. 4 DDU; Art. 15.4–15.5 escrow accounts for DDU; escrow blocks buyer funds until conditions in law/DDU; buyer opens escrow with authorized bank named in DDU/project declaration.
- Refusing to sign/register DDU → escrow not funded for that deal (mechanism: no registered DDU path for escrow transfer).

### Escrow (bank official pages — general физлица)
- VTB escrow page (fetched partial): DDU specifies escrow agent; depositor opens escrow for DDU settlements per 214-ФЗ.
- DOM.RF Bank press: remote escrow + accreditive in app (2024 press) — process automation after DDU registration.

### Housing payment timing (VS Plenum 22 official)
- URL: https://www.vsrf.ru/documents/own/16145/
- Maintenance fee (плата за содержание) size in MKD without HOA: determined considering UK proposal, set **not less than one year** (JK RF art. 44 p.5 p.2, art. 156 p.7).
- UK cannot unilaterally charge above contract/OSS decision (JK art. 156 p.7, 162).
- **Buyer maintenance obligation** for owned unit: typically from transfer act / possession, not from bron PDF (JK art. 153 — платежи с момента возникновения права или с даты передачи по акту; застройщик несёт расходы до передачи — standard reading in DDU templates and guides).

### DDU templates (illustrative, not Tyumen case)
- Typical DDU clauses: dольщик pays maintenance/utilities from **transfer act** date; may require future contract with UK named in project.
- Mandatory “smart home” or lump-sum service packages in appendix = **contractual additional obligation**, distinct from regulated communal indexation Oct 2026.

### Oct 2026 news vs UK ₽/m² in appendix
- Federal/regional **communal** indexation (water, heat, power) ≠ automatic legal ceiling for **содержание жилого помещения** line in future UK contract.
- Scout jump 52→186 ₽/m² is **not** explained by 17.2% regional index alone (math: 52×1.172≈61). Writer must treat gap as disclosure/contract issue in casus, not as “ЖКУ выросло с 1 октября” alone.

## Overlap check (published-titles-only)
- Near neighbors: B25 DDU finish promises; B27 declaration vs bron; B29–B32 pre-DDU/escrow stops; B33 “186 thousand” debt — different mechanism (utility debt secondary).
- B34 unique: UK tariff + mandatory service package in DDU appendix after bron.

## Constraints for research output
- Russian language
- Include: research_date, reader_problem, reader_outcome, practical_facts, constraints, voice_angle, surprising_fact, official_verifications, source_table, writer_safe_urls
- No h2_outline, FAQ, lead, action_outline
- Mark composite casus clearly
- official_source_audit: required for bank tariffs — this article uses UK ₽/m² as scenario + law/context; verify 214-ФЗ, VS Plenum, govt index where cited; do NOT claim bank commission tariffs
