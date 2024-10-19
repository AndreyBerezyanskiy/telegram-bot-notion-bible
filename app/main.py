from bot import app

from handlers.schedule import handle_schedule
from handlers.webhook import handle_webhook

def lambda_handler(event, context):
    match event:
        case {'httpMethod': "POST", 'path': '/webhook'}:
            return handle_webhook(event)
        case {'source': 'aws.events'}:
            return handle_schedule(event)



