# Создайте класс прямоугольник

class Rectangle:
    def __init__(self, side1: int, side2: int = None):
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1

    def area(self) -> int:
        return self.side2 * self.side1

    def perimetr(self) -> int:
        return 2 * (self.side1 + self.side2)

if __name__ == '__main__':
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(15)

    print(f'{rect1.area() = }, {rect1.perimetr() = }')
    print(f'{rect2.area() = }, {rect2.perimetr() = }')
    