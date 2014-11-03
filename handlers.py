import random

from groupme_api import post_message


def magic_8_ball(name, uid, text):
    bot_uid = u'173723'

    if bot_uid != uid:
        responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",

            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",

            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

        post_message("{name}: The Magic 8 Ball says... {response}".format(
            name=name, response=random.choice(responses).upper()))