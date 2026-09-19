# Scout handoff — B29

**topic_id:** B29  
**run_date:** 2026-09-19  
**slot:** 15:00 Asia/Yekaterinburg  
**tenant:** The Риэлтор / Святослав Шакин, Тюмень  
**status:** LOCKED

## Topic

**cluster_id:** `newbuild_developer_zero_down_program_expired_before_ddu_tyumen`

**Title draft / H1 direction:**

> В Тюмени за шесть дней до ДДУ банк снял ипотеку без взноса от застройщика — семья не успела собрать первоначальный платёж

**P0:** «ипотека от застройщика тюмень» — **514**  
**Wordstat source:** live MCP-KV Wordstat  
**Regions:** Тюмень — 55; Тюменская область — 11176; comparison region — RU 225

## Required Scout fields

```text
wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: clock_ran_out
newbuild_mechanism: квартира в новостройке Тюмени; sales office promised «ипотека без первоначального взноса от застройщика» through a developer-linked subsidized bank program; mortgage was initially approved on those terms, but six days before DDU the bank notified the family that the program/subsidy window had ended; projected monthly payment rose by approximately 18,000 ₽; family could not assemble the down payment before signing; deal stopped before escrow; booking payment of approximately 50,000–80,000 ₽ was withheld in the composite casus
why_newbuild_not_secondary: сюжет построен только вокруг ДДУ, developer promo, bank subsidy and escrow path in a Tyumen newbuild; no secondary-market seller, EGRN-clean apartment, guardianship, inheritance or bankruptcy plot
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK; today’s B27 and B28 excluded; closed-cluster check passed for the proposed cluster
dzen_casus_shape: PASS; event: family entered a Tyumen newbuild purchase track using a developer zero-down mortgage offer; risk: bank/developer subsidy program could disappear before DDU; time: six days before DDU; finale: family stopped before escrow, could not assemble the payment, and faced partial booking loss
comment_magnet_angle: «Если банк снимает “нулевой взнос” за неделю до ДДУ, вы бы торопились подписать или ждали, пока застройщик вернёт программу?»
wordstat_rework: probe «бронь новостройка тюмень» — MCP empty once → final demand spine «ипотека от застройщика тюмень» — 514; mechanism retained as zero-down developer-promo expiry
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «ипотека от застройщика тюмень» — 514
story_dup_check: PASS | cluster_id: newbuild_developer_zero_down_program_expired_before_ddu_tyumen
h1_fingerprint_check: PASS | fingerprint: six_days_before_DDU + developer_zero_down_mortgage_program_ended
formula_spam_check: PASS | last3_mechanisms: bank/developer promo clock; differs from B27 land-lease/declaration mismatch and B28 gas declaration-date mismatch
anti_dupe_hard: PASS
```

## Demand probes

| Запрос | Результат |
|---|---:|
| ипотека от застройщика | 715 |
| ипотека от застройщика тюмень | 514 |
| ипотека без первоначального взноса тюмень от застройщика | 197 |
| ипотека от застройщика без взноса | 210 |
| бронь новостройка тюмень | MCP empty once |

The final P0 keeps the strongest local buyer intent while preserving the newbuild mechanism and the news-casus shape.

## Editorial angle

The article should present a completed Tyumen newbuild incident rather than a generic mortgage guide:

1. A family selects a newbuild apartment and receives a zero-down offer from the sales office.
2. The mortgage is initially approved under a developer-linked subsidy.
3. Six days before DDU, the bank announces that the program or subsidy window has ended.
4. The monthly payment increases by approximately 18,000 ₽, while the family cannot quickly find the required down payment.
5. The deal stops before escrow; part of the booking payment is withheld.
6. The dispute turns on what was promised in writing: the booking terms, validity period of the subsidy, responsibility for program cancellation and refund conditions.

The article may end with a concise practical landing block about documents to obtain **before booking**, but the main form remains a news casus with a conflict, deadline and final outcome—not a calm checklist.

## Fact boundaries

- The casus is composite and must not be presented as a verified claim about a named family.
- Do not invent surnames, ЖК names, bank names, developer names, court rulings or exact contract wording.
- Use approximate figures only where marked: monthly payment increase of about 18,000 ₽ and booking loss of about 50,000–80,000 ₽.
- Do not shift the plot to a secondary apartment, seller problems, EGRN, inheritance, guardianship, bankruptcy or matkapital in a secondary transaction.
- Keep the mechanism tied to newbuild sales office promises, developer promotion, DDU and escrow.
- Do not retitle the story as a family-mortgage “child turned seven / 19 days to October 1” case.

## Top-energy mirror

**clock_ran_out**

The emotional core is not merely that a mortgage became more expensive. The family believed the financing path was available, then lost the window immediately before the legally and financially decisive step—the DDU. The deadline creates the central dispute: sign under materially different terms, or stop and risk losing the booking payment.

## Anti-dupe record

- **B27, 09:00:** land lease versus ownership in declaration — `paper_clean_then_broke`
- **B28, 12:00:** KP gas 2026 versus declaration 2028 — `paper_clean_then_broke`
- **B29, 15:00:** developer zero-down mortgage program expired before DDU — `clock_ran_out`

B29 uses a different mechanism, top-energy mirror and H1 fingerprint. It does not recycle the declaration-mismatch skeleton of B27 or B28.
