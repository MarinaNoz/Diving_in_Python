# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
#
# - doctest
# - unittest
# - pytest.

import pytest
from hw_14_doctest import *



def test_long_positive():
    assert long(2) == 13

def test_long_negative():
    with pytest.raises(ValueError, match=r'Заданный радиус не может быть меньше единицы'):
        long(-2)


def test_area_positive():
    assert area(3) == 28

def test_area_negative():
    with pytest.raises(ValueError, match=r'Заданный радиус не может быть меньше единицы'):
        area(-2)


if __name__ == '__main__':
    pytest.main(['-v'])
