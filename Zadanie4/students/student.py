class Student:
    """
    Класс для студента.
    Содержит свойства: ФИО, возраст, номер группы, средний балл.
    """
    # Константы для стипендий и оценок
    EXCELLENT_SCORE = 5.0
    MIN_SCORE = 0.0
    MAX_SCORE = 5.0
    EXCELLENT_SCHOLARSHIP = 6000.0
    REGULAR_SCHOLARSHIP = 4000.0

    def __init__(self,
                 full_name: str,
                 age: int,
                 group_number: str,
                 average_score: float):
        if not isinstance(full_name, str) or not full_name:
            raise ValueError(
                "ФИО должно быть "
                "непустой строкой."
            )
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст должен быть положительным целым числом.")
        if not isinstance(group_number, str) or not group_number:
            raise ValueError("Номер группы должен быть непустой строкой.")
        if not isinstance(average_score,
                          (int, float)) or not (self.MIN_SCORE <= average_score
                                                <= self.MAX_SCORE):
            raise ValueError(
                "Средний балл должен "
                "быть числом от 0 до 5."
            )

        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_score = average_score

    def get_info(self):
        """Возвращает информацию о человеке (ФИО, возраст)."""
        return f"ФИО: {self.full_name}, Возраст: {self.age}"

    def get_scholarship_amount(self):
        """Вычисляет и возвращает размер стипендии студента."""
        if self.average_score == self.EXCELLENT_SCORE:
            return self.EXCELLENT_SCHOLARSHIP
        elif self.MIN_SCORE <= self.average_score < self.EXCELLENT_SCORE:
            return self.REGULAR_SCHOLARSHIP
        else:
            return 0.0

    def is_scholarship_larger_than(self, other_student: 'Student'):
        """
        Сравнивает стипендию текущего студента с другим студентом/аспирантом.
        Возвращает True, если стипендия текущего студента больше.
        """
        return (
            self.get_scholarship_amount() >
            other_student.get_scholarship_amount()
        )
