import json
from typing import Callable

def deco(func: Callable):

    with open(f'{func.__name__}.json', 'r') as f:
        final_dict = json.load(f)

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        final_dict.update({str(res): args})
        final_dict.update({**kwargs})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(final_dict, f, indent=2)

    return wrapper

@deco
def multy(a: int, b: int, *args, **kwargs) -> int:
    return  a * b

multy(8, 9, c=3, d=4)