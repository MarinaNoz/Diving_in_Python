# №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# ●	загрузка данных (функция из задания 4)
# ●	вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть,
# получите его уровень из множества пользователей.
# ●	добавление пользователя. Если уровень пользователя меньше, чем ваш уровень,
# вызывайте исключение уровня доступа.

import json
from get_data import AccessError


class User:
    def __init__(self, level: int, user_id: int, name: str):
        self.level = level
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        return self.user_id == other.user_id and self.name == other.name

    def __str__(self):
        return f'{self.level} {self.user_id} {self.name}'


class Access:
    def __init__(self):
        FILE_NAME = 'data.json'
        data = self._read_json(FILE_NAME)
        user_list = self._parse_data(data)
        self.data = user_list

    def _read_json(self, file_name: str):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def _parse_data(self, data: dict):
        user_list = []
        for level, dict_users in data.items():
            for user_id, name in dict_users.items():
                user_list.append(User(int(level), int(user_id), name))
        return user_list

    def enter_system(self, user_id: int, name: str):
        temp_user = User(level=0, user_id=user_id, name=name)

        if temp_user in self.data:
            for user in self.data:
                if temp_user == user:
                    return user
        else:
            raise AccessError


if __name__ == '__main__':
    # data = read_json('data.json')
    # print(*parse_data(data))
    access = Access()
    print(*access.data)
    print(access.enter_system(1, "Андрей"))