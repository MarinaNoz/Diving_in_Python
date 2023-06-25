from typing import Callable
from random import randint

def deco(func: Callable):
    MIN_COUNT = 1
    MAX_COUNT = 10
    MIN_NUM = 1
    MAX_NUM = 100
    def wrapper(*args, **kwargs):
        input_count, input_num = args
        if MIN_COUNT > input_count or input_count > MAX_COUNT:
            input_count = randint(MIN_COUNT, MAX_COUNT)
            print(f'Введеное количество попыток вне диапазона, \n'
                  f'количество попыток будет назначено случайным')
        if MIN_NUM > input_num or input_num > MAX_NUM:
            input_num = randint(MIN_NUM, MAX_NUM)
            print(f'Введеное чило вне диапазона, загаданно будет случайное число')
        return func(input_count, input_num)
    return wrapper

@deco
def two_numbers(count: int, num: int) -> Callable[[], None]:

    def random_numbers():
        attempt = count
        for i in range(1, count + 1):

            user_input = int(input('Загадано число от 1 до 100, Ваше предположение: '))
            if user_input != num:
                attempt -= 1
                if user_input < num:
                    print(f'Не верно, Ваше число меньше. У Вас осталось {attempt} попытки')
                else:
                    print(f'Не верно, Ваше число больше. У Вас осталось {attempt} попытки')

            if user_input == num:
                print(f'Вы угадали с {i} попытки')
                break
        else:
            print(f'Вы не угадали, было загадано число {num}')
    return random_numbers

print(f'Правила игры: Вы водите колличество попыток в диапазоне от 1 до 10 \n'
              f'если введенное количество попыток будет вне диапазона, \n'
              f'то количество попыток будет назначено случайным, в диапазоне от 1 до 10. \n'
              f'Далее Вы водите число которое необходимо отгадать, в диапазоне от 1 до 100. \n'
              f'Если введенное число будет вне диапазона, \n'
              f'то оно будет назначено случайным, в диапазоне от 1 до 100. \n')

a = int(input('Введите количество попыток: '))
b = int(input('Введите число которое необходимо отгадать: '))
res = two_numbers(a, b)
res()