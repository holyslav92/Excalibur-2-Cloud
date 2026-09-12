# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч",
  "h1": "В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч",
  "slug": "v-tyumeni-prosrochili-rassrochku-zastrojschika-ddu-rastorgli-uderzhali-vznos",
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
  "h1": "В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч",
  "title": "В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч",
  "subject": "ДДУ на новостройку с рассрочкой от застройщика",
  "slug": "v-tyumeni-prosrochili-rassrochku-zastrojschika-ddu-rastorgli-uderzhali-vznos"
}
```

## description (BlogPosting)

В Тюмени семья задержала платёж по рассрочке на пять дней — и получила расторжение ДДУ с удержанием 180 тысяч. Святослав Шакин разбирает, когда короткая просрочка не даёт застройщику права забрать квартиру и взнос.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-prosrochili-rassrochku-zastrojschika-ddu-rastorgli-uderzhali-vznos/`
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

- headline: В Тюмени ДДУ расторгли из-за пяти дней просрочки — удержали 180 тысяч
- description: В Тюмени семья задержала платёж по рассрочке на пять дней — и получила расторжение ДДУ с удержанием 180 тысяч. Святослав Шакин разбирает, когда короткая просрочка не даёт застройщику права забрать квартиру и взнос.
- datePublished: 2026-09-07
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
