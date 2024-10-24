import asyncio
from bot import app

from handlers.schedule import handle_schedule
from handlers.webhook import handle_webhook

def lambda_handler(event, context):
    match event:
        case {'httpMethod': "POST", 'path': '/webhook'}:
            return asyncio.get_event_loop().run_until_complete(handle_webhook(event))
        case {'source': 'aws.schedule'}:
            return asyncio.get_event_loop().run_until_complete(handle_schedule(event))



