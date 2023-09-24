import time


def time_of_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        result = func(*args, **kwargs)
        print(f'Время выполнения алгоритма: {time.monotonic() - start_time}')
        return result
    return wrapper
