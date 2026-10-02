# Schema inputs — B34

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени 35 ₽ в презентации ЖК, 89 ₽ в ДДУ — банк урезал ипотеку",
  "h1": "В Тюмени 35 ₽ в презентации ЖК, 89 ₽ в ДДУ — банк урезал ипотеку",
  "slug": "v-tyumeni-v-prezentacii-zhk-vznos-35-v-ddu-89-ipoteku-urezali",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "date": "2026-10-02",
  "description": "Семья внесла 150 тысяч за бронь, в презентации было 35 ₽ за квадрат — в приложении к ДДУ оказалось 89 ₽, и банк урезал ипотеку примерно на 620 тысяч.",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B34",
  "h1": "В Тюмени 35 ₽ в презентации ЖК, 89 ₽ в ДДУ — банк урезал ипотеку",
  "title": "В Тюмени 35 ₽ в презентации ЖК, 89 ₽ в ДДУ — банк урезал ипотеку",
  "subject": "Плата за содержание в презентации новостройки и приложении к ДДУ"
}
```

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-prezentacii-zhk-vznos-35-v-ddu-89-ipoteku-urezali/`
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

- headline: В Тюмени 35 ₽ в презентации ЖК, 89 ₽ в ДДУ — банк урезал ипотеку
- description: Семья внесла 150 тысяч за бронь, в презентации было 35 ₽ за квадрат — в приложении к ДДУ оказалось 89 ₽, и банк урезал ипотеку примерно на 620 тысяч.
- datePublished: 2026-10-02
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» с парами h3+p, theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
