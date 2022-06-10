

handlers_list = []


def event_handler_wrapper():
    def wrapper(func):
        print(func, 'wrapped')
        handlers_list.append(func)
    return wrapper
