import socket
import telebot

telegram_key = "xxx"                          #enter tocken of telegram bot
bot = telebot.TeleBot(telegram_key)
socket_ip_addres = "255.255.255.255"          #enter ip addres of server
socket_port = 8080                            #enter port of server
sock = socket.socket()
sock.bind((socket_ip_addres, socket_port))
sock.listen()
conn, addr = sock.accept()

@bot.message_handler(content_types=['text'])
def get_message(message):
    mgs = message.text
    data = mgs + '\n'
    conn.send(data.encode())
    bot.send_message(message.chat.id, "led is " + mgs)

bot.polling(none_stop=True)