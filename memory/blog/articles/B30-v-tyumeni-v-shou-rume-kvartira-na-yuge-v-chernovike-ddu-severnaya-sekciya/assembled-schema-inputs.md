# Schema inputs — B30

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция",
  "h1": "В шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция",
  "slug": "v-tyumeni-v-shou-rume-kvartira-na-yuge-v-chernovike-ddu-severnaya-sekciya",
  "topic_id": "B30",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-19",
  "description": "«Просто другой подъезд» — так семье в Тюмени объяснили окна на соседний корпус вместо двора. ДДУ они не подписали, но часть денег за бронь всё равно потеряли.",
  "theme_blocks": { "faq": "skip" }
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-shou-rume-kvartira-na-yuge-v-chernovike-ddu-severnaya-sekciya/`
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

- headline: В шоу-руме квартира на юге — в черновике ДДУ та же площадь, но северная секция
- description: «Просто другой подъезд» — так семье в Тюмени объяснили окна на соседний корпус вместо двора. ДДУ они не подписали, но часть денег за бронь всё равно потеряли.
- datePublished: 2026-09-19
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
