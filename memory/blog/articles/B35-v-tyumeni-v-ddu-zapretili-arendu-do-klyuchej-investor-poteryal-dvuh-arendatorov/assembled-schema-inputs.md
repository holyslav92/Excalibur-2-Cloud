# Schema inputs — B35

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов",
  "h1": "В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов",
  "slug": "v-tyumeni-v-ddu-zapretili-arendu-do-klyuchej-investor-poteryal-dvuh-arendatorov",
  "topic_id": "B35",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-11",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B35",
  "h1": "В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов",
  "title": "В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов",
  "subject": "новостройка в Тюмени, ДДУ с запретом сдавать квартиру до ключей и инвестор под аренду"
}
```

## description-brief.json

Двое жильцов уже ждали квартиру, но в приложении к ДДУ нашёлся запрет до регистрации права. В Тюмени Святослав Шакин разбирает, почему бронь и арендаторы ушли в соседний ЖК.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-ddu-zapretili-arendu-do-klyuchej-investor-poteryal-dvuh-arendatorov/`
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

- headline: В Тюмени за 7 дней до ДДУ запретили аренду — инвестор потерял 2 жильцов
- description: Двое жильцов уже ждали квартиру, но в приложении к ДДУ нашёлся запрет до регистрации права. В Тюмени Святослав Шакин разбирает, почему бронь и арендаторы ушли в соседний ЖК.
- datePublished: 2026-09-11
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
