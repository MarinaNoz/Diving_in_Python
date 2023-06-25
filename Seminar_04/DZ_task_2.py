#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ - значение переданного аргумента, а значение - имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление.

from collections.abc import Hashable


def f(**kwargs) -> dict:
    my_dict = {}
    for key, item in kwargs.items():
        if not isinstance(item, Hashable):
            item = str(item)
        my_dict[item] = key

    return my_dict


print(f(name= 'Ivan', age=33, my=[1, 2]))