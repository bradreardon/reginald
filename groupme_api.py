import json
import os
import requests


def post_message(text, attachments=[]):
    endpoint = 'https://api.groupme.com/v3/bots/post'
    bot_id = os.environ.get('BOT_ID')

    payload = {
        'bot_id': bot_id,
        'text': text,
        'attachments': attachments,
    }

    headers = {
        'Content-Type': 'application/json',
    }

    requests.post(endpoint, data=json.dumps(payload), headers=headers)