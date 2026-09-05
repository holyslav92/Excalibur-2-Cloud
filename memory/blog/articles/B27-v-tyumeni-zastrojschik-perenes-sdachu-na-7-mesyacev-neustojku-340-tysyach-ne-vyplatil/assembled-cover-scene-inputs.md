# Cover-scene inputs — B27

ROLE: cover-scene. Выход: **только валидный JSON** без markdown fences.

## Контекст

- topic_id: B27
- tenant: The Риэлтор, Тюмень
- H1: Застройщик в Тюмени задержал ключи на 7 месяцев — 340 тысяч не выплатил
- hook (cover-text): «Застройщик задержал ключи — требуйте выплату» (highlight: «выплату»)
- sticky: «Подпись не отменяет выплату»
- phone_cta: +7 922 001 65 05 (обязательно на обложке)
- angle: за три недели до ключей письмо о переносе на 7 месяцев; претензия на неустойку ~340 тыс.; застройщик признал перенос, деньги не выплатил; предлагает допсоглашение без неустойки; ключи получили, эскроу закрыли — спор о неустойке отдельно

## Wordstat stickers (manifest log ONLY — NEVER paint on cover)

- «новостройки тюмень» — 4660
- «неустойка с застройщика» — 3701 (RU225)
- «неустойка застройщик дду» — 18 (Tyumen)

## meme_picks (from cover-text.json)

- cover: this_is_fine_dog, surprised_pikachu
- inline_1: james_doakes
- inline_5: change_my_mind
- inline_7: skeleton_shield

## Variety lock (HARD — изобрети с нуля)

FACE i2i only: face-studio-2026-06-23.jpg (WHO). INVENT outfit/action/emotion/pose каждый run.

**FORBIDDEN combo (FAIL):** чёрный пиджак + бюст слева + боковой взгляд.

**Recent covers to differ from:**
- B23: light blue shirt handover room EGRN vs DDU full-body right
- B22: yellow shirt bank mortgage desk full-body center
- B12: light blue showroom letter calendar +12m waist right
- B20: terracotta overshirt MFC corridor two DDU

**Required:** light/bright #FFF high-key, sun flare; this_is_fine_dog people-meme + surprised_pikachu small stickers; NO Wordstat query strips/bars on canvas; NO dark cinematic; NO daypart formula; NOT bank/MFC/handover duplicate; NEW location (bright construction sales pavilion with timeline slip board and penalty documents).

## Inline slots (scene_hint + alt for each; NO host face on inline)

### inline_1 — realistic_photo — «За три недели до ключей — письмо о переносе на семь месяцев» (pair with inline_2)
Labels: Перенос на семь месяцев | ДДУ не меняется | Допсоглашение в приложении | Ипотека уже идёт
Meme: james_doakes tiny corner

### inline_2 — comparison_table — pair with inline_1
Labels: Претензия 340 тысяч | Расчёт по 214-ФЗ | Перенос признан | Деньги не выплатили | Снова допсоглашение
NO meme

### inline_3 — realistic_photo — «Финал: ключи получили, эскроу закрыли — неустойку не заплатили»
Labels: Ключи через семь месяцев | Эскроу закрыли | Неустойка отдельно | Досудебная претензия | Два разных процесса
NO meme — bright keys on tray next to closed escrow folder and separate penalty claim envelope

### inline_4 — realistic_photo — «Просрочка наступила: претензия на 340 тысяч и ответ застройщика»
Labels: Подпишите сейчас | Срок переносят | О выплате молчат | Не подписали | Право сохранили
NO meme — unsigned addendum on bright desk with red "no penalty clause" highlight

### inline_5 — process_flow — «Допсоглашение без неустойки: что предлагают «ради скорости»»
Labels: Мораторий сняли | Отсрочка до 31.12.2026 | Статья 333 ГК РФ | Расчёт 340 тысяч | Не гарантия суда
Meme: change_my_mind tiny corner

### inline_6 — bar_timeline_chart — «Неустойка в 2026: начисление вернулось, выплата может ждать»
Labels: Срок в ДДУ | Письмо о переносе | Дата передачи ключей | Претензия и ответ | Переписка в мессенджерах
NO meme

### inline_7 — structure_diagram — «Что проверить в ДДУ и переписке — таблица»
Labels: Проверьте до подписи | Не спешите с допом | Ключи получили | Деньги отдельный спор | Цена подписи
Meme: skeleton_shield tiny corner

## JSON schema (обязательные поля)

```json
{
  "cover_emotion": "...",
  "cover_motifs": { "composition", "location", "meme", "prop_set", "sticker_set", "joke", "outfit", "emotion", "pose_framing", "action" },
  "wordstat_stickers": ["...", "...", "..."],
  "slots": {
    "cover": { "scene_hint", "alt", "cover_emotion", "meme_picks" },
    "inline_1": { "scene_hint", "alt", "meme_picks" },
    ...
  }
}
```
