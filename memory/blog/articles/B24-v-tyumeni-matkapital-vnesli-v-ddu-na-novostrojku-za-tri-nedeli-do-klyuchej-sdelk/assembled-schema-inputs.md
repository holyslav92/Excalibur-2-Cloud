# Schema inputs — B24

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей",
  "h1": "За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей",
  "slug": "v-tyumeni-matkapital-vnesli-v-ddu-na-novostrojku-za-tri-nedeli-do-klyuchej-sdelk",
  "topic_id": "B24",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-08",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B24",
  "h1": "За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей",
  "title": "За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей",
  "subject": "ДДУ с маткапиталом и обязательством выделить детям доли в новостройке"
}
```

## description (teaser)

За три недели до ключей банк остановил регистрацию: маткапитал на эскроу, а доли детей в ДДУ, заявлении СФР и банке описаны по-разному. Святослав Шакин — что сверить до акта приёма.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-matkapital-vnesli-v-ddu-na-novostrojku-za-tri-nedeli-do-klyuchej-sdelk/`
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

- headline: За 3 недели до ключей ДДУ с маткапиталом остановили из-за детских долей
- description: За три недели до ключей банк остановил регистрацию: маткапитал на эскроу, а доли детей в ДДУ, заявлении СФР и банке описаны по-разному. Святослав Шакин — что сверить до акта приёма.
- datePublished: 2026-09-08
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage.
