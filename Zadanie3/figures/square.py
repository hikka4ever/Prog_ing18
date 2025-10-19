from .figure import Figure


class Square(Figure):
    """Класс для квадрата."""
    def __init__(self, side: float):
        if side <= 0:
            raise ValueError(
                "Сторона квадрата должна быть "
                "положительным числом."
            )
        self.side = side

    def get_area(self):
        """Вычисляет площадь квадрата."""
        return self.side ** 2

    def get_perimeter(self):
        """Вычисляет периметр квадрата."""
        return 4 * self.side
