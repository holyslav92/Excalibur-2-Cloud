Сгенерируй ТОЛЬКО финальный Scout handoff-документ для Excalibur BLOG. Без мета-комментариев, без инструкций «как запустить Derouter», без таблиц gate status. Только поля handoff — plain text, по одному полю на строку.

## Данные (MCP-KV live, 2026-08-21)

topic_id: B06
priority: P0
article_dir: memory/blog/articles/B06-avtoocenka-minus-dva-milliona-k-rinku

title draft: Автооценка показала на два миллиона меньше рынка — и начался цирк с просмотрами

external_signal: Свежий пост @klyshin_A (август 2026): ЦИАН/Домклик/Сбер дают «рекомендованную цену» на 1–2 млн ниже живого спроса; собственник занижает объявление, получает очередь на показ и авансы, снимает объект и поднимает цену выше рынка. Для покупателя вторички в Тюмени это ловушка: «дешёвая» квартира по алгоритму ≠ реальная цена сделки.

signal_urls:
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- {{SITE_BASE}}/blog/
- https://t.me/holyslav92

wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, 2026-08-21)

klyshin_hook: cian_autoprice_minus_million | original: «автооценка ЦИАН/Домклик минус миллион к рынку» | angle: автооценка vs живой рынок Тюмени — покупатель не ориентируется на «рекомендованную цену» сервиса | signal: https://t.me/klyshin_A

wordstat_rework: probe «оценка квартиры тюмень» 73 → «купить квартиру в тюмени вторичка» 3943 → «вторичка в тюмени» 5799 → final P0 «купить квартиру в тюмени» 23066 | clusters tried: оценка квартиры тюмень, купить квартиру в тюмени вторичка, вторичка в тюмени, купить квартиру в тюмени; отклонены tired_buyer_bad_flat (нет своего кластера), five_court_schemes (overlap B03/B04, банкротство 30), phone_scammers_notary (мошенники 1), notary_not_shield_70k (anti-dup сайт)

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «купить квартиру в тюмени» 23066 | RU225 «купить квартиру в тюмени» 40585 | stickers «вторичка в тюмени» 5799 | «купить квартиру в тюмени вторичка» 3943

Факты в статье: Святослав Шакин / Тюмень. Не копипаст канала Клышина.

Выведи handoff ровно в этом формате — topic_id, priority, article_dir, title draft, external_signal, signal_urls (списком), wordstat_preflight, klyshin_hook, wordstat_rework, wordstat. Ничего лишнего.
