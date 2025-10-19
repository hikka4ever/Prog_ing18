import math
from .figure import Figure


class Triangle(Figure):
    """Класс для треугольника."""
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                "Стороны треугольника должны быть "
                "положительными числами."
            )
        if (
            side_a + side_b <= side_c or
            side_a + side_c <= side_b or
            side_b + side_c <= side_a
        ):
            raise ValueError(
                "Сумма двух сторон треугольника должна быть "
                "больше третьей стороны."
            )
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        """Вычисляет площадь треугольника."""
        s = self.get_perimeter() / 2
        return math.sqrt(
            s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)
        )

    def get_perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.side_a + self.side_b + self.side_c
