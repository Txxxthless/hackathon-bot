# hackathon-bot
# Бот Лєщова Павла Сергійовича ПЗ-22-3

Усі підпункти ТЗ виконати не вдалося. Деякі реалізовані дещо топорно, зокрема парсер таблиці. Я там завантажив свою таблицю, бо с нормальним парсингом тої, що нам кидають, не зміг впоратись. Також не реалізована команда виведення випадкових чисел в залежності від введених аргументів (у моєму варіанті ця команда
дає тільки випадкові числа від 1 до 100).

# Бота задеплоїно на Heroku. Сам бот - https://t.me/txxthlesshackathonBot .

# Функціонал бота:
 # КОМАНДИ:
   1. /start - команда для старту бота. Не робить нічого окрім привітання користувача та запрошення ознайомитись з функціоналом.
   2. /help - команда, що показує усі доступні команди.
   3. /randomphrase - ця команда повертає випадкову фразу, сформовану із трьох слів (зазначені у масивах в хардкоді). 
   4. /randompaste - команда видає копіпасту.
   5. /randomcat - команда видає випадкову світлину із котиком. ! Для цієї команди я використав сайт https://cataas.com/cat . Вдень він працює нормально, але останні два дні під вечір сайт падає, тому команда може не працювати.
   6. /dota - створює опитування "Го в доту" -> "Так" або "Ні".
   7. /forward - пересилає випадковий пост із каналу https://t.me/lifethingss .
   8. /rollformid - видає випадкове число від 1 до 100.
   9. /schedule - парсинг таблиці ексель (таблиця надана у репозиторії).
   10. /play - гра "Життя". Опис гри доступний при використанні цієї команди.
 
 # INLINE-MODE:
   Для використання inline-mod'у бота треба використати такий формат: @txxthlesshackathonBot "команда" .
   1. @txxthlesshackathonBot фраза - видає фразу як у команді /randomphrase.
   2. @txxthlesshackathonBot киця - надсилає одну із запропонованих світлин із котиками (6 варіантів).
   3. @txxthlesshackathonBot бен - надсилає аудіофайл (2 варіанти).
   4. @txxthlesshackathonBot рол - випадкове число від 1 до 100.
   5. @txxthlesshackathonBot паста - паста як у команді /randompaste (5 варіантів).
