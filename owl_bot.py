#!/usr/bin/env python
import json
import os
from random import choice

import requests
import telebot


def load_config(filename):
    """ Возвращает словарь с настройками

    Настройки прокси, файл с текстом приветствия, директория для
    сохранения временных файлов)
    """
    with open(filename, encoding='utf-8') as data:
        config = json.load(data)

    config['token'] = os.environ['TGBOT_TOKEN']
    config['proxy'] = dict(https=config['proxy']) if config['proxy'] else None
    return config


# загрузка конфигурации и прокси (если указаны)
config = load_config('config.json')
telebot.apihelper.proxy = config['proxy']

bot = telebot.TeleBot(config['token'])


@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
    """ Возвращает пользователю отправленный им стикер в виде фото """
    sticker_info = bot.get_file(message.sticker.file_id)
    path, emoji = sticker_info.file_path, message.sticker.emoji

    # сформировать ссылку для скачивания
    link = config['download_link'] + 'bot{}/{}'.format(config['token'], path)

    response = requests.get(link, proxies=config['proxy'])
    if not os.path.exists(config['temp_dir']):
        os.mkdir(config['temp_dir'])

    # сохранить стикер
    filename = '{}/{}'.format(config['temp_dir'], 'sticker.png')
    with open(filename, 'wb') as photo:
        photo.write(response.content)

    # отправить стикер
    with open(filename, 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=emoji)


@bot.message_handler(regexp=r'подтвер[ж]?д[аи]+[е]?(?:шь)?')
def confirm_smth(message):
    """ Отправляет пользователю сообщение, если пользователь попросил
    что-либо подтвердить """
    reply = choice(config['bot_replies'])
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    """ Приветственное сообщение """
    with open(config['start_msg_file'], encoding='utf-8') as f:
        welcome_msg = f.read()
    bot.send_message(message.chat.id, welcome_msg)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, config['help_msg'])


@bot.message_handler(func=lambda m: True)
def other_messages(message):
    bot.reply_to(message, config['help_msg'])


bot.polling()
