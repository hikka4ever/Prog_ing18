import re


def IsPalindrome(text: str):
    """ Функция для проверки паллидромности строки """

    # Заменяем всю не латиницу, киррилицу или цифры на '' и
    # приводим строку к нижнему регистру
    clean_text = re.sub(r'[^0-9а-яa-z]', '', text.lower())

    return clean_text == clean_text[::-1]

