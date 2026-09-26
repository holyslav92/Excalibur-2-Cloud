# Scout inputs — weekend slot 12:00 YEKT 2026-09-26

## Director constraints
- DIFFERENT mechanism from morning 09:00 slot (PR #210 / B33): `acceptance_act_area_shortfall_mortgage_tyumen` — акт приёмки меньше ДДУ, пересчёт ипотеки.
- ALSO avoid live today: `v-tyumeni-za-5-dnej-do-ddu-v-novostrojke-pomenyali-planirovku-v-broni-54-kvadrat` (площадь/планировка в брони vs ДДУ).
- topic_id: B34
- newbuild only Tyumen; families + investors; news-casus; Wordstat live MCP-KV.

## Live WP recent (from excalibur_blog_today.py 2026-09-26)
- B33 cluster morning: площадь в акте приёмки меньше ДДУ — банк пересчитал ипотеку
- Same day: за 5 дней до ДДУ планировка 54→49 м² в брони

## Proposed lock (director pre-check PASS)
- cluster_id: `newbuild_booking_discount_revoked_before_ddu_tyumen`
- H1 direction: В Тюмени за 3 дня до ДДУ скидку 380 тысяч из брони вычеркнули — банк поднял первый взнос
- top_energy_mirror: number_claimed_vs_unpaid (в брони/PDF была скидка, в ДДУ цена полная)
- newbuild_mechanism: семья/инвестор бронирует квартиру в ЖК Тюмени; менеджер фиксирует цену со скидкой ~380 тыс ₽; банк одобряет ипотеку под эту сумму и взнос; за 3 дня до ДДУ в проекте договора скидки нет — банк пересчитывает ЛTV и требует больший первый взнос; сделку останавливают до пересборки одобрения
- why_newbuild_not_secondary: только бронь застройщика + ДДУ + эскроу на строящийся объект
- comment_magnet: «Скидку в брони вы бы фиксировали письмом от юрлица застройщика или верили PDF в чате?»
- scout_helper --check-story: ANTI-DUPE HARD PASS (booking_expired fingerprint, new cluster)
- topic_focus: PASS

## Wordstat MCP-KV (live 2026-09-26)
- wordstat_get_user_info: OK
- P0 spine «купить новостройку в тюмени» — 892 (region 11176)
- compare «новостройки тюмень» — 4326 (11176)
- mechanism probe «срок сдачи новостройки» — 6 (11176); rework kept P0 spine + booking/price casus jargon in H1
- regions: 55 (fail empty once), 11176 primary, RU 225 compare on «срок сдачи новостройки» 791

Write full handoff to `.cursor/excalibur-blog-handoff.md` per skill format with all required fields dzen_casus_shape PASS, anti_dupe_hard PASS.
