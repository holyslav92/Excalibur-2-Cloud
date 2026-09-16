# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (draft — parallel with Writer)

```json
{
  "title": "В Тюмени забронировали машино-место — его номера не было в декларации",
  "h1": "В Тюмени забронировали машино-место — его номера не было в декларации",
  "slug": "v-tyumeni-za-3-dnya-do-ddu-sverili-mashinomesto-v-deklaracii-ne-okazalos-nomera",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-16",
  "description": "За три дня до ДДУ сверили номер машино-места с проектной декларацией — в разделе 15.3 корпуса его не оказалось",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени забронировали машино-место — его номера не было в декларации",
  "title": "В Тюмени забронировали машино-место — его номера не было в декларации",
  "subject": "Машино-место в тюменской новостройке: номер из брони не подтвердился в проектной декларации",
  "slug": "v-tyumeni-za-3-dnya-do-ddu-sverili-mashinomesto-v-deklaracii-ne-okazalos-nomera"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-za-3-dnya-do-ddu-sverili-mashinomesto-v-deklaracii-ne-okazalos-nomera/`
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

- headline: В Тюмени забронировали машино-место — его номера не было в декларации
- description: За три дня до ДДУ сверили номер машино-места с проектной декларацией — в разделе 15.3 корпуса его не оказалось
- datePublished: 2026-09-16
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. article.html ещё нет; theme_blocks.faq = skip; в research нет FAQ-секции.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
