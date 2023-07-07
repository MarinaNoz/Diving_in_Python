# №2
# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат ее работы в файл
# Напишите аналогичныйдекоратор, но внутри используйте модуль logging

# №3
# Дорабатываем задачу 2
# Сохранить в логфайл раздельно:
#  - уровень логирования
#  - дату события
#  - имя функции
#  - аргументы вызова
#  - результат

import logging
from typing import Callable

FORMAT = '{levelname} - {asctime}: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='info_deco.log', level=logging.INFO, encoding='utf-8')


logger = logging.getLogger(__name__)


def deco_logger(func: Callable):

    def wrapper(*args, **kwargs):
        a, b = args
        res = func(a, b)
        logger.info(f'{a} * {b} = {res}')

    return wrapper


@deco_logger
def multy(a: int, b: int, *args, **kwargs) -> int:
    return a * b


if __name__ == '__main__':
    multy(78, 97)

