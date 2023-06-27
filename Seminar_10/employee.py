# №4
# Создайте класс сотрудник

from seminar_10.human import Human
from random import randint
class Employee(Human):

    def __init__(self, prof: str, first_name: str, last_name: str, age: int, gender: str):
        super().__init__(first_name, last_name, age, gender)
        self.eml_id = self._gen_id()
        self.sec_level = self._secure_level()
        self.prof = prof


    def _gen_id(self):
        MIN_NUM = 1000000
        MAX_NUM = 10000000
        return randint(MIN_NUM, MAX_NUM)

    def _secure_level(self):
        sec_id = self._gen_id()
        LEVEL_NUM = 7
        level_num = 0
        while sec_id > 0:
            last_num = sec_id % 10
            level_num += last_num
            sec_id /= 10
        return round(level_num % LEVEL_NUM)

    def __str__(self):
        return f'{self.eml_id} {self.sec_level} {self.first_name} {self.last_name} {self.get_age()} {self.gender} {self.prof}'

if __name__ == '__main__':
    eml_1 = Employee('Master', 'Roman', 'Romanov', 35, 'men')
    eml_2 = Employee('worker', 'Zinaida', 'Petrova', 40, 'women')
    print(eml_1)
    print(eml_2)