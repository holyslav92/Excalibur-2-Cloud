# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (synthesized from title-brief + research-context)

```json
{
  "title": "В Тюмени в ДДУ зафиксировали трёшку — перед эскроу предложили двушку, сделку остановили",
  "h1": "В Тюмени в ДДУ зафиксировали трёшку — перед эскроу предложили двушку, сделку остановили",
  "slug": "v-tyumeni-v-ddu-zafiksirovali-treshku-pered-eskrou-zastrojschik-predlozhil-dvush",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-14",
  "description": "В ДДУ зафиксировали трёшку, а перед эскроу предложили двушку за те же деньги — семья остановила сделку до перевода средств",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени в ДДУ зафиксировали трёшку — перед эскроу предложили двушку, сделку остановили",
  "title": "В Тюмени в ДДУ зафиксировали трёшку — перед эскроу предложили двушку, сделку остановили",
  "subject": "Новостройка в Тюмени: зарегистрированный ДДУ с трёхкомнатной квартирой и предложение двухкомнатной перед эскроу",
  "slug": "v-tyumeni-v-ddu-zafiksirovali-treshku-pered-eskrou-zastrojschik-predlozhil-dvush"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-zafiksirovali-treshku-pered-eskrou-zastrojschik-predlozhil-dvush/`
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

- headline: В Тюмени в ДДУ зафиксировали трёшку — перед эскроу предложили двушку, сделку остановили
- description: В ДДУ зафиксировали трёшку, а перед эскроу предложили двушку за те же деньги — семья остановила сделку до перевода средств
- datePublished: 2026-09-14
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
