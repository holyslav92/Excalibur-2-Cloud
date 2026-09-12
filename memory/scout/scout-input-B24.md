# Scout assembled input — B24 slot 2026-09-12 (17:00 YEKT candidate)

## Date / slot
- today: 2026-09-12
- weekday slot guidance: 6th slot today — MUST differ from today's clusters

## Today's CLOSED same-day clusters (DO NOT reuse)
- installment_penalty_developer — рассрочка/скидка застройщика
- mortgage_rate_hike / bank cut — банк урезал ипотеку
- family_mortgage_oct1 — семейная ипотека 1 октября
- house_defect_850k — брак дома 850к
- ddu_amount_vs_escrow_zero — эскроу ноль 4.2млн
- extra_area_420k — лишние метры 420к

## Anti-repeat preflight
- used-clusters sync: 25 active locks (2026-09-12)
- closed cluster_ids include: ddu_amount_vs_escrow_zero, booking_expired_price_hike, installment_penalty_developer, trade_in_rejected_developer, newbuild_ddu_cellar, developer_legal_entity_change, escrow_not_opened (B19), mortgage_rate_hike (B22), ddu_apartment_vs_apartments (B23 dir exists)

## Picked angle (Scout decision)
- cluster_id: assignment_lost_to_faster_buyer
- top_energy_mirror: someone_else_took_object
- newbuild_mechanism: переуступка прав по ДДУ — семья согласовала цену с цессионарием, ждала документы неделю; застройщик принял бронь от другого покупателя на ту же планировку/лот
- why_newbuild_not_secondary: сделка идёт через договор цессии к ДДУ застройщика, бронь в офисе продаж ЖК — не вторичный договор купли-продажи
- klyshin_hook: none (no fresh TG needed; avoid dupe risk)

## Title draft (news headline)
В Тюмени неделю держали переуступку — другой внёс бронь на ту же планировку за сутки

## topic_id / slug
- topic_id: B24
- slug: v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku

## Dzen casus shape
- event: семья договорилась о переуступке, отложила бронь «до готовности пакета документов»
- risk: застройщик не держит устную бронь — лот уходит тому, кто внёс деньги первым
- time: «неделю ждали» → «за сутки до их визита бронь сняли»
- finale: объект ушёл другому покупателю, аванс по цессии не вносили — потеряли планировку и цену, не деньги на эскроу
- comment_magnet_angle: «Переуступку можно „держать“ без брони у застройщика — или это самообман?»

## Wordstat live MCP-KV (regions 55+11176, compare 225)
- wordstat_preflight: wordstat_get_user_info OK
- probe «переуступка тюмень» → 8 (weak local)
- probe «переуступка новостройки» 55+11176 → 14 (weak)
- probe «переуступка новостройка» RU 225 → 2475 (national buyer spine)
- probe «новостройки тюмень» 55+11176 → 4560
- probe «купить новостройку в тюмени» 55+11176 → 909
- rework: weak переуступка Tyumen → anchor P0 на buyer-intent «купить новостройку в тюмени» + casus hook переуступка/бронь
- final P0: «купить новостройку в тюмени» 909

## Signal URLs (for Research)
- https://t.me/Tyumen_Rieltor
- site blog newbuild posts (interlink siblings B12, B19, B22)

Write full Scout handoff per SKILL.md format with all mandatory fields.
