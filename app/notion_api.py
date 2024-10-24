import os
import requests
from config import notion_db_id_ssm, notion_token_ssm
from loggger import log


def create_notion_task(task_description, task_verse):
    """Function to create new task in database"""
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {notion_token_ssm}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"database_id": notion_db_id_ssm},
        "properties": {
            "Question": {
                "title": [
                    {
                        "text": {
                            "content": task_description
                        }
                    }
                ]
            },
        }
    }

    # Додаємо колонку Verse лише якщо task_verse не None
    if task_verse:
        data["properties"]["Verse"] = {
            "rich_text": [
                {
                    "text": {
                        "content": task_verse
                    }
                }
            ]
        }


    response = requests.post(url, headers=headers, json=data)

    log(log.INFO, "response====", response.text)

    if response.status_code == 200:
        return True
    else:
        return False
