from pathlib import Path
from random import randint, uniform, choice
from typing import TextIO


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def two_files_in_one(numbers: Path, words: Path, result: Path) -> None:
    with (open(numbers, 'r', encoding='utf-8') as f_num,
          open(words, 'r', encoding='utf-8') as f_word,
          open(result, 'w', encoding='utf-8') as f_res):
        len_numbers = sum(1 for _ in f_num)
        len_word = sum(1 for _ in f_word)
        for _ in range(max(len_numbers, len_word)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_word)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()} {abs(mult)}\n')
            elif mult > 0:
                f_res.write(f'{word.upper()} {round(mult)}\n')
