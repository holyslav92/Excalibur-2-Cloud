# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json (derived from title-brief + research-context)

```json
{
  "title": "Неделю ждали переуступку в Тюмени — квартиру забронировал другой",
  "h1": "Неделю ждали переуступку в Тюмени — квартиру забронировал другой",
  "slug": "v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku-za-",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-12",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "Неделю ждали переуступку в Тюмени — квартиру забронировал другой",
  "title": "Неделю ждали переуступку в Тюмени — квартиру забронировал другой",
  "subject": "Переуступка квартиры в тюменской новостройке",
  "slug": "v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku-za-"
}
```

## description (no description-brief yet — use teaser from article)

Тюменская семья неделю готовила переуступку по зарегистрированному ДДУ, но не внесла бронь у застройщика — за сутки до визита лот забрал другой покупатель. Святослав Шакин объясняет, почему согласованная цена не удерживает квартиру.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-nedelyu-derzhali-pereustupku-drugoj-vnes-bron-na-tu-zhe-planirovku-za-/`
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

- headline: Неделю ждали переуступку в Тюмени — квартиру забронировал другой
- description: Тюменская семья неделю готовила переуступку по зарегистрированному ДДУ, но не внесла бронь у застройщика — за сутки до визита лот забрал другой покупатель. Святослав Шакин объясняет, почему согласованная цена не удерживает квартиру.
- datePublished: 2026-09-12
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы» (нет h2 FAQ, нет h3+p пар).

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
