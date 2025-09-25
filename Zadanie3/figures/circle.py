import math
from .figure import Figure

class Circle(Figure):
    """ Класс для круга. """
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус круга должен быть положительным числом.")
        self.radius = radius

    def get_area(self):
        """ Вычисляет площадь круга. """
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        """ Вычисляет длину окружности (периметр круга). """
        return 2 * math.pi * self.radius