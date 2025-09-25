from decorator import timing_decorator


@timing_decorator
def sum_numbers(a, b):
    """
    Вычисляет и выводит в консоль сумму двух чисел.
    """
    result = a + b
    print(f"Сумма чисел {a} и {b} равна {result}")
    return result