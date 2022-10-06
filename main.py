import telebot
import random
import requests
import time
from telebot import types
from openpyxl import load_workbook
bot = telebot.TeleBot('5715762546:AAFOrpIoGNKEmx2_qHi-P1z95-pTGviuOYs')

# не пам'ятаю нащо мені знадобилися окремі функції :/
def randompaste_func():
    items1 = [f'Я', f'ФПМ', f'Міша', f'Ананас', f'Шевченко']
    items2 = [' - найкращий ', ' - дивний ', ' - неймовірно старанний ', ' - військовий ', ' - загальновизнаний ']
    items3 = ['чарівник.', 'геній.', 'кібервійськовий.', 'красень.', 'інопланетянин.']
    i1 = random.randint(0, 4)
    i2 = random.randint(0, 4)
    i3 = random.randint(0, 4)
    message = items1[i1] + items2[i2] + items3[i3]
    return message

def randomcatpic():
    url = 'https://cataas.com/cat'
    name = 'catpic.jpg'
    req = requests.get(url)
    with open(name, 'wb') as f:
        f.write(req.content)
    catPic = open('catpic.jpg', 'rb')
    return catPic

# команди
@bot.message_handler(commands=['start'])
def start(msg):
    message = f'<b>Привіт, {msg.from_user.first_name}.</b>'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    list = f'<b>Для ознайомлення із функціоналом введіть команду /help !</b>'
    bot.send_message(msg.chat.id, list, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(msg):
        message = f'<b>Я можу виконувати такі команди: </b>'
        bot.send_message(msg.chat.id, message, parse_mode='html')
        msgList = f'<b>/start - початок роботи' \
                  f'\n/help - перелік функціоналу' \
                  f'\n/randomphrase - випадково сгенерована фраза' \
                  f'\n/randompaste - випадкова паста з чату ФПМ'\
                  f'\n/randomcat - випадкова світлина з кицею' \
                  f'\n/dota - створення опитування про готовність піти у Dota 2' \
                  f'\n/forward - пересилання випадкового повідомлення із каналу з мудрими виразами' \
                  f'\n/rollformid - випадкове число від 1 до 100' \
                  f'\n/schedule - показати розклад ПЗ-22-3' \
                  f'\n/play - пограти у гру "Життя"</b>'
        bot.send_message(msg.chat.id, msgList, parse_mode='html')

@bot.message_handler(commands=['randomphrase'])
def randomphrase(msg):
        message = randompaste_func()
        bot.send_message(msg.chat.id, message, parse_mode='html' )

@bot.message_handler(commands=['randompaste'])
def randompaste(msg):
    pastelist = ['<b>Миша - военный, колдун, экстрасенс, чародей, психолог, спец по агентам, спец из рода панасенковых, порноактёр, гачибой, козак та й ваще норм мужик, пивка 0,5 бахнуть запросто, президент мира, стриптизер, ещё человек гений, и будущий президент, ещё он будет колонизировать марс, воевал, екзорцист, экстрасенс, идеолог, филантроп, интроверт, император Галактики, ещё не любит когда его перебивают</b>',
                 '<b>Привіт! Ти напевно гадаєш, хто ми, і як тебе знашли? Все просто. МИ хакери(ні), ми студрада ФПМ, вітаємо зі вступом. Якщо тебе немає в чаті абітурієнтів факультету, то заходь, обовʼязково.</b>',
                 '<b>как тут писать блин что-то, я как не зайду либо дота, либо гачи, либо ещё что-то за что я не шарю, так лучше совсем не писать ничего чем бред какой-то</b>',
                 '<b>Нет более глубокого одиночества, чем одиночество самурая, разве что, может быть, одиночество тигра в джунглях. пойду в доту шоль</b>',
                 '<b>джо байден присоединяйся в пт-22-1, мы не дадим в обиду</b>']
    item = random.randint(0, 4)
    bot.send_message(msg.chat.id, pastelist[item],parse_mode='html')

@bot.message_handler(commands=['randomcat'])
def randomcat(msg):
        catPic = randomcatpic()
        message = f'<b>Ось ваша киця:</b>'
        bot.send_message(msg.chat.id, message, parse_mode='html')
        bot.send_photo(msg.chat.id, catPic)

@bot.message_handler(commands=['dota'])
def dota(msg):
    message = f'Погнали в дотку?'
    bot.send_poll(msg.chat.id, message, ["Так!","Ні..."],False, close_date=int(round(time.time() + 3600)),)

@bot.message_handler(commands=['forward'])
def forward(msg):
    messageId = random.randint (3, 12)
    bot.forward_message(msg.chat.id, from_chat_id='-1001449056768', message_id=messageId)

@bot.message_handler(commands=['rollformid'])
def rollformid(msg):
    message = f'<b>{msg.from_user.first_name} отримує число від 1 до 100: </b>'
    rollNumber = random.randint(1, 100)
    bot.send_message(msg.chat.id, message, parse_mode='html')
    bot.send_message(msg.chat.id, f'{rollNumber}', parse_mode='html')

@bot.message_handler(commands=['schedule'])
def schedule(msg):
    monday = ['','','','','','']
    book = load_workbook(filename="D:\hachathon-bot\розклад.xlsx") #шлях до файла розклад.xlsx
    sheet = book['Лист1']
    for i in range(1, 7):
        number = sheet['A' + str(i)].value
        day = sheet['B' + str(i)].value
        monday[i-1] = f'{number} {day}'
    message = f'{monday[0]}\n{monday[1]}\n{monday[2]}\n{monday[3]}\n{monday[4]}\n{monday[5]}'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    for i in range(1, 7):
        number = sheet['A' + str(i)].value
        day = sheet['C' + str(i)].value
        monday[i-1] = f'{number} {day}'
    message = f'{monday[0]}\n{monday[1]}\n{monday[2]}\n{monday[3]}\n{monday[4]}\n{monday[5]}'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    for i in range(1, 7):
        number = sheet['A' + str(i)].value
        day = sheet['D' + str(i)].value
        monday[i-1] = f'{number} {day}'
    message = f'{monday[0]}\n{monday[1]}\n{monday[2]}\n{monday[3]}\n{monday[4]}\n{monday[5]}'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    for i in range(1, 7):
        number = sheet['A' + str(i)].value
        day = sheet['E' + str(i)].value
        monday[i-1] = f'{number} {day}'
    message = f'{monday[0]}\n{monday[1]}\n{monday[2]}\n{monday[3]}\n{monday[4]}\n{monday[5]}'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    for i in range(1, 7):
        number = sheet['A' + str(i)].value
        day = sheet['F' + str(i)].value
        monday[i-1] = f'{number} {day}'
    message = f'{monday[0]}\n{monday[1]}\n{monday[2]}\n{monday[3]}\n{monday[4]}\n{monday[5]}'
    bot.send_message(msg.chat.id, message, parse_mode='html')

# inline-мод
@bot.inline_handler(lambda query: query.query == 'фраза')
def query_text(inline_query):
    try:
        message = randompaste_func()
        result = types.InlineQueryResultArticle('1', 'Випадкова фраза', types.InputTextMessageContent(message))
        bot.answer_inline_query(inline_query.id, [result], cache_time=1)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'киця')
