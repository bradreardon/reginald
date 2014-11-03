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


def upload_image(image):
    endpoint = 'https://image.groupme.com/pictures'
    access_token = os.environ.get('ACCESS_TOKEN')

    payload = {
        'access_token': access_token,
    }

    files = {
        'file': image
    }

    headers = {
        'Content-Type': 'application/json',
    }

    r = requests.post(endpoint, data=json.dumps(payload), files=files, headers=headers)
    print r.json()
    return r.json()['payload']['url']


def post_image(url, text=''):
    post_message(attachments=[
        {
            'type': 'image',
            'url': '{}.large'.format(url),
        }
    ])