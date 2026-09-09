# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток",
  "h1": "В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток",
  "slug": "v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-reg",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-09",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток",
  "title": "В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток",
  "subject": "приёмка квартиры в новостройке по ДДУ, акт без замечаний и ипотечный транш"
}
```

## description-brief.json

«Подпишите, потом исправим» — так семья получила ключи, но оставила дефекты за рамками акта. Через два дня приёмщик нашёл около десяти проблем, а банк поставил пакет на паузу.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-na-priemke-novostrojki-podpisali-akt-bez-zamechanij-bank-ostanovil-reg/`
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

- headline: В Тюмени банк остановил транш после приёмки без замечаний: 10 дефектов через 2 суток
- description: «Подпишите, потом исправим» — так семья получила ключи, но оставила дефекты за рамками акта. Через два дня приёмщик нашёл около десяти проблем, а банк поставил пакет на паузу.
- datePublished: 2026-09-09
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
