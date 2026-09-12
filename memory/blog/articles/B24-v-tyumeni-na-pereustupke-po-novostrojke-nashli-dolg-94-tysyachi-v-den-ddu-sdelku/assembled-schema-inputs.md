# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени долг первого дольщика сорвал переуступку по ДДУ",
  "h1": "В Тюмени долг первого дольщика сорвал переуступку по ДДУ",
  "slug": "v-tyumeni-na-pereustupke-po-novostrojke-nashli-dolg-94-tysyachi-v-den-ddu-sdelku",
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
  "h1": "В Тюмени долг первого дольщика сорвал переуступку по ДДУ",
  "title": "В Тюмени долг первого дольщика сорвал переуступку по ДДУ",
  "subject": "Переуступка права по ДДУ в новостройке"
}
```

## description (article.meta — description-brief ещё нет)

В Тюмени долг первого дольщика сорвал переуступку по ДДУ

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-pereustupke-po-novostrojke-nashli-dolg-94-tysyachi-v-den-ddu-sdelku/`
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

- headline: В Тюмени долг первого дольщика сорвал переуступку по ДДУ
- description: В Тюмени долг первого дольщика сорвал переуступку по ДДУ
- datePublished: 2026-09-08
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
