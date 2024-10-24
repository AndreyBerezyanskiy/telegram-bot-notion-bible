import asyncio
from bot import app
from loggger import log

from handlers.schedule import handle_schedule
from handlers.webhook import handle_webhook

def lambda_handler(event, context):
    match event:
        case {'httpMethod': "POST", 'path': '/webhook'}:
            log(log.INFO, "Event from webhook: [%s]", event)
            return asyncio.get_event_loop().run_until_complete(handle_webhook(event))
        case {'source': 'aws.schedule'}:
            log(log.INFO, "Event from schedule: [%s]", event)
            return asyncio.get_event_loop().run_until_complete(handle_schedule(event))
        case _:
            log(log.WARNING, "Unhandled event: [%s]", event)



