# Напишите для задачи 1 тесты unittest. Проверяйте следующие варианты:
# - возвращает строки без изменений
# - возвращает строки с преобразованием регистра бе потери символов
# - возвращает строки с удалением знаков пунктуации
# - возвращает строки с удалением букв других алфавитов
# - возвращает строки с учетом всех пунктов (кроме п.1)

import pytest
from delete_text import remove_chars


def test_no_change():
    assert remove_chars('aaaa aaa') == 'aaaa aaa'


def test_lover():
    assert remove_chars('AAAA AAA') == 'aaaa aaa'


def test_sign():
    assert remove_chars('a!a,a@a# $a%a^a&') == 'aaaa aaa'


def test_cyrillic():
    assert remove_chars('ЫПятор фыкнЯЫНР536') == ' '


def test_upper():
    assert remove_chars('ЦЦЦ WWW, qqq') == 'www qqq'


if __name__ == '__main__':
    pytest.main(['-v'])
