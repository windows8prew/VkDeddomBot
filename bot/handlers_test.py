from vk_api.longpoll import VkEventType
from bot.utils import event_handler_wrapper

# {'atachments': {'reply': '{"conversation_message_id":45396}', 'fwd': '0_0'},  'chat_id': 156,  'datetime': datetime.datetime(2022, 6, 11, 13, 49, 40), 'extra': None, 'extra_values': {'from': '78306551', 'mentions': [234363080], 'marked_users': [[1, [234363080]]]},  'flags': 2105395, 'from': '78306551', 'from_chat': True, 'from_group': False, 'from_me': True, 'from_user': False, 'marked_users': [[1, [234363080]]], 'mentions': [234363080], 'message': 'test', 'message_data': None, 'message_flags': {<VkMessageFlag.CHAT: 16>, <VkMessageFlag.UNREAD: 1>, <VkMessageFlag.OUTBOX: 2>, <VkMessageFlag.FRIENDS: 32>}, 'message_id': 4629588, 'peer_id': 2000000156, 'random_id': 929359520, 'raw': [4, 4629588, 2105395, 2000000156, 1654955380, 'test', {'from': '78306551', 'mentions': [234363080], 'marked_users': [[1, [234363080]]]}, {'reply': '{"conversation_message_id":45396}', 'fwd': '0_0'}, 929359520], 'text': 'test', 'timestamp': 1654955380, 'to_me': False, 'type': <VkEventType.MESSAGE_NEW: 4>, 'type_id': None, 'user_id': 78306551}
# {'attachments': {},                                                           'chat_id': 156,  'datetime': datetime.datetime(2022, 6, 11, 13, 51, 49), 'extra': None, 'extra_values': {'from': '78306551'}, 'flags': 8243, 'from': '78306551', 'from_chat': True, 'from_group': False, 'from_me': True, 'from_user': False, 'message': 'bota', 'message_data': None, 'message_flags': {<VkMessageFlag.CHAT: 16>, <VkMessageFlag.UNREAD: 1>, <VkMessageFlag.OUTBOX: 2>, <VkMessageFlag.FRIENDS: 32>}, 'message_id': 4629601, 'peer_id': 2000000156, 'random_id': 2136011746, 'raw': [4, 4629601, 8243, 2000000156, 1654955509, 'bota', {'from': '78306551'}, {}, 2136011746], 'text': 'bota', 'timestamp': 1654955509, 'to_me': False, 'type': <VkEventType.MESSAGE_NEW: 4>, 'type_id': None, 'user_id': 78306551}

@event_handler_wrapper()
def simple_event_handler(client, event):
    return
    print(dict((name, getattr(event, name)) for name in dir(event) if not name.startswith('__')))
    if event.type == VkEventType.MESSAGE_NEW:
        print('Новое сообщение:')

        if event.from_me:
            print('От меня для: ', end='')
        elif event.to_me:
            print('Для меня от: ', end='')

        if event.from_user:
            print(event.user_id)
        elif event.from_chat:
            print(event.user_id, 'в беседе', event.chat_id)
        elif event.from_group:
            print('группы', event.group_id)

        print('Текст: ', event.text)
        print()

    elif event.type == VkEventType.USER_TYPING:
        print('Печатает ', end='')

        if event.from_user:
            print(event.user_id)
        elif event.from_group:
            print('администратор группы', event.group_id)

    elif event.type == VkEventType.USER_TYPING_IN_CHAT:
        print('Печатает ', event.user_id, 'в беседе', event.chat_id)

    elif event.type == VkEventType.USER_ONLINE:
        print('Пользователь', event.user_id, 'онлайн', event.platform)

    elif event.type == VkEventType.USER_OFFLINE:
        print('Пользователь', event.user_id, 'оффлайн', event.offline_type)

    else:
        print(event.type, event.raw[1:])
