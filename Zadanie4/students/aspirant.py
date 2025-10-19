from .student import Student


class Aspirant(Student):
    """
    Класс для аспиранта.
    Содержит свойства: ФИО, возраст, номер группы,
    средний балл и название научной работы.
    """
    # Константы для стипендий аспиранта
    EXCELLENT_SCHOLARSHIP = 8000.0
    REGULAR_SCHOLARSHIP = 6000.0

    def __init__(self,
                 full_name: str,
                 age: int,
                 group_number: int,
                 average_score: float,
                 research_work_title: str):
        super().__init__(full_name, age, group_number, average_score)
        if not isinstance(research_work_title, str) or not research_work_title:
            raise ValueError("Название научной работы "
                             "должно быть непустой строкой.")

        self.research_work_title = research_work_title

    def get_scholarship_amount(self):
        """ Переопределяет метод для вычисления стипендии аспиранта. """
        if self.average_score == self.EXCELLENT_SCORE:
            return self.EXCELLENT_SCHOLARSHIP
        elif self.MIN_SCORE <= self.average_score < self.EXCELLENT_SCORE:
            return self.REGULAR_SCHOLARSHIP
        else:
            return 0.0

    def get_info(self):
        """
        Переопределяет метод для вывода дополнительной информации об аспиранте.
        """
        base_info = super().get_info()
        return f"{base_info}, Научная работа: '{self.research_work_title}'"
