# Schema inputs — B28

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (derived)

```json
{
  "title": "В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ",
  "h1": "В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ",
  "slug": "v-tyumeni-zastrojschik-potreboval-doplatu-za-uluchshennuyu-otdelku-pered-klyucha",
  "topic_id": "B28",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-06",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B28",
  "h1": "В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ",
  "title": "В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ",
  "subject": "доплата за улучшенную отделку в новостройке Тюмени, которой нет в ДДУ"
}
```

## description (synthesize for BlogPosting.description)

Семья приехала за ключами в тюменской новостройке — а застройщик выставил счёт на 300 тысяч за «улучшенную отделку», которой нет в ДДУ. Святослав Шакин разбирает, как отделить передачу квартиры от навязанной доплаты.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-potreboval-doplatu-za-uluchshennuyu-otdelku-pered-klyucha/`
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

- headline: В Тюмени застройщик запросил 300 тысяч перед ключами — их нет в ДДУ
- description: Семья приехала за ключами в тюменской новостройке — а застройщик выставил счёт на 300 тысяч за «улучшенную отделку», которой нет в ДДУ. Святослав Шакин разбирает, как отделить передачу квартиры от навязанной доплаты.
- datePublished: 2026-09-06
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
