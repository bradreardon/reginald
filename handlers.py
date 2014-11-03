import random

import requests

from groupme_api import post_message, post_image, upload_image
from defines import MAGIC_8_BALL_RESPONSES, COOL_GUY_RESPONSES


def magic_8_ball(name, uid, text):
    bot_uid = u'173723'

    if bot_uid != uid:
        if 'spoken' not in text:
            post_message("{name}: The Magic 8 Ball says... {response}".format(
                name=name, response=random.choice(MAGIC_8_BALL_RESPONSES).upper()))


def cool_guy(name, uid, text):
    post_message(random.choice(COOL_GUY_RESPONSES))


def nigel_thornberry(name, uid, text):
    r = requests.get("http://www.reddit.com/r/smashing/hot.json")
    posts = r.json()['data']['children']
    post = random.choice(posts)
    url = post['data']['url']

    image = requests.get(url)
    image_url = upload_image(image.content)
    post_image(image_url)