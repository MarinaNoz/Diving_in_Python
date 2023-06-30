# №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от старт до стоп с шагом степ.
# если переданы два параметра, считаем степ == 1.
# Если передан один параметр, также считаем старт == 1.

class FactGenegator():
    def __init__(self, *args):
        match len(args):
            case 1 :
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args



    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            result = 1
            for j in range(2, self.start + 1):
                result *= j
            self.start += self.step
            return result
        raise StopIteration

fg = FactGenegator(5)
for i in fg:
    print(i)
