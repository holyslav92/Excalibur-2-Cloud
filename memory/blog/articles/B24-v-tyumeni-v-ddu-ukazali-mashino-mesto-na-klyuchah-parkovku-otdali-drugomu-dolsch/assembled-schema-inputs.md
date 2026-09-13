# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени машино-место по ДДУ отдали другому дольщику",
  "h1": "В Тюмени машино-место по ДДУ отдали другому дольщику",
  "slug": "v-tyumeni-v-ddu-ukazali-mashino-mesto-na-klyuchah-parkovku-otdali-drugomu-dolsch",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-13",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "На P-42 в Тюмени парковку по ДДУ отдали другому — через 3 дня чужая машина",
  "title": "На P-42 в Тюмени парковку по ДДУ отдали другому — через 3 дня чужая машина",
  "subject": "Машино-место в новостройке, указанное в приложении к ДДУ"
}
```

## description-brief.json

Место у лифта оплатили, а пользоваться им почему-то должен другой дольщик — такая история в новостройке Тюмени. Застройщик ссылается на «опечатку», но семья не согласна на замену: что теперь решает ДДУ?

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-ukazali-mashino-mesto-na-klyuchah-parkovku-otdali-drugomu-dolsch/`
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

- headline: На P-42 в Тюмени парковку по ДДУ отдали другому — через 3 дня чужая машина
- description: Место у лифта оплатили, а пользоваться им почему-то должен другой дольщик — такая история в новостройке Тюмени. Застройщик ссылается на «опечатку», но семья не согласна на замену: что теперь решает ДДУ?
- datePublished: 2026-09-13
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
