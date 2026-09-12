# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й",
  "h1": "В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й",
  "slug": "v-tyumeni-v-ddu-byl-12-j-etazh-na-klyuchah-otdali-kvartiru-na-2-m",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-07",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й",
  "title": "В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й",
  "subject": "Новостройка в Тюмени с этажом, указанным в ДДУ"
}
```

## description (для BlogPosting.description)

Семья из Тюмени приехала за ключами к квартире на 12-м этаже по ДДУ, а застройщик открыл дверь на втором. Святослав Шакин объясняет, почему акт они не подписали и что проверять до подписи.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-byl-12-j-etazh-na-klyuchah-otdali-kvartiru-na-2-m/`
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

- headline: В Тюмени по ДДУ был 12-й этаж — на ключах дали 2-й
- description: Семья из Тюмени приехала за ключами к квартире на 12-м этаже по ДДУ, а застройщик открыл дверь на втором. Святослав Шакин объясняет, почему акт они не подписали и что проверять до подписи.
- datePublished: 2026-09-07
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
