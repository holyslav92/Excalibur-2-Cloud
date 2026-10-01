CRITICAL: Your entire reply must be ONLY valid JSON (schema.org BlogPosting graph). No markdown fences, no Russian prose, no "checking repository".

## BlogPosting fields
- headline: За 4 дня до эскроу новостройка в Тюмени ушла в «сдам» — семейную ипотеку сняли
- description: Семья нашла объявление «сдам» по их лоту за четыре дня до эскроу — банк снял предодобрение семейной ипотеки, эскроу не открыли.
- datePublished: 2026-10-01
- inLanguage: ru-RU
- slug path (canonical, NO /blog/): za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke
- url and @id must include exactly: {{SITE_BASE}}/za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke/
- Use {{SITE_BASE}} placeholder everywhere for site URLs (never https:// literal, never [REDACTED])
- No FAQPage (article has no FAQ h3 section)

## Author (Person)
- name: Святослав Шакин
- jobTitle: Личный риэлтор в Тюмени
- @id: {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin

## Publisher (Organization)
- name: The Риэлтор
- @id: {{SITE_BASE}}/#organization

## Shape (prefer @graph like B33)
Example structure to follow:
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "{{SITE_BASE}}/#organization", "name": "The Риэлтор", "url": "{{SITE_BASE}}/" },
    { "@type": "Person", "@id": "{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin", "name": "Святослав Шакин", "jobTitle": "Личный риэлтор в Тюмени", "worksFor": { "@id": "{{SITE_BASE}}/#organization" } },
    { "@type": "BlogPosting", "@id": "{{SITE_BASE}}/za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke/#blogposting", "url": "{{SITE_BASE}}/za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke/", "headline": "...", "description": "...", "datePublished": "2026-10-01", "inLanguage": "ru-RU", "author": { "@id": "{{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin" }, "publisher": { "@id": "{{SITE_BASE}}/#organization" }, "mainEntityOfPage": { "@type": "WebPage", "@id": "{{SITE_BASE}}/za-4-dnya-do-eskrou-v-tyumeni-nashli-obyavlenie-na-sdachu-kvartiry-v-novostrojke/" } }
  ]
}

Output ONLY the JSON object.
