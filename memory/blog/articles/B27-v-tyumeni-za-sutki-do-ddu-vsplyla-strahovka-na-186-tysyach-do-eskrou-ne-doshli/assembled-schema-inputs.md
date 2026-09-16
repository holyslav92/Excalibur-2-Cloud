# Schema inputs — B27

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли",
  "h1": "В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли",
  "slug": "v-tyumeni-za-sutki-do-ddu-vsplyla-strahovka-na-186-tysyach-do-eskrou-ne-doshli",
  "topic_id": "B27",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-16",
  "description": "В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B27",
  "h1": "В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли",
  "title": "В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли",
  "subject": "Страховой пакет на 186 тысяч рублей в допсоглашении к сделке с новостройкой перед подписанием ДДУ"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-za-sutki-do-ddu-vsplyla-strahovka-na-186-tysyach-do-eskrou-ne-doshli/`
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

- headline: В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч — до эскроу не дошли
- description: В Тюмени за сутки до ДДУ всплыла страховка на 186 тысяч
- datePublished: 2026-09-16
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
