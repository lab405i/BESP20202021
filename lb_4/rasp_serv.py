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

class _state:
    def __init__(self):
        self.state = "off"
    def set_state(self, state):
        self.state = state
    def not_equal(self, state):
        return self.state != state
    def equal(self, state):
        return self.state == state

state_led = _state()
help_msg = "Команды:\n/on - Включение светодиода на плате. \n/off - Выключение светодиода на плате.\n/help - Вывод справки по командам бота"

def led_request(state):
    if (state_led.not_equal(state)):
        conn.send(state + '\n'.encode())
        state_led.set_state(state)
    else:
        pass

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте " + str(message.chat.username) + " !\nВас приветсвует телеграм бот созданый творцом two-dimensional-array\nДля отображения списка комманд введите /help", reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, help_msg, reply_markup=keyboard)

@bot.message_handler(commands=['on'])
def on_led(message):
    led_request("on")
    bot.send_message(message.chat.id, "Светодиод включен", reply_markup=keyboard)

@bot.message_handler(commands=['off'])
def off_led(message):
    led_request("off")
    bot.send_message(message.chat.id, "Светодиод выключен", reply_markup=keyboard)

bot.polling(none_stop=True)
