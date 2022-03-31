import logging
import sys

from dotenv import dotenv_values
from telegram import Bot
from telegram.ext import Updater, Dispatcher, CommandHandler

from telegram_bot.commands import start
from telegram_bot.utils import TelegramBotMeta


config = dotenv_values("/home/dfadeev/PycharmProjects/tg_blog_client/.env")
token = config["TELEGRAM_TOKEN"]


logger = logging.getLogger(__name__)

logging.basicConfig(
				stream=sys.stdout,
				format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
				level=logging.DEBUG
)

updater: Updater = Updater(token=token, use_context=True)
dispatcher: Updater = updater.dispatcher
bot: Bot = updater.bot


class TgBlogBot(metaclass=TelegramBotMeta):
				HANDLERS = (
								CommandHandler("start", start),
				)
				updater: Updater = updater
				dispatcher: Dispatcher = dispatcher
				bot: Bot = bot

				@classmethod
				def run(cls):
								cls.updater.start_polling()
								cls.updater.idle()
