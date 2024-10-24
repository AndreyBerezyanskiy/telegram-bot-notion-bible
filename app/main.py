import json
from logging import log

from aiogram import Bot, Dispatcher, types

from config import telegram_token_ssm
from handlers.telegram import start, add_task

# init App
# app = Application.builder().token(telegram_token_ssm).build()

# bot = Bot(token=telegram_token_ssm)

# # Add command handlers to the application
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("add", add_task))

# async def process_telegram_update(event):
#     # Create the update object
#     update = Update.de_json(data=json.loads(event['body']), bot=app.bot)

#     await app.initialize()
#     await app.process_update(update=update)
#     await app.shutdown()

# AWS Lambda funcs
async def register_handlers(dp: Dispatcher):
    """Registration all handlers before processing update."""

    dp.register_message_handler(start, commands=['start'])
    # dp.register_message_handler(echo)

    log('Handlers are registered.')


async def process_event(event, dp: Dispatcher):
    """
    Converting an AWS Lambda event to an update and handling that
    update.
    """

    log('Update: ' + str(event))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(event)
    await dp.process_update(update)

async def main(event):
    """
    Asynchronous wrapper for initializing the bot and dispatcher,
    and launching subsequent functions.
    """

    # Bot and dispatcher initialization
    bot = Bot(telegram_token_ssm)
    dp = Dispatcher(bot)

    await register_handlers(dp)
    await process_event(event, dp)

    return 'ok'

