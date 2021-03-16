import telebot
import random

TOKEN = '1671666913:AAFQhsx4fDlwLGrltwBnZps3Z2k7XH1HG4A'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "{0.first_name}, Поставьте 5)".format(message.from_user, bot.get_me()))

@bot.message_handler(commands=['random'])
def welcome(message):
    ranNum = random.randint(0,1000)
    bot.send_message(message.chat.id, str(int(ranNum)))

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
    randtext = random.randint(0, 10)
    if randtext == 0:
        bot.send_message(message.chat.id, "Ага, пиши дальше")
    if randtext == 1:
        bot.send_message(message.chat.id, "Мне все равно")
    if randtext == 2:
        bot.send_message(message.chat.id, "Я тебя не слушаю")
    if randtext == 3:
        bot.send_message(message.chat.id, "Лучше бы котов попросил")
    if randtext == 4:
        bot.send_message(message.chat.id, "ЧС")
    if randtext == 5:
        bot.send_message(message.chat.id, "Хватит")
    if randtext == 6:
        bot.send_message(message.chat.id, "Я занят")
    if randtext == 7:
        bot.send_message(message.chat.id, "Иди погуляй")
    if randtext == 8:
        bot.send_message(message.chat.id, "Оаоаоа ммм")
    if randtext == 9:
        bot.send_message(message.chat.id, "Ну сколько можно")
    if randtext == 10:
        bot.send_message(message.chat.id, "Я спать")
    

bot.polling(none_stop=True)
