import json
import asyncio

from app.main import main, process_telegram_update
from dynamo_helper import add_chat_id

async def handle_webhook(event):
    # Add chat id to DynamoDb
    body = json.loads(event['body'])
    chat_id = body['message']['chat']['id']

    if chat_id:
        add_chat_id(chat_id)

    # update telegram
    # asyncio.run(process_telegram_update(event))
    await main(event)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Webhook received"}),
    }