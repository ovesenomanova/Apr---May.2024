import telebot
from telebot.types import Message
from tokens import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message: Message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_0 = telebot.types.KeyboardButton(text='/Получить расчет')
    button_1 = telebot.types.KeyboardButton(text='/Посмотреть каталог')
    keyboard.add(button_0, button_1)
    user_id = message.from_user.id
    bot.send_message(user_id, "Привет!", reply_markup=keyboard)

# @bot.message_handler(commands=['double'])
# def double(message: Message):
#     text = message.text.split()
#     user_id = message.from_user.id
#     bot.send_message(user_id, str(int(text[-1])*2))


@bot.message_handler(commands=['Посмотреть'])
def catalog(message: Message):
    user_id = message.from_user.id
    bot.send_photo(user_id, "https://тортбери.рф/wa-data/public/shop/products/72/00/72/images/830/830.970.PNG")

@bot.message_handler(commands=['Получить'])
def count(message: Message):
    user_id = message.from_user.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(user_id, "Привет!", reply_markup=keyboard)

# @bot.message_handler()
# def read_message(message: Message):
#     user_id = message.from_user.id
#     bot.send_message(user_id, message.text)

bot.infinity_polling()
