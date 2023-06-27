# № 3
# Напишите класс для хранения информации о человеке

class Human:

    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age
        self.gender = gender

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.get_age()} {self.gender}'

if __name__ == '__main__':
    h_1 = Human('Ivan', 'Petroff', 50, 'men')
    h_2 = Human('Larisa', 'Ivanova', 30, 'women')
    print(h_1)
    print(h_2)
    h_1.birthday()
    h_2.birthday()
    print(h_1)
    print(h_2)