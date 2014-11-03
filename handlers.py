import random

import requests

from groupme_api import post_message, upload_image
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
    bot_uid = u'173723'

    if bot_uid != uid:
        ALLOWED_EXTENSIONS = ('.jpg', '.gif')
        headers = {'User-Agent': 'Sir Reginald, courtesy of /r/PixelEater'}
        r = requests.get("http://www.reddit.com/r/smashing/hot.json", headers=headers)
        posts = r.json()['data']['children']

        def get_link(posts):
            post = random.choice(posts)
            url = post['data']['url']
            if url.endswith(ALLOWED_EXTENSIONS):
                return url
            else:
                return get_link(posts)

        url = get_link(posts)
        image = requests.get(url)
        image_url = upload_image(image.content)
        post_message('SMASHING INDEED', picture_url=image_url)