# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
#
# - doctest
# - unittest
# - pytest.

import unittest
from hw_14_doctest import *

class TestCircle(unittest.TestCase):

    def test_long_positive(self):
        self.assertEqual(long(2), 13)

    def test_long_negative(self):
        with self.assertRaises(ValueError):
            long(-2)

    def test_area_positive(self):
        self.assertEqual(area(3), 28)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
