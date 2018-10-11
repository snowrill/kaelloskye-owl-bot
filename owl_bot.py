#!/usr/bin/env python
import os
import json
import telebot
from random import choice


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
    bot.send_message(message.chat.id, 'Вы прислали стикер!')


@bot.message_handler(regexp=r'подтвер[ж]?д[аи]+[е]?(?:шь)?')
def confirm_smth(message):
    """ Отправляет пользователю сообщение, если пользователь попросил
    что-либо подтвердить """
    reply = choice(config['bot_replies'])
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['start'])
def send_welcome_msg(message):
    """ Приветственное сообщение """
    with open(config['start_msg_file'], encoding='utf-8') as f:
        welcome_msg = f.read()
    bot.send_message(message.chat.id, welcome_msg)


bot.polling()
