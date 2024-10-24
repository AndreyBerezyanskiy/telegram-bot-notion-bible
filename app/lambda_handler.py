import asyncio

# from handlers.schedule import handle_schedule
# from handlers.webhook import handle_webhook
from app.logger import log


def lambda_handler(event, context):
    """AWS Lambda handler."""

    match event:
        case {'httpMethod': "POST", 'path': '/webhook'}:
            log("trigger from Webhook:[%s]", event)
            # return asyncio.get_event_loop().run_until_complete(handle_webhook(event))
        case {'source': 'aws.scheduler'}:
            log("unHandled event:[%s]", event)
            # return asyncio.get_event_loop().run_until_complete(handle_schedule(event))
        case _:
            log(log.WARNING, "trigger from Scheduler:[%s]", event)




