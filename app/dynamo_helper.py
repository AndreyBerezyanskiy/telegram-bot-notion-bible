# dynamo_helper.py
from loggger import log
import boto3
import os
from botocore.exceptions import ClientError

TABLE_NAME = os.getenv('TABLE_NAME')
REGION_NAME = os.getenv('REGION_NAME')

# Initialize DynamoDB resource
dynamo = boto3.resource('dynamodb', region_name=REGION_NAME)
table = dynamo.Table(TABLE_NAME)

def add_chat_id(chat_id: str):
    table = dynamo.Table(TABLE_NAME)

    try:
        table.put_item(
            Item={
                'chat_id': chat_id
            },
            ConditionExpression='attribute_not_exists(chat_id)'
        )

        log(log.INFO,f"Chat_id:{chat_id} was added")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            log(log.INFO, f"Chat_id: {chat_id} already exist")
        else:
            log(log.INFO, "something went wrong, error:", e)

def get_all_chat_ids():
    """Retrieve all chat_ids from the DynamoDB table"""
    try:
        response = table.scan()
        chat_ids = [item['chat_id'] for item in response['Items']]
        return chat_ids
    except ClientError as e:
        log(log.INFO, f"Error retrieving chat_ids from DynamoDB: {e}")
        return []