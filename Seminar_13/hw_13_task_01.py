# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.

from MyExceptions import NegativeLength

class Rectangle:
    '''Добавлен класс вычисления периметра, площади прямоугольника,
    сложение и вычитание периметров. Добавлена проверка - при вычитании
     отрицательные значения не допускаются.'''

    '''Доработаем прямоугольник и добавим экономию памяти для хранения свойств
       экземпляра без словоря dict.'''
    # №5
    __slots__ = ('_side1', '_side2')

    def __init__(self, side1: int, side2: int = None):
        '''Назначение сторон.'''
        if side1 > 0:
            self._side1 = side1
        else:
            raise NegativeLength(side1, 0)
        self._side1 = side1

        if side2 > 0:
            self._side2 = side2
        else:
            raise NegativeLength(side2, 0)
        self._side2 = side2 if side2 is not None else side1
        '''При отсутствии второй стороны строится квадрат.'''






if __name__ == '__main__':
    a = int(input('Введите длинну стороны а первого прямоугольника: '))
    b = int(input('Введите длинну стороны b первого прямоугольника: '))
    rect1 = Rectangle(a, b)
    c = int(input('Введите длинну стороны а второго прямоугольника: '))
    d = int(input('Введите длинну стороны b второго прямоугольника: '))
    rect2 = Rectangle(c, d)
    print(rect1.side1)
    print(rect1.side2)
    # rect1.side1 = 10
    # rect1.side1 = -10
    print(rect1)
    print(rect2)