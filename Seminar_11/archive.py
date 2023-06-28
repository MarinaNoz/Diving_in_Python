# №2
# Создайте класс Архив

# №3 Добавить к задачам 1 и 2 строки документации для классов

# №4 Добавить методы представления экземпляра для программиста и для пользователя

class Archive:

    # №3
    '''Сохраняем данные каждого экземпляра класса в списки numbers и values.'''

    numbers = []
    values = []
    def __new__(cls, number: int, value: str):
        '''Переопределяем метод new для сохранения аргументов и списков.'''
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        '''Определили метод инициализации экземпляра класса.'''
        self.number = number
        self.value = value

    # №4
    def __repr__(self):
        '''Добавлен метод представления экземпляра для программиста.'''
        return f'Archive ({self.number}, "{self.value}")'

    def __str__(self):
        '''Добавлен метод представления экземпляра для пользователя.'''
        return f'Номер: {self.number}, Значение: "{self.value}"'
    # /№4


if __name__ == '__main__':
    a_1 = Archive(1, 'One')
    # a_2 = Archive(2, 'Two')
    # print(f'{a_1.numbers} {a_1.values}')
    # print(f'{a_2.numbers} {a_2.values}')
    # a_3 = Archive(3, 'Three')
    # print(f'{a_3.numbers} {a_3.values}')
    # help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)
    help(Archive)