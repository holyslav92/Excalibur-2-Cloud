# Schema inputs — B20

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу",
  "h1": "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу",
  "slug": "v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot",
  "topic_id": "B20",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-01",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B20",
  "h1": "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу",
  "title": "В Тюмени застройщик сменил юрлицо — банк не открыл эскроу",
  "subject": "Новостройка в Тюмени: после смены юрлица застройщика семье прислали новый ДДУ, а банк остановил открытие эскроу."
}
```

## description-brief.json

```json
{
  "topic_id": "B20",
  "description": "В Тюмени у одной квартиры внезапно сменился продавец на бумаге. Святослав Шакин разбирает, почему банк поставил эскроу на паузу, а семья лишилась брони, сохранив деньги."
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-smenil-yurlico-dolschikam-prislali-novyj-ddu-eskrou-ne-ot/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/holyslav92, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени застройщик сменил юрлицо — банк не открыл эскроу
- description: В Тюмени у одной квартиры внезапно сменился продавец на бумаге. Святослав Шакин разбирает, почему банк поставил эскроу на паузу, а семья лишилась брони, сохранив деньги.
- datePublished: 2026-09-01
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
