# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки",
  "h1": "В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки",
  "slug": "v-tyumeni-kupili-dom-v-poselke-granicy-uchastka-v-vypiske-ne-sovpali-s-ddu",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-10",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки",
  "title": "В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки",
  "subject": "Дом в коттеджном посёлке Тюмени по ДДУ и участок при нём"
}
```

## description (из лида статьи)

Семья в Тюмени подписала ДДУ на дом с 12 сотками, а перед приёмкой в выписке ЕГРН увидела 10,5 — не хватило 1,5 сотки. Святослав Шакин разбирает, можно ли принимать дом, если граница участка в реестре не совпадает с приложением к договору.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-kupili-dom-v-poselke-granicy-uchastka-v-vypiske-ne-sovpali-s-ddu/`
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

- headline: В Тюмени подписали ДДУ на дом — в выписке не хватило 1,5 сотки
- description: Семья в Тюмени подписала ДДУ на дом с 12 сотками, а перед приёмкой в выписке ЕГРН увидела 10,5 — не хватило 1,5 сотки. Святослав Шакин разбирает, можно ли принимать дом, если граница участка в реестре не совпадает с приложением к договору.
- datePublished: 2026-09-10
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
