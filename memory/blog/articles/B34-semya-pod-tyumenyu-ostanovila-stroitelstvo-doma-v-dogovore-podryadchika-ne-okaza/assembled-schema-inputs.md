# Schema B34 — только JSON-LD

Выход: один валидный JSON без markdown. FAQPage не добавляй: в статье нет секции «Частые вопросы».

## Жёстко
- База сайта только плейсхолдер {{SITE_BASE}}. Не пиши живой хост и не пиши литерал [REDACTED].
- URL статьи: {{SITE_BASE}}/semya-pod-tyumenyu-ostanovila-stroitelstvo-doma-v-dogovore-podryadchika-ne-okaza/
- Запрещён путь /blog/ в URL.
- datePublished: 2026-10-04
- headline = H1 ниже, дословно.
- description: 1–2 предложения, не копия H1. Святослав Шакин, Тюмень, договор подряда на дом без счёта эскроу, семья не перевела деньги. Без слов «аванс», «ЕГРН», «ДКП».
- author Person: Святослав Шакин, @id {{SITE_BASE}}/#/schema/person/svyatoslav-shakin
- publisher Organization name: The Риэлтор, @id {{SITE_BASE}}/#organization
- @type BlogPosting
- inLanguage ru

## H1
Под Тюменью остановили договор на дом без эскроу: их уже 600

## Каркас
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "@id": "{{SITE_BASE}}/semya-pod-tyumenyu-ostanovila-stroitelstvo-doma-v-dogovore-podryadchika-ne-okaza/#article",
  "url": "{{SITE_BASE}}/semya-pod-tyumenyu-ostanovila-stroitelstvo-doma-v-dogovore-podryadchika-ne-okaza/",
  "headline": "Под Тюменью остановили договор на дом без эскроу: их уже 600",
  "description": "…",
  "datePublished": "2026-10-04",
  "inLanguage": "ru",
  "author": {
    "@type": "Person",
    "@id": "{{SITE_BASE}}/#/schema/person/svyatoslav-shakin",
    "name": "Святослав Шакин"
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{SITE_BASE}}/semya-pod-tyumenyu-ostanovila-stroitelstvo-doma-v-dogovore-podryadchika-ne-okaza/"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "{{SITE_BASE}}/#organization",
    "name": "The Риэлтор"
  }
}
