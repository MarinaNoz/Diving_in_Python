from pathlib import Path
from random import randint, uniform, choice


class FeelNumbers:



    MIN_NUM = -1000
    MAX_NUM = 1000

    def __init__(self, count: int, file_name: str):
        self.count = count
        self.file_name = file_name

    def feel_numbers(self, count: int, file_name: str | Path) -> None:
        with open(self.file_name, 'w', encoding='utf-8') as f:
            for _ in range(self.count):
                f.write(f'{randint(self.MIN_NUM, self.MAX_NUM)}|{uniform(self.MIN_NUM, self.MAX_NUM)}\n')


if __name__ == '__main__':
    FeelNumbers(3, 'file_1.txt')
