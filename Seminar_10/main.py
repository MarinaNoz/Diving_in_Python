from typing import Callable

import check_nums
import make_json
import deco_param


if __name__ == '__main__':

    @check_nums.deco
    def two_numbers(count: int, num: int) -> Callable[[], None]:

        def random_numbers():
            attempt = count
            for i in range(1, count + 1):
                user_input = int(input('Введите число для отгадывания от 1 до 100: '))
                if user_input != num:
                    attempt -= 1
                    print(f'Не верно, у Вас осталось {attempt} попытки')
                if user_input == num:
                    print(f'Вы угадали с {i} попытки')
                    break
            else:
                print(f'Вы не угадали, было загшадано число {num}')
        return random_numbers
