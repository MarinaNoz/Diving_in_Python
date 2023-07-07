# №4
# Функция получает на вход текст вида: "1-й четверг ноября", "3-я среда мая" итп
# Преобразуйте его в дату в текущем году
# Логируйте ошибки, если текст не соответствует формату
import logging
from datetime import datetime
from log_all import log_all

FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(format=FORMAT, style='{', filename='info_date.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

def parse_str(text: str):
    num_day, week_day, month = text.split()
    num_day = int(num_day[0])
    week_day = parse_day(week_day)
    month = parse_mount(month)
    year = datetime.now().year
    logger.info(f'{num_day}, {week_day}, {month}, {year}')
    spam_count = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == week_day:
            spam_count += 1
            if spam_count == num_day:
                return date

    # return num_day, day, mount, year


def parse_mount(mount: str) -> int:
    mounths = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'мая': 5, 'июн': 6, 'июл': 7,
            'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12}
    return mounths.get(mount[:3])


def parse_day(day: str) -> int:
    match day.lower():
        case 'понедельник':
            return 0
        case 'вторник':
            return 1
        case 'среда':
            return 2
        case 'четверг':
            return 3
        case 'пятница':
            return 4
        case 'суббота':
            return 5
        case 'воскресенье':
            return 6


if __name__ == '__main__':
    print(parse_str('3-я среда мая'))
    print(parse_str('1-й четверг ноября'))
    # print(parse_str('четверг 1-й ноября'))
    print(datetime.now().weekday())
    log_all()