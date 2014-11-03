import json
import os
import requests


def post_message(text, picture_url=None):
    endpoint = 'https://api.groupme.com/v3/bots/post'
    bot_id = os.environ.get('BOT_ID')

    payload = {
        'bot_id': bot_id,
        'text': text,
        'picture_url': picture_url
    }

    headers = {
        'Content-Type': 'application/json',
    }

    requests.post(endpoint, data=json.dumps(payload), headers=headers)


def upload_image(image):
    endpoint = 'https://image.groupme.com/pictures?access_token={}'
    access_token = os.environ.get('ACCESS_TOKEN')

    files = {
        'file': image
    }

    r = requests.post(endpoint.format(access_token), files=files)
    return r.json()['payload']['url']