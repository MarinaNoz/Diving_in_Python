class MyExceptions(Exception):
    pass


class NegativeLength (MyExceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value

    def __str__(self):

        if self.param < self.value:
            return f'Отрицательные значения не допустимы!\n' \
                   f'Заданное число {self.param} < {self.value}'
            # raise ValueError(f'Ошибка, сторона {value} не может быть отрицательной')



        # elif self.param == self.value:
        #     return f'Сторона прямоугольника не может быть нулевой!\n' \
        #            f'Заданное число {self.param} = {self.value}'
        #
