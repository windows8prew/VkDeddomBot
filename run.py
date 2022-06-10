import os
from dotenv import load_dotenv

import vk_api
from vk_api.longpoll import VkLongPoll

from bot.utils import handlers_list
import bot.handlers

load_dotenv()

APPID = int(os.getenv('APPID') or 6287487)
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
TOKEN = os.getenv('TOKEN')
CAPTCHA_TOKEN = os.getenv('CAPTCHA_TOKEN')


def main():
    vk_session = vk_api.VkApi(
        login=LOGIN,
        password=PASSWORD,
        token=TOKEN,
        app_id=APPID,
    )

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    long_poll = VkLongPoll(vk_session)

    for event in long_poll.listen():
        for handler in handlers_list:
            handler(event)


if __name__ == '__main__':
    main()
