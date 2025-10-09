from students.student import Student
from students.aspirant import Aspirant


def main():
    """Пример использования классов Student и Aspirant."""
    try:
        # Создание экземпляров
        student_excellent = Student(
            "Павелков Артём Владимирович",
            19,
            "30801",
            5.0
        )
        student_no_exellent = Student(
            "Афанасьев Дмитрий Павлович",
            20,
            "30701",
            3.5
        )
        aspirant_excellent = Aspirant(
            "Козлов Дмитрий Николаевич",
            25,
            "30501",
            5.0,
            "Влияние никотина на общество"
        )
        aspirant_no_exellent = Aspirant(
            "Железников Клим Алексеевич",
            50,
            "30502",
            3.333,
            "Почему"
        )

        # Вывод информации о студентах и аспирантах
        print(f"\nИнформация: {student_excellent.get_info()}")
        print(f"Стипендия: "
              f"{student_excellent.get_scholarship_amount():.2f} руб.")

        print(f"\nИнформация: {student_no_exellent.get_info()}")
        print(f"Стипендия: "
              f"{student_no_exellent.get_scholarship_amount():.2f} руб.")

        print(f"\nИнформация: {aspirant_excellent.get_info()}")
        print(f"Стипендия: "
              f"{aspirant_excellent.get_scholarship_amount():.2f} руб.")

        print(f"\nИнформация: {aspirant_no_exellent.get_info()}")
        print(f"Стипендия: "
              f"{aspirant_no_exellent.get_scholarship_amount():.2f} руб.")

        # Сравнение стипендий
        print(
            "\nСтипендия студента-отличника > "
            "стипендии студента-не-отличника? "
            f"{student_excellent.is_scholarship_larger_than(student_no_exellent)}"
        )
        print(
            "Стипендия аспиранта-отличника > "
            "стипендии студента-отличника? "
            f"{aspirant_excellent.is_scholarship_larger_than(student_excellent)}"
        )
        print(
            "Стипендия студента-не-отличника > "
            "стипендии аспиранта-не-отличника? "
            f"{student_no_exellent.is_scholarship_larger_than(aspirant_no_exellent)}"
        )

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
