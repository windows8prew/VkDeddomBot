import time

from bot.utils import event_handler_wrapper, get_time_from_message
from vk_api.longpoll import VkEventType
import random

mutes = {}

@event_handler_wrapper()
def mute_handler(client, event):
    if event.from_chat and event.chat_id == 106 and hasattr(event, 'user_id') and mutes.get(event.user_id, 0) >= time.time():
        client.messages.delete(peer_id=2000000106, message_ids=event.message_id, delete_for_all=True)

@event_handler_wrapper()
def handler(client, event):
    if event.type == VkEventType.MESSAGE_NEW and event.from_chat and event.chat_id == 106:
        message_text_split = event.text.split()
        random_id = random.randint(0, 2147483647)
        print(dict((name, getattr(event, name)) for name in dir(event) if not name.startswith('__')))
        if len(message_text_split) == 2 and message_text_split[0].lower() == '/мут':
            if 'mentions' in event.extra_values:
                mute_time = get_time_from_message(message_text_split[1])
                if mute_time:
                    client.messages.send(peer_id=2000000106, message='Пользователь замьючен', random_id=random_id)
                    mutes[int(event.mentions[0])] = mute_time
                else:
                    client.messages.send(peer_id=2000000106, message='Не верно указано время. Доступно: с, м, ч, д.', random_id=random_id)
            elif 'mentions' not in event.extra_values:
                client.messages.send(peer_id=2000000106, message='Пользователь не выбран', random_id=random_id)
            else:
                client.messages.send(peer_id=2000000106, message='Че то не так', random_id=random_id)