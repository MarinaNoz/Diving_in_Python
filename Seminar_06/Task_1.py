# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from datetime import datetime
from sys import argv


def valid_date (date_text: str) -> bool:
    try:
        datetime.strptime(date_text, "%d.%m.%Y").date()
        return True
    except:
        return False


def valid_year(year_: str) -> bool:
    year_ = int(year_.split('.')[-1])
    if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    valid_date(argv[-1])

    date_ = input('Введите дату в формате dd.mm.yyyy: ')
    year_ = input('Введите год: ')
    print(valid_date(date_))
    print(valid_year(year_))