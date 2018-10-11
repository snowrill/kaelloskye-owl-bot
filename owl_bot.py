#!/usr/bin/env python

import telebot
from random import choice

# токен и прокси для запуска на локальной машине
TGBOT_TOKEN = '695541521:AAGv5DL2dt4GYuaD1qU2JKVdNMJ9nCtBT8E'
TGBOT_PROXY = 'socks5://tg-kaelloskye:VACey4bI@ru.socksy.seriyps.ru:7777'

# если прокси указан - использовать
if TGBOT_PROXY:
    telebot.apihelper.proxy = dict(https=TGBOT_PROXY)

bot = telebot.TeleBot(TGBOT_TOKEN)


@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
    bot.send_message(message.chat.id, 'Вы прислали стикер!')


@bot.message_handler(regexp=r'подтвер[ж]?д[аи]+[е]?(?:шь)?')
def confirm_smth(message):
    words = ['Подтверждаю', 'Угу']
    bot.send_message(message.chat.id, choice(words))


@bot.message_handler(commands=['start'])
def send_welcome_msg(message):
    with open('joke.txt', encoding='utf-8') as f:
        welcome_msg = f.read()
    bot.send_message(message.chat.id, welcome_msg)


bot.polling()
