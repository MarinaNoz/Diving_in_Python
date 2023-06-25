from typing import Callable

def count_run(param: int):
    def deco(func: Callable):
        my_list = []
        def wrapper(*args, **kwargs):
            for i in range(param):
                res = func(*args, **kwargs)
                my_list.append(res)
            return my_list

        return wrapper
    return deco

@count_run(3)
def fact(num: int) -> int:
    res = 1
    for i in range(1, num+1):
        res *= i
    return res

if __name__ == '__main__':
    print(fact(int(input('Введите число: '))))
