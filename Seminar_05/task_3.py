# Создайте функцию генератор чисел Фибоначчи

def fibonach(to: int):
    if to > 0:
        f = [0, 1]
        while to > 0:
            yield f[-1]
            f.append(f[-1] + f[-2])
            to -= 1

    elif to < 0:
        f = [0, -1]
        while to < 0:
            yield f[-1]
            f.append(f[-1] + f[-2])
            to += 1
for number in fibonach(int(input('Введите число: '))):
    print(number)


