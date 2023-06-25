# Программа загадывает число от 0 до 1000
from random import randint
num = randint(0, 1000)
print(f'Мы загадали число от 0 до 1000, попробуйте его отгадать')
band = 10
for i in range(band):
    n = int(input('Введите число: '))
    if n < num:
        print(f'Число {n} меньше загаданного')
    elif n > num:
        print(f'Число {n} больше загаданного')
    elif n == num:
        print(f'Победа! Загаданно число {n}')
        break
print(f'Увы и ах, Вы не отгадали, было загаданно число {num}')
