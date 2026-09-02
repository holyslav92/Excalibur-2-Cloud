# Schema inputs — B21

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли",
  "h1": "В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли",
  "slug": "v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok",
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
  "h1": "В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли",
  "title": "В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли",
  "subject": "Новостройка в Тюмени с рассрочкой по ДДУ"
}
```

## description (для BlogPosting.description)

В Тюмени семья год платила рассрочку по зарегистрированному ДДУ, а за месяц до ключей застройщик прислал допсоглашение с ростом остатка. Святослав Шакин разбирает, когда цену можно менять и что делать до подписи.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-platili-rassrochku-po-ddu-pered-sdachej-zastrojschik-podnyal-ostatok/`
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

- headline: В Тюмени 14 месяцев платили по ДДУ — перед сдачей остаток подняли
- description: В Тюмени семья год платила рассрочку по зарегистрированному ДДУ, а за месяц до ключей застройщик прислал допсоглашение с ростом остатка. Святослав Шакин разбирает, когда цену можно менять и что делать до подписи.
- datePublished: 2026-09-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip. Comment magnet в конце — не FAQ.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
