# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание",
  "h1": "В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание",
  "slug": "v-tyumeni-na-eskrou-ne-hvatalo-400-tysyach-do-summy-ddu-bank-ostanovil-podpisani",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-06",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание",
  "title": "В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание",
  "subject": "Новостройка в Тюмени: на открытом эскроу оказалось на 400 тысяч рублей меньше суммы ДДУ, и банк остановил подписание."
}
```

## description (article.meta — description-brief ещё нет)

В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-eskrou-ne-hvatalo-400-tysyach-do-summy-ddu-bank-ostanovil-podpisani/`
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

- headline: В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание
- description: В Тюмени на эскроу не хватило 400 тысяч до ДДУ — банк остановил подписание
- datePublished: 2026-09-06
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
