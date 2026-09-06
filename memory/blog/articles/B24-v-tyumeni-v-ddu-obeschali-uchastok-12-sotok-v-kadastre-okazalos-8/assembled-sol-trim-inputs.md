Assembled Sol TRIM — B24 — 2026-09-06

ROLE: Sol TRIM pass — сжать финальный article.html. НЕ переписывать с нуля.
Derouter powerful tier gpt-6-astra. Пиши HTML напрямую.

Задача: убрать spine-once повторы (12/8 соток, эскроу на паузе, «докупить», бронь сняли — не дублировать в соседних H2 и в agency ending), удалить **второй** comment magnet (оставить один — сразу после H2 «Бронь сняли…», до H2 «Дорога…»), убрать дубль inline-05.
ЦЕЛЬ: итог **1400–1600 слов** (сейчас ~1960). Агрессивно режь повторы; не трогай таблицу и факты.

СОХРАНИТЬ БЕЗ ИЗМЕНЕНИЙ URL/структуры:
- все 6 H2 дословно
- ровно 7 <figure class="inline-quad" data-slot="inline_01…inline_07"> (zero-padded inline-01…07), alt пустой
- excalibur-cta-early, excalibur-cta-mid, excalibur-cta-end целиком
- comment magnet **один раз**: «Если в ДДУ указаны 12 соток, а межевание показывает 8, подписали бы договор ради почти готового дома или отказались от брони?»
- все 4 interlink href
- таблицу целиком
- casus spine: лид, финал брони, agency ending (1–2 абзаца перед end CTA)

ЗАПРЕЩЕНО: новые факты, composite disclaimer, TL;DR, удаление H2/inline/CTA.
HTML: <b> не <strong>, <i> не <em>. Выход: только HTML фрагмент без fences.

CURRENT article.html (trim this):
