import re
import datetime
import time

handlers_list = []


def event_handler_wrapper():
    def wrapper(func):
        print(func, 'wrapped')
        handlers_list.append(func)
    return wrapper


def get_time_from_message(text):
    match = re.match(r'(\d+)\s*([а-яА-Я]+)', text)
    if not match:
        return
    group = match.groups()
    if len(group) != 2:
        return
    period, measure = int(group[0]), group[1]
    now = time.time()
    if measure == 'с':
        delta = datetime.timedelta(seconds=period)
    elif measure == 'м':
        delta = datetime.timedelta(minutes=period)
    elif measure == 'ч':
        delta = datetime.timedelta(hours=period)
    elif measure == 'д':
        delta = datetime.timedelta(days=period)
    else:
        return
    return now + delta.total_seconds()
