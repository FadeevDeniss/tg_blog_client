from typing import Callable, Any

import requests
from bs4 import BeautifulSoup

from telegram import Update
from telegram.ext import Dispatcher, CallbackContext


class TelegramBotMeta(type):
    def __new__(mcs, name, bases, dct):
        cls = type.__new__(mcs, name, bases, dct)
        dispatcher: Dispatcher = dct['dispatcher']
        for handler in getattr(cls, 'HANDLERS'):
            dispatcher.add_handler(handler)
        return cls


def clear_command_message(func: Callable) -> Callable:
    def wrapper(update: Update, context: CallbackContext):
        message_id: int = update.message.message_id
        chat_id: int = update.message.chat_id
        res: Any = func(update, context)
        context.bot.deleteMessage(chat_id=chat_id, message_id=message_id)
        return res
    return wrapper


def get_link():
    content = requests.get('https://vc.ru/new')
    html = content.content
    parser = BeautifulSoup(html, 'html.parser')
    for link in parser.find('body').parent.find_all('a', class_='content-link'):
        yield link['href']



