from figures.square import Square
from figures.rectangle import Rectangle
from figures.circle import Circle
from figures.triangle import Triangle


def main():
    """ Пример использования классов фигур. """
    try:
        # Создаем экземпляры фигур
        square = Square(7)
        rectangle = Rectangle(4, 6)
        circle = Circle(3)
        triangle = Triangle(3, 4, 5)

        # Вычисляем и выводим площади и периметры
        print(f"Площадь квадрата: {square.get_area():.2f}")
        print(f"Периметр квадрата: {square.get_perimeter():.2f}")

        print(f"\nПлощадь прямоугольника: {rectangle.get_area():.2f}")
        print(f"Периметр прямоугольника: {rectangle.get_perimeter():.2f}")

        print(f"\nПлощадь круга: {circle.get_area():.2f}")
        print(f"Периметр круга: {circle.get_perimeter():.2f}")

        print(f"\nПлощадь треугольника: {triangle.get_area():.2f}")
        print(f"Периметр треугольника: {triangle.get_perimeter():.2f}")

        # Сравниваем фигуры
        print("\n--- Сравнение фигур ---")
        print(f"Площадь квадрата > площади прямоугольника? {square.is_area_larger_than(rectangle)}")
        print(f"Периметр круга > периметра квадрата? {circle.is_perimeter_larger_than(square)}")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()