# Функция принимает два аргумента: лямбда-функцию для фильтрации массива
# и массив строк
def filter_strings(filter_func, list_of_strings):
    """Функция-фильтр списка строк, использующая заданную лямбда-функцию."""

    # Проверка на пустой список
    if not list_of_strings:
        raise ValueError("Список не должен быть пустым")

    # Проверка, что все элементы являются непустыми строками
    for item in list_of_strings:
        if not isinstance(item, str):
            raise ValueError("Все элементы списка должны быть строками")
        if not item.strip():
            raise ValueError("Строки не могут быть пустыми")

    # Применение лямбда-функции для фильтрации массива строк
    return list(filter(filter_func, list_of_strings))
