from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
import requests
import re


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Sebelum make saya kamu perlu konfigurasi dulu secara personal ke @tatangthebot dulu!")


def config(update, context):
    type_chat = str(update.message.chat.type).lower()
    if type_chat == "private":
        yes = KeyboardButton(
            text="Iya", request_contact=True)
        no = KeyboardButton(
            text="Tidak", request_contact=False)
        keyboard = ReplyKeyboardMarkup([[yes, no]], resize_keyboard=True)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='Yakin mau daftar nih?', reply_markup=keyboard)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Harus chat personal bosque kalo mau pake ini!")


def phone(update, context):
    number = update.message.contact.phone_number
    user_id = update.message.contact.user_id

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="No HP : {}, ID User : {}".format(number, user_id))

    print(update.message)


def main():
    updater = Updater(
        'TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('config', config))
    dp.add_handler(MessageHandler(Filters.contact, phone))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
