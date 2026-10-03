# Schema inputs — B34

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В новостройке Тюмени БТИ добавило 4 м² — ключи отложили",
  "h1": "В новостройке Тюмени БТИ добавило 4 м² — ключи отложили",
  "slug": "v-tyumeni-v-novostrojke-na-priemke-bti-4-kv-m-doplata-380-tysyach-do-klyuchej",
  "topic_id": "B34",
  "author_id": "svyatoslav-shakin",
  "date": "2026-10-03",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B34",
  "h1": "В новостройке Тюмени БТИ добавило 4 м² — ключи отложили",
  "title": "В новостройке Тюмени БТИ добавило 4 м² — ключи отложили",
  "subject": "приёмка квартиры в тюменской новостройке: замер БТИ увеличил площадь по ДДУ на 4 м² перед выдачей ключей"
}
```

## description (Дзен teaser — из лида статьи)

Семья приехала за ключами от трёшки в тюменской новостройке — уехала без них: обмер БТИ добавил почти четыре метра, застройщик выставил 380 000 ₽ до ключей. Акт в тот день не подписали. Сверяете площадь до подписи или платите «чтобы закрыть сегодня»?

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-v-novostrojke-na-priemke-bti-4-kv-m-doplata-380-tysyach-do-klyuchej/`
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

- headline: В новостройке Тюмени БТИ добавило 4 м² — ключи отложили
- description: (см. блок description выше)
- datePublished: 2026-10-03
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
