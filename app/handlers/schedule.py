import asyncio
import json
from dynamo_helper import get_all_chat_ids

async def send_message(chat_id, message):
    # await app.bot.send_message(chat_id=chat_id, text=message)


def handle_schedule(event):
    all_chat_ids = get_all_chat_ids()
    message = "Час читати Біблію"

    if not all_chat_ids:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "There is no chat ids"})
        }

    for chat_id in all_chat_ids:
        print('chat_ids', all_chat_ids)
        print('chat_id', chat_id)

        if type(chat_id) is not int:
            print("chat_id is not int: [%s]", chat_id)

        # asyncio.run(send_message(chat_id, message))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": f"Message was sent to chat id: {chat_id}"})
    }