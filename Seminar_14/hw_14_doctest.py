# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
#
# - doctest
# - unittest
# - pytest.

import doctest
from math import pi


def long(r: float) -> float:
    """
    Проверим является ли заданный радиус меньше единицы
    >>> long(-2)
    Traceback (most recent call last):
        ...
    ValueError: Заданный радиус не может быть меньше единицы

    Проверим правильность вычисления длинны окружности (округлено до целого)
    >>> long(2)
    13
    """
    if r < 1:
        raise ValueError('Заданный радиус не может быть меньше единицы')
    else:
        return round(2 * pi * r)

def area(r: float) -> float:
    """
    Проверим является ли заданный радиус меньше единицы
    >>> area(-2)
    Traceback (most recent call last):
        ...
    ValueError: Заданный радиус не может быть меньше единицы

    Проверим правильность вычисления длинны окружности (округлено до целого)
    >>> area(3)
    28
    """
    if r < 1:
        raise ValueError('Заданный радиус не может быть меньше единицы')
    else:
        return round(pi * pow(r, 2))

if __name__ == '__main__':
    # print(f'{round(long(2)) = } {round(area(3)) = }')
    doctest.testmod(verbose=True)
