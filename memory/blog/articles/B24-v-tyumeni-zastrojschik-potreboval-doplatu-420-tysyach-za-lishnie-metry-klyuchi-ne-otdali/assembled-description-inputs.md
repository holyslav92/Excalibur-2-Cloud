# Assembled Description Inputs — B24

**CRITICAL EXECUTION CONTEXT:** You are running inside `excalibur_blog_derouter_opus_chat.py` (powerful tier gpt-6-astra).
**Your job is ONLY to produce `description-brief.json`** per `skills/description-excalibur-blog/SKILL.md`.
Output raw valid JSON ONLY, no markdown wrapping, no explanation.

## Context
- topic_id: B24
- H1: В Тюмени застройщик потребовал 420 тысяч за лишние метры — ключи не выдал
- Lead: В Тюмени семье с двумя детьми выставили счёт на 420 тысяч рублей за «лишние метры» в новостройке — застройщик заморозил передачу ключей и отказал в выдаче квартиры до оплаты...
- Rules: 1–2 предложения для карточки Дзена (~120–220 символов). Ритм Klyshin + news headline. Не копировать H1, не копировать лид.

Expected output schema:
```json
{
  "topic_id": "B24",
  "description": "...",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```
