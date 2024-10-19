import boto3
import os

REGION_NAME = os.getenv('REGION_NAME')

ssm = boto3.client('ssm', region_name=REGION_NAME)

# get keys from Parameter Store
telegram_token_ssm = ssm.get_parameters(Names=["/telegram-notion-bible/TELEGRAM_TOKEN"], WithDecryption=True)['Parameters'][0]['Value']
notion_token_ssm = ssm.get_parameters(Names=["/telegram-notion-bible/NOTION_TOKEN"], WithDecryption=True)['Parameters'][0]['Value']
notion_db_id_ssm = ssm.get_parameters(Names=["/telegram-notion-bible/NOTION_DATABASE_ID"], WithDecryption=True)['Parameters'][0]['Value']
