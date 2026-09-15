# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (синтез из title-brief + research-context)

```json
{
  "title": "В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ",
  "h1": "В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ",
  "slug": "v-tyumeni-bank-snyal-zhk-s-akkreditacii-ipoteka-zamerla-za-sutki-do-ddu",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-15",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ",
  "title": "В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ",
  "subject": "Новостройка в Тюмени и ипотека, замершая после снятия ЖК с аккредитации",
  "slug": "v-tyumeni-bank-snyal-zhk-s-akkreditacii-ipoteka-zamerla-za-sutki-do-ddu"
}
```

## description (description-brief ещё нет)

В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ — ипотека замерла, семья не дошла до эскроу.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-bank-snyal-zhk-s-akkreditacii-ipoteka-zamerla-za-sutki-do-ddu/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505, {{SITE_BASE}}/, {{SITE_BASE}}/rieltor-tyumen/, {{SITE_BASE}}/kontakty/

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ
- description: В Тюмени банк снял ЖК с аккредитации за сутки до ДДУ — ипотека замерла, семья не дошла до эскроу.
- datePublished: 2026-09-15
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h2 FAQ и пар h3+p).

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
