import datetime
import logging
import sys
from telegram import Update
from telegram.ext import CallbackContext

from telegram_bot.tg_client import config
from telegram_bot.utils import get_link

logger = logging.getLogger(__name__)
chat_id = config["CHAT_ID"]
logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


def post(context: CallbackContext):

    get_update = get_link()
    link = next(get_update)
    message = f"""[*Подробнее*]({link})"""
    context.bot.send_message(chat_id=chat_id,
                             text=message,
                             parse_mode='MarkdownV2')


def start(update: Update, context: CallbackContext) -> None:
    """Start sending news in chat."""
    chat_id = update.message.chat_id
    context.job_queue.run_repeating(post, interval=datetime.timedelta(minutes=2), context=chat_id, name=str(chat_id))
    update.message.reply_text(f'JOB SUCCESSFULLY STARTED AT {datetime.datetime.now()}')















