# Cover-scene B34 — только JSON

Святослав Шакин, 28 лет, то же лицо что на референсе identity-real, medium slim. Новая одежда, новая поза, новая эмоция. Руки анатомически нормальные: ровно пять пальцев, без лишних и без сросшихся. Не копируй студийную закрытую улыбку.

Сюжет обложки: светлый шатёр подрядчика под Тюменью, на столе открытый договор подряда на дом и макет деревянного дома. Он смотрит на пустой раздел оплаты — там реквизиты фирмы, счёта эскроу нет. High-key, солнце, без тёмного кино.

Не повторять: чёрный пиджак, терракота, оливковый жилет, песочная куртка, голубая рубашка с горчичным жилетом, коленопреклонённый замер, бюст слева.

Hook уже задан: «Семья остановила перевод за новый дом». Телефон на обложке текстом +7 922 001 65 05, не в руке.

inline: без лица хоста, без второго человека-героя. 2–4 realistic_photo (inline_1, inline_2, inline_4). Остальные — схемы с цифрами. Пара фото+схема: inline_1 photo и inline_2 diagram на одном бите — поставь placement_group pair только если поле есть; иначе просто scene_hint.

Выход JSON:
{
  "cover_emotion": "скептический боковой взгляд на пустую строку договора, губы сжаты, брови чуть сведены",
  "cover_motifs": {
    "composition": "host standing right of center, hook zone upper left, phone text bottom right, meme stickers in corners",
    "location": "bright sunlit contractor canopy near a timber house model, white table, open podryad contract, Tyumen summer",
    "meme": "side_eye_chloe + polite_cat corner stickers",
    "prop_set": "open contractor contract, timber house model, yellow sticky",
    "sticker_set": "side_eye_chloe top-left, polite_cat bottom-left, clear of hook face and phone",
    "joke": "side-eye at a contract that says protected while the payment line is just the firm account",
    "outfit": "white oxford rolled sleeves, rust chinos, no blazer no vest",
    "emotion": "skeptical side glance at the empty escrow line, lips pressed, not a studio smile",
    "pose_framing": "standing three-quarter from the right, waist-up, both hands on the table edge of the folder, not a left bust",
    "action": "points at the payment clause that has only company bank details and no escrow account"
  },
  "slots": {
    "cover": {
      "scene_hint": "Светлый шатёр, белая рубашка, договор на столе, скептический взгляд, нормальные руки, солнце.",
      "cover_emotion": "скептический боковой взгляд"
    },
    "inline_1": {"scene_hint": "Светлый стол, открытый договор подряда, реквизиты фирмы, без лиц."},
    "inline_2": {"scene_hint": "Схема: реквизиты фирмы против счёта эскроу, без людей."},
    "inline_3": {"scene_hint": "Схема: закон 186-ФЗ с 1 марта 2025, эскроу не обязателен, без людей."},
    "inline_4": {"scene_hint": "Светлый участок под дом, макет, папка договора, без лиц."},
    "inline_5": {"scene_hint": "Схема: заказчик открывает счёт, выплата после приёмки, без людей."},
    "inline_6": {"scene_hint": "Диаграмма: около 600 домов и 1,5 тысячи договоров, без людей."},
    "inline_7": {"scene_hint": "Сравнение августа: 1441 договор и 581 сданный дом, без людей."}
  }
}

Только JSON, без markdown.
