# Напишите для задачи 1 тесты doctest. Проверяйте следующие варианты:
# - возвращает строки без изменений
# - возвращает строки с преобразованием регистра бе потери символов
# - возвращает строки с удалением знаков пунктуации
# - возвращает строки с удалением букв других алфавитов
# - возвращает строки с учетом всех пунктов (кроме п.1)
import doctest
import string


def remove_chars(text: str) -> str:
    '''
    text
    >>>  remove_chars('aaaa aaa')
    'aaaa aaa'
    >>>  remove_chars('BB BBB')
    'bb bbb'
    >>>  remove_chars('a!a,a@a# $a%a^a&')
    'aaaa aaa'
    >>>  remove_chars('ЫПятор фыкнЯЫНР536')
    ''
    >>>  remove_chars('ЦЦЦ WWW, qqq. ЙЙЙ/ 6+54')
    'www qqq'
    '''
    alpha = string.ascii_letters + ' '
    print(alpha)
    result = text
    for t in text:
        if t not in alpha:
            result = result.replace(t, '')
    return result.lower()


if __name__ == '__main__':
    # print(remove_chars('addSDGdsafsdfsd aghавпыпFSDHряывап 23552#%13'))
    doctest.testmod(verbose=True)
