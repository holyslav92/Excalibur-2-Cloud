# Scout handoff — B24

**run_date:** 2026-09-07  
**slot:** Monday, ~09:00 YEKT  
**tenant:** The Риэлтор — Святослав Шакин, Тюмень  
**market_focus:** newbuild_only  
**topic_id:** B24  
**status:** TOPIC LOCKED

## Locked topic

**Title draft / H1:**  
# В Тюмени в ДДУ был 12-й этаж — на ключах отдали квартиру на 2-м

**Slug:** `v-tyumeni-v-ddu-byl-12-etazh-na-klyuchah-otdali-kvartiru-na-2-m`

**Cluster ID:** `ddu_floor_changed_at_keys_tyumen`

**P0 demand spine:** `новостройки тюмень`

---

## Mandatory gates

klyshin_hook: optional | none | original: none
wordstat_rework: probe «этаж новостройка дду» empty (55+11176) → probe «приемка новостроек тюмень» 36 → probe «купить новостройку в тюмени» 865 → final P0 «новостройки тюмень» 4663 (55+11176) / 8691 (225)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «новостройки тюмень» 4663

**wordstat_preflight:** mcp-kv `wordstat_get_user_info` OK; Yandex Cloud API, Folder ID `b1g6bq34gkivjj20be06`.

**anti_repeat_preflight:** live_blog_20 + ledger + used-clusters sync OK; 29 active locks as of 2026-09-07. Closed/recent plots reviewed and excluded: escrow shortfall before DDU; 12-to-8 cadastral plot in КП; one apartment sold to two families; surcharge for finishing before keys; seven-month completion delay and unpaid penalty; 45 m² in DDU versus 41 m² in declaration; acceptance defects and penalty; apartments instead of apartment; instalment discount loss; rental ban before keys; assignment resale profit; failed trade-in before DDU. Proposed cluster is distinct.

**story_dup_check:** PASS  
**cluster_id:** `ddu_floor_changed_at_keys_tyumen`  
Distinct mechanism: floor and object fixed in booking/DДУ/application versus a different physical floor presented at key handover after alleged section redistribution or technical project correction.

**h1_fingerprint_check:** PASS  
**fingerprint:** `ddu_floor_fixed_vs_different_floor_at_keys_12_to_2`

**formula_spam_check:** PASS  
**last3_mechanisms:** apartment-status substitution; instalment discount loss on early payoff; rental restriction before keys. Current mechanism is a material mismatch of the DДУ object’s floor at acceptance, not a repeat of those skeletons.

**anti_dupe_hard:** PASS

---

## Newbuild-only lock

**top_energy_mirror:** `paper_clean_then_broke`

**newbuild_mechanism:** Этаж, секция and characteristics of the apartment are fixed in the booking documents, DДУ and its appendix. At handover, the developer offers keys to an apartment physically located on another floor, referring to project-documentation changes, section redistribution or a technical correction. The conflict is tied to acceptance act, mortgage disbursement, registration and remedies under 214-ФЗ.

**why_newbuild_not_secondary:** This is exclusively a newbuild chain: booking → DДУ → construction completion → key handover → acceptance act → mortgage/escrow and registration. There is no secondary-market seller, inherited title, EGRN-cleanliness plot, guardianship or resale transaction.

**klyshin_hook:** optional | none | original: none. Fresh Tyumen newbuild floor-mismatch casus selected without Klyshin; this is preferred because the hook is independently strong and does not reopen a closed plot.

---

## Dzen news-casus shape

**dzen_casus_shape:** PASS

- **Event:** A Tyumen family selected an apartment on the 12th floor of a new building because of the view, quietness and perceived value, paid the booking and signed a DДУ where the floor is stated in the appendix.
- **Risk:** On key handover, the developer leads them to an apartment on the 2nd floor. The view, street noise exposure, privacy and market value are materially different. The developer cites a redistribution inside the section or a technical project correction. Without an acceptance act, the mortgage’s final stage and registration of title are stalled.
- **Time:** The dispute erupts on the day of key handover and acceptance, two to three years after signing the DДУ, when the family arrives expecting to take possession and arrange furniture delivery.
- **Finale:** The family does not sign the acceptance act. The developer offers a “compensation” framed as a parking discount; the family refuses. A pre-trial claim follows, mortgage payments become a pressure point, keys are not received, and the conflict moves toward a demand for replacement of the object or DДУ termination.

**comment_magnet_angle:** «В ДДУ чётко написан 12-й этаж, а на ключах дают 2-й: вы бы подписали акт ради мебели и ипотеки — или пошли бы в суд, даже если застройщик предложит скидку на паркинг?»

---

## Wordstat demand spine

**wordstat_rework:**

