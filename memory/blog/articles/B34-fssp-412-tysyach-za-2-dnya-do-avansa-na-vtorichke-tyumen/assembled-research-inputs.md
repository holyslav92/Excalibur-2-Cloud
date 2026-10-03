# Research inputs — B34 (assembled by Cursor conductor, 2026-10-03)

## date_context
- today_iso: 2026-10-03
- timezone: Europe/Moscow

## topic
- topic_id: B34
- title: ФССП 412 тысяч за 2 дня до аванса на вторичке Тюмень
- slug: fssp-412-tysyach-za-2-dnya-do-avansa-na-vtorichke-tyumen
- slot_rubric: vtorichka (Scout handoff note: owner lock rejected for 17:00 novostroyki slot — research still runs for article dir)
- cluster_id: secondary_fssp_enforcement_before_advance_tyumen
- viral_mechanism: почти сорванная сделка перед авансом; выписка ЕГРН «чистая», расширенная проверка ФССП выявила взыскание
- comment_magnet_angle: «Если ФССП показывает 412 тысяч за два дня до аванса, а продавец говорит “это не моё” — вы бы шли дальше или ждали бы снятия?»

## modeled casus (Writer boundary — not press report)
- Вторичка, Тюмень, семья-покупатель, ипотека предварительно одобрена.
- Плановый аванс ~350–420 тыс. ₽ (в заголовке stakes **412 000 ₽** как сумма взыскания в БДИП).
- За **2 дня** до аванса риэлтор/покупатель проверяет продавца в «Банке данных исполнительных производств» (ФИО + дата рождения + регион Тюменская область / несколько подразделений).
- Выписка ЕГРН по объекту без обременений; продавец устно отрицает долг («ошибка», «не моё», «закрою завтра»).
- В БДИП — открытое ИП, сумма требований **412 000 ₽** (механика: кредит/штраф/алименты — не фиксировать конкретный тип без источника).
- Сделку **останавливают до аванса**; аванс не переводят.
- Без фамилий, адреса ЖК, номера ИП, банка.

## scout handoff excerpt
- signal_urls from SERP: https://dzen.ru/a/arzxl4wtABJAoLzA (соседний casus ~400k, 4 дня), https://dzen.ru/a/apKOyl_t_ztB8tNf (приставы/регистрация Тюмень), https://vk.ru/r72_fssp
- Wordstat P0: «купить квартиру в тюмени вторичка» — **3375** (regions 55, 11176) live 2026-10-03

## overlap (published-titles-only)
- B33: долг ЖКУ 186k за 3 дня до аванса — другой кластер (utility), не дублировать механику.
- Нет опубликованного заголовка про ФССП 412k перед авансом.

## fresh_signal_this_week (required)
1. **2026-09-28** vsluh.ru — пресс-служба УФССП по Тюменской области: проверять задолженность до выезда; порог ограничения выезда **>10 000 ₽**; сервисы: r72.fssp.gov.ru, БДИП, Госуслуги; тел. 8 (3452) 49-53-31.
   URL: https://vsluh.ru/novosti/dengi/tyumenskie-pristavy-prizyvayut-otpusknikov-proveryat-dolgi-pered-vyezdom-za-granitsu_430535/
2. **2026-08-12** 72.ru — цитата УФССП Тюмени: запрет регистрационных действий с недвижимостью; за 1 полугодие 2026 — **17** жилых помещений и **2** ЗУ с домом переданы на принудительную реализацию.
   URL: https://72.ru/text/house/2026/08/12/76584267/

## wordstat (accessed 2026-10-03)
| phrase | region | total |
| купить квартиру в тюмени вторичка | 55,11176 | 3375 |
| банк данных исполнительных производств | 225 | 56440 |
| запрет регистрационных действий на квартиру | 225 | 1955 (top line) |
| проверка фссп перед покупкой квартиры | 225 | WORDSTAT PARTIAL totalCount=2 only |

## official / law facts (for official_verifications — NOT bank tariffs)
### 229-ФЗ «Об исполнительном производстве»
- **ст. 6.1** — ФССП ведёт БДИП; общедоступная часть на fssp.gov.ru/iss/ip/; сервис только на официальном сайте и r**.fssp.gov.ru/iss/ip/ (текст на странице ФССП, accessed 2026-10-03).
- **ст. 64 п. 7** — исполнительное действие: арест имущества (в т.ч. для обеспечения взыскания).
- **ст. 80 ч. 1** — пристав вправе наложить арест на имущество должника, в т.ч. в срок добровольного исполнения; арест включает запрет распоряжения.
- **Форма постановления** — Приложение № 62 к приказу ФССП: запрет регистрационных действий в отношении объектов недвижимого имущества; основание — **ст. 64** 229-ФЗ (КонсультантПлюс LAW_349351).
- БДИП: после оплаты запись обновляется **3–7 дней** (официальная памятка fssp.gov.ru/iss/ip/).
- Риск **ошибочной идентификации** однофамильца — официальная памятка ФССП (паспорт, СНИЛС, ИНН).

### 218-ФЗ «О гос. регистрации недвижимости»
- **ст. 26 п. 37** — приостановление регистрации, если в орган поступил акт о **аресте** или **запрете** совершать действия с недвижимостью (до снятия).
- **ст. 27** — отказ, если за срок приостановления препятствия не сняты.

### Практика покупателя (обзоры — не единственный источник law)
- Выписка ЕГРН может не показывать **будущий** запрет, если ИП открыто после выписки или запрет ещё не внесён в ЕГРН — проверка продавца в БДИП отдельно от «чистой» выписки по объекту.
- Банк при ипотеке часто проверяет продавца по приставам, но в интересах залога, не заменяет проверку до аванса (обзоры: gradbase.ru, cherehapa.ru — контекст).

## constraints for Writer
- Не утверждать точные сроки снятия запрета в ЕГРН после оплаты без оговорки «зависит от пристава и Росреестра».
- **412 000 ₽** — сумма casus/БДИП в сюжете, не тариф банка/госоргана.
- Не писать h2_outline, lead, FAQ.
- official_verifications: law + fssp.gov.ru; **no bank commission claims**.
- official_source_audit.status: PASS (no bank tariff digits).

## writer_safe_urls (CTA)
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- tel:+79220016505
- https://fssp.gov.ru/iss/ip/
- https://dzen.ru/holyslav

## INSTRUCTION TO DEROUTER
You ARE the Derouter utility tier run invoked by excalibur_blog_derouter_opus_chat.py. Live fetch/MCP/Wordstat was ALREADY completed by the Cursor conductor on 2026-10-03; all facts below are verified inputs.

Your ONLY task: transform this assembled input into complete research-notes.md (markdown sections listed below). Do NOT refuse, do NOT output DEROUTER RESEARCH BLOCKER, do NOT ask for more web research.

Produce full research-notes.md with sections:
research_date, topic_id, cluster_id, reader_problem, reader_outcome, casus_boundary, practical_facts (bullets), constraints, voice_angle, surprising_fact, official_verifications (table), source_table (columns: id | title | url | type | accessed_at), writer_safe_urls.
All accessed_at = 2026-10-03.
Do NOT include h2_outline, action_outline, lead paragraph, FAQ.
Write in Russian for prose sections; tables as specified in skill.
