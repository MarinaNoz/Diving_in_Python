# DZ_1
# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.



from animals import Bird, Dog, Fish


class AnimalFactory:
    def create_animal(self, type_: str, *args, **kwargs):
        new_animal = self._type_animal(type_)
        return new_animal(*args, **kwargs)

    def _type_animal(self, type_: str):
        types = {'bird': Bird, 'dog': Dog, 'fish': Fish}
        return types[type_.lower()]


if __name__ == '__main__':
    factory = AnimalFactory()

    select_animal = int(input(f'Выберите тип животного: \n'
                          f'1: Bird\n'
                          f'2: Dog\n'
                          f'3: Fish\n'
                              f': '))
    if select_animal == 1:
        type_ = 'Bird'
        name = input('Введите имя птички: ')
        weight = int(input('Введите вес птички: '))
        age = int(input('Введите возраст птички: '))
        bird_type = input('Введите тип птички: ')
        sound = input('Какие звуки издает птичка? ')

        factory = AnimalFactory()
        create_animal = factory.create_animal(type_, name, weight, age, bird_type, sound)

    elif select_animal == 2:
        type_ = 'Dog'
        name = input('Введите имя собачки: ')
        weight = int(input('Введите вес собачки: '))
        age = int(input('Введите возраст собачки: '))
        dog_type = input('Введите породу собачки: ')
        sound = input('Собачка лает? ')

        factory = AnimalFactory()
        create_animal = factory.create_animal(type_, name, weight, age, dog_type, sound)

    elif select_animal == 3:
        type_ = 'Fish'
        name = input('Введите вид рыбки: ')
        weight = int(input('Введите вес рыбки: '))
        age = int(input('Введите возраст рыбки: '))
        fish_type = ''
        sound = ''

        factory = AnimalFactory()
        create_animal = factory.create_animal(type_, name, weight, age, fish_type, sound)



    print(create_animal)



