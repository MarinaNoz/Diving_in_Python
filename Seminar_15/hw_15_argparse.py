# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import argparse
import logging
from MyExceptions import MyMinLengthError, MyTriangleError

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(format=FORMAT, style='{', filename='argparse.log', level=logging.INFO, encoding='utf-8')
# logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")



def check_sides(a, b, c):
    if a < 1:
        logging.error('Сторона а меньше 1', exc_info=True)
        raise MyMinLengthError(a, 0)

    if b < 1:
        logging.error('Сторона b меньше 1', exc_info=True)
        raise MyMinLengthError(b, 0)
    if c < 1:
        logging.error('Сторона c меньше 1', exc_info=True)
        raise MyMinLengthError(c, 0)
    else:
        check1 = a + b
        check2 = a + c
        check3 = b + c
    if check1 < c or check2 < b or check3 < a:
        logging.warning(f'Tреугольника со сторонами {a}, {b}, {c} не существует!', exc_info=True)
        raise MyTriangleError(a, b, c)
    else:
        if (a == b and b == c and c == a):
            logging.info(f'Tреугольник со сторонами {a}, {b}, {c} - равносторонний \n')
            print('Треугольник равносторонний')
        elif (a == b or b == c or c == a):
            logging.info(f'Tреугольник со сторонами {a}, {b}, {c} - равнобедренный \n')
            print('Треугольник равнобедренный')
        else:
            logging.info(f'Tреугольник со сторонами {a}, {b}, {c} - разносторонний \n')
            print('Треугольник разносторонний')


if __name__ == '__main__':
    # print(check_sides(2, 3, 9))
    parser = argparse.ArgumentParser(description='Проверка построения треугольника')
    parser.add_argument('-a', metavar='a', type=float, help='Для проверки построения трегулольника получаем сторону a:')
    parser.add_argument('-b', metavar='b', type=float, help='Для проверки построения трегулольника получаем сторону b:')
    parser.add_argument('-c', metavar='c', type=float, help='Для проверки построения трегулольника получаем сторону c:')
    args = parser.parse_args()
    print(check_sides(args.a, args.b, args.c))

# python .\seminar_15\hw_15_argparse.py -a 2 -b 12 -c 15
