# Description inputs — B27

Write the Dzen card teaser. Return a single JSON object (no markdown, no explanation).

topic_id: B27

H1 (do NOT copy): В Тюмени ипотека сгорела на 87-й день: ДДУ не дождались

Angle: Семья получила одобрение ипотеки, но почти трёхмесячная очередь на подписание ДДУ съела срок решения банка. Переодобрение оказалось хуже, покупатели отказались от сделки.

Opening para (do NOT truncate or copy): На 87-й день ожидания ДДУ семья в Тюмени получила проект договора, но купить квартиру по прежнему расчёту уже не могла: старое одобрение ипотеки банк закрыл. Квартира стояла в брони…

Case beats:
- «Ипотеку одобрили — ждём договор» — ложное спокойствие
- Трижды «на следующей неделе» — прошло почти три месяца
- На 87-й день пришёл проект ДДУ, банк уже закрыл одобрение
- Переодобрение: меньше сумма, выше ставка — бронь сняли до аванса
- Тюмень, новостройка, Святослав Шакин

Rules: 1–2 sentences, 120–220 chars (max 250). Klyshin case hook. ≠ H1. ≠ lead. Cyrillic. No checklist blurb.

Output JSON:
{
  "topic_id": "B27",
  "description": "<your teaser here>",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
