import json
import os
import asyncio

import boto3
from botocore.exceptions import ClientError

from telegram import Update
from telegram.ext import Application, CommandHandler

from bot_handlers import start, add_task

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# REGION_NAME = os.getenv['REGION_NAME']
TABLE_NAME = os.getenv('TABLE_NAME')

application = Application.builder().token(TELEGRAM_TOKEN).build()

dynamo = boto3.resource('dynamodb')

# Add command handlers to the application
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("add", add_task))

async def add_chat_id(chat_id: str):
    table = dynamo.Table(TABLE_NAME)

    try:
        table.put_item(
            Item={
                'chat_id': chat_id
            },
            ConditionExpression='attribute_not_exists(chat_id)'
        )

        print(f"Chat_id:{chat_id} was added")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            print(f"Chat_id: {chat_id} already exist")
        else:
            print("something went wrong, error:", e)


async def process_telegram_update(event):
    # Create the update object
    update = Update.de_json(data=json.loads(event['body']), bot=application.bot)

    body = json.loads(event['body'])

    chat_id = body['message']['chat']['id']

    # Add chat id to DynamoDb
    await add_chat_id(chat_id)

    await application.initialize()
    await application.process_update(update=update)
    await application.shutdown()

def lambda_handler(event, context):
    # Run the asynchronous function using asyncio.run()

    asyncio.run(process_telegram_update(event))

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Webhook received"}),
    }
