import telebot
import random
import requests
import time
from telebot import types

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
                  f'\n/rollformid - випадкове число від 1 до 100</b>'
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

bot.polling(none_stop=True)