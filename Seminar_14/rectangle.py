# №5 На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest


class Rectangle:
    """Добавлен класс вычисления периметра, площади прямоугольника,
    сложение и вычитание периметров. Добавлена проверка - при вычитании
    отрицательные значения не допускаются.
    Доработаем прямоугольник и добавим экономию памяти для хранения свойств
    экземпляра без словоря dict."""

    # №5
    __slots__ = ('_side1', '_side2')

    def __init__(self, side1: int, side2: int = None):
        '''Назначение сторон.'''
        self._side1 = side1
        self._side2 = side2 if side2 is not None else side1
        'При отсутствии второй стороны строится квадрат.'

    @property
    def side1(self):
        return self._side1

    @property
    def side2(self):
        return self._side2

    @side1.setter
    def side1(self, value):
        if value > 0:
            self._side1 = value
        else:
            raise ValueError(f'Ошибка, сторона {value} не может быть отрицательной')

    @side2.setter
    def side2(self, value):
        if value > 0:
            self._side2 = value
        else:
            raise ValueError(f'Ошибка, сторона {value} не может быть отрицательной')

    def area(self) -> int:
        """Вычисление площади прямоугольника."""
        return self.side2 * self.side1

    def perimetr(self) -> int:
        """Вычисление периметра прямоугольника."""
        return 2 * (self.side1 + self.side2)

    def __add__(self, other):
        """Вычитание периметров прямоугольников,
        Определение минимальной стороны прямоугольника."""
        new_rectangle = self.perimetr() + other.perimetr()
        a = min(self.side1, self.side2, other.side1, other.side2)
        b = new_rectangle / 2 - a
        return Rectangle(a, b)

    def __sub__(self, other):
        """Сложение периметров прямоугольников."""
        new_rectangle = abs(self.perimetr() + other.perimetr())
        a = self.side1
        b = new_rectangle / 2 - a
        return Rectangle(a, b)

    def __str__(self):
        """Переопределен метод вывода экземпляра класса"""
        return f'Прямоугольник {self.side1} x {self.side2}'


class TestRectangle(unittest.TestCase):

    def setUp(self) -> Rectangle:
        self.rectangle_1 = Rectangle(2, 3)
        self.rectangle_2 = Rectangle(5, 10)
        self.rectangle_3 = Rectangle(5)

    def test_perimetr(self):
        self.assertEqual(self.rectangle_1.perimetr(), 10)

    def test_area(self):
        self.assertEqual(self.rectangle_2.area(), 50)

    def test_sum_rect(self):
        self.assertEqual((self.rectangle_1 + self.rectangle_2).perimetr(), 40)

    def test_str(self):
        self.assertEqual(self.rectangle_1.__str__(), f'Прямоугольник 2 x 3')




if __name__ == '__main__':
    unittest.main(verbosity=True)
