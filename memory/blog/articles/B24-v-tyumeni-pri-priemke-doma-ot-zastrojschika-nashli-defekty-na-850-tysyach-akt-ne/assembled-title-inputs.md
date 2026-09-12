# Assembled title inputs — B24 (for Derouter title role)

**MANDATORY:** Derouter powerful tier `gpt-6-astra` is operational. You ARE running inside `scripts/excalibur_blog_derouter_opus_chat.py --role title`. Output ONLY valid JSON for `title-brief.json` with fields `topic_id`, `h1`, `title`, `subject`, `angle`, `comment_magnet_angle`, `slug`, `slug_confirmed`, `verdict`.

**CRITICAL CONSTRAINT:** The tenant topic focus is `newbuild_only`. The H1 MUST explicitly contain a newbuild keyword like «застройщика» or «от застройщика».
Candidate H1: «В Тюмени в доме от застройщика нашли дефекты на 850 тысяч — акт не подписали»

**topic_id:** B24  
**h1:** В Тюмени в доме от застройщика нашли дефекты на 850 тысяч — акт не подписали  
**title:** В Тюмени в доме от застройщика нашли дефекты на 850 тысяч — акт не подписали  
**slug:** v-tyumeni-pri-priemke-doma-ot-zastrojschika-nashli-defekty-na-850-tysyach-akt-ne  
**tenant:** The Риэлтор (Святослав Шакин, Тюмень)  
**niche:** Новостройки Тюмени (дома и квартиры от застройщика)  
**cluster_id:** acceptance_defects_penalty  

## Scout Handoff & Research
- event: На приёмке нового дома в коттеджном посёлке под Тюменью независимый технадзор выявил дефекты утепления, промерзание и брак на 850 000 рублей.
- consequence: Семья отказалась подписывать чистый передаточный акт под обещание гарантийного ремонта, составила дефектную ведомость и остановила приёмку.
- comment_magnet_angle: Застройщик обещает устранить дефекты по гарантии после подписания акта — вы бы подписали акт ради ключей или остановили приёмку?
- P0 Wordstat: «приемка квартир тюмень» (279), «дома в тюмени от застройщика» (279)

Сгенерируй `title-brief.json` строго по контракту skills/title-excalibur-blog/SKILL.md.
