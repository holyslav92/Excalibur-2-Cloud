# Schema inputs — B14

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было",
  "h1": "В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было",
  "slug": "v-tyumeni-obeschali-kladovku-v-podarok-v-vypiske-egrn-ee-ne-okazalos",
  "topic_id": "B14",
  "author_id": "svyatoslav-shakin",
  "date": "2026-08-29",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B14",
  "h1": "В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было",
  "title": "В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было",
  "angle": "Показать, как обещанная кладовка повлияла на выбор квартиры, но не подтвердилась отдельным правом в ЕГРН и остановила сделку до аванса."
}
```

## description-brief.json

Отсутствует. Использовать description из article.meta.json:
«В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было».

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-obeschali-kladovku-v-podarok-v-vypiske-egrn-ee-ne-okazalos/`
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

- headline: В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было
- description: В Тюмени кладовка «в подарок» остановила сделку — в ЕГРН её не было
- datePublished: 2026-08-29
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
