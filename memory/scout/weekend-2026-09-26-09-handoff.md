# Scout handoff — weekend slot 2026-09-26 09 YEKT

wordstat_preflight: mcp-kv wordstat_get_user_info OK
top_energy_mirror: paper_clean_then_broke
newbuild_mechanism: в акте приёмки квартиры площадь меньше, чем в ДДУ и ипотечном заключении — банк пересчитывает сумму кредита накануне регистрации
why_newbuild_not_secondary: сюжет только про приёмку квартиры от застройщика по ДДУ и эскроу, без вторички и без проверки ЕГРН продавца
klyshin_hook: none
anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK | closed_clusters: keys_delay_penalty_unpaid, acceptance_defects_penalty, ddu_apartment_vs_apartments_mismatch (distinct: area shortfall vs defects vs апартаменты)
dzen_casus_shape: PASS | event: семья пришла на ключи с одобренной ипотекой | risk: в акте −1,8 кв.м к ДДУ — банк режет лимит | time: за день до регистрации права | finale: остановили подписание акта и пересогласовали цену/допник до эскроу
comment_magnet_angle: Вы бы подписали акт с меньшей площадью, если банк уже одобрил кредит «под старую» цифру?
wordstat_rework: probe «неустойка застройщика тюмень» partial → «взыскать неустойку с застройщика» 659 → «приемка квартиры в новостройке» 5914 → final P0 «купить новостройку в тюмени» 1928
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 1928 | mechanism «приемка квартиры в новостройке» 5914 | compare225 «взыскать неустойку с застройщика» 659
story_dup_check: PASS | cluster_id: acceptance_act_area_shortfall_mortgage_tyumen
h1_fingerprint_check: PASS | fingerprint: area_shortfall_act_vs_ddu_mortgage_recalc
formula_spam_check: PASS | last3_mechanisms: escrow_wrong_entity, insurance_payment_hike, assignment_resale_ban (new: acceptance area vs DDU)
anti_dupe_hard: PASS

topic_id: B33
title_draft: В Тюмени в акте приёмки площадь оказалась меньше ДДУ — банк пересчитал ипотеку за день до регистрации
signal_urls:
- {{SITE_BASE}}/blog/
- https://dzen.ru/holyslav
