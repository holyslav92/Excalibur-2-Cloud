# Schema inputs — B21

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось",
  "h1": "В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось",
  "slug": "v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo",
  "topic_id": "B21",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-02",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B21",
  "h1": "В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось",
  "title": "В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось",
  "subject": "Оплаченная кладовка в новостройке Тюмени, указанная в ДДУ"
}
```

## description (из article.html лида)

Ключи от квартиры семья получила, кладовку из ДДУ — нет. Святослав Шакин разбирает, что делать, если акт на квартиру подписан, а оплаченное помещение не передали.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-oplatili-kladovku-po-ddu-na-klyuchah-pomescheniya-ne-bylo/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs: dzen.ru/holyslav, t.me/Tyumen_Rieltor, t.me/[REDACTED], vk.ru/tymenrieltor, wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени оплатили кладовку по ДДУ — на ключах её не оказалось
- description: Ключи от квартиры семья получила, кладовку из ДДУ — нет. Святослав Шакин разбирает, что делать, если акт на квартиру подписан, а оплаченное помещение не передали.
- datePublished: 2026-09-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
