# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени семья сверила бронь с ДДУ — и отказалась от другой квартиры",
  "h1": "В Тюмени семья сверила бронь с ДДУ — и отказалась от другой квартиры",
  "slug": "v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "description": "В брони — вид на набережную, в приложении к ДДУ — другая секция и этаж. Семья остановила сделку до эскроу.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени семья сверила бронь с ДДУ — и отказалась от другой квартиры",
  "title": "В Тюмени семья сверила бронь с ДДУ — и отказалась от другой квартиры",
  "subject": "Бронь квартиры в тюменской новостройке и проект ДДУ на другой объект",
  "slug": "v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-broni-etazh-s-vidom-v-ddu-drugaya-sektsiya-sdelku-ostanovili/`
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

- headline: В Тюмени семья сверила бронь с ДДУ — и отказалась от другой квартиры
- description: В брони — вид на набережную, в приложении к ДДУ — другая секция и этаж. Семья остановила сделку до эскроу.
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
