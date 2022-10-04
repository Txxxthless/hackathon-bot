import telebot
import random
import requests
import time
from telebot import types

bot = telebot.TeleBot('5715762546:AAFOrpIoGNKEmx2_qHi-P1z95-pTGviuOYs')


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
        msgList = f'<b>/start - початок роботи\n/help - перелік функціоналу' \
                  f'\n/randompaste - випадково сгенерована фраза' \
                  f'\n/randomcat - випадкова світлина з кицею' \
                  f'\n/dota - створення опросу про готовність піти у Dota 2</b>'
        bot.send_message(msg.chat.id, msgList, parse_mode='html')


@bot.message_handler(commands=['randompaste'])
def randompaste(msg):
        items1 = [f'<b>Я</b>', f'<b>ФПМ</b>', f'<b>Міша</b>', f'<b>Ананас</b>', f'<b>Шевченко</b>']
        items2 = [' - найкращий ', ' - дивний ', ' - неймовірно старанний ', ' - військовий ', ' - загальновизнаний ']
        items3 = ['чарівник.','геній.','кібервійськовий.','красень.','інопланетянин.']
        i1 = random.randint (0, 4)
        i2 = random.randint (0, 4)
        i3 = random.randint (0, 4)
        message = items1[i1] + items2[i2] + items3[i3]
        bot.send_message(msg.chat.id, message, parse_mode='html' )


@bot.message_handler(commands=['randomcat'])
def randomcat(msg):
        url = 'https://cataas.com/cat'
        name = 'catpic.jpg'
        req = requests.get(url)
        with open(name, 'wb') as f:
            f.write(req.content)
        catPic = open('catpic.jpg', 'rb')
        message = f'<b>Ось ваша киця:</b>'
        bot.send_message(msg.chat.id, message, parse_mode='html')
        bot.send_photo(msg.chat.id, catPic)

@bot.message_handler(commands=['dota'])
def dota(msg):
    message = f'Погнали в дотку?'
    bot.send_poll(msg.chat.id, message, ["Так!","Ні..."],False, close_date=int(round(time.time() + 3600)),)



bot.polling(none_stop=True)