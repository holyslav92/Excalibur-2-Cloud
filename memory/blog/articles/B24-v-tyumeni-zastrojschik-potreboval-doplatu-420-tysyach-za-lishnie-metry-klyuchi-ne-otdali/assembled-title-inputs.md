# Assembled title inputs — B24

**CRITICAL EXECUTION CONTEXT:** You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier gpt-6-astra).
**Your job is ONLY to generate `title-brief.json`** per `skills/title-excalibur-blog/SKILL.md`.
Output raw valid JSON ONLY, no markdown wrapping, no explanation.

## Topic & Context
- topic_id: B24
- Proposed H1: В Тюмени застройщик потребовал доплату 420 тысяч за лишние метры — ключи не отдали
- Proposed slug: v-tyumeni-zastrojschik-potreboval-doplatu-420-tysyach-za-lishnie-metry-klyuchi-ne-otdali
- City: Тюмень
- Hero: Святослав Шакин
- Format: Dzen news-casus
- Subject: Доплата за лишние метры в новостройке перед выдачей ключей
- Comment magnet: «А вы бы в такой ситуации сразу заказывали независимый обмер квартиры или взяли бы кредит на доплату, лишь бы быстрее получить ключи?»
- P0 Wordstat demand spine: новостройки тюмень

Output `title-brief.json` format:
```json
{
  "topic_id": "B24",
  "h1": "В Тюмени застройщик потребовал доплату 420 тысяч за лишние метры — ключи не отдали",
  "title": "В Тюмени застройщик потребовал доплату 420 тысяч за лишние метры — ключи не отдали",
  "subject": "Доплата за лишние метры в новостройке Тюмени и удержание ключей застройщиком",
  "angle": "Застройщик перед выдачей ключей насчитал 420 тысяч рублей за превышение площади, заблокировал передачу квартиры, но контрольный обмер выявил ошибку в расчёте лоджии и перегородок.",
  "comment_magnet_angle": "Застройщик требует 420 тысяч за лишние метры перед ключами — вы бы пошли на независимый обмер или взяли кредит, чтобы не срывать переезд?",
  "slug": "v-tyumeni-zastrojschik-potreboval-doplatu-420-tysyach-za-lishnie-metry-klyuchi-ne-otdali",
  "slug_confirmed": true,
  "verdict": "PASS"
}
```
