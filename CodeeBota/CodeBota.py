import telebot

token = '1517233098:AAGQgq1X3WdaQ58WYj35IZVrugs1E2xlcuQ'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def qwe_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Привет,я бот Фредерико, который должен научиться показывать время")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Спроси меня сколько времени?")
    else:
        bot.send_message(message.from_user.id, "У меня есть только часы, большего я не могу. Могу подсказать тебе время")

bot.polling(none_stop=True)