def query_photo(inline_query):
    try:
        result = types.InlineQueryResultPhoto('1',
                                         'https://cdn2.thecatapi.com/images/TdxQ2VvJK.jpg',
                                         'https://cdn2.thecatapi.com/images/TdxQ2VvJK.jpg',)
        result2 = types.InlineQueryResultPhoto('2',
                                          'https://cdn2.thecatapi.com/images/9c6.jpg',
                                          'https://cdn2.thecatapi.com/images/9c6.jpg')
        result3 = types.InlineQueryResultPhoto('3',
                                         'https://cdn2.thecatapi.com/images/9ea.jpg',
                                         'https://cdn2.thecatapi.com/images/9ea.jpg',)
        result4 = types.InlineQueryResultPhoto('4',
                                         'https://cdn2.thecatapi.com/images/CRcbyTIzQ.jpg',
                                         'https://cdn2.thecatapi.com/images/CRcbyTIzQ.jpg', )
        result5 = types.InlineQueryResultPhoto('5',
                                         'https://cdn2.thecatapi.com/images/115.png',
                                         'https://cdn2.thecatapi.com/images/115.png')
        result6 = types.InlineQueryResultPhoto('6',
                                         'https://cdn2.thecatapi.com/images/a4p.jpg',
                                         'https://cdn2.thecatapi.com/images/a4p.jpg', )
        bot.answer_inline_query(inline_query.id, [result, result2, result3,result4,result5,result6])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'бен')
