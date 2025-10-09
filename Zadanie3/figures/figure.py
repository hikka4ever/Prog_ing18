from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Абстрактный базовый класс для всех геометрических фигур.
    Определяет общие методы для вычисления площади и периметра,
    и для их сравнения.
    """

    @abstractmethod
    def get_area(self):
        """Вычисляет и возвращает площадь."""
        pass

    @abstractmethod
    def get_perimeter(self):
        """Вычисляет и возвращает периметр."""
        pass

    def is_area_larger_than(self, other_shape: 'Figure'):
        """
        Сравнивает площадь текущей фигуры с площадью другой фигуры.
        Возвращает True, если площадь текущей фигуры больше.
        """
        return self.get_area() > other_shape.get_area()

    def is_perimeter_larger_than(self, other_shape: 'Figure'):
        """
        Сравнивает периметр текущей фигуры с периметром другой фигуры.
        Возвращает True, если периметр текущей фигуры больше.
        """
        return self.get_perimeter() > other_shape.get_perimeter()
