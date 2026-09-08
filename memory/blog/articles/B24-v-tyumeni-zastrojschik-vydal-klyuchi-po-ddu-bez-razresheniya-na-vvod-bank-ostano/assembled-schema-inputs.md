# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку",
  "h1": "В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку",
  "slug": "v-tyumeni-zastrojschik-vydal-klyuchi-po-ddu-bez-razresheniya-na-vvod-bank-ostano",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-08",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку",
  "title": "В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку",
  "subject": "новостройка в Тюмени, ДДУ и остаток ипотечного кредита"
}
```

## description (description-brief ещё нет)

В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-vydal-klyuchi-po-ddu-bez-razresheniya-na-vvod-bank-ostano/`
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

- headline: В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку
- description: В Тюмени ключи по ДДУ получили за 2 дня — банк заморозил ипотеку
- datePublished: 2026-09-08
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
