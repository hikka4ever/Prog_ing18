from filter_strings import filter_strings


def main():
    # Пример массива строк
    input_strings = [' person', 'man', 'woman', 'bo y', 'girl ', 'age', 'Arm']

    # Фильтры
    no_spaces = lambda s: ' ' not in s  # noqa: E731
    no_a_start = lambda s: s[0].lower() != 'a'  # noqa: E731
    long_strings = lambda s: len(s) >= 5  # noqa: E731

    # Применение фильтров и вывод результатов
    print("Без пробелов:", filter_strings(no_spaces, input_strings))
    print("Не начинаются с 'a':", filter_strings(no_a_start, input_strings))
    print("Длина >= 5:", filter_strings(long_strings, input_strings))


if __name__ == "__main__":
    main()
