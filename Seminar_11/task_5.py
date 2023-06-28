# From seminar_10 - Создайте класс прямоугольник
# Добавить возможность сложения и вычитания
# При этом должен создаваться новый экземпляр прямоугольника
# Складываем и вычитаем периметры, а не длинну и ширину
# Отрицательные значения не допускаются.


class Rectangle:
    '''Добавлен класс вычисления периметра, площади прямоугольника,
    сложение и вычитание периметров. Добавлена проверка - при вычитании
     отрицательные значения не допускаются.'''

    def __init__(self, side1: int, side2: int = None):
        '''Назначение сторон.'''
        self.side1 = side1
        self.side2 = side2 if side2 is not None else side1
        '''При отсутствии второй стороны строится квадрат.'''

    def area(self) -> int:
        '''Вычисление площади прямоугольника.'''
        return self.side2 * self.side1

    def perimetr(self) -> int:
        '''Вычисление периметра прямоугольника.'''
        return 2 * (self.side1 + self.side2)

    def __add__(self, other):
        '''Вычитание периметров прямоугольников.'''
        new_rectangle = self.perimetr() + other.perimetr()
        a = min(self.side1, self.side2, other.side1, other.side2)
        '''Определение минимальной стороны прямоугольника.'''
        b = new_rectangle / 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        '''Сложение периметров прямоугольников.'''
        new_rectangle = abs(self.perimetr() + other.perimetr())
        a = self.side1
        b = new_rectangle / 2 - a
        return Rectangle(a, b)


if __name__ == '__main__':
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(5, 15)

    print(f'{rect1.area() = }, {rect1.perimetr() = }')
    print(f'{rect2.area() = }, {rect2.perimetr() = }')
    rect_sum = rect1 + rect2
    print(f'{rect_sum.side1, rect_sum.side2}')
    rect_sub = rect1 - rect2
    print(f'{rect_sub.side1, rect_sub.side2}')
    help(Rectangle)
