import telebot
from genbot import gen_pass
from telebot import types
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7652257258:AAFpqRaIc_HCBcOtsHdXDyGDrfzef38DD8Q")
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def getpassword(message):
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['how old are you?'])
def send_how(message):
    bot.reply_to(message, 'Мне 1 неделя')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands = ['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Кнопка')
    item2 = types.KeyboardButton('что')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup = markup)

@bot.message_handler(content_types = 'text')
def message_reply(message):
    if message.text == 'Кнопка':
        bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=NmCCQxVBfyM')
    elif message.text == 'что':
        bot.send_message(message.chat.id,'https://pytba.readthedocs.io/ru/latest/types.html')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
print('Бот запущен')
bot.polling()