import logging
import os
import sys
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class VPNBot:
    """Minimal Telegram bot that loads token from .env and supports /start."""

    def __init__(self):
        load_dotenv()
        self.token = os.getenv('BOT_TOKEN') or os.getenv('TOKEN')
        if not self.token:
            logger.error('Bot token not found. Set BOT_TOKEN in .env or environment variables.')
            sys.exit(1)

        self.app = Application.builder().token(self.token).build()
        self.app.add_handler(CommandHandler('start', self.start))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        name = user.first_name or user.username or str(user.id)
        await update.message.reply_text(f'Hi, {name}! This bot is minimal.')

    async def echo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        name = user.first_name or user.username or str(user.id)
        text = update.message.text
        await update.message.reply_text(f"{name} сказал: {text}")

    def run(self):
        self.app.run_polling()


def main():
    bot = VPNBot()
    bot.run()


if __name__ == '__main__':
    main()