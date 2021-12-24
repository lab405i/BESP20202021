import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to PLCInformer Bot.")


@bot.message_handler(commands=['info', 'IO'])
def get_IO_info(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text = "Yes", callback_data = "yes")
	item_no = types.InlineKeyboardButton(text = "No", callback_data = "no")

	markup_inline.add(item_yes, item_no)
	bot.send_message(message.chat.id, "Do you want to know about IO status?", reply_markup = markup_inline )


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
	if call.data == "yes":
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)

		item_inputs = types.KeyboardButton("Inputs")
		item_outputs = types.KeyboardButton("Outputs")

		markup_reply.add(item_inputs, item_outputs)
		bot.send_message(call.message.chat.id, "Choose what you want", reply_markup = markup_reply )

	elif call.data == "no":
		pass


@bot.message_handler(content_types = ["text"])
def get_text(message):
	if message.text == "Inputs":

            with sqlite3.connect("db/database.db") as db:
                cursor = db.cursor()
                query11 = """ SELECT * FROM inputs """

                cursor.execute(query11)
                for res11 in cursor:
                    pass

                    bot.send_message (message.chat.id, f" Inputs : {res11}")

	elif message.text == "Outputs":

            with sqlite3.connect("db/database.db") as db:
                cursor = db.cursor()
                query21 = """ SELECT * FROM outputs """

                cursor.execute(query21)
                for res21 in cursor:
                    pass

                    bot.send_message (message.chat.id, f" Outputs : {res21}")


#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
	#bot.reply_to(message, message.text)


bot.polling()
