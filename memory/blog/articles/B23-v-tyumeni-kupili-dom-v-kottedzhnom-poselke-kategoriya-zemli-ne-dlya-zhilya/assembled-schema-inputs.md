# Schema inputs — B23

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени категория земли сорвала выдачу ипотеки на дом в посёлке",
  "h1": "В Тюмени категория земли сорвала выдачу ипотеки на дом в посёлке",
  "slug": "v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya",
  "topic_id": "B23",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-04",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B23",
  "h1": "В Тюмени категория земли сорвала выдачу ипотеки на дом в посёлке",
  "title": "В Тюмени категория земли сорвала выдачу ипотеки на дом в посёлке",
  "subject": "Дом от застройщика в коттеджном посёлке Тюмени: статус земли в ЕГРН не совпал с обещанным ИЖС"
}
```

## description (description-brief.json)

Дом уже построен, ипотека одобрена, деньги лежат на эскроу. Но одна строка в ЕГРН заставила семью в Тюмени не подписывать акт — застройщик обещал исправить категорию когда-нибудь.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-kupili-dom-v-kottedzhnom-poselke-kategoriya-zemli-ne-dlya-zhilya/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени категория земли сорвала выдачу ипотеки на дом в посёлке
- description: Дом уже построен, ипотека одобрена, деньги лежат на эскроу. Но одна строка в ЕГРН заставила семью в Тюмени не подписывать акт — застройщик обещал исправить категорию когда-нибудь.
- datePublished: 2026-09-04
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
