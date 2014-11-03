import functools
import json
import re
import os

from flask import Flask, request

import handlers

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Reginald, at your service.'


@app.route('/callback', methods=['POST'])
def callback():
    owner_id = '22722313'
    data = json.loads(request.data)

    name, uid, text = data['name'], data['user_id'], data['text']
    process_message(name, uid, text)


def process_message(name, uid, text):
    regex = functools.partial(re.compile, flags=re.IGNORECASE + re.UNICODE)
    processors = {
        regex('magic (8|eight) ball'): handlers.magic_8_ball,
        regex('/cool guy$'): handlers.cool_guy,
    }

    for pattern, process_func in processors.iteritems():
        if pattern.search(text):
            return process_func(name, uid, text)  # Match on first occurrence


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
