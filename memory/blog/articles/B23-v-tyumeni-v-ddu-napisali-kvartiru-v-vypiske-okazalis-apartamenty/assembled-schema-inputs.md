# Schema inputs — B23

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты",
  "h1": "В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты",
  "slug": "v-tyumeni-v-ddu-napisali-kvartiru-v-vypiske-okazalis-apartamenty",
  "topic_id": "B23",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-05",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B23",
  "h1": "В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты",
  "title": "В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты",
  "subject": "новостройка в Тюмени и статус объекта в ЕГРН"
}
```

## description-brief.json

В тюменской новостройке семья ждала ключи, а банк остановил ипотеку: в ЕГРН объект оказался нежилым. Святослав Шакин разбирает, почему решающей стала строка в приложении к ДДУ.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-napisali-kvartiru-v-vypiske-okazalis-apartamenty/`
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

- headline: В Тюмени подписали ДДУ на квартиру — в ЕГРН нашли апартаменты
- description: В тюменской новостройке семья ждала ключи, а банк остановил ипотеку: в ЕГРН объект оказался нежилым. Святослав Шакин разбирает, почему решающей стала строка в приложении к ДДУ.
- datePublished: 2026-09-05
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