def query_audio(inline_query):
    try:
        result = types.InlineQueryResultAudio(id='1',audio_url='https://cdn.discordapp.com/attachments/622518716210610187/1027172627124600912/yes.mp3',title='Yes')
        result2 = types.InlineQueryResultAudio(id='2',audio_url='https://cdn.discordapp.com/attachments/622518716210610187/1027172672427282522/no.mp3',title='No')
        bot.answer_inline_query(inline_query.id, [result, result2])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'рол')
def query_text(inline_query):
    try:
        rollNumber = random.randint(1, 100)
        message = f'Ваш рол: {rollNumber} !'
        result = types.InlineQueryResultArticle('1', 'Ролимо за мід', types.InputTextMessageContent(message))
        bot.answer_inline_query(inline_query.id, [result], cache_time=1)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'тримай')
def query_gif(inline_query):
    try:
        r = types.InlineQueryResultGif('1', gif_url='https://media.tenor.com/t_OITIPhJTkAAAAC', thumb_url='https://media.tenor.com/t_OITIPhJTkAAAAC')
        bot.answer_inline_query(inline_query.id, [r])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'паста')
def query_text(inline_query):
    try:
        result = types.InlineQueryResultArticle('1', 'Правда про Мішу', types.InputTextMessageContent('Миша - военный, колдун, экстрасенс, чародей, психолог, спец по агентам, спец из рода панасенковых, порноактёр, гачибой, козак та й ваще норм мужик, пивка 0,5 бахнуть запросто, президент мира, стриптизер, ещё человек гений, и будущий президент, ещё он будет колонизировать марс, воевал, екзорцист, экстрасенс, идеолог, филантроп, интроверт, император Галактики, ещё не любит когда его перебивают'))
        result2 = types.InlineQueryResultArticle('2', 'Тебе знайшли', types.InputTextMessageContent('Привіт! Ти напевно гадаєш, хто ми, і як тебе знашли? Все просто. МИ хакери(ні), ми студрада ФПМ, вітаємо зі вступом. Якщо тебе немає в чаті абітурієнтів факультету, то заходь, обовʼязково.'))
        result3 = types.InlineQueryResultArticle('3', 'Чат ФПМ', types.InputTextMessageContent('как тут писать блин что-то, я как не зайду либо дота, либо гачи, либо ещё что-то за что я не шарю, так лучше совсем не писать ничего чем бред какой-то'))
        result4 = types.InlineQueryResultArticle('4', 'Мудрощі', types.InputTextMessageContent('Нет более глубокого одиночества, чем одиночество самурая, разве что, может быть, одиночество тигра в джунглях. пойду в доту шоль'))
        result5=types.InlineQueryResultArticle('5', 'Джо Байден', types.InputTextMessageContent('джо байден присоединяйся в пт-22-1, мы не дадим в обиду'))
        bot.answer_inline_query(inline_query.id, [result, result2,result3,result4,result5])
    except Exception as e:
        print(e)


# гра


class player:
    hp = int
    karma = int
    balance = int
    deathcounter = int
    def __init__(self, hp, karma, balance, deathcounter):
        self.hp = hp
        self.karma = karma
        self.balance = balance
        self.deathcounter = deathcounter
    def healthcheck(self):
        if self.hp <= 0:
            status = f'<b>Здоров\'я на критичному рівні! Ви попадаєте до лікарні, де ваше здоров\'я трохи покращюється.</b>'
            self.hp = 40
            self.deathcounter += 1
            return status
        else:
            return f'<b>Здоров\'я на нормальному рівні</b>'
    def karmacheck(self):
        if self.karma <= 0:
            status = f'<b>Ваша карма на низькому рівні, тому ви стикаєтесь із невдачею і втрачаєте здоров\'я.</b>'
            self.hp -= 5
            return status
        else:
            return f'<b>Карма на нормально рівні</b>'
    def balancecheck(self):
        if self.balance <= 0:
            status = f'<b>У вас замало коштів для підтримання нормальног життя і ви втрачаєте здоров\'я.</b>'
            self.hp -= 5
            return status
        else:
            return f'<b>Баланс на нормальному рівні</b>'


