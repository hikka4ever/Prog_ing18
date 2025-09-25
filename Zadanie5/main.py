from function_cons import sum_numbers
from function_file import sum_from_file



def main():
    """
    Главная функция, которая запускает все остальные.
    """
    # Тестирование функции суммы, которая выводится на консоль
    sum_numbers(10, 90)

    # Тестирование функции суммы, которая читает файл input.txt
    sum_from_file()


if __name__ == "__main__":
    main()