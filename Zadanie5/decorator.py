import time


def timing_decorator(func):
    """
    Декоратор, измеряющий время выполнения функции.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Функция '{func.__name__}' выполнилась за "
            f"{end_time - start_time} секунд."
        )
        return result
    return wrapper
