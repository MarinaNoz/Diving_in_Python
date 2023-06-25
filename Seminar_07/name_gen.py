from pathlib import Path
from random import randint, uniform, choice

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjkmnpqrstvwxz'

def name_gen(count: int, str_len_min: int, str_len_max: int, file_2 : Path) -> None:
    with open(file_2, 'a', encoding='utf-8') as f:
        for i in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                                                           for i in range(randint(str_len_min, str_len_max)))
            f.write(f'{rad_string.capitalize()}\n')