from cmath import sqrt
from random import randint
import csv
import json
import random
from pathlib import Path
from typing import Callable
from functools import wraps


def create_csv(name: str = 'new_csv', count_rows: int = randint(100, 1000)):
    rows = []
    for _ in range(count_rows):
        a, b, c = random.sample(range(100, 1000), 3)
        rows.append({'a': a, 'b': b, 'c': c})

    with open(name + '.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def load_csv(file: str):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file, 'r', encoding='utf-8') as f:
                data = csv.reader(f)
                for i, row in enumerate(data):
                    if i == 0:
                        continue
                    args = (complex(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result

        return wrapper

    return deco



def save_2_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                dct = {'args': args, **kwargs, 'result': str(result)}
                json_file.append(dct)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            else:
                break

    return wrapper

@save_2_json
@load_csv('new_csv.csv')
def square(a: complex, b: complex, c: complex) :
    # a, b, c = args
    if a != 0:
        d: complex = b * b - 4 * a * c
        x1: complex = (-b + sqrt(d)) / (2 * a)
        x2: complex = (-b - sqrt(d)) / (2 * a)
        return d, x1, x2
    else:
        return 0, 0, 0


if __name__ == '__main__':
    create_csv()
    square()