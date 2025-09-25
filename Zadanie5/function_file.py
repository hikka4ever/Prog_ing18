from decorator import timing_decorator


@timing_decorator
def sum_from_file():
    """
    Читает два числа из файла 'input.txt', вычисляет их сумму
    и записывает результат в файл 'output.txt'.
    """
    try:
        with open('input.txt', 'r') as infile:
            lines = infile.readlines()
            a = int(lines[0].strip())
            b = int(lines[1].strip())

        result = a + b

        with open('output.txt', 'w') as outfile:
            outfile.write(str(result))

        print(f"Результат суммы ({result}) записан в файл 'output.txt'.")
        return result

    except FileNotFoundError:
        print("Файл 'input.txt' не найден.")
    except (ValueError, IndexError):
        print("Ошибка при чтении чисел из файла 'input.txt'. ")