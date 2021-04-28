import socket
import telebot

telegram_key = "xxx"                                      #enter token of telegram bot
bot = telebot.TeleBot(telegram_key)
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('/off', '/on')
socket_ip_addres = "255.255.255.255"                      #enter ip addres of server
socket_port = 8080                                        #enter port of server
sock = socket.socket()
sock.bind((socket_ip_addres, socket_port))
sock.listen()
conn, addr = sock.accept()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте " + str(message.chat.username) + " !\nВас приветсвует телеграм бот созданый творцом two-dimensional-array\n", reply_markup=keyboard)

@bot.message_handler(commands=['on'])
def on_led(message):
    conn.send("on\n".encode())
    bot.send_message(message.chat.id, "Светодиод включен", reply_markup=keyboard)

@bot.message_handler(commands=['off'])
def off_led(message):
    conn.send("off\n".encode())
    bot.send_message(message.chat.id, "Светодиод выключен", reply_markup=keyboard)

bot.polling(none_stop=True)
