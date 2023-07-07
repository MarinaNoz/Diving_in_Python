# Напишите программу которая использует модуль logging для вывода сообщения об ошибке.

import logging

logging.basicConfig(filename='error_div.log', level=logging.ERROR, encoding='utf-8')


def division(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zd:

        logging.error(f'Ошибка, деление на ноль {zd}')


if __name__ == '__main__':
    division(1, 0)
