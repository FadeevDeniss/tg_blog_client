import logging
import sys

from telegram_bot.tg_client import TgBlogBot

logger = logging.getLogger(__name__)

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

if __name__ == "__main__":
    TgBlogBot.run()
