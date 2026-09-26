TASK: Emit ONLY valid JSON-LD for schema.org @graph. No markdown, no prose, no code fences. First character must be { last must be }.

B33 BlogPosting fields:
- headline: Инвестор свернул сделку — запрет аренды всплыл в ДДУ за 3 дня до эскроу
- description: За три дня до эскроу в проекте ДДУ всплыл запрет сдавать квартиру на два года — инвестор остановил покупку новостройки в Тюмени до подписания.
- datePublished: 2026-09-26
- inLanguage: ru-RU
- url and mainEntityOfPage @id: {{SITE_BASE}}/v-proekte-ddu-v-tyumenskoj-novostrojke-vsplyl-zapret-sdavat-kvartiru-2-goda-inve/
- BlogPosting @id: same path + #blogposting
- NO FAQPage
- Use {{SITE_BASE}} placeholder everywhere for site host (never [REDACTED])
- Organization The Риэлтор @id {{SITE_BASE}}/#organization
- Person Святослав Шакин @id {{SITE_BASE}}/rieltor-tyumen/#svyatoslav-shakin jobTitle Личный риэлтор в Тюмени
- Person sameAs only external: https://dzen.ru/holyslav https://t.me/Tyumen_Rieltor https://vk.ru/tymenrieltor https://wa.me/79220016505
- logo {{SITE_BASE}}/wp-content/uploads/logo.png

Match structure of neighbor article B30 schema.jsonld (Organization + Person + BlogPosting in @graph).
