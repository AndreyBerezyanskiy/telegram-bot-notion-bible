import json
import os
import asyncio

import boto3
from botocore.exceptions import ClientError

from telegram import Update
from telegram.ext import Application, CommandHandler

from config import telegram_token_ssm
from dynamo_helper import add_chat_id, get_all_chat_ids
from bot_handlers import start, add_task

application = Application.builder().token(telegram_token_ssm).build()

# Add command handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("add", add_task))

async def process_telegram_update(event):
    # Create the update object
    update = Update.de_json(data=json.loads(event['body']), bot=application.bot)

    await application.initialize()
    await application.process_update(update=update)
    await application.shutdown()

def lambda_handler(event, context):
    # Run the asynchronous function using asyncio.run()
    body = json.loads(event['body'])

    # Add chat id to DynamoDb
    chat_id = body['message']['chat']['id']

    if chat_id:
        add_chat_id(chat_id)

    # Get chatIds
    print("--chat_ids------",get_all_chat_ids())

    asyncio.run(process_telegram_update(event))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Webhook received"}),
    }
