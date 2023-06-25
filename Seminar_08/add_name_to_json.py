import json


def add_data(name: str, personal_id: int, level: int) -> dict[int: dict[str, int]]:
    return {level: {personal_id: name}}


def write_json(data: dict) -> None:
    file = 'data.json'
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def read_json():
    with open('data.json', 'r', encoding='utf-8') as read_f:
        data_from_file = json.load(read_f)
    return data_from_file

def make_base():
    base_list = []
    read_data = read_json()
    base_list.append(read_data)
    return base_list

def ui():
    base_dict = read_json()
    exit_prog = False
    print('Welcome!')
    while not exit_prog:
        personal_id = int(input('Введите id: '))
        name = input('Введите имя: ')
        level = int(input('Введите уровень доступа: '))
        continue_prog = input('Продолжить/выход? y/n: ')
        if continue_prog == 'n':
            exit_prog = True
        res_dict = add_data(name, personal_id, level)
        if level in base_dict:
            base_dict[level].update({personal_id: name})
        else:
            base_dict[level] = {personal_id: name}
    write_json(base_dict)
