import json
from bot import app
from dynamo_helper import get_all_chat_ids

from loggger import log

async def send_message(chat_id, message):
    await app.bot.send_message(chat_id=chat_id, text=message)

async def handle_schedule(event):
    all_chat_ids = await get_all_chat_ids()

    if not all_chat_ids:
        log(log.WARNING, "No chat ids")
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "There is no chat ids"})
        }



    for chat_id in all_chat_ids:
        log(log.INFO, "Send message to chat_id: [%s]", chat_id)
        await send_message(chat_id, "Hello world")
        log(log.INFO, "Message to chat_id: [%s] was sent", chat_id)
