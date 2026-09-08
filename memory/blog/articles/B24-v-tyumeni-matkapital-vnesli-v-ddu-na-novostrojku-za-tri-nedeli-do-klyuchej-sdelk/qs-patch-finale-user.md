TARGETED PATCH — output ONLY two replacement HTML fragments, separated by blank line. No fences.

Rephrase to avoid repeating middle phrase «собственность владельца сертификата супруга» and «выдачу ключей перенесли примерно». Same facts. Do NOT use those exact word sequences.

Fragment 1 — replace this paragraph:
<p>Юрист подготовил дополнительное соглашение к ДДУ и соглашение о будущих долях. В них закрепили обязанность оформить квартиру в общую собственность владельца сертификата, супруга и обоих детей после передачи объекта и регистрации права. Порядок согласовали с банком, включая снятие залога.</p>

Fragment 2 — replace ONLY the table cell text in row ДДУ (keep <tr> structure):
<td>Одинаково ли описана обязанность оформить жильё в общую собственность владельца сертификата, супруга и всех детей</td>
→ output full <td>...</td> with rephrased text (parents + children, no «владельца сертификата супруга» cluster)

Also rephrase this paragraph to avoid «выдачу ключей перенесли примерно»:
<p>После согласования исправленный пакет снова направили на проверку. Банк возобновил подготовку регистрации — первоначальный график вернуть не удалось: подписание акта и выдачу ключей перенесли примерно на месяц.</p>

Output: 3 HTML fragments (2 full <p>, 1 full <td>).
