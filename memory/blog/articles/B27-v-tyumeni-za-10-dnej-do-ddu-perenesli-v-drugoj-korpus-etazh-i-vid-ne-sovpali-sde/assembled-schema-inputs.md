# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась",
  "h1": "В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась",
  "slug": "v-tyumeni-za-10-dnej-do-ddu-perenesli-v-drugoj-korpus-etazh-i-vid-ne-sovpali-sde",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-17",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась",
  "title": "В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась",
  "subject": "Другой корпус новостройки вместо забронированного — предложение застройщика перед подписанием ДДУ."
}
```

## description-brief.json

Бронь стоила 200 тысяч, но выбранный лот внезапно исчез из сделки. В Тюмени семье предложили другой этаж, другой вид и возврат денег через 45 дней — вместо ДДУ.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-za-10-dnej-do-ddu-perenesli-v-drugoj-korpus-etazh-i-vid-ne-sovpali-sde/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени за 10 дней до ДДУ предложили другой корпус — семья отказалась
- description: Бронь стоила 200 тысяч, но выбранный лот внезапно исчез из сделки. В Тюмени семье предложили другой этаж, другой вид и возврат денег через 45 дней — вместо ДДУ.
- datePublished: 2026-09-17
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
