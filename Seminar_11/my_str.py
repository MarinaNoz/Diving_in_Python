# №1
# Создайте класс моя строка

# №3 Добавить к задачам 1 и 2 строки документации для классов

import time


class MyString(str):

    # №3
    '''Рассширяем класс str.'''

    def __new__(cls, value: str, name: str):
        # №3
        '''Расширяем метод new параметрами value и name.'''
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance



if __name__ == '__main__':
    mystr = MyString('Test', 'dop str')
    print(mystr)
    print(mystr.created_at)
    print(mystr.name)
    print(mystr.upper())
    help(MyString)

