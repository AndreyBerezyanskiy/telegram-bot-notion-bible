import os
import requests

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

def create_notion_task(task_description, task_verse):
    """Function to create new task in database"""
    url = "https://api.notion.com/v1/pages"

    print("token", NOTION_TOKEN)
    print("base", NOTION_DATABASE_ID)
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
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

    print("response====", response.text)

    if response.status_code == 200:
        return True
    else:
        return False
