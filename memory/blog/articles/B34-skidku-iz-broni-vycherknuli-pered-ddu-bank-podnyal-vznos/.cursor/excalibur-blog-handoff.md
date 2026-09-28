# Scout handoff — B34

slot: weekend 12:00 YEKT
date: 2026-09-26
topic_id: B34
market: Тюмень
audience: семьи с детьми + инвесторы
format: Dzen news-casus
newbuild_only: PASS

title_draft: «В Тюмени за 3 дня до ДДУ скидку 380 тысяч из брони вычеркнули — банк поднял первый взнос»

slug: v-tyumeni-za-3-dnya-do-ddu-skidku-iz-broni-vyrknuli-bank-podnyal-pervyj-vznos

top_energy_mirror: number_claimed_vs_unpaid

newbuild_mechanism: «Семья или инвестор бронирует квартиру в строящемся ЖК Тюмени. Менеджер фиксирует цену со скидкой около 380 тысяч рублей, а банк одобряет ипотеку и первоначальный взнос под эту сумму. За 3 дня до подписания ДДУ в проекте договора скидки нет: цена возвращается к полной, банк пересчитывает LTV и требует больший первый взнос. Сделка останавливается до пересборки одобрения».

why_newbuild_not_secondary: «Сюжет строится только вокруг брони застройщика, проекта ДДУ, цены строящегося объекта, ипотечного одобрения и эскроу. Вторичный рынок не используется».

klyshin_hook: none | original: не используется (свежий Tyumen newbuild casus без Klyshin)

anti_repeat_preflight: live_blog_20 + ledger + used-clusters sync OK
same_day_avoid: B33 acceptance_act_area_shortfall; live планировка 54→49 м²

dzen_casus_shape: PASS
comment_magnet_angle: «Скидку в брони вы бы фиксировали письмом от юрлица застройщика или верили PDF в чате?»

wordstat_preflight: mcp-kv wordstat_get_user_info OK

wordstat_rework: probe «срок сдачи новостройки» — 6 (11176) → сохранён spine «купить новостройку в тюмени» + booking/price casus в H1

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить новостройку в тюмени» 892 | compare «новостройки тюмень» 4326 (11176) | «срок сдачи новостройки» 791 (225)

story_dup_check: PASS
cluster_id: newbuild_booking_discount_revoked_before_ddu_tyumen

h1_fingerprint_check: PASS
formula_spam_check: PASS
anti_dupe_hard: PASS
