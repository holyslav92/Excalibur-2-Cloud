CTA-ONLY PATCH — output ONLY the replacement `<div class="excalibur-cta-end excalibur-social-cta">...</div>` block. No fences, no other HTML.

Use B20 structure as template (adapt text to B24: маткапитал, ДДУ, ключи, документы перед актом):

B20 template:
<div class="excalibur-cta-end excalibur-social-cta">
<p>... dual CTA: consult word (консультац/напишите) + deal word (подключусь до брони / веду сделк) ... agency tone, B24 topic</p>
<p>Святослав Шакин, The Риэлтор, Тюмень. Работаю по новостройкам и веду сделку от брони до открытия эскроу.</p>
<p>Telegram: <a href="https://t.me/Tyumen_Rieltor">@Tyumen_Rieltor</a><br>MAX: <a href="https://max.ru/id561413315447_biz">Написать в MAX</a><br>Телефон: <a href="tel:+79220016505">+7 922 001 65 05</a><br>Дзен: <a href="https://dzen.ru/holyslav">dzen.ru/holyslav</a><br>ВКонтакте: <a href="https://vk.ru/tymenrieltor">vk.ru/tymenrieltor</a></p>
<p>Ещё по теме: <a href="/">сайт</a> · <a href="/gajdy/">гайды по сделкам</a> · <a href="{{SITE_BASE}}/rieltor-tyumen/">риэлтор в Тюмени</a></p>
</div>

HARD required hrefs in output:
- href="/"
- href="/gajdy/"
- https://t.me/Tyumen_Rieltor
- https://max.ru/id561413315447_biz
- https://dzen.ru/holyslav
- https://vk.ru/tymenrieltor
- tel:+79220016505
- {{SITE_BASE}}/rieltor-tyumen/

dual_cta_soft: first <p> MUST include «консультац» or «напишите» AND «подключусь до брони» or «веду сделк»

Current block to replace:
<div class="excalibur-cta-end excalibur-social-cta">
<p>Если нужен спокойный разбор новостройки и ипотечного пакета в Тюмени, приходите в <a href="https://t.me/Tyumen_Rieltor">Telegram</a> или <a href="https://max.ru/id561413315447_biz">MAX</a>. Связаться со мной можно по телефону <a href="tel:+79220016505">+7 922 001 65 05</a>.</p>
<p>Ещё больше разборов — на <a href="https://dzen.ru/holyslav">Дзене</a> и в <a href="https://vk.ru/tymenrieltor">VK</a>. Полезные материалы собраны в <a href="{{SITE_BASE}}/gajdy/">гайдах</a>, информация о работе — на странице <a href="{{SITE_BASE}}/rieltor-tyumen/">риэлтора в Тюмени</a>.</p>
</div>
