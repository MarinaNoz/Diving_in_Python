# №5 №6
# Создайте три или более классов животное



class Animal:

    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'

class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return 'Fly'

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.bird_type} {self._sound}'

class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str, sound: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type
        self._sound = sound

    def move(self):
        return 'Run'

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.dog_type} {self._sound}'

class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str, sound: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type
        self._sound = sound

    def move(self):
        return 'Swim'

    def say(self):
        return self._sound

    def __str__(self):
        return f'{super().__str__()} {self.fish_type} {self._sound}'

if __name__ == '__main__':
    dog = Dog('Бобик', 40, 5, 'Болонка', 'Молчит')
    bird = Bird('Гоша', 1, 2, 'Попугай', 'Разговаривает')
    fish = Fish('Хариуз', 2, 3, 'Речной')

    print(dog)
    print(bird)
    print(fish)
