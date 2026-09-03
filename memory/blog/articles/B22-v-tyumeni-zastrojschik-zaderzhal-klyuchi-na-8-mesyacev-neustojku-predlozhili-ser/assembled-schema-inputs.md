# Schema inputs — B22

ROLE: schema. Выход: только валидный JSON-LD без markdown fences.

## article.meta.json

```json
{
  "title": "В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом",
  "h1": "В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом",
  "slug": "v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser",
  "topic_id": "B22",
  "author_id": "svyatoslav-shakin",
  "date": "2026-09-03",
  "theme_blocks": { "faq": "skip" }
}
```

## title-brief.json

```json
{
  "topic_id": "B22",
  "h1": "В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом",
  "title": "В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом",
  "subject": "Задержка ключей в новостройке и сертификат вместо денежной неустойки по ДДУ",
  "angle": "Заголовок показывает главный конфликт в день выдачи ключей: после восьми месяцев просрочки застройщик предлагает ограниченный сертификат вместо денежной выплаты."
}
```

## description (BlogPosting)

В Тюмени семья восемь месяцев платила ипотеку и аренду, а в день ключей получила сертификат вместо неустойки. Святослав Шакин разбирает, какие бумаги в этот день закрывают деньги за просрочку по ДДУ.

## Site base

- Использовать `{{SITE_BASE}}` (НЕ [REDACTED], НЕ живой host)
- Canonical URL: `{{SITE_BASE}}/v-tyumeni-zastrojschik-zaderzhal-klyuchi-na-8-mesyacev-neustojku-predlozhili-ser/`
- Запрещено `/blog/` в URL

## Author (shared/authors-registry.json)

- id: svyatoslav-shakin
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- worksFor: The Риэлтор
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin
- sameAs (без [REDACTED]): https://dzen.ru/holyslav, https://t.me/Tyumen_Rieltor, https://vk.ru/tymenrieltor, https://wa.me/79220016505

## Organization

- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization
- url: {{SITE_BASE}}/
- logo: {{SITE_BASE}}/wp-content/uploads/logo.png

## BlogPosting

- headline: В Тюмени ключи задержали на 8 месяцев — неустойку дали сертификатом
- description: В Тюмени семья восемь месяцев платила ипотеку и аренду, а в день ключей получила сертификат вместо неустойки. Святослав Шакин разбирает, какие бумаги в этот день закрывают деньги за просрочку по ДДУ.
- datePublished: 2026-09-03
- inLanguage: ru-RU
- author: @id svyatoslav-shakin
- publisher: @id organization

## FAQPage

НЕ создавать. В article.html нет секции «Частые вопросы», theme_blocks.faq = skip.

## Формат

@context + @graph с Organization, Person, BlogPosting. Без FAQPage. Без литерала [REDACTED].
