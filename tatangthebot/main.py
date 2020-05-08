import telebot
from telebot import types

bot = telebot.TeleBot("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user = str(message.from_user.id)
    bot.reply_to(message, "Howdy, how are you doing? You talk with user {} and his user ID: {} ".format(
        user, user))


@bot.message_handler(commands=['number'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(
        text="Share Contact to Tatang", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(
        message.chat.id, 'Would you mind sharing your contact with me?', reply_markup=keyboard)


@bot.message_handler(content_types=['contact'])
def contact(message):
    bot.reply_to(message, "Ini nomor kamu ya {} dan id_user {}".format(
        message.contact.phone_number, message.contact.user_id))


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

bot.polling()