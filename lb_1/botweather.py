import telebot
import pyowm

telegram_key = "1674358018:AAGL0D1AUwKhjAE4Fu_CumHVfL-G5lT_8nM"
weather_key = "435bbedf7b7efd8558701840fe9ad312"

bot = telebot.TeleBot(telegram_key)
owm = pyowm.OWM(weather_key)
mgr = owm.weather_manager()
user_id = []
place_list = []
help_msg = "Hey!!!\nКоманды:\n/place - Ввод названия города. \n/update - Обновление информации об погоде в текущем городе \n/current_place - Вывод текущего города. \n/help - Вывод справки по командам бота"

keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard.row('/place', '/update','/current_place','/help')

@bot.message_handler(commands=['start'])
def start_message(message):
    set_user(message.chat.id)
    bot.send_message(message.chat.id, help_msg,reply_markup=keyboard)

@bot.message_handler(commands=['place'])
def get_message(message):
    bot.send_message(message.chat.id, "Введите название вашего города:")
    bot.register_next_step_handler(message, ask_place)

@bot.message_handler(commands=['update'])
def update(message):
    index = find_user(message.chat.id)
    place = place_list[index]
    if place == None or len(place) > 20:
        place = "Город не найден"
    try:
        mgr.weather_at_place(place)
    except pyowm.commons.exceptions.APIRequestError:
        bot.send_message(message.chat.id, "Не верно введён город!\nВведите название вашего города:")
        bot.register_next_step_handler_by_chat_id(message.chat.id, ask_place)
        return
    except pyowm.commons.exceptions.NotFoundError:
        bot.send_message(message.chat.id, "Не верно введён город!\nВведите название вашего города:")
        bot.register_next_step_handler_by_chat_id(message.chat.id, ask_place)
        return
    bot.send_message(message.chat.id, output_data(place),reply_markup=keyboard)

def ask_place(message):
    place = message.text
    if place == None or len(place) > 20:
        place = "Город не найден"
    try:
        mgr.weather_at_place(place)
    except pyowm.commons.exceptions.APIRequestError:
        bot.send_message(message.chat.id, "Не верно введён город!\nВведите название вашего города:")
        bot.register_next_step_handler_by_chat_id(message.chat.id, ask_place)
        return
    except pyowm.commons.exceptions.NotFoundError:
        bot.send_message(message.chat.id, "Не верно введён город!\nВведите название вашего города:")
        bot.register_next_step_handler_by_chat_id(message.chat.id, ask_place)
        return
    index = find_user(message.chat.id)
    place_list.insert(index, place)
    bot.send_message(message.chat.id, output_data(place),reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, help_msg,reply_markup=keyboard)

@bot.message_handler(commands=['current_place'])
def current_place(message):
    index = find_user(message.chat.id)
    place = place_list[index]
    bot.send_message(message.chat.id, place,reply_markup=keyboard)

def set_user(user_name):
    user_id.append(user_name)
    place_list.append("Город не задан")

def find_user(user_name):
    try:
        user_id.index(user_name)
    except ValueError:
        set_user(user_name)
    index = user_id.index(user_name)
    return index
    
def output_data(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    answear = "В городе " + place + " " + str(w.detailed_status) + "\n"
    answear += "Температура воздуха составляет " + str(w.temperature('celsius')["temp"]) + " °C\n"
    answear += "Влажность воздуха равняется " + str(w.humidity) + "%\n"
    answear += "Скорость ветра состовляет " + str(w.wind()["speed"]) + " м/с\n"
    answear += "Облачность равняется " + str(w.clouds) + "% \n"
    answear += "Восход солнца: " + str(w.sunrise_time(timeformat='iso')) + "\n"
    answear += "Заход солнца: " + str(w.sunset_time(timeformat='iso')) + "\n"
    return answear

bot.polling(none_stop=True)