1. Probe `этаж новостройка дду`, regions 55 + 11176 → API empty, no usable tail; phrase is too narrow. The casus was retained.
2. Probe `приемка новостроек тюмень`, regions 55 + 11176 → 36; relevant to the keys stage, but insufficient as the primary demand spine.
3. Probe `купить новостройку в тюмени`, regions 55 + 11176 → 865; strong buyer-intent support.
4. Rework toward broader local buyer language while retaining the DДУ/keys casus in the headline and narrative.
5. Final P0: `новостройки тюмень`.

**wordstat:** mcp_kv live | regions 55, 11176, compare 225 | P0 `новостройки тюмень` — **4,663** for regions 55 + 11176; **8,691** for RU region 225.

**Supporting Wordstat signals:**

| Query | Regions | Frequency |
|---|---:|---:|
| приёмка новостроек тюмень | 55 + 11176 | 36 |
| приёмка квартиры в новостройке тюмень | 55 + 11176 | 33 |
| купить новостройку в тюмени | 55 + 11176 | 865 |
| новостройки тюмень | 55 + 11176 | 4,663 |
| новостройки тюмень | 225 | 8,691 |

---

## Research brief for Research role

### Core fact pattern to investigate

Research must treat the stated family story as a **news-casus narrative frame**, not as a verified claim about a named Tyumen developer. Build the article around the legally and practically decisive question: what follows if the apartment handed over under a DДУ does not match the floor/object characteristics fixed in the contract and annexes.

Verify:

1. Which characteristics of a shared-construction object must be set out in a DДУ and its annexes: project, section, entrance, floor, conditional number, area, layout and other identifying specifications.
2. Whether a developer can unilaterally replace an apartment on the 12th floor with one on the 2nd floor by reference to a changed project declaration or technical correction.
3. The distinction between:
   - permissible project-documentation amendments;
   - actual changes to the individual DДУ object;
   - a buyer’s consent through an additional agreement;
   - handover of an object that does not correspond to the contract.
4. What a buyer should document before any signature: DДУ, annex with plan/floor, booking agreement, correspondence, project declaration versions, notice of changes, viewing video, acceptance-act wording and developer explanations.
5. What refusal to sign the act means in practice and how to state objections accurately; avoid claiming that a buyer may simply stop mortgage payments as a legal remedy.
6. Available routes to examine with a lawyer: demand for a conforming object where possible, price reduction/compensation issues, defect or non-compliance claim, termination grounds, damages and court procedure. Legal outcomes depend on the DДУ wording and evidence.
7. Mortgage/escrow operational consequences: clarify the lender’s and escrow bank’s procedures rather than asserting automatic outcomes. Explain that acceptance, registration and credit disbursement processes may be affected, but conditions are bank- and contract-specific.
8. Price and consumer logic: why 12th versus 2nd floor can be material for view, noise, privacy, security and market perception; do not invent a universal percentage of discount.

### Required narrative arc

Open immediately with the key-handover scene: the family expects the 12th floor from the DДУ, arrives with plans for furniture, and is brought to the second floor. Then reveal the developer’s explanation and the pressure created by the unsigned act, mortgage process and delayed move-in. Finish with the unresolved pre-trial dispute and the reader question.

This must remain a news-casus, not a calm “how to accept a newbuild apartment” checklist.

### Compliance and wording constraints

- Do not present the described developer conduct as a proven real case unless a publicly verifiable case with documents is found.
- Do not name a developer without reliable source evidence.
- Do not guarantee contract termination, compensation, mortgage suspension or a court result.
- Clearly distinguish a project-documentation amendment from contractual consent to change a particular apartment.
- Keep the plot entirely in Tyumen newbuilds and DДУ mechanics.
- Do not drift into secondary housing, EGRN, seller insolvency, inheritance, guardianship, matкапитал-secondary or generic legal guides.
- Do not use Meta/Instagram/Facebook/LinkedIn/X/Discord/VPN hooks or heroes.

---

## Signal URLs

- https://dzen.ru/holyslav — channel context; not a duplicate-cluster source.
- https://www.consultant.ru/document/cons_doc_LAW_51057/ — ГрК РФ; project documentation and amendments.
- https://www.consultant.ru/document/cons_doc_LAW_122475/ — 214-ФЗ; DДУ and participant rights where the object differs from contractual terms.
- https://www.domrf.ru/ — developer registry and project-declaration verification.
- https://t.me/Tyumen_Rieltor
- https://t.me/klyshin_A — checked, not used in this slot.
- `{{SITE_BASE}}/blog/` — live publication history and local editorial context.

---

## Final lock

**final P0:** `новостройки тюмень`  
**final title:** `В Тюмени в ДДУ был 12-й этаж — на ключах отдали квартиру на 2-м`  
**final slug:** `v-tyumeni-v-ddu-byl-12-etazh-na-klyuchah-otdali-kvartiru-na-2-m`  
**topic_market_focus:** newbuild_only  
**dzen_casus_shape:** PASS  
**anti_dupe_hard:** PASS
