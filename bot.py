import string
import telebot
import random
from pyowm import OWM
from telebot.util import is_string

TOKEN = '1671666913:AAFQhsx4fDlwLGrltwBnZps3Z2k7XH1HG4A'
bot = telebot.TeleBot(TOKEN)
owm = OWM('2362c46caf311c3c4abba004d7472578')
mgr = owm.weather_manager()
a = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "{0.first_name}, Поставьте 5)".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['random'])
def welcome(message):
    ranNum = random.randint(0,1000)
    bot.send_message(message.chat.id, str(int(ranNum)))

@bot.message_handler(commands=['weather'])
def welcome(message):
    sent = bot.send_message(message.chat.id, "В каком городе?".format(message.from_user, bot.get_me()))
    bot.register_next_step_handler(sent, get_city)
    
def get_city(message):
    city = message.text
    try: 
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        clouds = w.detailed_status
        wind = w.wind()['speed']
        rain = w.rain
        sent = bot.send_message(message.chat.id, "Погода: "+clouds+"\n"+"Температура: "+str(float(temp))+"C*"+"\n"+"Скорость ветра: "+str(float(wind))+"m/s".format(message.from_user, bot.get_me()))
    except:
        bot.send_message(message.chat.id, "Город не найден, повторите попытку".format(message.from_user, bot.get_me()))


@bot.message_handler(commands=['sendcats'])
def sendcats(message):
    rand = random.randint(0, 5)
    if rand == 0:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALXqmArxzB9MK9hhCdYCRST4luOb8mfAAJVAAOVv0kybXX0TMF2OiIeBA")
    if rand == 1:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALXsGAryFZ8Fiy2b7XqXY9bgS734fpMAAIOAQAC7umcB1pPlhh0W_94HgQ")
    if rand == 2:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALXrWAryCrYtZGjULyAGtcorvBIUX4GAALnAAPSqCYXKetSLEhjRW8eBA")
        bot.send_message(message.chat.id, "Ой, не то")
    if rand == 3:
        bot.send_sticker(message.chat.id, "CAACAgUAAxkBAALXs2AryGKuMiDH3fFuh0YUVcHtpGyTAAKSAANxffwU7BFGF0nhZEYeBA")
    if rand == 4:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAALXtmAryHZ7ZKt5D-Hyo_mkhgMBJrMzAAIgAAP-D1IdgwMoLdXKfIkeBA")
    if rand == 5:
        bot.send_sticker(message.chat.id, "CAACAgEAAxkBAALXuWAryJzlpDnonZy4FVRxxfsTaoQmAAKqDwACmX-IArdolco1Ckz9HgQ")
    
@bot.message_handler(content_types=['text'])
def mess(message):
    randtext = random.randint(0, 3)
    if randtext == 0:
        bot.send_message(message.chat.id, "Отличный денёк!")
    if randtext == 1:
        bot.send_message(message.chat.id, "Как жизнь?")
    if randtext == 2:
        bot.send_message(message.chat.id, "Здравствуй!")


bot.polling(none_stop=True)