import json
from bot import app
from dynamo_helper import get_all_chat_ids

async def send_message(chat_id, message):
    await app.bot.send_message(chat_id=chat_id, text=message)

def handle_schedule(event):
    all_chat_ids = get_all_chat_ids()

    if not all_chat_ids:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "There is no chat ids"})
        }

    for chat_id in all_chat_ids:
        send_message(chat_id, "Hello world")
