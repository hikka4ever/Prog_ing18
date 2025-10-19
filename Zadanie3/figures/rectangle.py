from .figure import Figure


class Rectangle(Figure):
    """Класс для прямоугольника."""
    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError(
                "Ширина и высота прямоугольника должны быть "
                "положительными числами."
            )
        self.width = width
        self.height = height

    def get_area(self):
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    def get_perimeter(self):
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)
