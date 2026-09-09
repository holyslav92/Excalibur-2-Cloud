# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени пропал балкон на ключах — банк заморозил транш",
  "h1": "В Тюмени пропал балкон на ключах — банк заморозил транш",
  "slug": "v-tyumeni-izmenili-proektnuyu-deklaraciyu-v-novoj-planirovke-propal-balkon-iz-dd",
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
  "h1": "В Тюмени пропал балкон на ключах — банк заморозил транш",
  "title": "В Тюмени пропал балкон на ключах — банк заморозил транш",
  "subject": "Балкон в квартире новостройки по ДДУ"
}
```

## description (для BlogPosting.description)

На приёмке новостройки в Тюмени семья нашла глухую стену вместо балкона из ДДУ. Застройщик сослался на новую проектную декларацию, акт не подписали, банк заморозил последний ипотечный транш. Святослав Шакин разбирает, какие документы решают спор.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-izmenili-proektnuyu-deklaraciyu-v-novoj-planirovke-propal-balkon-iz-dd/`
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

- headline: В Тюмени пропал балкон на ключах — банк заморозил транш
- description: На приёмке новостройки в Тюмени семья нашла глухую стену вместо балкона из ДДУ. Застройщик сослался на новую проектную декларацию, акт не подписали, банк заморозил последний ипотечный транш. Святослав Шакин разбирает, какие документы решают спор.
- datePublished: 2026-09-09
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip. Comment magnet в конце — не FAQ.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