@bot.message_handler(commands=['play'])
def play(msg):
    rules = f'<b>Правила</b>'
    bot.send_message(msg.chat.id, rules, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    startkey = types.KeyboardButton('Старт!')
    markup.add(startkey)
    bot.send_message(msg.chat.id, 'Готові?', reply_markup=markup)
    p = player(5, 5, 200, 0)

    @bot.message_handler()
    def level(choice):

        def deathscreen(healthmessage):
            if healthmessage == f'<b>На жаль, ваш герой загинув...</b>':
                var = types.KeyboardButton('/play')
                endmarkup = types.ReplyKeyboardMarkup()
                endmarkup.add(var)
                bot.send_message(choice.chat.id, 'На цьому все!', parse_mode='html', reply_markup=endmarkup)

        if choice.text == "Старт!":
            choicemarkup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Сказати щось на дитячому')
            var2 = types.KeyboardButton('Спати')
            choicemarkup.add(var1, var2)
            message = f'<b>Вітаю у грі життя. На данний момент ви тільки народилися. У вас все ще попереду. Здоров\'я та карма на максимумі.\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance}</b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup)

        if choice.text == "Сказати щось на дитячому" or choice.text == "Спати":
            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Нащо та домашка? Футбол цікавіше')
            var2 = types.KeyboardButton('Мабудь, дійсно треба повчитись')
            var3 = types.KeyboardButton('Саме час почати кар\'єру алкаша')
            choicemarkup1.add(var1,var2,var3)
            message = f'<b>Життя йде дуже швидко, хоча вам так і не здається. Ви вчитесь у школі. Батьки знову і звону кажуть вчити домашку, та вам це аж ніяк не цікаво.\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance} </b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == "Нащо та домашка? Футбол цікавіше":
            p.hp -= 5
            bot.send_message(choice.chat.id, 'Граючи у футбол, ви трохи скалічились.', parse_mode='html')
        if choice.text == "Саме час почати кар\'єру алкаша":
            p.hp -= 25
            p.karma -= 1
            p.balance -= 40
            bot.send_message(choice.chat.id, 'Це... Явно був не кращий вибір.', parse_mode='html')

        if choice.text == "Нащо та домашка? Футбол цікавіше" or choice.text == "Мабудь, дійсно треба повчитись" or choice.text == "Саме час почати кар\'єру алкаша":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Готуватись до іспиту')
            var2 = types.KeyboardButton('Час регнути в дотку')
            var3 = types.KeyboardButton('Трохи побухати, а потім за навчання')
            choicemarkup1.add(var1,var2,var3)
            message = f'<b>Ну і нашо ти вибрав фізику одним із предметів на ЗНО? Що ж, перед тобою вибір, який багато хто вважає невмовірно серьозним. Навіть вирішальним.\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance} </b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == "Час регнути в дотку":
            p.karma -= 1
            bot.send_message(choice.chat.id, 'Трохи пограли в доту: втратили трохи карми через неперевні аморальні вислови, але потім в тільті пішли робити домашку', parse_mode='html')
        if choice.text == "Трохи побухати, а потім за навчання":
            p.hp -= 25
            p.balance -= 50
            bot.send_message(choice.chat.id, 'Момент \'а потім за навчання\' звучав дуже впевненно, але ні', parse_mode='html')
            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Використати')
            var2 = types.KeyboardButton('Не використовувати')
            choicemarkup1.add(var1,var2)
            bot.send_message(choice.chat.id, 'В локації \'ШАРАГА\' ви знайшли унікальний предмет \'СНЮС\'. Використати його для попвнення здоров\'я?', parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == "Використати": p.hp += 5

        if choice.text == "Не використовувати" or choice.text == "Використати" or choice.text == "Готуватись до іспиту" or choice.text == "Час регнути в дотку":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('На завод')
            var2 = types.KeyboardButton('В унік')
            var3 = types.KeyboardButton('В дотку')
            choicemarkup1.add(var1, var2, var3)
            message = f'<b>Всі дороги ведуть...\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance} </b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == "На завод":
            p.hp -= 25
            p.balance += 1000
            message = 'Ну, норм вибір.'
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice.text == "В унік":
            p.hp -= 20
            message = 'Ви відчуваєье втому в усьому.'
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice.text == "В дотку":
            p.karma -= 2
            message = 'Мінус карма. А що робити?'
            bot.send_message(choice.chat.id, message, parse_mode='html')

        if choice.text == "На завод" or choice.text == "В унік" or choice.text == "В дотку":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Втекти')
            var2 = types.KeyboardButton('Битися')
            var3 = types.KeyboardButton('Пощада')
            choicemarkup1.add(var1, var2, var3)
            message = f'<b>По дорозі ви натрапляєте на елітного моба \'ГОПНІК\'. Цей моб входить у режим битви із вами.\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance} </b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == "Втекти":
            message = 'Не дуже мужнью, але яка різниця?'
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice.text == "Битися":
            p.balance -= 100
            p.hp -= 30
            message = 'Здається, що він ходив на бокс. А ще в вас вкрали гроші.'
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice.text == "Пощада":
            p.hp -= 30
            message = 'Сміливо'
            bot.send_message(choice.chat.id, message, parse_mode='html')

        if choice.text == "Битися" or choice.text == "Пощада" or choice.text == "Втекти":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Забрати')
            var2 = types.KeyboardButton('Не чіпати')
            choicemarkup1.add(var1, var2)
            message = f'На дорозі ви знаходите гроші. Залишити їх чи забрати?<b>\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance}</b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice.text == 'Забрати':
            message = f'Ви забрали гроші та втратили карму.'
            p.balance += 200
            p.karma -= 3
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice.text == 'Не чіпати':
            message = f'Ви вирішуєте не чіпати грошей. Ваша карма стала трохи більшою'
            p.karma += 2
            bot.send_message(choice.chat.id, message, parse_mode='html')

        if choice.text == "Забрати" or choice.text == "Не чіпати":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('Скористатися можливітсю')
            var2 = types.KeyboardButton('Не робити цього')
            var3 = types.KeyboardButton('Чекати на більш вигідну пропозицію')
            choicemarkup1.add(var1, var2, var3)
            message = f'Ви отримуєте можливіть працевлаштуватися, але заробіток обіцяють невеликий. Чи скористаєтесь цим?<b>\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance}</b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)
        if choice == 'Скористатися можливітсю':
            message = f'Ви скористалися можливітсю, але отримали не дуже багато грошей і з часом покинули компанію.'
            p.balance += 280
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice == 'Не робити цього':
            message = f'Ви нічого не зробили.'
            bot.send_message(choice.chat.id, message, parse_mode='html')
        if choice == 'Чекати на більш вигідну пропозицію':
            message = f'Ви вирішили почекати і з часом отримали можливість працевлаштування із великою заробітнью платою. Але вийшло так, що вас звільнили...'
            p.balance += 720
            bot.send_message(choice.chat.id, message, parse_mode='html')

        if choice.text == "Скористатися можливітсю" or choice.text == "Не робити цього" or choice.text == "Чекати на більш вигідну пропозицію":

            karmamessage = p.karmacheck()
            bot.send_message(choice.chat.id, karmamessage, parse_mode='html')
            balancemessage = p.balancecheck()
            bot.send_message(choice.chat.id, balancemessage, parse_mode='html')
            healthmessage = p.healthcheck()
            bot.send_message(choice.chat.id, healthmessage, parse_mode='html')
            deathscreen(healthmessage)

            choicemarkup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            var1 = types.KeyboardButton('1')
            var2 = types.KeyboardButton('2')
            var3 = types.KeyboardButton('3')
            choicemarkup1.add(var1, var2, var3)
            message = f'sit<b>\n\n❤: {p.hp} / 100 \n⭐: {p.karma}  \n💰: {p.balance}</b>'
            bot.send_message(choice.chat.id, message, parse_mode='html', reply_markup=choicemarkup1)

        if choice.text == "1" or choice.text == "2" or choice.text == "3":
            message = f'<b>Гру закінчено! Ваші результати:\n   \n❤: {p.hp}\n ⭐: {p.karma}\n 💰: {p.balance}\n 🏥: {p.deathcounter}</b>'
            bot.send_message(choice.chat.id, message, parse_mode='html')
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
            endbutton = types.KeyboardButton('/endgame')
            markup.add(endbutton)
            bot.send_message(choice.chat.id, f'<b>Для закінчення виберіть команду /endgame !</b>', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['endgame'])
def endgame(msg):
    message = f'<b>Гру закінчено. Нагадую функціонал: </b>'
    bot.send_message(msg.chat.id, message, parse_mode='html')
    msgList = f'<b>/start - початок роботи' \
              f'\n/help - перелік функціоналу' \
              f'\n/randomphrase - випадково сгенерована фраза' \
              f'\n/randompaste - випадкова паста з чату ФПМ' \
              f'\n/randomcat - випадкова світлина з кицею' \
              f'\n/dota - створення опитування про готовність піти у Dota 2' \
              f'\n/forward - пересилання випадкового повідомлення із каналу з мудрими виразами' \
              f'\n/rollformid - випадкове число від 1 до 100' \
              f'\n/schedule - показати розклад ПЗ-22-3' \
              f'\n/play - пограти у гру "Життя"</b>'
    bot.send_message(msg.chat.id, msgList, parse_mode='html')


bot.polling(none_stop=True)