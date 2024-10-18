#!/bin/bash

# get variables from .env
export $(grep -v '^#' .env | xargs)

# set keys to AWS Parametr Store
aws ssm put-parameter --name "/$APP_NAME/TELEGRAM_TOKEN" --value "$TELEGRAM_TOKEN" --type SecureString --profile andrii
aws ssm put-parameter --name "/$APP_NAME/NOTION_TOKEN" --value "$NOTION_TOKEN" --type SecureString --profile andrii
aws ssm put-parameter --name "/$APP_NAME/NOTION_DATABASE_ID" --value "$NOTION_DATABASE_ID" --type SecureString --profile andrii

echo "Set key to AWS Store"
