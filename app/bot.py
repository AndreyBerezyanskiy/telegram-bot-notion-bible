import json

from telegram.ext import Application, CommandHandler
from telegram import Update

from config import telegram_token_ssm
from handlers.telegram import start, add_task

# init App
app = Application.builder().token(telegram_token_ssm).build()

# Add command handlers to the application
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add_task))

async def process_telegram_update(event):
    # Create the update object
    update = Update.de_json(data=json.loads(event['body']), bot=app.bot)

    await app.initialize()
    await app.process_update(update=update)
    await app.shutdown()